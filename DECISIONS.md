# Decision log

Why this site looks and works the way it does. `AGENTS.md` holds the rules;
this file holds the reasoning, including things that were tried and rejected.
Read it before proposing a change that contradicts something here.

Last updated: 29 September 2026.

---

## Who this is for

Md. Forhan Shahriar Fahim, Lecturer in CSE at Pundra University of Science &
Technology, seeking **AI PhD opportunities beginning in Fall 2028**.
The audience is faculty and admissions committees. Every design decision is
judged by one question: does this help a busy academic reader find the research,
or does it make the page look like a developer portfolio?

## One-page direction, 26 September 2026

Forhan wants the PhD application site to work as one scrollable academic
profile. Faculty should be able to find the research narrative, complete paper
list, teaching, and background without visiting separate site pages. Younus
Ahamed's site is the primary reference for the breadth and order of academic
sections; Aritra Mazumder's visible in-page links are a useful navigation idea.
Neither design is a template to copy. The desired result is distinctive and
polished while remaining credible, factual, fast, and researcher-first.

`ONE-PAGE-ROADMAP.md` records the architecture, issue sequence, acceptance
criteria, and progress. On 26 September 2026, Forhan approved R1's recommended
direction: the editorial research profile in wireframe A, with a restrained
connection between the three research threads from wireframe B. The order is
identity and About, Research, Publications, Research work, Teaching, Academic
background, Updates, Blog, Contact. Research tools stay in the PDF CV; the full
blog article and PDF CV are optional deeper links. Previous visual preferences
in this log remain relevant, especially the preferred wide prose measure.
See `planning/R1-CONTENT-AND-WIREFRAMES.md` for the content inventory and images.

### R11 owner-reviewed design, 28 September 2026

The owner reviewed the isolated mockups and selected the editorial one-line
Research Interests treatment (concept B). Four names remain visible with no
introductory sentence or expansion control. The owner subsequently supplied
a revised one-paragraph About, quoted exactly in the R11 roadmap; the current
hero stays. This shortens the first research scan while the deeper
`research.html` page carries the explanations.

The owner prefers top navigation to the desktop chapter rail. The latest
direct academic destinations are Research, Education, Awards, Experience,
and Projects. Research covers Research Interests, Publications, and Research
Work. Community is a direct link to News and
Updates, without a caret or dropdown. Its active pill remains highlighted
through Blog and Contact. The reading-progress line remains. About stays on
the page but leaves the navigation. A narrow-screen Sections disclosure has
direct News and Updates, Blog, and Contact anchors under a Community heading.
The owner made this correction after reviewing the dropdown in the local site.

Education uses one restrained timeline node for the B.Sc. only. Dates, both
averages, and the EMG thesis stay together. The Selected coursework line
contains eight owner-provided course titles, with “Computer Networks”
confirmed as the intended correction. It shares the thesis line's font size.
This replaces the earlier five-course PDF-based proposal. It adapts the
degree-and-grade hierarchy of Azmine Wasi's education page without copying
its multi-degree or exhaustive coursework format. Awards & Recognition sits
immediately after Education, with the two previously verified awards and a
short Awards nav link. This gives the awards one clear home instead of repeating them under
Education and Experience.

Experience has its own section after Awards. The Lecturer appointment contains
Teaching and Supervision groups; the optional teaching page retains depth.
Projects follows as two quiet GitHub cards with no dates. The owner approved
these treatments in the mockup. The homepage News and Updates list is always
in a fixed-height scrolling region, with no view-all control; all entries stay
in source HTML and print expands the region. Blog and Contact remain separate
sections under Community navigation. The mockup and R11a-f implementation
plan are in `planning/top-nav-community-news-mockup.html` and
`ONE-PAGE-ROADMAP.md`. This is the target design. R11a Education and Awards,
R11b top navigation, R11c About and Research Interests, and R11d Experience
and Projects, and R11e Community and News are implemented locally; R11f remains pending. The four homepage interest names use a compact
list with small markers, wrapping naturally on phones; longer explanations
remain on `research.html`.

