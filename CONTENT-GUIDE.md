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
| `index.html` | One-page academic profile, updates, full publication list, and publication `ItemList` JSON-LD |
| `research.html` | Research overview, four stated interests, current and past projects |
| `publications.html` | Legacy publication URL bridge; title links and old bookmark anchors lead to the homepage |
| `teaching.html` | Courses, research supervision, mentoring |
| `blog.html` | Index of posts |
| `blog/*.html` | One file per post |
| `cv.html` | Web version of the CV; links to the PDF |
| `assets/cv/` | The PDF CV |
| `assets/css/style.css` | All styling. Colours live in the `:root` block at the top |
| `assets/js/main.js` | Theme toggle, footer year and date, news collapse, back-to-top, homepage scroll tracking |
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

You do not need to delete anything: the fixed-height News region scrolls through
every item, including with JavaScript off. Print expands the entire list. The
`datetime` attribute should be `YYYY` or
`YYYY-MM`; the visible text between the tags can be written however you like.

---

## Add a publication

The homepage is the source for all published and accepted records.
`publications.html` is a short bridge for old links and bookmarks, not a second
publication list. `check.py` matches its title links and IDs to the homepage
and checks the homepage `ItemList` against visible titles, years, statuses,
author order, venues, and title links. The web CV still needs a manual citation
review.

### 1. `index.html`: the canonical visible entry

Find `<section id="publications">` and add a complete `<article>` block. Give it
a **unique** `id`. Keep accepted work clearly marked and separate from the
published count in the section introduction.

```html
<article class="pub" id="pub-shortname-2027">
  <div class="pub__date-status"><span class="pub__year">2027</span><span class="pub__status">Published</span></div>
  <div class="pub__body">
    <h3 class="pub__title"><a href="https://doi.org/DOI-HERE" target="_blank" rel="noopener">Title of the paper</a></h3>
    <p class="pub__authors">First Author, <span class="me">Md. Forhan Shahriar Fahim</span>, Last Author</p>
    <p class="pub__venue">Venue name, vol. 1, no. 1, pp. 1&ndash;10, 2027</p>
  </div>
</article>
```

- The year and status form a separate column on desktop and sit above the title
  on phones. The year must match the verified publication or conference year.
- Link the published title to its verified DOI. The arrow appears through CSS;
  do not add an arrow character to the title text. Do not show a separate DOI
  or BibTeX control.
- `<span class="me">` is what bolds your own name. Keep it on your name only.

Also update the `ItemList` JSON-LD block in the `<head>` of `index.html`. Add a
`ListItem`, keep positions consecutive, and match the visible title, author
order, venue, and `sameAs` DOI. This is the machine-readable publication list.

### 2. `publications.html`: the old URL bridge

Add a title link under Accepted or Published work, with the **same** `id` and
title as the homepage article. Its `href` must point to `index.html#ID`, and
its `data-canonical-target` must be the same ID. Do not duplicate the citation,
DOI action, or `ItemList` on this page. The shared script sends visitors who
have JavaScript to the matching homepage anchor; without JavaScript, they can
follow the visible title link. Keep the established old fragment IDs intact.

Add or update the short citation in `cv.html`, then run `python check.py` and
compare the web CV against the complete homepage record.

### Accepted papers

Use `<span class="pub__status pub__status--accepted">Accepted</span>` on the
homepage and place a title link in the Accepted section of
`publications.html`. Leave the homepage title as plain text until a verified
paper URL exists. Include accepted status in the homepage `ItemList` description
and the web CV. Do not invent a DOI, page range, or publication date before
those details exist. When the paper is
published, move its bridge link to Published work and update the complete
homepage record, structured data, and web CV with verified details. Preserve
the `#accepted` old bookmark route while at least one accepted paper exists.

---

## Add a post

### 1. Create the post file

Copy `blog/ml-pipeline-common-mistakes.html` to a new file in `blog/` and
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

### 2. List it on `blog.html`

Copy the `<li class="note-card">` block and edit the title, link, date, reading
time, and summary. The little SVG thumbnail is inline: change the shapes or
reuse it as-is.

Also add a short `<article class="blog-preview__post">` to the homepage
`.blog-preview`, newest first, with the post date, title link, and one-line
summary. The homepage shows a scrollable recent-post list after three previews;
the full archive remains on `blog.html`. Keep the one-post state unbounded.

### 3. Grouping, once there is more than a handful

The section carries technical pieces, reflections, and the occasional post about
where the work is going. Once there are more than about four, split the index
under two headings, **Technical** and **Reflections**, with Technical first. A
reader arriving from an application should meet the technical work before the
personal writing. Until then a single list is fine.

### 4. Update the sitemap

```bash
python check.py --write-sitemap
```

This regenerates `sitemap.xml` from indexable pages. The legacy publication
bridge and `404.html` are omitted. CI fails if you forget, so it will not
silently go stale.

---

## House style

- **Never use an em dash (`&mdash;`).** Rewrite with a colon, semicolon, comma,
  parentheses, or two sentences. Runs of em-dash asides make prose read as
  machine-written.
- En dashes (`&ndash;`) are correct and stay, but only in ranges
  (`2019&ndash;2024`, `pp. 1&ndash;6`) and compounds (`CNN&ndash;LSTM`).
- British spelling throughout.

## News grows on its own

Add `<li>` entries to the top of the list on `index.html`, newest first.
The fixed-height `.news-window` is keyboard-focusable and scrollable. Do not
prune older entries. Print expands the entire list; no-JavaScript rendering
keeps all entries available.

## Add an award, course, or project

On the homepage, awards are `<li>` entries in `.awards-list`, selected software
projects are undated whole-card `<a class="project-card">` links, and current or
earlier courses are in the Teaching row of `.role__details` under the Lecturer
entry in Experience. AMIR Lab is a separate `.role`; keep its internship dates
and review contribution distinct from the longer Research Work record.
Keep project descriptions factual and link each card to its repository. For a
dated CV or detail-page record, use the existing `.entry` pattern:

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
larger; anything else is centre-cropped by CSS. The homepage displays it in a
circle. Keep the filename.

---

## Change the colours

Everything is defined once, at the top of `assets/css/style.css`:

```css
:root {
  --accent: #1d4e89;   /* links, current-page underline, buttons */
  --warn:   #a1442a;   /* pitfall callouts in posts */
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

If you add or rename a homepage destination, update `.site-nav__links` and
`.site-nav__menu-links` in the `<nav>` block of
**every** `.html` file, including posts in `blog/`. About remains on the page
without a nav link. The direct academic links are Research, Education, Awards,
Experience, and Projects. Research lands at `#research` and stays active through
Publications and Research Work; those two sections retain direct hash URLs.
Community links directly to News and Updates. The mobile Sections menu has
direct News and Updates, Blog, and Contact links. The homepage content
order now matches these academic links. Run
`python check.py`; it checks the section and nav maps and compares the shared
blocks. Post pages and `404.html` use root-absolute paths (`/#research` for
a homepage section); the checker normalises these paths.

Regenerate the sitemap with `python check.py --write-sitemap` after adding a page.

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

The PhD application timing (`Fall 2028`) appears in the About paragraph on
`index.html`. Update or remove it once you have decisions.
