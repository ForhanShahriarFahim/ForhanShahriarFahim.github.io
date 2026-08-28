# Content guide

Everything on this site is plain HTML. There is no build step, no framework, and
nothing to install. Edit a file, save, commit, push — GitHub Pages republishes in
about a minute.

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

---

## Where things live

| File | What it holds |
|---|---|
| `index.html` | Photo, bio, research interests, **News**, selected publications, contact |
| `research.html` | Research overview, the three research threads, current and past projects |
| `publications.html` | The full publication list with DOIs and BibTeX |
| `teaching.html` | Courses, research supervision, mentoring |
| `cv.html` | Web version of the CV; links to the PDF |
| `assets/cv/` | The PDF CV |
| `assets/css/style.css` | All styling. Colours live in the `:root` block at the top |
| `assets/js/main.js` | Theme toggle and the footer year. Nothing else |

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

Keep the list to roughly six items — delete from the bottom as you add to the top.
The `datetime` attribute should be `YYYY` or `YYYY-MM`; the visible text between
the tags can be written however you like.

---

## Add a publication

This is the one edit that touches **two** files. `check.py` will fail if you
forget the second one, so you cannot ship a mismatch by accident.

### 1. `publications.html` — the canonical entry

Find `<!-- ===== PUBLICATION ENTRY` and copy the whole `<article>` block. Give it
a **unique** `id`, and put it in the right year section (add a new
`<section id="y2027"><h2>2027</h2>` if the year does not exist yet).

```html
<article class="pub" id="pub-shortname-2027">
  <span class="tag">Journal</span>
  <h3 class="pub__title">Title of the paper</h3>
  <p class="pub__authors">First Author, <span class="me">Md. Forhan Shahriar Fahim</span>, Last Author</p>
  <p class="pub__venue">Venue name, vol. 1, no. 1, pp. 1&ndash;10, 2027</p>
  <div class="pub__links">
    <a class="btn-link" href="https://doi.org/DOI-HERE" target="_blank" rel="noopener">DOI</a>
  </div>
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
</article>
```

- Use `<span class="tag">Journal</span>` for journals and
  `<span class="tag tag--muted">Conference</span>` for conferences.
- `<span class="me">` is what bolds your own name. Keep it on your name only.
- Add a `<a class="btn-link" href="...">PDF</a>` next to the DOI link if you have
  a preprint to host.

Also update the `ItemList` JSON-LD block in the `<head>` of the same file — it is
what search engines read. Copy the last `ListItem`, bump `"position"`, and change
the title, authors, venue, and `sameAs` DOI.

### 2. `index.html` — the homepage summary

Paste the **same** `<article>` block into the `<section id="publications">`, but
**delete the `<details class="bibtex">` part** and the `id`. The homepage shows a
short list; the full record with BibTeX stays on `publications.html`.

Then run `python check.py` to confirm the two lists agree.

---

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
Nothing else needs changing — every link points at that path.

---

## Change the photo

Replace `assets/img/profile.jpg`. Use a **square** image, ideally 600×600 or
larger; anything else will be centre-cropped by CSS. Keep the filename.

---

## Change the colours

Everything is defined once, at the top of `assets/css/style.css`:

```css
:root {
  --accent: #1d4e89;   /* links, current-page underline, buttons */
  --bg:     #fdfdfc;   /* page background */
  --text:   #1a1a1a;   /* body text */
}
```

If you change a colour, change it in **all three** places — the `:root` block,
the `@media (prefers-color-scheme: dark)` block, and the `:root[data-theme="dark"]`
block. The last two are what make the dark theme and the manual toggle work.

---

## Editing the navigation

The nav and footer are copied into all six pages deliberately — injecting them
with JavaScript would hide them from search engines and break the page for anyone
with JavaScript disabled.

If you add or rename a page, edit the `<nav>` block in **every** `.html` file, then
run `python check.py`, which compares them and fails on any difference. Note that
`404.html` uses absolute paths (`/research.html`) because it can be served from any
URL depth; the checker accounts for this.

Remember to add the new page to `sitemap.xml` too — the checker verifies that as well.

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