### R12 refinement, 29 September 2026

The owner approved a single Research nav link to the Research Interests
section. The active state continues through Publications and Research Work;
their headings and direct hashes remain. This cuts two desktop nav buttons
without another disclosure menu. The optional `research.html` page gains a
fixed return link to the homepage Research Interests section so direct visits
also have an obvious route back.

Research Work remains the name for ongoing and completed studies. No arXiv
paper exists yet. A future arXiv paper belongs in Publications as a preprint;
Research Work may describe its study only when doing so adds distinct context.

Two owner-supplied school scholarships follow the 2025 faculty and 2023 Dean's
awards: a 2016 SSC General Scholarship and a 2014 JSC Talentpool Scholarship,
both under Dinajpur Education Board. The displayed years are examination years;
the owner has not supplied individual result documents. Project cards are
whole-card GitHub links with a quiet colour change on hover and keyboard focus.
The six hero profile actions retain their labels, fit one line when space
allows, and wrap naturally on narrower screens.

### R13 refinement, 29 September 2026

The owner selected the role-led Experience concept in
`planning/R13-experience-contact-mockups.html`. The old Teaching and
Supervision columns were uneven because Supervision needed longer copy.
Both are now short labelled rows under the Lecturer appointment, followed by
a distinct AMIR Lab Research Intern entry. The owner supplied its May 2025
to December 2025 dates and described screening and analysis for the
PRISMA-guided cancer-imaging review, plus drafting sections and figures.
The role copy is concise; Research Work retains the manuscript status and
broader study description. The supplied PDF lists ELITE Research Lab but not
AMIR; the owner explicitly requested AMIR in HTML and did not request ELITE
there, so ELITE remains in the PDF only.

The owner selected a compact Contact strip instead of the tall panel. Six
hero actions keep their existing icons and desktop one-row layout, now with
equal label weight and the order Email, CV, Google Scholar, ORCID, GitHub,
LinkedIn. Contextual return links on Teaching and the individual Blog post
follow the existing Research detail-page pattern. The stable CV URL now serves
the exact owner-supplied PDF file. These changes remain local for owner review.

### R10 planning decision, 28 September 2026

**Implementation update, 28 September 2026:** R10a-e now run in the local
draft. The condensed index has eight primary links, with direct sublinks in
the narrow-screen menu. Education follows Research Work. Projects contains
CSE Academic Operations Hub and BookHive; the EMG thesis is in Education.
The owner's later About text and Fall 2028 date supersede the earlier proposed
copy. News shows three recent entries with an accessible all-updates scroll
view; Blog shows its one current post and an archive link. The same-site CV PDF
has been replaced. Historical sections below describe decisions at the time,
not the current implementation status. See `CONTEXT.md` for current truth.

The owner subsequently supplied his own About wording, naming AI safety and
interpretability, computer vision, large language models, and vision-language
models, with a Fall 2028 PhD start. He then selected a new hero tagline:
"I want to understand what AI models learn, why they make certain predictions,
and where they fail." The overlapping sentence was removed from About. The
The Research Interests cards now use the same four fields.

Forhan selected the condensed eight-link section index after comparing it with
the grouped eleven-link version. The page will still expose Education, Projects,
Teaching, Experience, News, and Blog as distinct readable sections with stable
direct anchors. The rail groups Projects/Teaching/Experience under Academic
Work and News/Blog under News & Blog. This reduces navigation height while
retaining the whole one-page reading path. See R10 in `ONE-PAGE-ROADMAP.md`.

Forhan also clarified that Projects means built systems, not the EMG thesis,
systematic review, or student projects he supervises. The updated CV's CSE
Academic Operations Hub and BookHive are the two concise entries. They
appear after publications and research, and are labelled as software projects
without recasting them as research results. The research internship remains in
the PDF CV only until he requests it in HTML.

The CV button should point to one stable same-site PDF URL, opened normally for
in-browser viewing. A separate download action can be added if useful. Google
Drive is not the primary destination because it adds a second access setting
and a different viewing surface for a small static PDF. The user-supplied
replacement has been copied to the public asset path in the local draft.

