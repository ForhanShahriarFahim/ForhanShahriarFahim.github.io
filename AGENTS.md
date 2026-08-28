# Agent instructions

Personal academic website for Md. Forhan Shahriar Fahim, used for US PhD
applications. The audience is faculty and admissions committees, so the site
must read as a researcher's page — plain, quiet, and fast — not as a developer
portfolio.

Read this before changing anything. `CONTENT-GUIDE.md` covers routine content
edits in more detail.

## Hard rules

1. **No build step, no dependencies, no frameworks.** Plain HTML, one CSS file,
   one small vanilla JS file. Do not add npm, Jekyll, Hugo, Tailwind, React, or
   any CDN `<script>`/`<link>`. The only external request is Google Fonts, and
   every font has a local fallback stack.
2. **Run `python check.py` after every change.** It is the safety net for the
   duplicated markup described below. CI runs it too; a failure blocks deploy.
3. **The `<nav>` and `<footer>` blocks are byte-identical across all pages,
   on purpose.** Injecting them with JavaScript would hide them from search
   engines and break no-JS rendering. If you touch one, touch all of them
   (`*.html` and `notes/*.html`) and let `check.py` confirm they match.
4. **Pages in `notes/` use root-absolute paths** (`/assets/css/style.css`,
   `/index.html`), because they sit one directory below the root. `404.html`
   does the same. Root pages use relative paths. `check.py` normalises this
   before comparing navigation.
5. **Colours are defined in three places** in `assets/css/style.css`: the
   `:root` block, the `@media (prefers-color-scheme: dark)` block, and the
   `:root[data-theme="dark"]` block. Changing one without the others breaks
   either the dark theme or the manual toggle.
6. **Keep text contrast at 4.5:1 or better** against its background, in both
   themes. `--text-faint` is already at the floor; do not lighten it.
7. **Never persist a theme to `localStorage` on page load** — only on an
   explicit click. Writing on load pins the site to whatever the OS happened to
   be on the first visit and stops it following the system afterwards.
8. **Do not publish personal contact details beyond email.** No phone number, no
   home address, and no referees' email addresses on the site. Those stay in the
   PDF CV only.

## Tone and content

- Understated and factual. No marketing language, no emoji, no exclamation
  marks, no claims the CV does not support.
- British spelling is used throughout the prose.
- Research framing: one question — making deep models legible and
  label-efficient enough to trust in high-stakes settings — across three threads:
  interpretability, computer vision, and health/medical AI. The published
  vulnerability-detection papers belong under interpretability, because that is
  what they actually are (LIME, explainable multi-task transformers).
- Web-development projects and competitive-programming ratings stay at the
  bottom of `cv.html` only. They must not appear on the homepage or the research
  page; leading with them signals "web developer" rather than "researcher".

## Layout

```
index.html            About, interests, news, selected publications
research.html         Overview, three threads, current and past projects
publications.html     Full list with DOIs and BibTeX; ItemList JSON-LD in <head>
teaching.html         Courses, supervision, mentoring
notes.html            Index of notes
notes/*.html          One file per note (root-absolute paths)
cv.html               Web CV; links to the PDF
404.html              Not-found page (root-absolute paths)
check.py              Consistency checker; also regenerates sitemap.xml
assets/css/style.css  All styling. Numbered sections; tokens at the top
assets/js/main.js     Theme toggle and footer year only
.github/workflows/    Check-then-deploy to GitHub Pages
```

## Reusable components

Defined in `assets/css/style.css` — prefer these over new CSS:

| Class | Use |
|---|---|
| `.entry` + `.entry__head/__title/__date/__sub` | A dated CV-style item |
| `.timeline` wrapping `.entry` items | Vertical rail with a node per entry |
| `.pub` + `.pub__title/__authors/__venue/__links` | A publication record |
| `.tag`, `.tag--muted` | Journal / Conference chips |
| `.rows` + `.row` (`<dl>`) | Label-and-value pairs, e.g. skills |
| `.news` | Dated news list on the homepage |
| `.stages` + `.stage` + `.stage__mistake` | Numbered walkthrough in a note |
| `.pitfall` | Warning callout in a note |
| `.checklist` | Checklist with square markers |
| `.callout` + `.btn` | Boxed row with an action, e.g. CV download |

## Verifying

```bash
python check.py                  # links, anchors, nav/footer drift, metadata
python check.py --write-sitemap  # regenerate sitemap.xml after adding a page
python -m http.server 4173       # local preview
```

Check both themes and at least 375px, 780px, and 1100px widths after any layout
change. The navigation collapses to two rows below 780px and must never wrap its
link row.

## Deploying

Push to `main`. `.github/workflows/deploy.yml` runs `check.py`, and publishes to
GitHub Pages only if it passes. Pages source must be set to **GitHub Actions**
(not "deploy from a branch"). No manual step is needed.

## Facts

Do not invent credentials. Current, verified values:

- Lecturer, Dept. of CSE, Pundra University of Science & Technology (Mar 2025–)
- B.Sc. CSE, University of Rajshahi, 2019–2024, CGPA 3.66
- Three publications, all 2026 — see `publications.html` for exact records
- Email `forhan.shahriar.fahim@gmail.com` · ORCID `0009-0006-8705-4598`
- Scholar `jkZQkCYAAAAJ` · GitHub & LinkedIn `ForhanShahriarFahim` /
  `forhanshahriarfahim`
