# Naming a project

A falkOSS project's name is its GitHub organisation, its domains and – later – its trademark at once. A name is only
taken when all three are free. `bin/check-name <name>` does the parts that can be automated; the rest is listed here.

## The name itself

- **Lowercase**, always – in text, at the start of a sentence, in titles and logos (omaflake, kernoid, notenwart).
  Only code identifiers and environment variables follow their own rules (`OmaflakeCore`, `NOTENWART_URL`).
- **Short and pronounceable**, ASCII letters only (a hyphen only if nothing else works – it costs domain and handle
  clarity).
- **Distinctive, not descriptive.** A plain description ("open accounting", "mail server") can neither be registered
  as a trademark nor as a company name. Invented words, compounds and words from other languages work (kernoid,
  notenwart, spezado from Esperanto).
- **Meaning checked.** A word from another language is confirmed by someone who speaks it (OPEN until then); check
  that it means nothing unwanted in German, English and the main European languages.
- **No collision in IT.** Search the name and close variants: an existing product, company or well-known project with
  the same or a similar name in software is a no-go (kernoid was renamed from "Earendil" and is not "Kerno" because of
  existing companies). "Falcon" is a warning example: densely used in IT.

## GitHub organisation

`github.com/<name>` must be free. The API answers 404 for a free name – but also for hidden, suspended or reserved
accounts, so a free result is only confirmed when the organisation can actually be created. The main repository has
the organisation's name (`<name>/<name>`).

## Domains

| TLD | When | Use |
|---|---|---|
| **.org** | **required** | main domain of the website (unless .app is) |
| **.dev** | **required** | documentation (GitHub Pages from the main repository's `docs/`), later developer services |
| **.app** | required if the project is an app | then the main domain of the website (omaflake.app, notenwart.app) |
| **.eu** | required if the project is EU-specific | redirect, or main domain for a European audience |
| **.de** | required if the project is Germany-specific | redirect; only falkOSS itself is a German company with a .de |
| **.com** | nice to have – often only parked | redirect |

- All domains other than the main one **redirect with 301** to it (path kept).
- **Domain hacks** (notenw.art, speza.do, kerno.id, omafla.ke) are welcome as short URLs and redirects – never as the
  main address: the registry is foreign and its rules can change.
- **Not bought on purpose:** .io, .net, hyphenated variants and other defensive registrations – protection comes from
  the trademark, not from domains.
- **Registrar:** IONOS for everything it offers; other registrars only for TLDs IONOS does not have.

## Trademark (first check)

A name passes the first check when:

- the **.com domain is not in use by a company or project** with a similar purpose (parked or for sale is fine);
- **DPMA, EUIPO, TMview and the WIPO Global Brand Database** show no identical or confusingly similar mark in
  **classes 9 (software) and 42 (software services)** – also check close variants;
- a **web search** shows no company, product or project of the same name in software (unregistered rights such as
  company names count too);
- the **package registries** that matter for the project (crates.io, npm, PyPI) do not already have it – a nice to
  have, not a blocker.

`check-name` prints the search pages; the searches themselves are done by hand and their date written down. The
registration itself (word mark, classes 9 and 42) is filed by falkOSS later; a professional search before filing is
OPEN for every project.

## Write it down

Record the result with its date in the project's private working folder (`CLAUDE.md`, section "Domains" and "Name"):
what is free, what was bought, what was searched where. Unverified points stay **OPEN**.