### R3 opening and research treatment

The homepage now pairs the concise research question with direct Email, Scholar,
and PDF CV links in the first screen. ORCID, GitHub, and LinkedIn remain visible
as quieter secondary links. About is a single short paragraph, so research
appears sooner in the scroll path without removing the verified application
statement.

Three numbered research rows share a thin vertical rule. This is the restrained
connection approved from wireframe B: it makes the threads read as one agenda
while keeping the text and papers as the focus. The copy separates published
software-security work, current medical-imaging supervision, a completed review
with manuscript in preparation, and future interests. The existing portrait,
typefaces, wide text measure, and serif italic opening line remain as chosen in
the earlier site review.

### R4 publication source

The homepage is now the source of truth for the full published and accepted
record. R4 placed all four complete citations, DOI and BibTeX actions where
verified, and the single publication `ItemList` JSON-LD block there. R9d later
removed the separate actions while retaining verified paper destinations. This lets a
faculty reader inspect the evidence without opening another page. VulPatchNet
remains visibly accepted and has no invented DOI or BibTeX record.

R4 temporarily kept identical articles on `publications.html` for existing
links. R7 replaced that duplicate with the legacy route described below. The
in-preparation cancer-imaging manuscript remains outside the published and
accepted count, under Research Work on the homepage.

### R5 academic record and footer spacing

Research Work now gives the completed cancer-imaging review and the earlier EMG
thesis enough detail to show methods and status without implying a published
review paper. Teaching uses the existing definition-row pattern so current
courses, earlier courses, and research supervision can be scanned separately.
Academic Background adds both verified awards, after appointment and degree.

The Contact-to-footer gap came from large main bottom padding combined with a
second footer top margin. One compact main spacing value now separates the last
paragraph from the footer rule. The adjustment applies consistently to all
pages, and keeps the footer at the bottom of short pages.

### R6 final content pass

Updates now records the completed September 2026 cancer-imaging review and
points to Research Work on the same page. The award remains visible in Academic
Background but no longer appears as an undated item among month-specific news;
its month has not been verified. This keeps the update list unambiguously newest
first without inventing a date.

The Blog preview identifies its article as a longer optional read. Contact now
offers one direct email route. The institutional postal line was removed because
the role and institution are already visible above, and email is the intended
public contact method.

### R7 legacy URLs and publication ownership

The homepage owns the complete publication records and structured data. The old
`publications.html` URL remains as a small bridge with the same paper IDs and
visible title links. The shared script sends a visitor directly to the matching
homepage anchor; a reader without JavaScript can follow the title link. Older
`#accepted`, `#y2026`, and `#in-progress` bookmarks also have mapped targets.
This preserves old entry points without maintaining a second set of citations
that could drift.

The bridge has a homepage canonical URL and `noindex,follow`, and is omitted
from the sitemap. Research, teaching, CV, and blog pages remain optional deeper
reads with their own canonical URLs because they contain material beyond the
one-page summary. The sitemap lists only indexable pages and does not claim a
modification date that the repository cannot verify. A version query on the
bridge's script request prevents a stale browser cache from blocking the new
redirect during this transition.

### R8 owner-directed visual and content revision

The owner chose a circular portrait, short rounded links in the opening, a
rounded navigation group, a section-aware active pill, and a thin reading
progress line. Aritra Mazumder's navigation supplied the interaction idea; the
site keeps its own typography, colours, section order, and quiet academic tone.
The progress bar and current-section state are added by JavaScript on the
homepage. The native links and all content remain usable without it. Reduced
motion removes transition effects, and the bar follows scroll position without
an animation of its own.

The opening CV link now reads simply "CV". Three supported phrases in About
receive restrained bold emphasis. The owner also named four interests: AI
safety and interpretability, large language models, computer vision, and
medical AI. The language-model section states a future research interest, not
an existing publication claim. The visible navigation shortens "Research
Interests" to "Interests" so five links still fit on one row at phone widths;
the `#research` and `#interests` bookmarks remain valid.

### R9 owner feedback, 27 September 2026

