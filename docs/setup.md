# Setting up a project

From the name to the first push. **[script]** marks what starterpack does, **[maintainer]** what is done by hand – creating
organisations and repositories, tokens and every repository setting (visibility, Pages, domains, secrets) stay with
the maintainer; the agent token cannot change them on purpose.

## 1. Name [script + maintainer]

`bin/check-name <name> [--app] [--eu] [--de]`, then the manual checks in [naming.md](naming.md). Buy the required
domains once the name passes.

## 2. Decision [maintainer]

A project with its own organisation, domain, brand, team or money needs a decision of the falkOSS shareholders; a
small project without any of these goes to **falkoss-labs** instead and needs none. Record the decision in
`falkoss/legal` (private).

## 3. GitHub organisation [maintainer]

- Create `github.com/<name>` (free plan for now; after the founding: business terms of the gUG, **two owners**).
- Profile: display name `<name>` (lowercase), URL of the main domain, e-mail `support@…`, avatar
  `<name>/brand/png/social/github-avatar-500.png` (written in step 5).
- Verify the domains in the organisation (DNS TXT) once they are registered.

## 4. Repositories and token [maintainer]

Create, **private** to begin with: `.github`, `website`, `<name>` and, if there is one, `whitepaper`. Empty – no
README, licence or .gitignore (the first commit comes from starterpack).

Token – a **fine-grained personal access token** (<https://github.com/settings/personal-access-tokens/new>):

| Setting | Value |
|---|---|
| Resource owner | the organisation `<name>` (the organisation may have to approve it) |
| Repository access | All repositories |
| Contents | **Read and write** |
| Workflows | **Read and write** |
| Actions | **Read and write** |
| Metadata | Read (added automatically) |
| Everything else | no access – no Administration, no Pages, no Secrets |
| Expiration | as long as allowed; note the date in the working folder's `CLAUDE.md` |

Paste it into `~/.<name>/developer/agent.env` after `GITHUB_TOKEN=` (step 5 creates the file, mode 600). Never print,
log or commit it. Each organisation has its own token – never mix them.

## 5. Working folder [script]

```sh
bin/new-project <name> --tagline "One line in English" [--app] [--eu] [--de] [--whitepaper]
                       [--licence MIT] [--doc-licence CC-BY-SA-4.0] [--accent "#5AA9E6"] [--port 8014]
```

It writes the working folder next to `falkoss/` with `CLAUDE.md` (German, private), `.claude/launch.json`, the
repositories with a first signed-off commit and their remotes, and `~/.<name>/developer/agent.env`. The brand kit is
generated with a provisional design (`<name>/brand/generate.py`) and its web assets are copied into `website/` and the
profile. It never overwrites: an existing folder stops it.

## 6. First push [maintainer's OK]

Push only after the maintainer said yes. In each repository, with an empty credential helper first (otherwise the
keychain answers with old data):

```sh
set -a; . ~/.<name>/developer/agent.env; set +a
git -c credential.helper= -c credential.helper='!f() { echo username=x-access-token; echo "password=$GITHUB_TOKEN"; }; f' push -u origin main
```

`gh` is not installed: `GH_TOKEN=$GITHUB_TOKEN nix run nixpkgs#gh -- …`.

## 7. Domains and Pages [maintainer]

- DNS at the registrar: apex A records to GitHub Pages `185.199.108.153`, `185.199.109.153`, `185.199.110.153`,
  `185.199.111.153`; `www` as CNAME to `<name>.github.io`. DNSSEC where possible.
- `website`: Settings → Pages → Source **GitHub Actions**; custom domain (writes `CNAME`); **Enforce HTTPS** once the
  certificate is there. Then add `canonical`, `og:url`, an absolute `og:image` and `Canonical:` in
  `.well-known/security.txt`.
- `.dev`: documentation from `<name>/docs/` as soon as the main repository is public (Pages from private repositories
  needs a paid plan).
- All other domains: redirect 301 to the main domain.
- Mail: `support@falkoss.org` is the contact until the project has its own mail (MX, SPF, DKIM, DMARC).

## 8. Brand [maintainer + script]

Replace the provisional design in `<name>/brand/generate.py` (mark, wordmark, colours – the export part in
`brandkit.py` stays), run it, copy `brand/web/*` to `website/` and the lockups to `website/assets/` and
`.github/profile/assets/`. Set the social preview (`png/social/<name>-social-1280x640.png`) in each repository's
settings and the avatar in the organisation. Update the colours in the whitepaper template.

## 9. falkOSS [script + maintainer]

- falkOSS working folder `CLAUDE.md`: the project, its organisation and folder.
- **Once public:** add it to falkoss.org and the falkOSS profile (icon from the brand kit to
  `website/assets/projects/`), in the agreed order.

## 10. Before going public [maintainer]

- Reset each repository's history to one commit (the projects start their public history clean).
- Check: no personal data, no paths like `/Users/…`, REUSE clean, CI green.
- Switch visibility: `.github` and `website` first, the main repository with its first release.
- Trademark: a professional search, then the word mark (classes 9 and 42) – filed by falkOSS.
