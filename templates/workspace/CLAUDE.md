# CLAUDE.md – {{name}}-Arbeitsordner (privat)

Dieser Ordner ist **kein** Git-Repository und wird nie veröffentlicht. Er bündelt die Checkouts der
GitHub-Organisation `{{name}}`. Repo-spezifisches Wissen gehört in die `CLAUDE.md`-Dateien der Repos – die werden
öffentlich, deshalb gehört alles Persönliche hierher. Angelegt {{date}} mit `falkoss/starterpack` (`bin/new-project`).

## Worum es geht

**{{name}}** – {{tagline}}. Ein falkOSS-Projekt (Beschluss der Gesellschafter: OFFEN).
<!-- OFFEN: Zweck, Zielgruppe, Abgrenzung; Herkunft und Bedeutung des Namens. -->

| Ordner | Repo | Inhalt |
|---|---|---|
| `{{name}}/` | `{{name}}/{{name}}` | Software und Brand-Kit (`brand/`, vorläufig) – **{{licence}}**. Regeln: `{{name}}/CLAUDE.md` |
{{#whitepaper}}
| `whitepaper/` | `{{name}}/whitepaper` | Whitepaper (Markdown → Typst → PDF, `build.sh`), Text **{{doc_licence_label}}** |
{{/whitepaper}}
| `website/` | `{{name}}/website` | One-Page (GitHub Pages), Englisch; Impressum/Datenschutz verlinkt auf falkoss.org |
| `.github/` | `{{name}}/.github` | Org-Profil |

**Stand {{date}}:** lokal angelegt, je ein Commit, **nicht gepusht**. Organisation und Repos auf GitHub: OFFEN
(legt der Maintainer an, privat). Vorschau der Website: `preview_start` mit `{{name}}-website` (Port {{port}}).

## Name und Domains

Prüfung mit `falkoss/starterpack/bin/check-name {{name}}{{check_flags}}` – Ergebnis mit Datum hier eintragen.
Hauptdomain: **{{main_domain}}** (Website), **{{docs_domain}}** (Doku). Pflicht: {{required_domains}}.
Registriert: OFFEN. Markenrecherche (DPMA, EUIPO, TMview, WIPO; Klassen 9/42): OFFEN.

## Zugang

- Token: `~/.{{name}}/developer/agent.env` enthält `GITHUB_TOKEN` (fine-grained, Org `{{name}}`: Contents,
  Workflows, Actions je Read and write; Ablaufdatum: OFFEN). **Nie ausgeben, loggen oder in Dateien/Repos/Commits
  kopieren.** Pushen mit leerem Helper vorweg:
  `set -a; . ~/.{{name}}/developer/agent.env; set +a; git -c credential.helper= -c credential.helper='!f() { echo username=x-access-token; echo "password=$GITHUB_TOKEN"; }; f' push`
- `gh`: `nix run nixpkgs#gh --` mit `GH_TOKEN=$GITHUB_TOKEN`.
- Repo-Einstellungen (Sichtbarkeit, Pages, Domains, Secrets) macht der Maintainer, nicht das Token.

## Regeln

- Mit dem Maintainer Deutsch; in den Repos alles Englisch (Code, Doku, Commits).
- Keine persönlichen Daten in getrackten Dateien. Nichts löschen – nach `_to_delete/` verschieben.
- Belegt vor behauptet; Unbelegtes als `OPEN`/`OFFEN` markieren.
- Kein Tracking, keine Telemetrie, keine extern geladenen Schriften/Skripte. Alles inklusive.
- Commits mit Sign-off (`-s`, DCO), **pushen nur nach Rückfrage**.
- Vor dem Public-Schalten Historien auf einen Commit zurücksetzen (`falkoss/starterpack/docs/setup.md`, Schritt 10).
