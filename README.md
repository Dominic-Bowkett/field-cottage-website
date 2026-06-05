# Field Cottage Peterstow — Website

A fast, modern, SEO-optimised **static website** for Field Cottage, a
5-bedroom self-catering holiday cottage in Peterstow, near Ross-on-Wye in the
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
| Meetings & Retreats | `meetings.html` |
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
4. **Check the booking link** — the Airbnb URL is in the footer and contact
   page; confirm it points to your listing.
5. **Confirm the domain** in `CNAME` (currently `www.fieldcottagepeterstow.com`).

---

## 🚀 Deploying — Cloudflare Pages

This site is deployed with **Cloudflare Pages**, connected to this GitHub
repo. The **production branch is `main`** — every push/merge to `main`
publishes automatically, and any other branch gets its own preview URL.

### One-time setup (Cloudflare dashboard)

1. **Workers & Pages → Create → Pages → Connect to Git**, and choose this
   repository.
2. Build settings:
   - **Production branch:** `main`
   - **Framework preset:** None
   - **Build command:** *(leave blank)*
   - **Build output directory:** `/`
3. **Save and Deploy.** You'll get a live URL like
   `https://field-cottage-website.pages.dev` within ~1 minute.

The `_headers` file applies security headers + long-lived asset caching, and
`404.html` is served automatically as the not-found page.

### Custom domain (DNS managed outside Cloudflare)

The domain's DNS currently lives at the registrar (not Cloudflare), so:

1. In the Pages project → **Custom domains → Set up a domain**, add
   `www.fieldcottagepeterstow.com`.
2. Cloudflare shows a target like `field-cottage-website.pages.dev`. At your
   registrar's DNS, add a **CNAME** record:
   `www` → `field-cottage-website.pages.dev` (proxy/redirect as instructed).
3. For the apex/root `fieldcottagepeterstow.com`, add it too and either use a
   CNAME-flattening/ALIAS record to the same target, or a redirect to `www`.
4. SSL is issued automatically once DNS resolves.

> Alternatively, move the domain's **nameservers** to Cloudflare (add the
> site in the Cloudflare dashboard first) for one-click custom domains and
> full CDN — but the CNAME route above works without changing nameservers.

> Note: no `CNAME` file is needed in the repo for Cloudflare Pages — that's a
> GitHub Pages convention. Custom domains are configured in the dashboard.

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
