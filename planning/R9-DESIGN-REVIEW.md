# R9a design comparison

**Date:** 27 September 2026
**Status:** Design direction selected; production UI unchanged.
**Tracking:** [GitHub issue #1](https://github.com/ForhanShahriarFahim/ForhanShahriarFahim.github.io/issues/1).

## Artifacts

- [Concept A: academic index](R9-concepts/concept-a.html): a two-level top header, a horizontal section strip, a wide reading column, four interest labels, and publication rows with a separate year column.
- [Concept B: chapter rail](R9-concepts/concept-b.html): a persistent ten-section desktop index, a native full-width section menu on phones, compact interest blocks, and year/status chips above paper titles.
- [375px phone comparison](R9-concepts/phone-review.html): both responsive prototypes shown at a fixed 375px inner viewport.

These are isolated, static planning artifacts. They abbreviate the publication
list and do not add claims to the public website. The Projects text is visibly
marked as a placeholder because distinct verified academic project records are
not yet available in the current HTML.

## What the references contributed

I viewed the current local homepage and both references in the browser. Younus
Ahamed's page demonstrates an academic path through news, education, research,
publications, teaching, Blog, and contact. Aritra Mazumder's site makes section
navigation and paper destinations prominent, with visible paper years. Neither
site is a visual template for these concepts. They retain Forhan's quieter
serif/sans pairing, factual copy, light borders, and own research narrative.

## Comparison

| Criterion | A: academic index | B: chapter rail |
|---|---|---|
| Faculty scan on desktop | Wide citations and visible top navigation. The row with year at left is especially easy to scan. | Every requested section is visible in a stable side index, and section starts are clear. Main text remains readable. |
| Navigation at 375px | The horizontal strip fits only the first two or three links. The remaining seven require a swipe, so Education, Experience, News, Blog, and Contact are easy to miss. | “All sections” opens a full-width, two-column list with all ten destinations. It costs one tap but makes the complete map explicit. |
| First screen | Portrait, role, question, and public pills fit cleanly. | The same essentials fit; the portrait and menu stay separate. |
| Research Interests | Pill shapes look attractive but can suggest clickable controls where none exist. | Four quiet labelled blocks read as fields, with less prose and no false action cue. |
| Publications | A distinct year column and title arrow work well on desktop; year/status must stack on phones. | Compact badges use less width and work on phones; the title area is somewhat less distinctive on desktop. |
| News and Blog | Bounded recent list and native all-updates disclosure. | The same behaviour fits the section rhythm. A one-post Blog has no scrollbar in either concept. |
| Risk | Off-screen mobile navigation undermines the owner's main request. | The desktop index consumes width; the phone menu needs careful anchor, focus, and active-state behaviour. |

## Browser and static checks

- Opened both concepts at the desktop browser width and in the 375px comparison.
  Confirmed the hero, section navigation, publication rows, and lower-page
  lists render. Concept A's phone publication labels initially collided with
  titles; the prototype now stacks year/status above each title. Concept B's
  phone menu initially compressed into a narrow column; it now opens across
  the full width. Its first phone styling also caused horizontal overflow;
  removing the negative header margins fixed the visible scrollbar.
- Clicked Publications in each desktop prototype. Clicked Publications and
  News & Update in the phone comparison. The fragment destinations reached
  their corresponding sections. Opened B's ten-link phone menu and its
  “View all updates” disclosure. The update list has its own visible scroll
  affordance and a keyboard-focusable labelled region.
- The prototypes contain no JavaScript. Their native links and disclosure
  remain usable without scripting. Print CSS removes navigation and releases
  the news and Blog height caps; this was checked in source, not visually
  printed yet.
- Spot-checked contrast in the proposed light palettes. A's body, muted text,
  and accepted status range from 5.59:1 to 14.75:1. B's body, muted text,
  kicker, badges, and footnote range from 5.17:1 to 13.55:1. A full component
  contrast audit and dark-theme review remain part of implementation.
- Ran `python check.py` after every artifact edit; all eight production pages
  pass. The prototypes are not part of the checker or sitemap.

## Selected direction

Use **B's chapter index and phone menu** for information architecture, with
**A's flatter year-column publication rows on desktop** and the tested stacked
year/status treatment on phones. Keep B's four labelled interest blocks and
restrained contact panel. Carry over the existing site colours and type unless
a tested improvement earns a change. Preserve the existing scroll progress
and active-section behaviour; these static artifacts only illustrate their
placement.

For News & Update, implement one canonical chronological list. A future
“View all updates” action should expand that same list on the homepage, so the
one-page goal remains intact; no second copy of records should be maintained.
Without JavaScript, the full list must remain accessible. Apply the height cap
only when it actually hides items. For Blog, show the most recent few posts on
the homepage, reveal a bounded scroll region only when the list is long enough,
and link “View all blogs” to `blog.html`.

## R9b handoff

1. Build the selected responsive navigation and page anchors in production.
   Update the shared nav in every HTML page and adapt active-section tracking
   and the progress bar. Test 320, 375, 780, and 1100px, both themes, keyboard,
   reduced motion, and no-JavaScript.
2. Split Academic Background into Education and Experience with only verified
   information. Keep the CV-only internship out of HTML.
3. Before adding substantive Projects copy, obtain or verify distinct academic
   project title, role, dates, and outcomes. Avoid duplicating Research Work or
   Teaching. A neutral section shell can be implemented first, but the planning
   placeholder must never be published as site copy.
4. Keep `#research`, `#interests`, `#updates`, `#news`, and publication IDs
   working. The label changes to **News & Update**; the stable `#updates` URL
   does not need to change.

R9c through R9f remain in the roadmap and GitHub issue. The next checkpoint
is R9b, not deployment.
