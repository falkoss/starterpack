# {{name}} Whitepaper

The whitepaper of **{{name}}** – {{tagline_lower}}. A [falkOSS](https://falkoss.org) project.

| File | Content | Status |
|---|---|---|
| [whitepaper.md](whitepaper.md) | the whitepaper – the only source | v0.1, outline |
| [whitepaper.pdf](whitepaper.pdf) | set with Typst from the Markdown | generated |

## Building

`whitepaper.md` is the only source. `whitepaper.typ` (Typst) and `whitepaper.pdf` are generated from it – rebuild
after every change and commit all three:

```sh
./build.sh               # all documents (needs the pandoc and typst versions in build.sh, otherwise uses nix)
./build.sh whitepaper.md # only this one
```

Title, version and status come from the YAML front matter; with `status: Draft` a light DRAFT is drawn behind every
page. The footer shows status, the date of the document's last commit and the short hash of its content
(`git log --find-object=<hash>` finds the commit a PDF was made from). Author notes (`> [!NOTE]`, the section "Open
points") stay in the Markdown only. CI (`.github/workflows/pdf.yml`) rebuilds on every push, checks that the
committed `.typ` is current and, for a tag `v*`, attaches the PDF to a GitHub release.

The template (`template/{{name}}.typ`) is provisional until {{name}} has its final brand kit (OPEN).

## Licence

The text: [{{doc_licence_label}}](LICENSES/{{doc_licence}}.txt). The build tooling (`build.sh`, `template/`):
[AGPL-3.0-or-later](LICENSES/AGPL-3.0-or-later.txt). Fonts: IBM Plex, [SIL Open Font License 1.1](LICENSES/OFL-1.1.txt).

## Contributing

Issues and pull requests are welcome, with a [DCO](https://developercertificate.org) sign-off (`git commit -s`).
Every claim needs a source; unverified statements are marked **OPEN**.

© {{year}} {{publisher}} and the {{name}} contributors
