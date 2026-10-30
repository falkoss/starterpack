<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/{{name}}-lockup-on-dark.svg">
    <img src="assets/{{name}}-lockup-on-light.svg" alt="{{name}}" width="480">
  </picture>
</p>

<p align="center"><b>{{tagline}}.</b><br>
<sub>a <a href="https://falkoss.org">falkOSS</a> project</sub></p>

<!-- OPEN: two or three sentences – what it is and for whom. -->
**{{name}}** is free software – everything included, no telemetry.

{{#whitepaper}}
> {{name}} is at its beginning: there is nothing to install yet. Start with the
> [whitepaper](https://github.com/{{name}}/whitepaper).
{{/whitepaper}}
{{^whitepaper}}
> {{name}} is at its beginning: there is nothing to install yet.
{{/whitepaper}}

### Same rules as falkOSS

- **Free licences** – {{licence}}; contributions with a DCO sign-off, no CLA.
- **Everything included** – one edition, every feature free; no paid tiers, nothing held back.
- **No telemetry** – nothing phones home.
- **In the open** – issues, plans, reviews and decisions happen in public.

### The name

<!-- OPEN: where the name comes from – the same text as on the website, in the README and the whitepaper
     (starterpack docs/naming.md, "Explaining the name"). -->
*…* is … for …

### Repositories

| Repository | What |
|---|---|
| [{{name}}](https://github.com/{{name}}/{{name}}) | the software and its documentation ([{{docs_domain}}](https://{{docs_domain}})) |
| [brand](https://github.com/{{name}}/brand) | the brand kit – logo, colours, icons |
{{#whitepaper}}
| [whitepaper](https://github.com/{{name}}/whitepaper) | the whitepaper – Markdown, set to PDF with Typst |
{{/whitepaper}}
| [website](https://github.com/{{name}}/website) | the landing page |

<sub>{{name}} is free software and a project of <a href="https://falkoss.org">falkOSS</a> – {{publisher}}, from Falkensee.</sub>
