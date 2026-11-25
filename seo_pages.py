# Search-focused guide pages for the Technology section.
# Edit the text here, upload this file to GitHub, and Netlify rebuilds the site.
# Links look like [[technology/hotel-pms]] or [[contact]] and are turned into real links by gen.py.
# Each page needs: slug, title (Google title), desc (Google description), h1, intro, blocks, faqs.
# blocks = list of (heading, html). Keep claims factual: describe Foodle+ only with what is true.

FP_LINE = "Foodle+ is Revotel's hotel PMS, guest experience management system (GEMS) and POS, built with AI and powered by automation. It syncs with the STAAH and Aiosell channel managers."

GUIDES = [

# ------------------------------------------------------------------ 1
dict(
 slug="best-cloud-pms-for-hotels",
 crumb="Best cloud PMS by property type",
 title="Best Cloud PMS for Hotels, Resorts & B&Bs: How to Choose (2026) | Revotel",
 desc="How to choose the best cloud-based PMS for a hotel, resort or B&B. A checklist by property type, the questions to ask vendors, and where an AI PMS like Foodle+ fits.",
 h1="Best cloud PMS options by property type: how to choose the right system",
 intro="The best cloud PMS is the one that fits how your property sells and runs. A 20-room B&B, a beach resort and a premium city hotel need different things. This guide shows what to check for each, so you can shortlist a hotel PMS with confidence.",
 blocks=[
  ("What a cloud-based PMS does", """<p>A property management system (PMS) is the software your front office runs on: reservations, room status, guest records, billing and reports. A <strong>cloud-based PMS</strong> runs over the internet, so your team can open it from the front desk, from home or from a phone, and you do not run a server at the property.</p>
<p>For most independent hotels the question is no longer whether to move to a cloud PMS, but which one. These are the things that separate a good fit from a frustrating one.</p>"""),
  ("Best cloud PMS by property type", """<div class="table-scroll"><table><thead><tr><th>Property type</th><th>What matters most</th><th>What to ask a vendor</th></tr></thead><tbody>
<tr><td>Hotel (20 to 100 rooms)</td><td>Fast front desk, clean room status, reliable channel manager sync and daily reports.</td><td>Does it sync rates and inventory with my channel manager in both directions?</td></tr>
<tr><td>Resort</td><td>Restaurant and outlet billing, packages, group and event bookings, guest requests across a large site.</td><td>Is there a POS for food and beverage, and how do guest requests reach the right team?</td></tr>
<tr><td>B&amp;B, homestay and small guesthouse</td><td>Simple set-up, low monthly cost, easy mobile use and quick OTA sync.</td><td>Can one person run it from a phone, and what does it cost per room?</td></tr>
<tr><td>Premium and luxury property</td><td>Guest experience, upgrades, upsells, multi-language support and clean data for pricing.</td><td>Can guests request services and upgrades without calling the desk?</td></tr>
</tbody></table></div>
<p class="caption">A starting checklist. Always test the system with your own rates and room types before you commit.</p>"""),
  ("Ten questions to ask before you choose a hotel PMS", """<ul class="checks">
<li>Is it truly cloud-based, and can staff use it on a phone or tablet?</li>
<li>Which channel managers does it sync with? Ask for names, not a general yes.</li>
<li>Does it handle Indian GST invoicing the way your accountant needs?</li>
<li>Is there a POS for restaurant, bar and room service, or is that a separate product?</li>
<li>How do guests make requests: phone calls, WhatsApp, or a QR code?</li>
<li>Which languages do guests and staff see?</li>
<li>What reports do you get without building them by hand?</li>
<li>Who does the training, and who do you call when something breaks?</li>
<li>What happens to your data if you leave?</li>
<li>What is the total yearly cost, including set-up, add-ons and per-room charges?</li></ul>"""),
  ("Where Foodle+ fits", """<p>""" + FP_LINE + """ You can use the PMS on its own, the PMS integrated with your channel manager, or the guest experience system (GEMS) as a standalone product.</p>
<p>Guests scan a QR code on their phone to order services, send housekeeping requests, order in-room dining, ask for a room upgrade and leave a review. The experience is offered in five languages, including Hindi and English. Read more about the <a href="[[technology/hotel-pms]]">Foodle+ hotel PMS</a> and the <a href="[[technology/guest-experience-system]]">guest experience management system</a>.</p>"""),
  ("A PMS is only half of the revenue picture", """<p>The PMS holds your bookings. Your revenue comes from the rates and restrictions you set on every channel. Revotel runs <a href="[[revenue-management]]">hotel revenue management</a> alongside the technology, so the system and the pricing work together.</p>"""),
 ],
 faqs=[
  ("What is the best cloud PMS for a hotel?","There is no single best system for every hotel. The right choice depends on your room count, whether you run a restaurant, which channel manager you use and how your guests make requests. Shortlist two or three systems and test them with your own rates."),
  ("What is the best cloud-based PMS for a resort?","A resort should look for outlet and restaurant billing, package and group handling, and a good way for guests to request services across a large property. Foodle+ includes a POS and a QR-based guest experience system."),
  ("What is the best cloud-based PMS for a B&B?","A B&B usually needs a simple set-up, easy mobile use, quick OTA sync and a fair price per room. Ask for a demo and check that one person can run it alone."),
  ("What does a cloud PMS cost?","Prices vary by vendor, room count and add-ons. Ask for the total yearly cost including set-up. For Foodle+, send your room count and what you need on WhatsApp and we will send a quote."),
  ("Can a hotel switch from its current PMS?","Yes. The work is mapping your rooms and rates, moving guest and booking data, and training staff. Plan it for a quiet period."),
 ]),

# ------------------------------------------------------------------ 2
dict(
 slug="pms-compatible-with-staah",
 crumb="PMS compatible with STAAH",
 title="PMS Compatible with STAAH (and Aiosell) for Hotels | Foodle+ by Revotel",
 desc="Looking for a hotel PMS that works with STAAH? Foodle+ syncs with the STAAH and Aiosell channel managers. See what syncs, how to set it up and what to check.",
 h1="A PMS that works with STAAH: Foodle+ syncs with STAAH and Aiosell",
 intro="If your hotel already sells through the STAAH channel manager, you do not need to change it to get a modern PMS. Foodle+ syncs with both STAAH and Aiosell, so rates, inventory and bookings stay in step between your PMS and your channels.",
 blocks=[
  ("Why PMS and channel manager sync matters", """<p>When your PMS and your channel manager do not talk to each other, someone re-types bookings, and a room can sell twice. A synced setup keeps one picture of availability across the front desk and every online channel.</p>
<ul class="checks"><li>Fewer double bookings and manual updates</li><li>Rates and inventory managed from one plan</li><li>Bookings from OTAs reach the front desk without re-entry</li><li>Reports that use the same numbers your channels see</li></ul>"""),
  ("Three ways to set this up", """<div class="table-scroll"><table><thead><tr><th>Setup</th><th>Best for</th><th>What you get</th></tr></thead><tbody>
<tr><td>Foodle+ PMS with STAAH</td><td>Hotels that already use STAAH</td><td>Keep your channel manager and add the PMS.</td></tr>
<tr><td>Foodle+ PMS with Aiosell</td><td>Hotels that use or prefer Aiosell</td><td>The same PMS, synced with Aiosell.</td></tr>
<tr><td>GEMS only</td><td>Hotels that are happy with their PMS</td><td>The guest QR system as a standalone product.</td></tr>
</tbody></table></div>"""),
  ("What to check with any PMS and channel manager pair", """<ul class="checks">
<li>Is the sync two-way, so bookings and availability move both ways?</li>
<li>How quickly does a change reach the channels?</li>
<li>How are rate plans, room types and restrictions mapped?</li>
<li>Who fixes it when a mapping breaks?</li></ul>
<p>Revotel's revenue team works inside STAAH and Aiosell every day, so mapping and rate set-up are handled by people who use them. Read about our <a href="[[technology/channel-manager]]">channel manager setup</a>.</p>"""),
 ],
 faqs=[
  ("Which PMS works with STAAH?","Foodle+ syncs with STAAH. Ask any PMS vendor for the names of the channel managers they sync with, and check how the sync works."),
  ("Is Foodle+ compatible with Aiosell?","Yes. Foodle+ syncs with both STAAH and Aiosell."),
  ("Do I need to change my channel manager to use Foodle+?","No. You can keep STAAH or Aiosell and add the Foodle+ PMS."),
  ("Can I use the guest experience system without the PMS?","Yes. The GEMS can be used on its own."),
  ("Do you manage my STAAH account too?","Yes, as part of Revotel's revenue management, our team can manage rates, inventory and OTA connections in STAAH or Aiosell."),
 ]),

# ------------------------------------------------------------------ 3
dict(
 slug="best-pms-in-india",
 crumb="Best PMS in India",
 title="Best PMS in India (2026): AI & Automation, Goa, Uttarakhand, Thailand | Revotel",
 desc="How to pick the best PMS in India for your hotel. What to check in 2026, how AI and automation help, and notes for hotels in Goa, Uttarakhand and Thailand.",
 h1="Best PMS in India: what to check in 2026, from Goa to Uttarakhand and Thailand",
 intro="Indian hotels are moving to cloud systems with channel sync, guest self-service and AI-assisted reporting. This page covers what to look for in a hotel PMS in India in 2026, and what changes by destination.",
 blocks=[
  ("What to look for in a PMS in India", """<ul class="checks">
<li><strong>Cloud-based</strong>, usable on a phone and a front-desk computer</li>
<li><strong>Channel manager sync</strong> with the tools you already use, such as STAAH or Aiosell</li>
<li><strong>GST-ready billing</strong> that your accountant accepts</li>
<li><strong>A POS</strong> if you run a restaurant, bar or in-room dining</li>
<li><strong>Guest self-service</strong> by QR code or WhatsApp, in Hindi and English at least</li>
<li><strong>Local support</strong> in your time zone, in a language your team speaks</li></ul>"""),
  ("AI and automation in a hotel PMS", """<p>AI in a PMS is useful when it removes work your team does by hand. Two examples of what to look for:</p>
<ul class="checks"><li><strong>Analysis and reports:</strong> the system does the analysis and backend work, so managers see the picture without building spreadsheets.</li>
<li><strong>Guest requests:</strong> a guest sends a request, and automation sends it to the right place, so staff get clear tasks and not phone calls.</li></ul>
<p>This is how Foodle+ works. The AI handles analysis and backend work in the PMS, and automation routes guest requests from the QR code to the PMS or to WhatsApp. See the <a href="[[technology/foodle-plus]]">Foodle+ AI hotel PMS</a>.</p>"""),
  ("Best PMS in Goa", """<p>Goa hotels sell hard in a short peak season and run on OTAs, so fast channel sync and clean rate control matter most. Beach resorts also need restaurant billing and a simple way for guests to ask for services. Look for a PMS with a POS, channel manager sync and a guest request system that works for visitors from many countries. Revotel works with <a href="[[destinations/goa]]">hotels across Goa</a>.</p>"""),
  ("Best PMS in Uttarakhand", """<p>Uttarakhand has pilgrimage, hill-station and adventure markets with strong seasons and sudden demand spikes. Properties range from large hotels to small mountain stays, so a simple set-up and a good mobile experience matter. Check that staff can work from a phone and that your channel manager stays in sync. Revotel has an office in Dehradun and works with <a href="[[destinations/uttarakhand]]">hotels across Uttarakhand</a>.</p>"""),
  ("Best PMS in Thailand", """<p>Thailand hotels serve guests from many countries, so languages and a smooth guest request flow matter. Check for multi-language support, channel manager sync with the OTAs your market uses, and a clear way to manage rates by season. See our <a href="[[destinations/thailand]]">hotel consulting for Thailand</a>.</p>"""),
  ("Best PMS in India: a short method", """<ol class="steps"><li><h3>List what you sell</h3><p>Rooms, restaurant, events, packages. This decides whether you need a POS.</p></li>
<li><h3>Confirm channel manager sync</h3><p>Ask for the exact names, and for a live demo of a booking reaching the PMS.</p></li>
<li><h3>Test with your own rates</h3><p>Load your room types and a few rate plans and run a day of bookings.</p></li>
<li><h3>Compare the total yearly cost</h3><p>Include set-up, training and add-ons.</p></li></ol>"""),
 ],
 faqs=[
  ("What is the best PMS in India?","It depends on your property. For most hotels the deciding factors are channel manager sync, GST billing, a POS if you run a restaurant, guest self-service and local support. Use the checklist on this page to shortlist."),
  ("What PMS features are trending in India in 2026?","Cloud access on mobile, QR-based guest self-service, WhatsApp guest messaging, AI-assisted reports and tight channel manager sync."),
  ("How does AI help in a hotel PMS?","AI can do analysis and backend work so managers do not build reports by hand, and automation can route guest requests to the right team."),
  ("Which PMS is best for hotels in Goa?","Goa hotels should check channel manager sync, restaurant and outlet billing, and guest request handling. Foodle+ includes a POS and a QR-based guest experience system."),
  ("Which PMS is best for hotels in Uttarakhand?","Look for a simple set-up, strong mobile use and reliable channel sync. Revotel has an office in Dehradun and can help you shortlist."),
 ]),

# ------------------------------------------------------------------ 4
dict(
 slug="hotel-pms-software-list",
 crumb="Hotel PMS software list",
 title="Hotel PMS Software List (2026): Hotelogix, Cloudbeds, IDS & More | Revotel",
 desc="A neutral list of hotel PMS software hoteliers shortlist, including Hotelogix, Cloudbeds, IDS Next and Foodle+, with a checklist to compare them for your property.",
 h1="Hotel PMS and software list: how to shortlist and compare",
 intro="Hotel owners often start with a list of names. This page lists well-known hotel PMS options as a starting point, then shows how to compare them for your own property. It is a neutral starting list, not a ranking.",
 blocks=[
  ("Hotel PMS names to start your shortlist", """<div class="table-scroll"><table><thead><tr><th>Name</th><th>What it is</th><th>Check</th></tr></thead><tbody>
<tr><td>Foodle+</td><td>Hotel PMS, guest experience management system (GEMS) and POS from Revotel, built with AI and powered by automation. Syncs with STAAH and Aiosell.</td><td><a href="[[technology/foodle-plus]]">See Foodle+</a></td></tr>
<tr><td>Hotelogix</td><td>A cloud-based hotel PMS for independent hotels.</td><td>Ask the vendor about channel sync, pricing and support in your city.</td></tr>
<tr><td>Cloudbeds</td><td>A cloud property management platform that also offers channel manager and booking tools.</td><td>Ask about India support, GST invoicing and pricing per room.</td></tr>
<tr><td>IDS Next</td><td>Hotel software from IDS covering PMS and distribution tools, used by hotels in India.</td><td>Ask which modules you need and how they are priced.</td></tr>
<tr><td>eZee</td><td>A cloud PMS and related hotel software from an Indian vendor.</td><td>Ask which products and channel managers it connects with.</td></tr>
<tr><td>Oracle OPERA Cloud</td><td>An enterprise PMS used by larger hotels and chains.</td><td>Check whether the scale and cost suit an independent property.</td></tr>
</tbody></table></div>
<p class="caption">Names and trademarks belong to their owners. This is a starting list, not a ranking or a feature comparison. Check each vendor's own website for current features and pricing.</p>"""),
  ("How to compare them for your hotel", """<ul class="checks">
<li><strong>Fit:</strong> room count, restaurant, events and group bookings</li>
<li><strong>Distribution:</strong> the exact channel managers it syncs with, such as STAAH or Aiosell</li>
<li><strong>India needs:</strong> GST billing, local support and Hindi and English for staff</li>
<li><strong>Guest experience:</strong> requests by QR code, WhatsApp or phone</li>
<li><strong>Cost:</strong> total yearly price including set-up, add-ons and per-room charges</li>
<li><strong>Exit:</strong> can you take your data with you?</li></ul>"""),
  ("Guest experience management systems (GEMS)", """<p>A guest experience management system lets guests make requests, order services and leave feedback from their own phone. In Foodle+ the GEMS works through a QR code, offered in five languages, and requests go to the PMS or to WhatsApp. It can be used on its own, which helps if you want to keep your current PMS. Read more about the <a href="[[technology/guest-experience-system]]">Foodle+ GEMS</a>.</p>"""),
  ("Need help to choose?", """<p>Revotel advises hotels on technology as part of <a href="[[revenue-management]]">revenue management</a>. Send your room count, your channel manager and what you need, and we will tell you what fits.</p>"""),
 ],
 faqs=[
  ("What is the most widely used hotel PMS?","There is no single answer that applies to every market, and published rankings differ by region and property size. Build a shortlist from the options that sync with your channel manager and meet your needs."),
  ("What is IDS software for hotels?","IDS is a hospitality software vendor. IDS Next is its hotel software suite. Check the vendor's website for the modules and pricing that apply to you."),
  ("Is Foodle+ an alternative to Hotelogix or Cloudbeds?","Foodle+ is a hotel PMS, so it can be shortlisted alongside them. Compare on your own needs: channel sync, GST billing, POS, guest experience and cost."),
  ("What should be on a hotel software list?","A PMS, a channel manager, a booking engine, a POS and a guest experience system. Some vendors offer several of these together."),
 ]),
]
