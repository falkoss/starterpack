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

## Explaining the name

An invented name says nothing by itself – so every project tells where its name comes from, as falkOSS does with
Falcon Lake → Falkensee → falkOSS. A name with a story is easier to remember and to pronounce, and the explanation
shows that it was chosen, not generated.

- **Where:** in four places, with the same text – the **website** (a section `name`, like on falkoss.org), the
  **organisation profile** (`### The name`), the main repository's **README** (`## The name`) and, if there is one,
  the **whitepaper**. The documentation on `.dev` may repeat it on its start page. `bin/new-project` writes the
  headings with an OPEN placeholder.
- **What:** the words it is built from, their language and meaning (*kerno* – Esperanto for core), how they are put
  together, and, if there is one, a second reading (kernoid: *kern.id*, the kernel of a map). Two to five sentences –
  a derivation in a few lines of monospace (like the falkOSS one) is welcome, a lecture is not.
- **How:** in English, the source words in italics with their language named; pronunciation only where it is not
  obvious. Every claim about a language is confirmed by someone who speaks it – until then the text stays OPEN in the
  working folder and is not published.

## Esperanto as a source

kernoid (*kerno*, core), spezado (*spezado*, the continuing turnover of money) and librotenado (*librotenado*,
bookkeeping) take their names from Esperanto. It is a good quarry for new names, too:

- **A language built for Europe.** L. L. Zamenhof published it in 1887 as a neutral second language for everyone.
  Its roots come mostly from Romance and Germanic languages, some from Slavic ones and Greek – so a word often looks
  familiar across Europe without belonging to any one nation. That suits projects that care about Europe, open
  standards and digital sovereignty without sounding national.
- **Designed, so it composes.** Words are built from roots and a small set of regular affixes, which makes precise
  new names easy and their explanation short: *libro* (book) + *ten-* (keep) + *-ado* (ongoing action) =
  *librotenado*, bookkeeping.
- **Distinctive.** Esperanto words are real words with a meaning, yet rarely used for products – trademark searches
  usually come back clean, and the domains are often free.
- **Easy to say.** Spelled as spoken, stress always on the second-to-last syllable (*li-bro-te-NA-do*).

Building blocks that make good names:

| Ending | Meaning | Example |
|---|---|---|
| `-o` | noun | *kerno* – core, *libro* – book |
| `-ado` | ongoing action | *spezado* – turnover going on, *librotenado* – bookkeeping |
| `-ejo` | place for | *lernejo* – school (*lerni*, to learn) |
| `-ilo` | tool for | *tranĉilo* – knife (*tranĉi*, to cut) |
| `-isto` | someone who does it as a job | *programisto* – programmer |
| `-aro` | a collection of | *vortaro* – dictionary (*vorto*, word) |
| `-ujo` | container for | *monujo* – purse (*mono*, money) |

Rules on top of the ones above: **no letters with diacritics** (ĉ, ĝ, ĥ, ĵ, ŝ, ŭ) – the name has to be ASCII, so
choose a word without them rather than dropping the accent; check that the word means nothing unwanted in other
languages; and have the meaning confirmed by someone who speaks Esperanto (OPEN until then). Esperanto is a
suggestion, not a rule – German compounds (notenwart) and other invented words remain just as welcome.

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
| **.eu** | only if it fits the topic – data protection, digital sovereignty (kernoid) | redirect, or main domain for a European audience |
| **.de** | only if Germany matters – a German company (falkOSS), a German name or German pilot users (notenwart) | redirect |
| **.com** | nice to have – if it is cheap or only parked | redirect |

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
