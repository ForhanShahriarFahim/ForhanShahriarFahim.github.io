# Agent instructions

Personal academic website for Md. Forhan Shahriar Fahim, used for US PhD
applications. The audience is faculty and admissions committees, so the site
must read as a researcher's page: plain, quiet, and fast, not a developer
portfolio.

Read this before changing anything.

- `CONTEXT.md` is the shared, current orientation to the site and its source
  files. Read it at the start of every task and update it when a durable fact,
  page, workflow, or project status changes.
- `DECISIONS.md` explains *why* the site is built this way, including what was
  tried and rejected. Read it before proposing something this file forbids.
- `CONTENT-GUIDE.md` covers routine content edits in more detail.
- `ONE-PAGE-ROADMAP.md` holds the condensed design, implementation history,
  and next action. Read its Current task, R13, and Next task before continuing.

The R11 mockup is historical visual guidance, not current site behaviour.
R11a-e, R12a-c, and R13a-c are implemented and owner reviewed; release status
and integrated checks are recorded in the roadmap.
The owner subsequently grouped the three research sections under one Research
nav link and changed Community to a direct News anchor. Begin at the roadmap's
Next task when continuing; do not paste the mockup over the production page.

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
   (`*.html` and `blog/*.html`) and let `check.py` confirm they match.
4. **Pages in `blog/` use root-absolute paths** (`/assets/css/style.css`,
   `/index.html`), because they sit one directory below the root. `404.html`
   does the same. Root pages use relative paths. `check.py` normalises this
   before comparing navigation.
5. **Colours are defined in three places** in `assets/css/style.css`: the
   `:root` block, the `@media (prefers-color-scheme: dark)` block, and the
   `:root[data-theme="dark"]` block. Changing one without the others breaks
   either the dark theme or the manual toggle.
6. **Keep text contrast at 4.5:1 or better** against its background, in both
   themes. `--text-faint` is already at the floor; do not lighten it.
7. **Never persist a theme to `localStorage` on page load.** Only on an
   explicit click. Writing on load pins the site to whatever the OS happened to
   be on the first visit and stops it following the system afterwards.
8. **Do not publish personal contact details beyond email.** No phone number, no
   home address, and no referees' email addresses on the site. Those stay in the
   PDF CV only.
9. **The theme toggle is a sibling of `.site-nav__links` and
   `.site-nav__menu`, not inside either.** On phones it shares the first row
   with the name; the full section menu occupies the second row. On desktop
   it sits to the right of the top navigation.
10. **No em dashes anywhere.** Use a colon, semicolon, comma, parentheses, or a
   full stop instead. Strings of em-dash asides read as machine-written, which
   is the last impression this site should give. En dashes stay, but only for
   ranges (`2019&ndash;2024`, `pp. 1&ndash;6`) and compounds (`CNN&ndash;LSTM`).
   `grep -c mdash *.html blog/*.html` must return zero.
11. **Write CSS escapes with six hex digits** (`"\0000B7"`). A four-digit form
   generated through a script once produced a literal NUL byte that rendered as
   visible mojibake. `check.py` now fails on NUL bytes and U+FFFD.

## Tone and content

- Understated and factual. No marketing language, no emoji, no exclamation
  marks, no claims unsupported by the CV or an explicit owner statement.
- British spelling is used throughout the prose.
- Research framing: interest in what AI models learn, why they make certain
  predictions, and where they fail, across four stated interests: AI safety and interpretability,
  computer vision, large language models, and vision-language models. The
  owner is seeking PhD opportunities beginning in Fall 2028. Language and
  vision-language models are interests, not claims of completed work. The published
  vulnerability-detection papers belong under interpretability, because that is
  what they actually are (LIME, explainable multi-task transformers).
- The owner explicitly asked for the May–December 2025 AMIR Lab internship in
  HTML, based on his account of work on the cancer-imaging review. The 29
  September PDF omits AMIR and removes the ELITE entry from its earlier version.
  The YOLO crop-disease project has ended and should not be presented as
  current work.
- The homepage Projects section contains selected built projects from the
  updated CV and GitHub, not the EMG thesis, systematic review, or students'
  supervised research. CSE Academic Operations Hub and BookHive are two concise
  software records after the research sections.
  Do not present them as PhD research. Competitive-programming ratings stay at
  the bottom of `cv.html` only.

