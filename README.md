# forhanshahriarfahim.github.io

Personal academic website of **Md. Forhan Shahriar Fahim**, Lecturer in Computer
Science & Engineering, Pundra University of Science & Technology.

Live at <https://forhanshahriarfahim.github.io/>

## Stack

Plain HTML, one CSS file, and a small vanilla JavaScript file. No build step, no
dependencies, no framework.

```
index.html          About, research interests, news, selected publications
research.html       Research overview, threads, current and past projects
publications.html   Full publication list with DOIs and BibTeX
teaching.html       Courses, supervision, mentoring
notes.html          Index of written notes
notes/              One file per note
cv.html             Web CV, links to the PDF
404.html            Not-found page
check.py            Consistency checker; run after every edit
assets/
  css/style.css     All styling; design tokens at the top
  js/main.js        Theme toggle and footer year
  img/              Profile photo and favicon
  cv/               PDF CV
```

## Working on it

Preview locally:

```bash
python -m http.server 4173
```

Check for broken links, dead anchors, and navigation drift:

```bash
python check.py
```

Regenerate `sitemap.xml` after adding a page:

```bash
python check.py --write-sitemap
```

- [CONTENT-GUIDE.md](CONTENT-GUIDE.md): how to add a publication, news item, or note.
- [AGENTS.md](AGENTS.md): conventions and hard rules for AI coding agents.
- [DECISIONS.md](DECISIONS.md): why the site is built this way, and what was rejected.

## Deploying

Push to `main`. [`.github/workflows/deploy.yml`](.github/workflows/deploy.yml)
runs `check.py` and publishes to GitHub Pages **only if it passes**, so a broken
edit fails the build instead of taking the live site down. Nothing else is
needed; there is no manual deploy step.

Pages source is set to **GitHub Actions** under *Settings → Pages*.

## Features worth knowing about

- **Dark mode** follows the operating system and can be overridden with the nav
  toggle; the choice persists in `localStorage`, and nothing is written there
  until you actually click, so the site keeps following the OS otherwise.
- **Structured data**: `schema.org` `Person` on the homepage, `ScholarlyArticle`
  on the publications page, `BlogPosting` on notes.
- **Accessible**: semantic landmarks, a skip link, visible focus rings, and
  AA-contrast colours verified in both themes.
- **Prints cleanly**: the CV page drops navigation and chrome when printed.