The owner requested explicit Education, Experience, Research Work, Projects,
and Blog navigation; **News & Update** as the Updates label; compact Research
Interests; prominent publication years and statuses with a title-adjacent
link; rounded public-profile links; fuller Contact; and a centred circular
portrait crop. The owner also asked for scrollable recent News and Blog lists
with an all-items action, plus fewer and clearer agent documents. These are
tracked in [GitHub issue #1](https://github.com/ForhanShahriarFahim/ForhanShahriarFahim.github.io/issues/1)
and staged in `ONE-PAGE-ROADMAP.md`. R9a compared two original browser-rendered
concepts at desktop and 375px; see `planning/R9-DESIGN-REVIEW.md`. The selected
direction is B's desktop section index and full-width phone menu, combined
with A's separate year/status publication rows on desktop and stacked labels
on phones. R9b implemented the selected section index and phone menu across
all pages, with eleven homepage destinations. About also appears in the map so
the menu covers every visible section. The existing `#background` fragment
points to Experience, and `#interests` and `#news` still resolve. Research Work
contains the completed review; Projects contains the EMG thesis and clearly
identified supervised student work; Experience and Education use only verified
facts. A native `<details>` keeps all section links available without
JavaScript, while JavaScript adds the current label and scroll position. The
publication treatment is reserved for R9d. R8's reviewed preview is a
baseline, not an approved release.

### R9c visual pass and deferred content review, 28 September 2026

Four research-interest names now form a compact two-column set on desktop and
one column on phones. Native disclosures keep the existing descriptions
available by click, keyboard, and without JavaScript. This saves space while
preserving the current draft text for later review. The portrait remains round,
with its crop centred on the face. ORCID, GitHub, and LinkedIn use quiet rounded
links in the opening. Contact groups the public email and Scholar, ORCID,
GitHub, and LinkedIn links in a restrained correspondence panel. The panel adds
no new personal details.

The owner has explicitly withheld approval of the current About wording and
the organisation of Research Work, Projects, Experience, and Education. Their
facts may be supported, but the presentation is provisional. Preserve it during
the remaining R9 visual passes; review the updated CV and the owner's preferred
ordering before rewriting. [Issue #2](https://github.com/ForhanShahriarFahim/ForhanShahriarFahim.github.io/issues/2)
tracks that separate content gate. The draft must not be released as final PhD
application copy until that review is resolved.

### R9d publication rows and portrait crop, 28 September 2026

The owner asked to remove the visible DOI and BibTeX controls, show each paper's
year, and zoom the portrait out slightly. The homepage now uses a distinct year
and status column on desktop, stacked above the title on phones. All four
records show 2026. The accepted paper remains explicitly accepted and has no
paper link until a verified URL exists. The three published titles link to
their verified DOI destinations, with a small visual arrow after each title.
This keeps the destination available without a separate citation toolbar. The
complete authors and venues, stable bookmarks, and `ItemList` remain. Unused
BibTeX markup, styling, and copy behaviour were removed. The portrait crop
changed from 108% to 103% within the same circular frame.

This request reopens the earlier decision against a scrollable news box. Its
touch-scrolling, keyboard, focus, no-JavaScript, and print concerns remain
real. The R9a comparison favours one bounded recent News list and an in-page
all-updates expansion of that same list. Without JavaScript, the full list
should remain visible; print should release the height cap. Blog should cap
its recent list only once several posts exist, with the all-blogs action
reaching `blog.html`. An Experience
section cannot expose the CV-only internship without a later request, and a
Projects section needs verified academic content distinct from Research Work.

## The research narrative (do not flatten this)

The three published papers are all software-vulnerability detection, while the
stated interests are AI safety and interpretability, large language models,
computer vision, and medical AI. The papers apply LIME and explainable
multi-task transformers, providing evidence for the interpretability interest.
The site states one question, "how do we make deep models legible and
label-efficient enough to be trusted when the cost of a mistake is high", and
uses the four interests to describe where Forhan wants to pursue it.
Anyone rewriting the About or Research copy must preserve that thread. The
accepted 2026 VulPatchNet paper concerns patch generation and is labelled as
accepted, without presenting it as another explainability result.

## Deliberate omissions

- **Web-development projects and competitive-programming ratings** sit at the
  bottom of `cv.html` only. Leading with them signals "web developer".
- **No phone number, home address, or referees' email addresses** anywhere on
  the site. Those live in the PDF CV.
- The PDF CV has had the "I hereby declare" statement, the signature image, and
  the trailing name line removed, because that convention reads oddly to US
  committees. Removal was done at the content-stream level, so the text is not
  recoverable. **If the CV is recompiled from its LaTeX source, this comes back;
  delete those lines in the `.tex` instead.**

---

## Architecture

| Decision | Why |
|---|---|
| Plain HTML, one CSS file, one small JS file, no build step | Content volume is three published papers, one accepted paper, and one post. A content-collection system is machinery without payoff, and nothing can break during application season. |
| Nav and footer duplicated across every page | Injecting them with JS would hide them from search engines and break no-JS rendering. `check.py` detects drift, which makes the duplication safe. |
| `blog/` pages and `404.html` use root-absolute paths | They are served from a different depth. `check.py` normalises this before comparing navigation. |
| Deploy through GitHub Actions, not branch deploy | It lets `check.py` gate the deploy, so a broken edit fails the build instead of taking the live site down. |
| Screenshots captured with headless Chrome | The preview pane scales and sometimes returns mid-paint frames. Chrome gives real resolution. Note it enforces a ~500px minimum window width, so 390px shots must be rendered inside a 390px iframe and cropped. |

## Rejected alternatives

- **Jekyll / academicpages**: dated visuals, jQuery-heavy, painful Ruby setup on
  Windows, and instantly recognisable as a template.
- **Hugo Blox**: content coupled to remotely-versioned modules, three breaking
  rebrands, growing paid-tier push. Built for labs with 1,000+ papers.
- **Astro**: needs Node plus a build step for content that does not justify it.
- **A scrollable news box** (as on some faculty pages): can trap touch scrolling on
  phones, hides items below its own fold, clips when printed, and needs
  `tabindex` plus a label for keyboard access. `main.js` collapses entries past
  the sixth behind a toggle in the current draft. The owner explicitly reopened
  this choice in R9; the final design is pending the accessibility comparison.
- **Highwire `citation_*` meta tags** on `publications.html`: those describe
  exactly one article per page, and that page lists several. `schema.org`
  `ScholarlyArticle` markup is used instead.

---

## The design review, 29 August 2026, and the partial revert

**Outcome: the typographic changes were reverted at Forhan's request on
29 August 2026.** He did not like the resulting page formatting. What survives
from the review is the functional half; what went back is the visual half.

**Kept from the review:**
- DOI and BibTeX as text links joined by a middot, rather than two outlined
  buttons.
- The mobile navigation rebuild: the theme toggle is a sibling of
  `.site-nav__links`, not a child, which is what keeps six links on one row at
  390px with 44px tap targets. Below 345px they form a 3-column grid.
- `.interest h3` at 1.08rem, so subheads are no longer smaller than the body
  text they head.
- Dark `--border` at `#31353d`; at `#2a2e35` the section rules were invisible.
- The back-to-top control kept but quiet: no accent fill, shadow, or hover lift.
- The theme toggle icon naming the theme it switches to, matching its aria-label.
- The tighter portrait crop.
- Removal of the dead `h2 { margin-top: 4.5rem }` rule, and the reading-time
  estimate on the note.

**Reverted at his request:**
- The `--prose` measure. Running text is back to the full 890px frame at roughly
  118 characters per line, with body line-height back at 1.75. This is a
  deliberate, informed choice: he prefers the fuller column and matched it to a
  reference site he likes. **Do not "fix" this again without asking him.**
- The serif italic hero tagline with its accent bar, and the original hero
  spacing.
- The `JOURNAL` / `CONFERENCE` chips above publication titles.
- The frosted-glass sticky nav and the tighter news row padding.
- The contact row showing "Email" rather than the address itself.

### What the review said originally

An external design review was run against the live site and screenshots. Its
recommendations were applied selectively. What was **accepted**:

1. **Prose measure.** Running text measured **118 characters per line**, far past
   the 45 to 75 convention. Added `--prose` (52ch, about 66 to 76 characters in
   practice) applied to running text only, and dropped body line-height from
   1.75 to 1.65. The 930px frame stays for publication rows, CV entries, and the
   news date column.
2. **Mobile navigation.** At 390px the header was three rows, 121px tall, with
   26px tap targets and CV orphaned beside the toggle. The toggle moved out of
   `.site-nav__links`, so the name and toggle share row one and all six links sit
   on row two with 44px targets. Below 345px the links become a 3-column grid,
   giving two balanced rows rather than a ragged wrap.
3. **Hierarchy inversion.** `.interest h3` was 15.52px against 16.8px body text,
   so the subheads were physically smaller than the prose they headed.
4. **Publication rows.** DOI and BibTeX were two identically weighted outlined
   buttons, reading as a toolbar. They are now text links separated by a middot.
   The `JOURNAL`/`CONFERENCE` chips became quiet text at the end of the venue
   line, where they no longer compete with the title.
5. **Density, borders, chrome.** News rows evened out against publication rows;
   dark `--border` lifted from `#2a2e35` to `#31353d` because section rules were
   nearly invisible; the frosted-glass nav dropped; the hero tagline demoted from
   serif italic with an accent bar to a plain lead sentence; the dead space under
   the hero cut from 80px to 56px; reading-time estimates removed.

What was **rejected, and why**:

- **Remove the back-to-top button.** It was specifically requested. Kept, but
  stripped of its accent fill, drop shadow, and lift-on-hover, which removes the
  marketing-page character the reviewer objected to.
- **Remove the CV timeline rail.** Also specifically requested, and it is what
  makes the CV page visually distinct. Kept.

Still **open**, deliberately not actioned:

- **The portrait.** It is a passport-style photo on a white studio background,
  which becomes the brightest object on the dark theme. Cropped tighter as a
  partial fix; the real fix is a relaxed head-and-shoulders photograph against a
  wall or bookshelf.
- **Inter to Source Sans 3.** Reasonable (it would pair with Source Serif 4 as
  one superfamily) but a taste call, not a defect. Not made.
- ~~Renaming "Notes".~~ **Settled as "Blog" on 29 August 2026.** The section
  carries technical pieces, reflections, and life events, and "Notes" promised
  only short technical jottings. It was briefly "Writing", which was my
  recommendation because it covers all three without implying a posting
  schedule, and because "Blog" is the label admissions committees most associate
  with developer portfolios. Forhan considered that and chose "Blog" anyway.
  **It is his call; do not re-propose "Writing".** "Journal" was rejected by both
  of us as actively confusing beside a Publications page listing journal
  articles. Both renames were done while nothing linked to the old URLs.
- **Adding PDF or arXiv links per paper.** A content task; needs preprint URLs.
- **Superseded by R4 and R7:** The former homepage teaser showed DOI only while
  `publications.html` held BibTeX. The one-page profile now includes the full
  records and BibTeX on the homepage; the legacy page holds title links only.

## Corrections made to the review itself

- It claimed the prose ran to about 105 characters. Measured: **118**.
- It claimed sections use 4.5rem spacing. They use **3rem**: every section holds
  exactly one `h2`, so `h2:first-of-type` always won and the 4.5rem rule was dead
  CSS. That rule has been removed.
- It claimed a scrollbox would hide content from in-page search. It would not;
  browsers search inside overflow containers. The real objections are listed
  above.

---

## Verification expectations

Any layout change should be re-checked at **320, 360, 375, 390, 430, 700, 780,
900 and 1440px**, in both themes, for: shared left and right edges across nav,
content and footer; no horizontal overflow; the nav link row staying on one line
above 345px; 44px tap targets at phone widths; and WCAG AA contrast on every
text element. The current state passes all of these, with roughly 950 elements
checked for contrast.
