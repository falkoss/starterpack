# CLAUDE.md – starterpack

Rules for working in this repository. This file is public: nothing personal goes here (no names, addresses, tokens,
paths like `/Users/…`).

## What this is

The toolkit for new falkOSS projects: `docs/` (naming, setup), `bin/check-name`, `bin/new-project` and `templates/`
(one folder per repository; `workspace/` is the private working folder and is German, everything else English).

## Rules

- **Templates follow the projects, not the other way round.** When a pattern changes in the projects (CI, Typst
  template, brand export, website), carry it over here – and note in the commit which project it came from.
- Placeholders: `{{key}}` (values in `bin/new-project`), `{{#whitepaper}}`/`{{^whitepaper}}` … `{{/whitepaper}}` on
  lines of their own. `bin/new-project` stops on unknown keys.
- `bin/` uses the Python standard library only. The brand export lives in `templates/main/brand/brandkit.py`.
- Test after every change: `bin/new-project <test> --tagline … --whitepaper --root <tmp> --home <tmp>` – CI does the
  same and runs REUSE on the result.
- Nothing about one project's content belongs here (no Nix, no accounting, no mail); keep templates general.
- English in code, docs and commits; commits signed off (`git commit -s`). Unverified statements are marked **OPEN**.
