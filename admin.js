// Revotel admin API. Keeps the list of LinkedIn posts in posts.json in your GitHub repository.
// Each change commits to GitHub, and Netlify then rebuilds the website automatically.
// Settings (Netlify > Site configuration > Environment variables):
//   ADMIN_PASSWORD  the password you type on /admin/
//   GITHUB_TOKEN    a fine-grained token with "Contents: Read and write" on this one repository
//   GITHUB_REPO     for example  yourname/revotel-site
//   GITHUB_BRANCH   optional, defaults to main
const crypto = require("crypto");

const FILE = "posts.json";
const json = (code, obj) => ({ statusCode: code, headers: { "Content-Type": "application/json", "Cache-Control": "no-store" }, body: JSON.stringify(obj) });
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

function passwordOk(given) {
  const want = process.env.ADMIN_PASSWORD || "";
  if (!want || typeof given !== "string") return false;
  const a = crypto.createHash("sha256").update(given).digest();
  const b = crypto.createHash("sha256").update(want).digest();
  return crypto.timingSafeEqual(a, b);
}

async function gh(path, opts = {}) {
  const repo = process.env.GITHUB_REPO;
  const res = await fetch(`https://api.github.com/repos/${repo}/contents/${path}`, {
    ...opts,
    headers: {
      Authorization: `Bearer ${process.env.GITHUB_TOKEN}`,
      Accept: "application/vnd.github+json",
      "User-Agent": "revotel-admin",
      ...(opts.headers || {}),
    },
  });
  return res;
}

async function readPosts() {
  const branch = process.env.GITHUB_BRANCH || "main";
  const res = await gh(`${FILE}?ref=${encodeURIComponent(branch)}`);
  if (res.status === 404) return { posts: [], sha: undefined };
  if (!res.ok) throw new Error("Could not read posts from GitHub (" + res.status + "). Check GITHUB_REPO and GITHUB_TOKEN.");
  const j = await res.json();
  const posts = JSON.parse(Buffer.from(j.content, "base64").toString("utf8") || "[]");
  return { posts, sha: j.sha };
}

async function writePosts(posts, sha, message) {
  const branch = process.env.GITHUB_BRANCH || "main";
  const res = await gh(FILE, {
    method: "PUT",
    body: JSON.stringify({
      message,
      branch,
      sha,
      content: Buffer.from(JSON.stringify(posts, null, 1), "utf8").toString("base64"),
    }),
  });
  if (res.status === 409 || res.status === 422) throw Object.assign(new Error("conflict"), { conflict: true });
  if (!res.ok) throw new Error("Could not save to GitHub (" + res.status + "). The token needs Contents: Read and write.");
}

function clean(b) {
  const title = String(b.title || "").trim().slice(0, 140);
  const text = String(b.text || "").replace(/\r\n/g, "\n").trim().slice(0, 20000);
  const url = String(b.url || "").trim();
  if (!title) throw new Error("Please add a headline.");
  if (text.length < 40) throw new Error("Please paste the full text of the post. Google can only read words that are on your site.");
  if (url) {
    let u;
    try { u = new URL(url); } catch (e) { throw new Error("That LinkedIn link does not look right."); }
    const h = u.hostname.toLowerCase();
    if (u.protocol !== "https:" || !(h === "linkedin.com" || h.endsWith(".linkedin.com") || h === "lnkd.in")) throw new Error("The link must be a linkedin.com address.");
  }
  let date = String(b.date || "").slice(0, 10);
  if (!/^\d{4}-\d{2}-\d{2}$/.test(date)) date = new Date().toISOString().slice(0, 10);
  return { title, text, url, date };
}

exports.handler = async (event) => {
  if (event.httpMethod !== "POST") return json(405, { error: "POST only" });
  let b;
  try { b = JSON.parse(event.body || "{}"); } catch (e) { return json(400, { error: "Bad request" }); }
  if (!passwordOk(b.password)) { await sleep(1200); return json(401, { error: "Wrong password." }); }
  if (!process.env.GITHUB_TOKEN || !process.env.GITHUB_REPO) return json(500, { error: "GITHUB_TOKEN and GITHUB_REPO are not set in Netlify yet." });

  try {
    if (b.action === "list") {
      const { posts } = await readPosts();
      return json(200, { posts: sortPosts(posts) });
    }
    for (let attempt = 0; attempt < 3; attempt++) {
      const { posts, sha } = await readPosts();
      let next = posts, msg;
      if (b.action === "add") {
        const c = clean(b);
        next = [{ id: Date.now(), ...c }, ...posts];
        msg = "Add post: " + c.title.slice(0, 60);
      } else if (b.action === "edit") {
        const c = clean(b);
        if (!posts.some((p) => String(p.id) === String(b.id))) throw new Error("Post not found.");
        next = posts.map((p) => (String(p.id) === String(b.id) ? { ...p, ...c } : p));
        msg = "Edit post: " + c.title.slice(0, 60);
      } else if (b.action === "delete") {
        next = posts.filter((p) => String(p.id) !== String(b.id));
        msg = "Delete post " + String(b.id).slice(0, 20);
      } else {
        return json(400, { error: "Unknown action" });
      }
      try {
        await writePosts(next, sha, msg);
        return json(200, { posts: sortPosts(next) });
      } catch (e) {
        if (!e.conflict) throw e;
      }
    }
    return json(409, { error: "Someone else saved at the same moment. Please try again." });
  } catch (e) {
    return json(400, { error: e.message });
  }
};

function sortPosts(posts) {
  return [...posts].sort((a, b) => (b.date || "").localeCompare(a.date || "") || String(b.id).localeCompare(String(a.id)));
}
