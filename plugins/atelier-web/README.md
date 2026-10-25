# Atelier web

Atelier web is a Claude Code plugin for designing and building beautiful, high-converting landing pages and web pages that match each brand exactly. Each project writes its brand doctrine once in `atelier/marque/` (colors, fonts, voice, allowed proof points, site components), and every skill reads it before producing anything. Skills are written in French; Claude builds pages in any language.

Full documentation, screenshots and installation: https://github.com/Littlpinguin/atelier-web

## What it contains

- **24 skills**: project setup (`demarrer-projet-web`), an 8-phase landing page playbook (`landing-page`), pages on an existing site (`page-web`), lead magnets, design direction and design systems, motion and scroll animation, conversion (page, form, popup, pricing), copywriting, rendering QA, accessibility, design review and a final brand check.
- **7 agents**: visual research, parallel section builders, and design, brand, conversion and accessibility reviewers.
- **A factory** (`fabrique/`): 44 slot-based landing sections, 6 landing templates, 10 interactive lead magnets, and Python scripts to assemble pages, measure the render, derive CSS tokens and lint brand compliance.
- **A hook**: after Claude writes a page under `atelier/`, directly or through a script such as `assemble-landing.py`, it runs the local brand linter and reminds Claude to run the brand check. It stays silent in projects without a brand doctrine and never blocks a tool call.
- **An eval suite** (`evals/`): `claude plugin eval` cases for routing, skill triggering, requests that must not trigger, and one end-to-end landing page, with a fictional brand doctrine as fixture.

## Getting started

Install from its marketplace (Claude Code 2.1.275 or later):

```
/plugin install atelier-web --marketplace Littlpinguin/atelier-web
```

Open Claude Code in your website's folder and run `/atelier-web:demarrer-projet-web`, then `/atelier-web:landing-page` or `/atelier-web:page-web`.

## What the plugin runs, sends and fetches

- **Scripts** (`fabrique/scripts/`) run locally with Python when a skill asks Claude to run them. They read the current project and write only the files you ask for (a page, generated CSS tokens). They send nothing over the network.
- **The hook** (`hooks/rappel-brand-check.py`) runs locally after Write and Edit calls on Markdown or HTML files under `atelier/`, and after Bash commands that mention `atelier`: for those, it looks under `atelier/` for Markdown and HTML files changed since their last check. It runs the local linter and adds its findings to Claude's context. It keeps a small per-session register of checked files in the system temporary directory, and sends nothing over the network.
- **The eval suite** (`evals/`) runs only when you call `claude plugin eval`; its fixture is a fictional brand, with no real person or client data.
- **Assembled pages** link Google Fonts (`fonts.googleapis.com`, `fonts.gstatic.com`) when their spec lists fonts, and load Google Tag Manager or Google Analytics only if you configure a tracking ID in the spec. Forms post to the endpoint you set. Visitors' browsers make these requests, not the plugin.
- **Rendering QA** (`qa-landing.py`, `controle-fonds.py`) opens your pages in a local headless Chromium through Playwright, which loads the fonts and resources those pages reference.
- **The research agent** (`landing-researcher`) reads public web pages (search results, design galleries) to collect inspiration, through Claude Code's own web tools. It never logs in anywhere and collects no personal data.
- No telemetry, no analytics, no account.

## License

MIT (see `LICENSE`). Some skills are adapted from third-party MIT and Apache-2.0 projects; each keeps its attribution footer, and provenance registers are in `docs/sources/`.
