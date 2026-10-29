# {{name}} – brand kit

**Provisional** – the placeholder design from [falkoss/starterpack](https://github.com/falkoss/starterpack) until {{name}} has
its own (OPEN). Every falkOSS project has its own name, logo, colours and look; falkOSS appears only as publisher.

Everything here is generated: edit `generate.py` (the drawing) – `brandkit.py` (the export) stays as it is – then run
`python3 generate.py` (needs `rsvg-convert` from Homebrew `librsvg`). It writes `svg/`, `png/` and `web/`.

| Use | File |
|---|---|
| GitHub organisation avatar | `png/social/github-avatar-500.png` |
| GitHub social preview, link previews | `png/social/{{name}}-social-1280x640.png` |
| Website head (copy to the website) | `web/` – favicon.svg (follows light/dark), favicon.ico, apple-touch-icon.png, icon-192/512.png, social.png, site.webmanifest |
| Headers, documents, profile | `svg/{{name}}-lockup-on-dark.svg`, `-on-light.svg` (PNG: `png/lockup/`) |
| Wordmark alone | `svg/{{name}}-wordmark-on-dark.svg`, `-on-light.svg` |
| Mark alone (transparent) | `svg/{{name}}-mark-on-dark.svg`, `-on-light.svg`; one colour: `-black.svg`, `-white.svg` |
| App-like icon | `png/icon/` (rounded), `png/icon-square/` (edge to edge), `png/icon-small/` (16–48 px) |

## Where it is used

This repository is the brand's one source; the others carry copies of what they show and are updated by copying,
never edited there:

| Repository | Copies |
|---|---|
| `{{name}}/website` | `web/`, the lockup and mark on dark (`assets/`) |
| `{{name}}/.github` | the lockups in the organisation profile |
| `{{name}}/{{name}}` | `web/favicon.*` and the lockup on dark in `docs/assets/`; `web/favicon.svg` in the web app's `web/public/` (if there is one) |

## Rules for the real design (as for all falkOSS projects)

- One accent colour, near-black or a clear light ground; straight edges where it fits; no glow, neon or gradients
  unless the project's idea needs them.
- A small variant for 16–48 px that still reads.
- A wordmark as outlines (no font needed where it is shown); fonts only under a free licence (e.g. SIL OFL), never
  loaded from a font service – fonts go to `fonts/` with their licence, and into `REUSE.toml`.
- The name is always lowercase.

## Licences and rights

| Files | Licence |
|---|---|
| `generate.py`, `brandkit.py`, this README | [MIT](LICENSES/MIT.txt) |
| the artwork: `svg/`, `png/`, `web/` | [CC BY-ND 4.0](LICENSES/CC-BY-ND-4.0.txt) |

The artwork may be copied and passed on – also in apps distributed through app stores and in other software – as it
is and naming falkOSS; changed versions may not be passed on. The licence covers the artwork's copyright, not the
name: {{name}}'s name and brand belong to {{publisher}}, the publisher of {{name}}. They may be used to refer to {{name}},
not for other products or in a way that suggests endorsement. **OPEN**: trademark search and registration, and a
review of these terms by someone who knows the law.
