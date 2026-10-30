# {{name}}

**{{tagline}}.** A [falkOSS](https://falkoss.org) project.

<!-- OPEN: what it is, for whom, how to try it. -->
{{name}} is at its beginning: there is nothing to install yet.
{{#whitepaper}}
The idea and the plan are in the [whitepaper](https://github.com/{{name}}/whitepaper).
{{/whitepaper}}
The documentation is at [{{docs_domain}}](https://{{docs_domain}}).

| Path | What |
|---|---|
{{#rust_app}}
| [crates/](crates/) | the Rust core: `{{name}}-core` (the domain), `-store`, `-app` (the one layer every interface uses), `-api` (HTTP/JSON), `-tui` (terminal), `{{name}}` (the command line) |
| [web/](web/) | the web app – Svelte and TypeScript, embedded into the binary |
| [api/](api/) | the API description in OpenAPI, generated from the code |
{{/rust_app}}
| [docs/](docs/) | the documentation site – Jekyll, published by GitHub Actions |

The brand kit lives in its own repository, [{{name}}/brand](https://github.com/{{name}}/brand).
{{#rust_app}}

## Try it

```sh
(cd web && pnpm install && pnpm build)   # the web app the binary embeds
cargo run -- tui                         # the terminal interface
cargo run -- serve                       # the API and the web app on http://127.0.0.1:{{api_port}}
```
{{/rust_app}}

## The name

<!-- OPEN: where the name comes from – the same text as on the website, in the profile and the whitepaper
     (starterpack docs/naming.md, "Explaining the name"). -->
```
…   → {{name}}
```

*…* is … for …

## Principles

- **Everything included** – one edition, every feature free; no paid tiers, licence keys or unlocks.
- **No telemetry** – only connections that are technically needed or that users start themselves.
- **In the open** – issues, plans, reviews and decisions happen in public.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Every commit is signed off under the
[Developer Certificate of Origin](https://developercertificate.org) (`git commit -s`); there is no CLA.

## Licence

[{{licence}}](LICENSES/{{licence}}.txt), an SPDX header in every source file ([REUSE](https://reuse.software)). The
copies of the brand's artwork are under [CC BY-ND 4.0](LICENSES/CC-BY-ND-4.0.txt); the brand (name, logo, marks)
itself is not covered by any licence.

© {{year}} {{publisher}} and the {{name}} contributors
