# Contributing to {{name}}

Thank you for helping. The rules for every {{name}} repository – sign-off, licences, everything included, no
telemetry – are in the [organisation's CONTRIBUTING.md](https://github.com/{{name}}/.github/blob/main/CONTRIBUTING.md).
This file adds how to work on this one.
{{#rust_app}}

## Build and test

Rust from `rust-toolchain.toml`, Node 26 and pnpm (the version in `web/package.json`).

```sh
(cd web && pnpm install && pnpm build)
cargo fmt --check && cargo clippy --all-targets && cargo test
cargo run -q -- openapi > api/openapi.json && (cd web && pnpm api)   # after changing the API
(cd web && pnpm check)
cargo deny check
scripts/check-age.py                                                  # after changing Cargo.lock
```

## Rules

- **One core, many interfaces:** the terminal interface, the API and the command line work through `{{name}}-app`
  only; the web app and the apps use the API.
- **Dependencies:** exact versions (`=` in `Cargo.toml`, no `^` in `package.json`), the newest that is at least 14
  days old – `scripts/check-age.py` for Cargo, `minimumReleaseAge` in `web/pnpm-workspace.yaml` for pnpm; a fix for
  a security advisory may be younger.
- **The TUI** can be used with the keyboard alone and with the mouse: a click does what the key does.
{{/rust_app}}
{{^rust_app}}

<!-- OPEN: how to build and test. -->
{{/rust_app}}
