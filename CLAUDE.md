# CLAUDE.md – starterpack

Rules for working in this repository. This file is public: nothing personal goes here (no names, addresses, tokens,
paths like `/Users/…`).

## What this is

The toolkit for new falkOSS projects: `docs/` (naming, setup, practices), `bin/check-name`, `bin/new-project`,
`templates/` (one folder per repository, `rust-app/` laid over `main/`; `workspace/` is the private working folder and
is German, everything else English) and the shared workflows in `.github/workflows/`.

## Rules

- **Templates follow the projects, not the other way round.** When a pattern changes in the projects (CI, Typst
  template, brand export, website), carry it over here – and note in the commit which project it came from.
- Placeholders: `{{key}}` (values in `bin/new-project`), `{{#flag}}`/`{{^flag}}` … `{{/flag}}` (flags `whitepaper`,
  `rust_app`) on lines of their own. `bin/new-project` stops on unknown keys.
- `bin/` uses the Python standard library only. The brand export lives in `templates/brand/brandkit.py`.
- The shared workflows in `.github/workflows/` (`reuse.yml`, `dco.yml`, `pages-jekyll.yml`) are called by every
  project, pinned by commit: change them compatibly, and only together with the templates that call them.
- `templates/rust-app/` holds generated files (`Cargo.lock`, `web/pnpm-lock.yaml`, `api/openapi.json`,
  `web/src/lib/api-types.ts`): after changing the code or a dependency, write a project, regenerate them there and
  carry them back with the name replaced by `{{name}}` – CI fails otherwise.
- Test after every change: `bin/new-project <test> --tagline … --whitepaper --rust-app --root <tmp> --home <tmp>` –
  CI does the same, runs REUSE and Jekyll on the result and the project's own Rust and web checks.
- Nothing about one project's content belongs here (no Nix, no accounting, no mail); keep templates general.
- English in code, docs and commits; commits signed off (`git commit -s`). Unverified statements are marked **OPEN**.
