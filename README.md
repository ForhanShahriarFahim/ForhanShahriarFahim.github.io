# forhanshahriarfahim.github.io

Personal academic website of **Md. Forhan Shahriar Fahim** — Lecturer in Computer
Science & Engineering, Pundra University of Science & Technology.

Live at <https://forhanshahriarfahim.github.io/>

## Stack

Plain HTML, one CSS file, and about forty lines of vanilla JavaScript. No build
step, no dependencies, no framework. GitHub Pages serves the files exactly as they
are committed.

```
index.html          About, research interests, news, selected publications
research.html       Research overview, threads, current and past projects
publications.html   Full publication list with DOIs and BibTeX
teaching.html       Courses, supervision, mentoring
cv.html             Web CV, links to the PDF
404.html            Not-found page
check.py            Consistency checker — run after every edit
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

Editing instructions — how to add a publication, a news item, an award — are in
[CONTENT-GUIDE.md](CONTENT-GUIDE.md).

## Deploying

Commit and push to `main`. GitHub Pages rebuilds automatically, usually within a
minute. Pages is configured under *Settings → Pages → Deploy from a branch →
`main` → `/ (root)`*.

## Features worth knowing about

- **Dark mode** follows the operating system by default and can be overridden with
  the toggle in the navigation bar; the choice persists in `localStorage`.
- **Structured data** — `schema.org` `Person` markup on the homepage and
  `ScholarlyArticle` markup on the publications page, so search engines link the
  profile and papers correctly.
- **Accessible** — semantic landmarks, a skip link, visible focus rings, and
  AA-contrast colours in both themes.
- **Prints cleanly** — the CV page drops the navigation and chrome when printed.
