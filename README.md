# starterpack

**The falkOSS starter pack** – what a new project usually starts with when it is set up the
[falkOSS](https://falkoss.org) way:

- its own GitHub organisation, with `.github`, `website`, the main repository and maybe a `whitepaper`
- a lowercase name that is free – organisation, `.org` and `.dev`, no trademark in the way
- AGPL-3.0-or-later, an SPDX header in every file, REUSE in CI
- a DCO sign-off on every commit, no CLA
- everything included, no telemetry, no tracking, no fonts from elsewhere
- its own look, made by `brand/generate.py`, and "a falkOSS project" in the footer
- a whitepaper typeset with Typst, DRAFT behind every page until it isn't one
- a private working folder and a token that can push but cannot change settings

Here: the name check, the setup steps, and the templates that write all of the above in one step. The starter pack
does not make a project a falkOSS project – that is decided by falkOSS itself ([docs/setup.md](docs/setup.md),
step 2); it only gives the project the usual shape. Most of the list is habit, not rule: a project may deviate where it has a
reason (MIT instead of AGPL, no whitepaper, …). What falkOSS's own rules require – everything included, no
telemetry – is not up to the starter pack.

A project like omaflake, kernoid, notenwart, spezado or librotenado gets its **own GitHub organisation** with the
same set of repositories, a private working folder on the maintainer's machine and its own access token. The
templates have the shape the existing projects already have.

| Path | What |
|---|---|
| [docs/naming.md](docs/naming.md) | how a project gets its name: organisation, domains, trademark, language |
| [docs/setup.md](docs/setup.md) | every step from the name to the first push – what is scripted, what the maintainer does by hand |
| [bin/check-name](bin/check-name) | checks a name: GitHub organisation, domains (RDAP/whois), package registries; prints the trademark searches |
| [bin/new-project](bin/new-project) | writes the working folder with all repositories, the brand kit and the token folder |
| [templates/](templates/) | what `new-project` fills in – one folder per repository |

## Quick start

```sh
bin/check-name spezado --app                       # is the name free?
bin/new-project spezado --tagline "Free accounting for everyone" --app --whitepaper
```

`new-project` writes next to the falkOSS working folder (default: the parent of `falkoss/`):

```
<name>/                      private working folder, not a repository
  CLAUDE.md                  private notes (German), from templates/workspace
  .claude/launch.json        website preview
  .github/                   <name>/.github   – organisation profile
  website/                   <name>/website   – one static page, GitHub Pages
  <name>/                    <name>/<name>    – the software, its brand kit, CI (REUSE, DCO)
  whitepaper/                <name>/whitepaper – Markdown → Typst → PDF (with --whitepaper)
~/.<name>/developer/agent.env   GITHUB_TOKEN= (empty, mode 600 – paste the token there)
```

Every repository gets `git init -b main`, a remote `https://github.com/<name>/<repo>.git` and a first signed-off
commit. Nothing is pushed and nothing is created on GitHub: the organisation, the repositories, the token and all
repository settings are the maintainer's ([docs/setup.md](docs/setup.md)).

## What the projects have in common so far

- **Licences:** software AGPL-3.0-or-later (MIT as the allowed exception), SPDX header in every own source file,
  [REUSE](https://reuse.software) checked in CI; documents under a Creative Commons licence; the brand (names, logos)
  is not covered by any of them.
- **Contributions** with a [DCO](https://developercertificate.org) sign-off (`git commit -s`), no CLA – checked in CI.
- **Everything included** – one edition, every feature free. **No telemetry.** No externally loaded fonts or scripts,
  no tracking on any website.
- **Own identity:** each project has its own name, logo, colours and website; falkOSS appears only as publisher
  ("a falkOSS project", copyright). Imprint and privacy policy link to falkoss.org.
- **English** in every repository; claims need a source, the unverified is marked **OPEN**.

## Requirements

`python3` (3.9 or later, standard library only), `git`, `rsvg-convert` (Homebrew: `librsvg`) for the brand kit,
`whois` for some domains. The whitepaper build needs pandoc and typst in pinned versions or `nix`.

## Licence

[AGPL-3.0-or-later](LICENSE). The templates are meant to be copied into falkOSS projects; IBM Plex fonts are under the
[SIL Open Font License 1.1](LICENSES/OFL-1.1.txt).

© 2026 falkOSS – Falcon Lake Open Source Software gUG (haftungsbeschränkt) i. G. and the starterpack contributors
