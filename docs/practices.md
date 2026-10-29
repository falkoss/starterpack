# Practices

How falkOSS projects are usually built – what `bin/new-project` writes and what existing projects move towards. Like
the rest of starterpack this is habit, not rule: a project may deviate where it has a reason, and says so in its
`CLAUDE.md`. What falkOSS itself requires – everything included, no telemetry – is not up to a project.

## Repositories

| Repository | When | What | Licence | Domain |
|---|---|---|---|---|
| `.github` | always | organisation profile and the default community files of every repository: CODE_OF_CONDUCT, CONTRIBUTING, SECURITY, SUPPORT, issue and pull request templates | CC BY 4.0 | – |
| `website` | always | the landing page, GitHub Pages through Actions | AGPL-3.0-or-later | `.app` for an app, else `.org` |
| `brand` | always | the brand kit: generator, artwork, fonts – the one source of the look | generator MIT, artwork **CC BY-ND 4.0**, fonts their own (e.g. OFL) | – |
| `<name>` | always | the software and its documentation (`docs/`) | AGPL-3.0-or-later (MIT where it fits better) | docs on `.dev` |
| `whitepaper` | optional | the idea and the plan: Markdown → Typst → PDF | text CC BY 4.0 | – |
| `apps` | while app stores are wanted | desktop and mobile apps that use only the open API | MIT | – |
| protocol | when it stands apart from the core | the specification and its library, in a repository or an organisation of its own; the core is one implementation | specification CC BY 4.0, library MIT | its own `.org`/`.dev` |

The other repositories carry **copies** of the brand's artwork – updated by copying from `brand`, never edited in
place, and marked CC BY-ND 4.0 in their `REUSE.toml`. Name and logo are protected by trademark law, not by a licence.

## Licences

- Every repository: `LICENSES/`, `REUSE.toml`, an SPDX header in every own source file, REUSE checked in CI.
- Software AGPL-3.0-or-later. MIT for apps that go into app stores, protocol libraries, templates to copy, and the API
  description (`api/openapi.json`) so that other clients may generate code from it.
- Texts – whitepapers, specifications, documentation prose – CC BY 4.0, so text can move freely between them.
- Contributions with a DCO sign-off (`git commit -s`), checked in CI; no CLA.

## The software (`--rust-app`)

- **One core, many interfaces.** A Rust workspace: `<name>-core` (the domain, no I/O), `<name>-store`, `<name>-app`
  (every command and query – the only layer interfaces use), `<name>-api`, `<name>-tui` and the binary `<name>`
  (`serve`, `tui`, `openapi`). The web app and the apps use the API; the API is also the licence boundary.
- **Rust:** edition 2024, the toolchain pinned in `rust-toolchain.toml`, workspace lints (`unsafe_code = "forbid"`,
  clippy), `rustfmt.toml`, `cargo deny`. CI runs on **Linux and macOS**; further targets (Windows, mobile, WASM)
  where the core has to run.
- **API:** REST and JSON, described in OpenAPI **from the code** (utoipa); `api/openapi.json` is checked in and CI
  checks it matches. GraphQL only where a project needs it.
- **TUI:** ratatui; everything with the keyboard, and with the mouse – a click does what the key does.
- **Web app:** Vite and Svelte 5 with TypeScript – 6 until Svelte supports 7 –, Node 26, pnpm; types and client
  from `api/openapi.json` (openapi-typescript, openapi-fetch); the build embedded into the binary (rust-embed) with a
  strict Content-Security-Policy.
- **Apps:** Flutter where they are cross-platform or mobile, native for macOS or Linux otherwise – in their own MIT
  repository while app-store distribution is wanted.
- **Dependencies:** exact versions, each the newest that is at least 14 days old – `scripts/check-age.py` for Cargo,
  `minimumReleaseAge` for pnpm; a fix for a security advisory may be younger.
- **i18n:** English source strings; translations next to them.

## Documentation and websites

- Documentation on `<name>.dev` from `docs/` in the main repository: Jekyll with the theme Just the Docs in the
  project's colours, built and published by GitHub Actions (`pages-jekyll.yml`), never from a branch.
- Websites and documentation load nothing from elsewhere (no font services, no external scripts), track nothing, and
  carry `.well-known/security.txt` where they are the project's front door.
- With Pages through Actions the custom domain lives in the repository settings – no `CNAME` file.

## CI

- The shared workflows of starterpack – `reuse.yml`, `dco.yml`, `pages-jekyll.yml` – are called pinned by commit;
  a fix there reaches a project when it moves the pin.
- Every action is pinned by commit, with its version as a comment.

## Releases

- Before a repository goes public, its history is reset to one commit.
- Releases are tags `vX.Y.Z` with a `CHANGELOG.md`; servers also as a container image on ghcr.io with a
  `deploy/compose.yaml`. OPEN: a release workflow template.
