# Revotel website

- `posts.json`  your LinkedIn posts, edited from https://www.revotel.in/admin/ (do not edit by hand)
- `gen.py`, `style.css`  the site generator and styling
- `netlify/functions/admin.js`  the admin page's password-protected save function

Netlify runs `python3 gen.py dist prod` on every change and publishes `dist`.
