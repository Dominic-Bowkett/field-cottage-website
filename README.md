# Field Cottage Peterstow — Website

A fast, modern, SEO-optimised **static website** for Field Cottage, a
4-bedroom self-catering holiday cottage in Peterstow, near Ross-on-Wye in the
Wye Valley, Herefordshire. **Sleeps 8 · Dog friendly.**

Built as plain HTML / CSS / JavaScript with **no build step and no
dependencies** — ideal for **GitHub Pages** and **Cloudflare Pages**.

---

## 📄 Pages

| Page | File |
|---|---|
| Home | `index.html` |
| About & Rooms | `about.html` |
| The Area | `area.html` |
| Gallery (with lightbox) | `gallery.html` |
| Blog index | `blog.html` |
| Blog posts | `blog/*.html` (6 articles) |
| Contact & booking | `contact.html` |
| 404 | `404.html` |

## 🖼️ Photos

The site ships with **placeholder images** so it looks complete immediately.
**Replace them with your own photos** — see
[`assets/images/README.md`](assets/images/README.md) for the simple file-name
mapping. All photography is © the owner.

> ⚠️ This project was generated in a sandbox that could not reach the live
> `fieldcottagepeterstow.com` site, so the original photos could not be
> downloaded automatically. Drop your photos into `assets/images/` (same file
> names) and they'll appear everywhere automatically.

## 🔍 SEO features included

- Unique `<title>` and meta description on every page
- Open Graph + Twitter Card tags for rich social sharing
- Canonical URLs on every page
- **JSON-LD structured data**: `LodgingBusiness` / `VacationRental`,
  `BreadcrumbList`, `FAQPage`, `Blog` and `BlogPosting`
- `sitemap.xml` and `robots.txt`
- Geo meta tags (Peterstow / HR9 6LG)
- Semantic, accessible HTML with descriptive `alt` text
- Fast, lightweight (no frameworks), lazy-loaded images, mobile-first
- PWA web manifest + SVG favicon

## ✏️ Before you go live — quick checklist

1. **Add your photos** (`assets/images/`).
2. **Set your contact email** — search the project for
   `info@fieldcottagepeterstow.com` and replace with your preferred address
   (it's used in the footer, contact form and structured data).
3. **Add a phone number** (optional) — fill in the empty `"telephone"` field
   in the JSON-LD in `index.html` and add it to the contact page.
4. **Check the booking links** — Airbnb / Booking.com URLs are in the footer
   and contact page; confirm they point to your listings.
5. **Confirm the domain** in `CNAME` (currently `www.fieldcottagepeterstow.com`).

---

## 🚀 Deploying

### Option A — Cloudflare Pages (recommended for this domain)

1. Push this repo to GitHub.
2. In the Cloudflare dashboard → **Workers & Pages → Create → Pages →
   Connect to Git**, choose this repo.
3. Build settings:
   - **Framework preset:** None
   - **Build command:** *(leave blank)*
   - **Build output directory:** `/`
4. Deploy, then add your **custom domain** `www.fieldcottagepeterstow.com`
   under the project's **Custom domains** tab (Cloudflare handles DNS + SSL).

The `_headers` file adds sensible security headers and long-lived caching for
assets automatically on Cloudflare Pages.

### Option B — GitHub Pages

1. Push to the `main` branch.
2. **Settings → Pages → Build and deployment → Source: GitHub Actions.**
   The included workflow (`.github/workflows/deploy-pages.yml`) publishes the
   site automatically on every push to `main`.
3. The `CNAME` file wires up the custom domain; set the matching DNS records
   at your registrar (a `CNAME` for `www` → `<user>.github.io`).

> `.nojekyll` is included so GitHub Pages serves the files as-is.

### Local preview

```bash
# from the project root
python3 -m http.server 8000
# then open http://localhost:8000
```

---

## 🎨 Customising

- **Colours / fonts:** all design tokens live at the top of
  `assets/css/styles.css` (`:root` variables).
- **Text content:** edit the relevant `.html` file directly.
- **New blog post:** copy any file in `blog/`, update the content, the
  `<title>`/meta/JSON-LD, add a card to `blog.html`, and a `<url>` entry to
  `sitemap.xml`.

Generated photography placeholders come from `tools/gen_placeholders.py`
(pure Python, no dependencies) — safe to delete once real photos are added.
