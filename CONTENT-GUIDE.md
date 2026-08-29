# Content guide

Everything on this site is plain HTML. There is no build step, no framework, and
nothing to install. Edit a file, commit, push. GitHub Actions checks it and
publishes it automatically, usually within a minute.

**After any edit, run the checker.** It catches broken links, dead anchors, and
navigation that has drifted out of sync between pages:

```bash
python check.py
```

To preview locally before pushing:

```bash
python -m http.server 4173
```

Then open <http://localhost:4173>.

> The same checker runs in CI on every push. If it fails, **the site is not
> deployed** and the previous version stays live, so a broken edit can never
> take the site down.

---

## Where things live

| File | What it holds |
|---|---|
| `index.html` | Photo, bio, research interests, **News**, selected publications, contact |
| `research.html` | Research overview, the three research threads, current and past projects |
| `publications.html` | The full publication list with DOIs and BibTeX |
| `teaching.html` | Courses, research supervision, mentoring |
| `notes.html` | Index of written notes |
| `notes/*.html` | One file per note |
| `cv.html` | Web version of the CV; links to the PDF |
| `assets/cv/` | The PDF CV |
| `assets/css/style.css` | All styling. Colours live in the `:root` block at the top |
| `assets/js/main.js` | Theme toggle, footer year and date, news collapse, BibTeX copy, back-to-top |
| `check.py` | Consistency checker. Also regenerates `sitemap.xml` |

---

## Add a news item

Open `index.html`, find `<!-- ===== NEWS`, and paste this as the **first** `<li>`
in the list (newest first):

```html
<li>
  <time datetime="2026-11">Nov 2026</time>
  <p>Short sentence describing what happened.</p>
</li>
```

You do not need to delete anything: past six items the older entries collapse
behind a toggle automatically. The `datetime` attribute should be `YYYY` or
`YYYY-MM`; the visible text between the tags can be written however you like.

---

## Add a publication

This is the one edit that touches **two** files. `check.py` fails if you forget
the second one, so you cannot ship a mismatch by accident.

### 1. `publications.html`: the canonical entry

Find `<!-- ===== PUBLICATION ENTRY` and copy the whole `<article>` block. Give it
a **unique** `id`, and put it in the right year section (add a new
`<section id="y2027"><h2>2027</h2>` if the year does not exist yet).

```html
<article class="pub" id="pub-shortname-2027">
  <span class="tag">Journal</span>
  <h3 class="pub__title">Title of the paper</h3>
  <p class="pub__authors">First Author, <span class="me">Md. Forhan Shahriar Fahim</span>, Last Author</p>
  <p class="pub__venue">Venue name, vol. 1, no. 1, pp. 1&ndash;10, 2027</p>
  <div class="pub__actions">
    <a class="btn-link" href="https://doi.org/DOI-HERE" target="_blank" rel="noopener">DOI</a>
    <details class="bibtex">
      <summary>BibTeX</summary>
    <pre><code>@article{key2027short,
  author  = {Surname, Given Names and Fahim, Md. Forhan Shahriar},
  title   = {Title of the paper},
  journal = {Venue name},
  year    = {2027},
  doi     = {DOI-HERE}
}</code></pre>
    </details>
  </div>
</article>
```

- Use `<span class="tag">Journal</span>` for journals and
  `<span class="tag tag--muted">Conference</span>` for conferences.
- `<span class="me">` is what bolds your own name. Keep it on your name only.
- Add `<a class="btn-link" href="...">PDF</a>` next to the DOI link if you have a
  preprint to host.

Also update the `ItemList` JSON-LD block in the `<head>` of the same file. It is
what search engines read. Copy the last `ListItem`, bump `"position"`, and change
the title, authors, venue, and `sameAs` DOI.

### 2. `index.html`: the homepage summary

Paste the **same** `<article>` block into `<section id="publications">`, but
**delete the `<details class="bibtex">` part** and the `id`. The homepage shows a
short list; the full record with BibTeX stays on `publications.html`.

Then run `python check.py` to confirm the two lists agree.

---

## Add a note

### 1. Create the post file

Copy `notes/ml-pipeline-common-mistakes.html` to a new file in `notes/` and
replace the content. Two things matter:

- **Post pages use root-absolute paths** (`/assets/css/style.css`,
  `/index.html`), not relative ones, because they sit one directory down. Keep
  them exactly as they are in the copied file. `check.py` compares the
  navigation across every page and will tell you if you break it.
- Update the `<title>`, `<meta name="description">`, `og:` tags, the `canonical`
  link, and the `BlogPosting` JSON-LD block at the top.

