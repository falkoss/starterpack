# {{name}} – website

One static page for **{{name}}**: no build step, no framework, no external resources, no cookies, no tracking.
A [falkOSS](https://falkoss.org) project.

| Path | What |
|---|---|
| `index.html`, `style.css`, `404.html` | the page (English) |
| `favicon.*`, `apple-touch-icon.png`, `icon-*.png`, `site.webmanifest`, `social.png` | head icons – **generated** by `brand/generate.py` in `{{name}}/{{name}}` (`brand/web/`), copied here |
| `assets/` | lockup and mark (from `brand/svg/`) |

Imprint and privacy policy are falkoss.org's – same operator, one place to keep them current.

Preview locally:

```sh
python3 -m http.server {{port}}
```

## Publishing

GitHub Pages via `.github/workflows/pages.yml` on every push to `main`. One-time setup: Repo → Settings → Pages →
Source: **GitHub Actions**.

**OPEN:** the domain ({{main_domain}}). Once it points here: set it as custom domain, **Enforce HTTPS**, and add
`canonical`, `og:url` and an absolute `og:image` to `index.html` and `Canonical:` to `.well-known/security.txt`. Until
then, `404.html` uses root paths that only resolve under a custom domain.

## Licence

The site's code is **AGPL-3.0-or-later** (`LICENSE`); the brand's artwork (favicons, icons, `assets/`) is copied from
`{{name}}/brand` under CC BY-ND 4.0, and the brand itself (name, logo, marks) is not covered by any licence.