## Layout

```
index.html            One-page academic profile: About, research interests,
                      full publications + ItemList JSON-LD, research work,
                      education, awards, experience (including teaching and
                      supervision), projects,
                      News and Updates, Blog, contact
research.html         Overview, four interests, recent and earlier work
publications.html     Legacy publication URL bridge with old bookmark anchors;
                      complete records live on the homepage
teaching.html         Courses, supervision, mentoring
blog.html           Index of posts
blog/*.html        One file per post (root-absolute paths)
cv.html               Web CV; links to the PDF
404.html              Not-found page (root-absolute paths)
check.py              Consistency checker; also regenerates sitemap.xml
assets/css/style.css  All styling. Numbered sections; tokens at the top
assets/js/main.js     Theme, dates, recent-news expansion, back-to-top,
                      homepage scroll tracking, legacy publication URL routing
.github/workflows/    Check-then-deploy to GitHub Pages
```

## Reusable components

Defined in `assets/css/style.css`. Prefer these over new CSS:

| Class | Use |
|---|---|
| `.entry` + `.entry__head/__title/__date/__sub` | A dated CV-style item |
| `.timeline` wrapping `.entry` items | Vertical rail with a node per entry |
| `.education-record`, `.awards-list` | Homepage degree timeline and separate awards |
| `.research-interest-list` | Compact four-interest homepage line; detail stays on `research.html` |
| `.role-list` + `.role` + `.role__details` | Separate Experience roles; Teaching and Supervision rows under Lecturer |
| `.project-cards` + `.project-card` | Two whole-card GitHub links for undated software projects |
| `.pub` + `.pub__date-status/__body/__title/__authors/__venue` | A publication row with year, status, and complete citation |
| `.rows` + `.row` (`<dl>`) | Label-and-value pairs, e.g. skills |
| `.news-window` + `.news` | Fixed-height scroll region and dated news list on the homepage |
| `.stages` + `.stage` + `.stage__mistake` | Numbered walkthrough in a note |
| `.pitfall` | Warning callout in a note |
| `.checklist` | Checklist with square markers |
| `.callout` + `.btn` | Boxed row with an action, e.g. PDF CV view |
| `.to-top` | Back-to-top button, injected by main.js on every page |

## Behaviour that lives in main.js, not markup

These are injected at runtime so no page carries duplicate HTML, and so readers
without scripting are never shown a control that could not work:

- the back-to-top button,
- the homepage scroll-progress line and current-section navigation state,
- Blog preview scrolling starts only after three homepage post entries; the
  archive link goes to `blog.html`. The News list is always scrollable in HTML
  and CSS, including without JavaScript; print expands it,
- the footer year and the "Last updated" date, which reads the page's own
  `Last-Modified` header.

## Verifying

```bash
python check.py                  # links, anchors, nav/footer drift, metadata
python check.py --write-sitemap  # regenerate sitemap.xml after adding a page
python -m http.server 4173       # local preview
```

Check both themes and at least 375px, 780px, and 1100px widths after any layout
change. At 1120px and above the top bar shows direct academic links and a
direct Community link to News and Updates; below that the full section map is
in a Sections disclosure. At 780px and below the name/toggle and menu
occupy separate rows. Keep every menu link reachable without JavaScript.

## Deploying

Push to `main`. `.github/workflows/deploy.yml` runs `check.py`, and publishes to
GitHub Pages only if it passes. Pages source must be set to **GitHub Actions**
(not "deploy from a branch"). No manual step is needed.

## Facts

Do not invent credentials. Current, verified values:

- Lecturer, Dept. of CSE, Pundra University of Science & Technology (Mar 2025–)
- B.Sc. CSE, University of Rajshahi, 2019–2024, CGPA 3.66
- Three published papers and one accepted conference paper, all 2026. See
  `index.html` for canonical visible records and status
- Email `forhan.shahriar.fahim@gmail.com` · ORCID `0009-0006-8705-4598`
- Scholar `jkZQkCYAAAAJ` · GitHub & LinkedIn `ForhanShahriarFahim` /
  `forhanshahriarfahim`