Components available inside a post:

```html
<!-- A numbered stage with a highlighted pitfall -->
<ol class="stages">
  <li class="stage">
    <div>
      <h3>Stage heading</h3>
      <p>Explanation.</p>
      <p class="stage__mistake"><strong>Common mistake:</strong> what goes wrong.</p>
    </div>
  </li>
</ol>

<!-- A standalone warning box -->
<div class="pitfall">
  <h4>Short label</h4>
  <p>The warning.</p>
</div>

<!-- A checklist -->
<ul class="checklist"><li>An item.</li></ul>
```

Ordinary `<p>`, `<h2>`, `<h3>`, `<blockquote>`, `<pre><code>`, and
`<figure>`/`<figcaption>` are all styled already.

### 2. List it on `notes.html`

Copy the `<li class="note-card">` block and edit the title, link, date, reading
time, and summary. The little SVG thumbnail is inline: change the shapes or
reuse it as-is.

### 3. Update the sitemap

```bash
python check.py --write-sitemap
```

This regenerates `sitemap.xml` from the files that actually exist. CI fails if
you forget, so it will not silently go stale.

---

## House style

- **Never use an em dash (`&mdash;`).** Rewrite with a colon, semicolon, comma,
  parentheses, or two sentences. Runs of em-dash asides make prose read as
  machine-written.
- En dashes (`&ndash;`) are correct and stay, but only in ranges
  (`2019&ndash;2024`, `pp. 1&ndash;6`) and compounds (`CNN&ndash;LSTM`).
- British spelling throughout.

## News grows on its own

Add `<li>` entries to the top of the list on `index.html` and stop thinking
about it. Once there are more than six, `main.js` collapses the older ones
behind a "Show earlier updates" button, so the homepage never gets long, and
nothing needs pruning by hand.

## Add an award, course, or project

These are ordinary lists. Copy a neighbouring `<li>`, `<div class="entry">`, or
`<div class="row">` and edit the text. The pattern for a dated entry is:

```html
<div class="entry">
  <div class="entry__head">
    <h3 class="entry__title">Title</h3>
    <span class="entry__date">Jan 2027 &ndash; present</span>
  </div>
  <p class="entry__sub">Role or subtitle</p>
  <ul>
    <li>What you did.</li>
  </ul>
</div>
```

---

## Replace the CV PDF

Overwrite `assets/cv/Md_Forhan_Shahriar_Fahim_CV.pdf`, keeping the same filename.
Nothing else needs changing; every link points at that path.

## Change the photo

Replace `assets/img/profile.jpg`. Use a **square** image, ideally 600×600 or
larger; anything else is centre-cropped by CSS. Keep the filename.

---

## Change the colours

Everything is defined once, at the top of `assets/css/style.css`:

```css
:root {
  --accent: #1d4e89;   /* links, current-page underline, buttons */
  --warn:   #a1442a;   /* pitfall callouts in notes */
  --bg:     #fdfdfc;   /* page background */
  --text:   #1a1a1a;   /* body text */
}
```

If you change a colour, change it in **all three** places: the `:root` block,
the `@media (prefers-color-scheme: dark)` block, and the `:root[data-theme="dark"]`
block. The last two are what make the dark theme and the manual toggle work.

Keep contrast at 4.5:1 or better against the background. `--text-faint` is
already at the limit; do not lighten it further.

---

## Editing the navigation

The nav and footer are copied into every page deliberately, because injecting them with
JavaScript would hide them from search engines and break the page for anyone with
JavaScript disabled.

If you add or rename a page, edit the `<nav>` block in **every** `.html` file
including the ones in `notes/`, then run `python check.py`, which compares them
and fails on any difference. Post pages and `404.html` use root-absolute paths
(`/research.html`); the checker normalises that before comparing.

Then regenerate the sitemap with `python check.py --write-sitemap`.

---

## Personal details used across the site

If any of these change, search and replace across all `.html` files:

| Item | Value |
|---|---|
| Email | `forhan.shahriar.fahim@gmail.com` |
| Google Scholar | `https://scholar.google.com/citations?user=jkZQkCYAAAAJ&hl=en` |
| ORCID | `https://orcid.org/0009-0006-8705-4598` |
| GitHub | `https://github.com/ForhanShahriarFahim` |
| LinkedIn | `https://www.linkedin.com/in/forhanshahriarfahim/` |
| Site URL | `https://forhanshahriarfahim.github.io/` |

The PhD application year (`Fall 2027`) appears once, in the third About paragraph
on `index.html`. Update or remove it once you have decisions.
