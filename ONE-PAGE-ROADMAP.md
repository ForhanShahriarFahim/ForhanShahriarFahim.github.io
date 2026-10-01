# One-page academic website roadmap

**Status:** R10a-e, R11a-e, R12a-c, and R13a-c implemented and published. R12d and R13d reviewed. GitHub Pages release verified on 29 September 2026.
**Last reviewed:** 29 September 2026.
**Current task:** Owner review of the published site and CV. Apply specific corrections as new tasks.
**Audience:** Faculty and admissions committees reviewing Fall 2028 PhD applications.

This is the handoff and progress record for the redesign. Start with `AGENTS.md`
and `CONTEXT.md`, then read Current task, R11, and Next action here. Older
R1-R11 sections record earlier targets; R12 supersedes their navigation and
award details. The current HTML combines local R10, R11, and R12 passes. Use
the R12 section and `CONTEXT.md` for current behaviour. Update the status table
and evidence log after each issue.

## R11: approved design and implementation sequence

The owner reviewed the isolated mockups in
`planning/top-nav-community-news-mockup.html` and approved the following
direction. This section is the **target design**, not a description of the
current homepage. Earlier choices in this roadmap are historical where they
conflict with R11. The mockup abridges the hero, Publications, Research Work,
Blog, and Contact to show layout; implementation must retain their complete
current content, portrait, actions, and paper records.

### Target page map and content rules

1. Keep the current `index.html` hero. Replace About with the owner's revised
   copy below as **one paragraph**, preserving the indicated emphasis. About
   stays visible on the page but has no navigation entry:

   > I am a Lecturer in Computer Science and Engineering at Pundra University
   > of Science & Technology. I am interested in what AI models learn and how
   > we can examine their behaviour. My current interests include **AI safety
   > and interpretability**, **computer vision**, **large language models**,
   > and **vision-language models**. **I am looking for PhD opportunities
   > beginning in Fall 2028.**
2. Research Interests becomes a single editorial line of the four existing
   labels. Remove the introductory sentence and disclosure descriptions from
   the homepage. On narrow screens the line may wrap naturally. The deeper
   `research.html` page retains substantive explanations.
3. Preserve all four homepage publication records, statuses, linked titles,
   and JSON-LD. Preserve the completed review's status in Research Work.
4. Education remains one B.Sc. entry only, in a restrained single-node
   timeline: University of Rajshahi, Jan 2019–Dec 2024, CGPA 3.66/4.00,
   last-two-years average 3.82/4.00, EMG thesis and supervisor. Add a short
   **Selected coursework** line with the owner's exact titles: Artificial
   Intelligence, Digital Image Processing, Algorithms, Data Structure,
   Database, Operating System, Computer Networks, and Cryptography and Network
   Security. The owner confirmed “Computer Networks”. This list supersedes
   the earlier five-course PDF-based selection; do not describe all eight as
   CV-verified. Use the same font size for Selected coursework and
   Undergraduate thesis.
5. Put **Awards & Recognition** directly after Education with the two verified
   entries: Young Enthusiastic Faculty Member Award (2025, Pundra University
   of Science & Technology) and Dean's Award (2023, University of Rajshahi).
   Remove their old duplicate rows in Education and Experience. The desktop
   top bar has a short **Awards** anchor.
6. Put **Experience** after Awards. The Lecturer appointment contains two
   labelled groups, Teaching and Supervision, using the current course and
   supervision facts. There is no separate homepage Teaching section, but
   `#teaching` must continue to land on its group and `teaching.html` remains
   the optional detail page. Keep the PDF-only research internship off HTML.
7. Put **Projects** after Experience. Show two quiet, equal cards for CSE
   Academic Operations Hub and BookHive, each with the existing GitHub mark,
   short factual summary, and repository link. No project dates, thesis,
   review, or supervised student projects in these cards.
8. Rename the homepage section **News and Updates**. Keep all news entries in
   source HTML, newest first, inside one fixed-height, independently scrollable
   area. No “View all updates” button. The region is keyboard focusable, touch
   scrollable, and expands fully in print. Blog and Contact remain separate
   readable sections; Blog retains its archive link and future recent-preview
   behaviour.

The sticky **top navigation** replaces the desktop chapter rail. Its direct
links are Research Interests, Publications, Research Work, Education, Awards,
Experience, and Projects. **Community** is a direct anchor to `#updates`,
without a caret or dropdown. On narrow screens one Sections disclosure shows
direct News and Updates, Blog, and Contact links under a Community subgroup.
The active pill tracks the current direct section or Community while reading
its three sections, and the thin page-progress line remains. The hero and
About have no falsely active section. The site remains readable and navigable
without JavaScript. Keep existing public hash destinations working, including
`#research`, `#interests`, `#background`, `#academic-work`, `#teaching`,
`#updates`, `#news`, `#news-blog`, `#blog`, and `#contact`.

### R11 implementation tasks

Complete one task at a time, run `check.py` after every change, then show and
inspect the changed portion before the next task. Keep the R10 working-tree
state intact; do not reset it while starting R11. The design mockup is a
reference, not production code to paste wholesale.

| Task | Scope and files | Acceptance evidence |
|---|---|---|
| R11a · education and awards (complete locally) | Replaced the short homepage Education rows with the one-degree timeline and owner-provided selected coursework. Added Awards & Recognition after it; removed duplicate award rows. Matched the thesis and coursework font sizes. Updated the section-order check in `check.py`; kept the current nav until R11b. | Degree and award details checked against `cv.html` and the existing PDF audit; coursework matches the owner copy. One degree, two awards, matching 15.04px text, no overflow at 375/780/1100px in both themes. `#awards` lands at 128px on a 375px phone with and without JS. `check.py` passes. Screenshots: `planning/R11a-375-light.png`, `planning/R11a-375-dark.png`, `planning/R11a-1100-light.png`, `planning/R11a-1100-dark.png`. |
| R11b · top navigation (complete locally) | Replaced the rail with a sticky top bar and native Community disclosure in the byte-identical `<nav>` on all eight HTML pages. Updated shared CSS, scroll tracking, and checker maps; retained old hash aliases and theme toggle position. | No overflow at 375/780/1100/1120/1160/1280px; 44px theme and nav targets; active Education/Community states and progress checked in both themes. Community and phone disclosures work by click and keyboard; Escape closes the phone menu; `#awards` works from a secondary page with JS disabled. `check.py` and JS syntax pass. Screenshots: `planning/R11b-*.png`. |
| R11c · About and interests (complete locally) | Replaced About with the exact owner paragraph above, using one `<p>` and five indicated strong phrases; kept the hero. Replaced the homepage disclosures and intro with an editorial list; removed their unused CSS. Kept `research.html` as the optional detailed read. | Exact About text and one paragraph confirmed in browser. Four interests, no disclosures or intro, one line at 780/1100/1280px and three short rows at 375px. No overflow in both themes; `#interests` works with and without JS; print retains the list; `check.py` passes. Screenshots: `planning/R11c-*.png`. |
| R11d · experience and projects (complete locally) | Moved Experience before Projects. Nested verified teaching, research and capstone supervision under the Lecturer role. Kept `#teaching`, `#academic-work`, and the teaching detail link. Replaced the project timeline with two GitHub cards. | No duplicate homepage Teaching section, project dates, thesis, or research work in cards. Correct repository URLs and teaching link confirmed. At 780/1100/1280px desktop cards measure equally; at 375px they stack. No overflow in light/dark at 375/780/1100/1280px. `#teaching` lands within Experience with and without JS. Print retains cards; `check.py` passes. Screenshots: `planning/R11d-*.png`. |
| R11e · community sections (complete locally) | Replaced the desktop Community disclosure across all eight pages with a direct `#updates` link, no caret or dropdown. Kept the mobile Sections disclosure with direct News, Blog, and Contact links. Renamed News and Updates, removed the JS show-all toggle, and added one fixed-height accessible list. Kept Blog and Contact content and anchors. Updated scroll tracking, `check.py`, and current-behaviour docs. | All six existing news entries remain in HTML and date order. Browser confirmed a scrollable region, keyboard PageDown, no horizontal overflow at 375/780/1100/1280px in light/dark, no view-all button, direct Community anchor, and active Community through Blog and Contact. At 375px with JavaScript disabled, all six entries remain unhidden and the menu Contact link works. Print expands News; a secondary-page Community link reaches `/#updates` with JS disabled. `check.py`, JS syntax, and `git diff --check` pass. Touch swipe and integrated release QA remain for R11f. Screenshots: `planning/R11e-1280-light.png`, `planning/R11e-375-dark.png`. |
| R11f · integrated review and handoff | Reconcile `CONTEXT.md`, `DECISIONS.md`, `CONTENT-GUIDE.md`, `AGENTS.md`, and the roadmap only where their current-behaviour descriptions changed. Inspect site and legacy entry points. | `check.py`, JS syntax, `git diff --check`, links/anchors, publication JSON-LD, sitemap if needed, PDF viewing in a standard browser, 375/780/1100/1280px light/dark, no-JS, reduced motion, keyboard, print, console, and contrast checks pass. Record screenshots, remaining risks, and owner review before any commit or deployment. |

**Handoff:** An agent beginning R11 should read `AGENTS.md`, `CONTEXT.md`,
this R11 section, then inspect the current files. `DECISIONS.md` explains
the rationale. `cv.html` and `assets/cv/Md_Forhan_Shahriar_Fahim_CV.pdf`
are sources for verified degree and award facts; the owner's copy above is
authoritative for the revised About and coursework. The mockup is visual
guidance. R11a-e are complete locally; start at R11f and
advance the `Current task` line only after its acceptance evidence is saved.

## Goal and boundaries

Make `/` a complete, scrollable academic profile. A professor should be able to
understand who Forhan is, what question guides his research, what he has
published, and what academic work he does without opening another site page.
Short in-page navigation may jump to sections, but ordinary scrolling must
reveal the same essential information. External DOI, Scholar, ORCID, email, the
PDF CV, and a full blog article are optional destinations.

Success means the page feels like an individual researcher's page: distinctive,
calm, credible, quick to scan, and fast to load. It must not become a developer
portfolio or a copy of either reference. Keep plain HTML, one CSS file, one
small vanilla JS file, GitHub Pages, no build step, and no dependencies. Every
claim must be supported by the current site or PDF CV.

The owner chose Younus Ahamed's one-page structure as the primary reference,
with room to improve it. This is a structural choice, not permission to copy
its visuals or content. Exact visual treatment, section copy, and legacy URL
handling remain subject to review.

## Reference findings and design direction

Reviewed on 26 September 2026:

| Source | Useful idea | Adaptation |
|---|---|---|
| [Younus Ahamed](https://community.wvu.edu/~ma00087/) | Academic profile, research, papers, teaching, and contact form one scroll path. Paper records show authors and venue. | Use similar academic breadth, a shorter opening, fewer secondary sections, and visible core papers without a "View Full List" action. |
| [Aritra Mazumder](https://www.aritramazumder.com/) | Visible section links help navigate a long page. Sections have clear visual starts. | Use concise in-page links and strong section hierarchy. Avoid the oversized hero, moving banner, and competition-first emphasis. |
| [Azmine Wasi](https://azminewasi.github.io/index.html) | The page contents index groups academic material into a short set of broad destinations. | Borrow the grouping discipline, while retaining one scrollable homepage and much shorter, calmer summaries. The multi-page top navigation and dense news/bio treatment do not fit this site's first-visit goal. |
| [Current site](https://forhanshahriarfahim.github.io/) | Understated typography, direct prose, publication metadata, theme support, and established content. | Evolve this identity. Consolidate pages and improve scanning, spacing, and section rhythm through reviewed prototypes. |

Proposed visual character: an editorial academic profile with a compact identity
area, clear headings, restrained accent, readable publication records, and one
subtle device connecting the four research interests. Any motif should explain
their relationship rather than decorate empty space. Avoid floating particles,
carousels, large animations, metric counters, and oversized cards. Preserve the
current wide prose measure unless Forhan explicitly approves a change; the
previous narrow-column revision was reverted. Review portrait and font changes
separately.

"Cool" should come from deliberate hierarchy and polished details: a strong
first screen, purposeful whitespace, precise type, attractive section rhythm,
and papers that are effortless to scan. All visual choices must work in light
and dark themes, with reduced motion and on small screens.

## Reader journey

1. **First glance:** Name, current role, institution, research question,
   portrait, email, Scholar, and PDF CV are easy to identify.
2. **First scroll:** Four research interests and the published evidence
   appear before general background or news.
3. **Deeper scan:** All published and accepted papers, current and earlier
   research, teaching, supervision, appointment, and education are available
   without a page transition.
4. **Optional depth:** linked paper titles, full CV, and blog article remain available
   without carrying essential information absent from `/`.

The R9b navigation now links all eleven sections, including Education,
Experience, Research Work, Projects, Blog, and News & Update. The homepage uses
a desktop chapter rail and a full section menu at narrower widths. The research
profile also remains readable through ordinary scrolling.

## Proposed page architecture

This is the current section order after R9b. R9c through R9e will refine the
presentation without removing essential information from the scroll path.

| Order | Section and purpose | Source | Content rule |
|---|---|---|---|
| 1 | Identity and short About: role, institution, question, contacts, CV | `index.html` | Keep the opening compact; no inflated claim. |
| 2 | Research Interests: one question, then four concise areas | `research.html`, `index.html` | Distinguish AI safety and interpretability, large language models, computer vision, and medical AI without presenting an interest as completed work. |
| 3 | Publications: full published and accepted record | `index.html`; old URL bridge in `publications.html` | One canonical visible list; exact titles, authors, venues, status, and linked titles where a paper destination is verified. Never imply accepted means published. |
| 4 | Research Work: cancer-imaging review | `research.html`, `cv.html` | The review is completed; manuscript in preparation. |
| 5 | Projects: EMG thesis and supervised medical-imaging work | `research.html`, `teaching.html`, `cv.html` | Label supervision honestly; no invented publication or ongoing status. |
| 6 | Teaching & Supervision | `teaching.html`, `cv.html` | Current courses first, then past courses and supervision. |
| 7 | Experience | `cv.html` | Lecturer appointment and verified faculty award; omit the PDF-only internship. |
| 8 | Education | `cv.html` | Rajshahi degree, CGPA, and Dean's Award. |
| 9 | News & Update | `index.html` | Dated updates stay chronological. |
| 10 | Blog | `index.html`, `blog.html` | The post is an optional long read. |
| 11 | Contact and footer | `index.html` | Email and public profiles only. |

Do not import the PDF CV's research internship into HTML until asked. Do not
revive the ended YOLO crop-disease project as current work. Keep web development
projects and competitive-programming ratings off the one-page academic profile.
Preserve the chosen **Blog** label. Skills stay in the PDF CV as approved in R1;
later issues refine the remaining section copy.

## Content migration and source of truth

The homepage holds all four complete published and accepted records and the
only publication `ItemList` JSON-LD. It is the content source of truth.
`publications.html` preserves old IDs with title links to those records, while
`cv.html` repeats short citations. `check.py` compares the bridge IDs, titles,
and targets with the homepage and checks structured titles, author order,
venues, and DOIs. Review web CV citations manually when a record changes.

The main visit stays on `/`. Existing publication URLs and bookmarks redirect
to matching homepage anchors when JavaScript runs; the legacy page remains a
readable title index without it. Research, teaching, CV, and blog pages remain
available as optional deeper reads. The canonical policy, fragment targets,
and sitemap treatment are in `planning/R7-URL-MAP.md`. Do not remove these
entry points or duplicate the full paper records.

## Issues and checkpoints

Each row is a separate reviewable issue. Complete one, show the result, then
move to the next. Run `python check.py` after every repository change. Layout
issues also require visual review in both themes and at phone, tablet, and
desktop widths.

| ID | Status | Deliverable | Exit criterion |
|---|---|---|---|
| R0 | Done | Reference review and roadmap | Goal, constraints, sources, sequence, and next task documented. |
| R1 | Done | Exact content inventory and annotated desktop and 375px phone wireframes in `planning/R1-CONTENT-AND-WIREFRAMES.md` | Owner approved A with B's subtle research connection, proposed order, and PDF-only skills. |
| R2 | Done | Semantic one-page skeleton and in-page navigation | Every navigation section is reachable by scrolling and anchors without JS; shared nav and checker pass. |
| R3 | Done | Identity, About, and research focus | Question and three threads read accurately; first screen and first scroll reviewed in both themes. |
| R4 | Done | Complete publications and structured data | Three published papers and one accepted paper have accurate metadata; DOI and BibTeX actions work; checker passes. |
| R5 | Done | Research work, teaching, and academic background | Status, courses, supervision, education, and recognition match sources; mobile rhythm reviewed. |
| R6 | Done | Updates, Blog preview, contact, and finishing details | All essential information is on `/`; optional links are clear; no private details appear. |
| R7 | Done | Legacy URLs, links, metadata, guide, checker, and sitemap | Old entry points work; homepage is canonical for the consolidated profile; checks pass. |
| R8 | In progress | Owner-directed visual revision, full quality review, and deployment preparation | Visual, accessibility, links, content, performance, print, and no-JS checks pass; owner reviews final preview before publishing. |
| [R9](https://github.com/ForhanShahriarFahim/ForhanShahriarFahim.github.io/issues/1) | Implemented locally; owner review pending | Design comparison, condensed navigation, compact interests, publication and list redesign, public links, portrait alignment, and documentation | Review the final preview before publishing. |
| D2 | Done locally | Condensed eight-link index, shorter Research Interests, Education after Research Work, and the verified two-year average | Browser and checker validation recorded below. |
| [C1](https://github.com/ForhanShahriarFahim/ForhanShahriarFahim.github.io/issues/2) | Implemented locally; owner voice review pending | Updated CV, owner-supplied About, and clean ownership of Research Work, Projects, Experience, and Education | Owner reviews wording and selected project presentation before publication. |
| R10 | R10a-e implemented locally; owner review pending | CV replacement, condensed structure, CV-backed projects, recent-list treatment, and release QA | Final preview and validation below; no deployment yet. |
| R11 | Design approved; implementation not started | Top navigation, editorial interests, B.Sc. timeline and coursework, awards, role-based experience, project cards, and fixed-height news | Complete R11a-f in order with per-task checks and owner review before release. |

### R9: owner feedback and implementation checkpoints

The owner's 27 September feedback is tracked as one umbrella issue in
[GitHub #1](https://github.com/ForhanShahriarFahim/ForhanShahriarFahim.github.io/issues/1).
The issue is the complete requested scope and acceptance checklist. Work in
reviewable passes:

1. **R9a, design artifacts:** audit the existing content and measure navigation
   space; draw at least two original desktop and 375px concepts, informed by
   Younus's academic structure and Aritra's publication interaction. Compare
   scanability, phone fit, accessibility, and visual balance. **Done:** selected
   B's desktop section rail and phone menu, with A's year-column publication
   rows. Evidence and caveats: `planning/R9-DESIGN-REVIEW.md`.
2. **R9b, page map and navigation:** make Education, Experience, Research Work,
   Projects, Blog, and News & Update explicit. Keep Teaching, Interests,
   Publications, and Contact easy to reach. Rework active-link behaviour for
   every section and preserve existing fragments and no-JavaScript links.
   **Done locally:** all eleven homepage sections appear in the desktop chapter
   rail and the phone/tablet menu. Research Work, Projects, Experience, and
   Education have separate verified content; `#background` still resolves.
3. **R9c, first screen and contact:** compact the four Research Interests,
   centre the portrait crop, add rounded ORCID/GitHub/LinkedIn links, and show
   email plus public profiles in Contact. **Done locally:** four compact native
   disclosures retain the existing descriptions; the circular crop is centred;
   the opening and Contact provide rounded public-profile links.
4. **R9d, publications:** surface 2026 and exact published/accepted status,
   pair titles with verified outbound links, remove the visible DOI/BibTeX
   toolbar, and retain complete records, structured data, and old URLs.
   **Done locally:** year/status labels and title-adjacent outbound arrows are
   present. The accepted paper has no unverified link. The portrait crop is
   slightly less zoomed in. Checker and browser review pass.
5. **R9e, recent lists:** design accessible scrollable News & Update and Blog
   previews. News gets a View all updates action; Blog links to `blog.html` for
   all posts. The one-post Blog state should not display an empty scrollbar.
   Test a simulated longer list without inventing public posts.
6. **R9f, documentation and release:** preserve durable rules and history while
   reducing the default agent reading set to `AGENTS.md`, `CONTEXT.md`, and this
   roadmap. Keep `README.md` for people; retain assistant-specific pointers
   only if they help discovery. Consolidate `DECISIONS.md` and
   `CONTENT-GUIDE.md` only after their unique information is migrated and
   reviewed. Run the checker after each edit, then repeat responsive, light/dark,
   keyboard, no-JS, reduced-motion, print, link, and content review before owner
   approval and any deployment.

### D2: structure preview and decision

The owner requested four linked changes and asked to see a design before they
are applied. The current production draft still has the eleven-link rail,
"Interests" as the rail label, Education after Experience, and larger interest
disclosures. The visual comparison is shown in the current Codex conversation;
its editable fragment is stored in the thread's visualization directory, not
in this repository. The two alternatives are:

- **Grouped index:** keep all eleven section anchors visible,
  but divide them into Profile, Research, Academic life, and More. Rename the
  rail label to Research Interests. This honours the earlier request for
  explicit Education, Experience, Projects, Blog, and Research Work links.
- **Condensed index, recommended:** eight primary anchors: About, Research Interests,
  Publications, Research Work, Education, Academic Work, News & Blog, and
  Contact. Academic Work covers Projects, Teaching, and Experience; News & Blog
  covers two existing sections. This better addresses the owner's concern
  about a crowded rail. It requires active section tracking and in-page
  sublinks so those destinations remain easy to find. **Chosen by the owner on
  28 September 2026.**

Both previews retain the one-page academic profile, make the four interest
areas compact, and place Education directly after Research Work. The current
PDF CV explicitly states **CGPA 3.66 and Last 2 Years Avg 3.82**. The preview
shows both in Education; use 3.82/4.00 only if the final on-page wording makes
the PDF's grading scale clear. The institution and dates remain unchanged.
The owner still considers the broader About, Projects, Experience, and Education
copy provisional; D2 should change only the verified metric and structure,
leaving C1's content rewrite separate.

After the owner reviews D2, implement in small passes: (1) reorder the semantic
homepage sections and legacy anchors, (2) update the byte-identical nav on all
eight pages plus active tracking, (3) reduce the interest control footprint
while retaining keyboard and no-JavaScript access to descriptions, (4) add the
verified two-year average to Education and reconcile `cv.html`/`CONTEXT.md`,
then (5) run `check.py`, inspect 375, 780, and 1100px in both themes, and
verify direct anchors, menu navigation, print, and no-JavaScript reading order.
R9e's recent-list work follows the structure and CV-led content passes in R10.

**C1, CV-led content review:** This is a separate release gate in
[issue #2](https://github.com/ForhanShahriarFahim/ForhanShahriarFahim.github.io/issues/2).
The owner considers the current About, Projects, Experience, and Education
presentation provisional. The updated PDF arrived on 28 September; R10 below
records the content map and proposed About wording. The owner has explicitly
excluded thesis and research work from Projects. R9f cannot finish until this
CV-led review is resolved.

Content gates: Experience may use the verified Lecturer appointment, but the
PDF-only internship stays out of HTML until the owner explicitly asks for it.
Projects may now show a small selection of verified built systems from the CV
and GitHub; describe them as software projects, not PhD research. Do not repeat
the thesis, systematic review, or supervised students there. The accepted paper has no invented DOI or
publication date. R9's user request to explore scrollable News and Blog
previews supersedes the earlier blanket rejection of a news scrollbox; the
final treatment must resolve its touch, keyboard, no-JS, and print problems.

### R10: finalisation plan and local implementation record

The following plan was written before implementation. For current behaviour,
read the status table above, the progress log below, and `CONTEXT.md`.

**Scope and source.** The owner selected the condensed design and provided
`C:/Users/Asus/Downloads/Md_Forhan_Shahriar_Fahim_CV_PHD_23_09_26_.pdf`.
The existing public asset is `assets/cv/Md_Forhan_Shahriar_Fahim_CV.pdf`.
Both PDFs are two pages; the replacement's visible academic facts are nearly
identical to the old PDF, while its DOI and CSE Hub links are clickable. It
still includes a research internship, telephone number, location, and referee
email addresses. Those remain PDF-only. The new PDF has **not** yet been copied
into the site. Verify the source path still exists when R10a starts.

**CV delivery decision.** Keep one site-hosted PDF at the existing stable URL.
The ordinary **CV** link opens that PDF in a new tab for browser viewing; an
optional separate **Download CV** link can use the same-origin `download`
attribute if a download affordance proves useful. Do not make Google Drive the
primary CV destination: the same-domain PDF has no separate sharing setting,
is easy to open and save, and preserves a stable link across revisions. A Drive
copy may be a private backup. A public Drive link would need its access set to
"Anyone with the link" and checked from a signed-out browser. Replacing the
asset removes the old CV from the current published tree but does not erase Git
history; do not rewrite history as part of this task.

**Final single-page order and eight navigation labels.** Every named content
section remains readable by scrolling, whether or not JavaScript runs:

| Nav label | Content reached | Legacy/direct anchor rule |
|---|---|---|
| About | Hero and About | Keep `#about`. |
| Research Interests | Four compact, expandable fields | Keep `#research` and `#interests`. |
| Publications | Four complete paper records | Keep `#publications` and paper IDs. |
| Research Work | Completed SSL review and correctly labelled research material | Keep `#research-work`. |
| Education | Rajshahi degree, thesis identification, awards, and both averages | Move after Research Work; keep `#education` and `#background`. |
| Academic Work | Projects, Teaching & Supervision, then Experience | Add group anchor; retain `#projects`, `#teaching`, `#experience`, and local sublinks. |
| News & Blog | News & Update, then Blog preview | Add group anchor; retain `#updates`, `#news`, and `#blog`, with local sublinks. |
| Contact | Email and public profiles | Keep `#contact`. |

The active rail pill follows the relevant group while scrolling through its
subsections. The phone disclosure shows the same eight primary labels plus
visible sublinks for Projects, Teaching, Experience, News, and Blog. No section
may become inaccessible when JavaScript is off. The Research Interests link
uses its full name, not "Interests". Compact disclosures keep four labels
visible without long descriptions dominating the page; opening one reveals its
existing detail. At 375px, targets remain at least 44px high and text must not
clip.

**Approved opening copy, now on the homepage.** The owner selected this hero
tagline after supplying his About text:

> I want to understand what AI models learn, why they make certain predictions,
> and where they fail.

The About paragraph keeps his role, interests, and Fall 2028 intent. Its
overlapping sentence was removed so it does not repeat the hero:

> I am a Lecturer in Computer Science and Engineering at Pundra University of
> Science & Technology. My current interests include **AI safety and
> interpretability**, **computer vision**, **large language models**, and
> **vision-language models**.
>
> **I am looking for PhD opportunities beginning in Fall 2028.**

The Research Interests cards still use the prior medical-AI framing. Reconcile
those cards with this owner-supplied list during R10b, while keeping all claims
factual and distinguishing interests from completed work.

**Section ownership and project selection.** This is a content map, not a
second citation list:

| Content | Destination | Evidence and wording limit |
|---|---|---|
| SSL cancer-imaging systematic review | Research Work | Updated CV; completed review, manuscript in preparation. |
| Force-invariant EMG thesis | Education, with detail under Research Work only if needed | Updated CV; never list it as a Project. Avoid duplicate full paragraphs. |
| Undergraduate medical-imaging supervision | Teaching & Supervision | Updated CV; these are students' projects, not Forhan's Projects entries. |
| CSE Academic Operations Hub | Projects | Updated CV and [repository](https://github.com/ForhanShahriarFahim/cse-academic-operations-hub). Describe scheduling, conflict checks, attendance, and workload without implying official deployment. Link to repository. |
| BookHive | Projects | Updated CV and [repository](https://github.com/ForhanShahriarFahim/BookHive). One short factual line about the Laravel/MySQL book catalogue and stock workflow. Link to repository. |
| ViT-family interpretability pipeline and MRI XAI prototype | Candidate future research/software highlights | Public repositories exist, but these are outside the current CV's Technical Projects list. Do not quietly add them to Projects or claim published results. Review separately if the owner wants them featured. |
| ELITE Research Lab / QUALM internship | PDF CV only for now | Present in the updated CV; owner previously deferred HTML inclusion. |

Show no more than two compact Projects rows on the homepage. Link the title or a
small text action directly to the corresponding GitHub repository. Projects
appear below the research evidence, so software work does not lead the page.

**Implementation checkpoints, one reviewable pass at a time:**

| Pass | Change | Acceptance evidence |
|---|---|---|
| R10a | Replace the old PDF asset at its stable path with the supplied PDF. Keep only one current public CV; check every CV link. | Byte/hash comparison against supplied PDF, local HTTP 200, browser open and optional download, PDF link audit, `check.py`. Do not delete the Downloads source. |
| R10b | Apply eight-link navigation, group anchors, Education order and 3.82 average, and smaller interest controls. Update duplicated nav on all pages, tracking JS, checker, docs. | 375, 780, 1100px in both themes; active group states; direct bookmarks; keyboard, no-JS, print, and no overflow. |
| R10c | Retain the owner-supplied About wording now on `index.html`; move EMG thesis out of Projects; add the two CV-backed software project rows; reconcile `research.html`, `cv.html`, and summaries. | CV/GitHub claim audit; no duplicated research or supervision; working repository links; `check.py`. |
| R10d | Complete R9e News & Update and Blog recent previews and all-items actions. | Simulated long list, one-post state, touch, keyboard, no-JS, print, and direct-link checks. |
| R10e | Consolidate documentation only after unique guidance is preserved; complete R9f and release QA. | `check.py`, `git diff --check`, links, content, performance, both themes, responsive widths, owner preview, then deployment decision. |

**Claude and other-agent handoff.** Start with `AGENTS.md` for binding rules,
`CONTEXT.md` for current truth, then this roadmap's Current task and R10 section.
Read `DECISIONS.md` only for a design reversal and `CONTENT-GUIDE.md` for a
routine content edit. `CLAUDE.md` and `GEMINI.md` should be short pointers to
these shared files, not parallel sources of facts. Never infer that an R10 pass
has shipped merely because it is planned: use the progress log and the actual
HTML/PDF. Run `python check.py` after every repository change.

### R1: content and wireframe decisions

- Inventory current pages field by field, noting repetition and the canonical
  source for every claim.
- Draft final section headings, concise copy limits, and a paper display pattern
  using the four verified records.
- Produce desktop and 375px phone wireframes showing initial viewport, section
  order, navigation, and papers. Compare a restrained variant with one slightly
  more expressive variant; both must feel academic.
- Resolve background versus teaching order, visible news length, and whether a
  compact skills line helps.
- Record the selected option and rationale in `DECISIONS.md` before R2.

### R2 to R6: implementation rule

Implement only the named part in each issue. Keep the working site consistent
between issues. A shared navigation edit updates every HTML copy, including
the blog post and `404.html`, and preserves the theme-toggle placement. Show
desktop and phone screenshots after each visual issue and record user feedback.

### R7 to R8: release rule

Keep the published site unchanged until the consolidated page and legacy URLs
are ready. Before publishing, click in-page links and a sample of external and
asset links in a real browser. Inspect with JS disabled, keyboard navigation,
reduced motion, print, system dark, manually selected dark, and light theme.
Check 320, 360, 375, 390, 430, 700, 780, 900, 1100, and 1440px where practical,
especially nav wrapping and horizontal overflow. Check contrast at 4.5:1 or
better. Run `python check.py` after every change and
`python check.py --write-sitemap` when page coverage changes.

## Progress log and handoff format

When an issue finishes, add a row with its date, issue ID, commit or PR if any,
files changed, checks, screenshot or preview path, user feedback, and remaining
concerns. Update the status table and `Current task` line above. Update
`CONTEXT.md` for material page or workflow changes and `DECISIONS.md` for
settled design rationale.

| Date | Issue | Evidence and outcome |
|---|---|---|
| 2026-09-26 | R0 | Reviewed both references and the current site; saved the roadmap. No production page or style changes. |
| 2026-09-26 | R1 draft | Inventoried current HTML, mapped repeated content, and prepared desktop and 375px wireframes A and B in `planning/`. Awaiting owner review; no production page or style changes. |
| 2026-09-26 | R1 approval | Owner chose the recommended hybrid: A's editorial structure and B's restrained research connection. Proceed to R2. |
| 2026-09-26 | R2 | Added all nine homepage sections in the approved order and changed shared navigation on all eight HTML pages to five in-page links. Preserved legacy `#interests` and `#news` anchors. Updated `check.py` for root-section links. Checker passes; headless Chrome confirms one-row links, no horizontal overflow, and light/dark rendering at 375, 780, and 1100px. Native Research anchor works with JavaScript disabled; a secondary page's Contact link returns to `/#contact`. Screenshots: `planning/R2-review/`. No commit or deployment. |
| 2026-09-26 | R3 | Refined the identity and concise About; made Email, Scholar, and PDF CV primary links; separated quieter public profiles; rewrote the research lead and three threads to distinguish published papers, current supervision, completed review, and interests. Added a restrained numbered rail and corrected sticky-nav anchor spacing. `check.py` passes. Headless Chrome reviewed light/dark at 375, 780, and 1100px with no overflow; CV is visible in the first 850px viewport; Research anchor works without JavaScript. Screenshots: `planning/R3-review/`. No commit or deployment. |
| 2026-09-26 | R4 | Copied four complete records, three DOI/BibTeX actions, and the publication `ItemList` to `index.html`; retained matching legacy articles on `publications.html`; pointed homepage updates at paper anchors. Strengthened `check.py` to compare article markup and structured metadata. Fixed mobile BibTeX overflow with and without JavaScript. Checker passes. Browser checks at 375, 780, and 1100px in light/dark found no overflow; all paper anchors and disclosures work; copy reaches `Copied`. Three DOI URLs redirected to Taylor & Francis or IEEE destinations, though publisher content was not independently readable in the automated browser. Screenshots: `planning/R4-review/`. No commit or deployment. |
| 2026-09-27 | R5 | Expanded the completed cancer-imaging review and EMG thesis entries with verified methods, status, supervisor, benchmarks, and result. Recast teaching as current courses, earlier courses, and research supervision; added both verified awards to Academic Background. Removed the stacked main/footer spacing that left a large gap after Contact. `check.py` passes. Fresh local browser and headless Chrome screenshots at 375, 780, and 1100px in light/dark show one navigation link row, no horizontal overflow, and a 40px gap from the last Contact paragraph to the footer border. Screenshots: `planning/R5-review/`. No commit or deployment. |
| 2026-09-27 | R6 | Added the September 2026 review completion to Updates and linked it to Research Work; removed the year-only award update because its month is unverified and the award is already in Academic Background. The six remaining updates run newest first. Marked the Blog article as an optional longer read and reduced Contact to a direct email invitation, removing the institutional postal line. `check.py` passes. Browser review at 375, 780, and 1100px in light/dark found no overflow, one navigation link row, and the compact footer gap; the review and Blog links reached their destinations. With JavaScript disabled, all six updates and the Blog and Contact links remained visible. Screenshots: `planning/R6-review/`. No commit or deployment. |
| 2026-09-27 | R7 | Replaced the duplicate publication page with a legacy URL bridge and preserved all old paper, accepted, year, and in-progress fragments. Rewired internal paper links to the homepage; checked canonicals and social URLs; excluded the bridge and 404 page from a six-URL sitemap. Updated the checker, content guide, agent orientation, and URL map. `check.py` passes. In the local in-app browser, nine publication URL cases reached their intended homepage anchors; the research, teaching, CV, and blog entry pages loaded with self-canonical URLs, and the Research navigation returned to `/#research`. The bridge's visible title links provide the no-JavaScript route; full no-JavaScript and visual review is part of R8. No commit or deployment. |
| 2026-09-27 | R8 design pass | Applied owner feedback: "CV" label, circular portrait, selective bold About phrases, four distinct research interests, "Research Interests" heading, rounded opening and navigation links, active section pill, and scroll progress. `#research` and `#interests` remain valid. `check.py` passes. Local browser checks at 320, 375, 390, 780, and 1100px found no horizontal overflow; five links stay on one row at 375px and above. Active states worked for Interests, Publications, Teaching, Updates, and Contact; the progress line reached 100% at the bottom. Both themes were inspected on a phone. A JavaScript-disabled browser showed all nine homepage sections and working Interests and legacy publication links; reduced motion was enabled for the latter. No commit or deployment. |
| 2026-09-27 | R8 quality review | Checked 320, 360, 375, 390, 430, 700, 780, 900, 1100, and 1440px in light and dark themes: no horizontal overflow, expected nav rows, at least 44px mobile link targets, and compact Contact-to-footer spacing. Contrast ratios for the new navigation state are 7.32:1 in light and 7.04:1 in dark; all checked text pairs exceed 4.5:1. Keyboard focus reaches the skip link and navigation with visible outlines. Reduced motion turns smooth scrolling off; print hides navigation and progress while retaining nine content sections. A JavaScript-disabled browser followed the legacy paper title to the homepage record. Browser console had no errors. `check.py` and `git diff --check` pass. GitHub Pages reports `build_type: workflow`; the stale workflow comment was corrected. Screenshots: `planning/R8-review/`. No commit or deployment. |
| 2026-09-27 | R9 planning | Owner supplied broader navigation, publication, list, contact, portrait, and documentation feedback. Created [GitHub issue #1](https://github.com/ForhanShahriarFahim/ForhanShahriarFahim.github.io/issues/1) with staged design and implementation gates. R8 preview remains unpublished and is no longer the final release candidate. No production UI change in this planning pass. |
| 2026-09-27 | R9a | Created two original responsive HTML artifacts and a 375px comparison in `planning/R9-concepts/`. Reviewed current site and both references in the browser; tested desktop and phone navigation, publication layout, the News disclosure, and spot contrast. Fixed a mobile paper-label collision and a compressed menu/overflow in the artifacts. Chose B's section index and phone menu plus A's desktop paper rows. See `planning/R9-DESIGN-REVIEW.md`. `check.py` passes; production UI and deployment unchanged. |
| 2026-09-27 | R9b | Implemented the eleven-section homepage map and shared navigation in all eight HTML pages. Desktop uses a persistent chapter rail; phone/tablet use an accessible native disclosure containing every section. Current-section highlighting, menu label, and scroll progress follow navigation and direct bookmarks. Separated verified review work, EMG thesis and supervised projects, Lecturer experience, and Rajshahi education; retained `#background`, `#interests`, and `#news`. Extended `check.py` to enforce the map. Local browser reviewed 375, 780, and 1100px in light/dark, section jumps, menu close, and no horizontal overflow; checker passes. Screenshots: `planning/R9b-review/`. Preview: <http://localhost:4175/>. No commit or deployment. |
| 2026-09-28 | R9c | Centred the circular portrait crop; replaced the four long interest blocks with compact native disclosures; added rounded ORCID, GitHub, and LinkedIn links in the opening; added a Contact correspondence panel with email and four public profiles. Kept existing research descriptions and all About, Projects, Experience, and Education copy for the CV-led review in issue #2. Browser reviewed 320, 375, 780, and 1100px, both themes, interest expansion, contact wrapping, 44px action targets, and no horizontal overflow. New text contrast checked above 5.7:1 in light and 7.4:1 in dark. `check.py` passes. Screenshots: `planning/R9c-review/`. No commit or deployment. |
| 2026-09-28 | R9d | Recast four publication rows with visible 2026 labels and exact Published/Accepted status. The three verified DOI destinations are title links with adjacent arrows; the accepted paper remains unlinked. Removed visible DOI/BibTeX actions and unused script/CSS, preserved full records, old anchors, and structured data; checker now enforces these relationships. Eased portrait crop from 108% to 103%. Browser reviewed phone light, desktop light/dark, and paper links; `check.py` passes. Screenshots: `planning/R9d-review/`. No commit or deployment. |
| 2026-09-28 | D2 preview | Reviewed Azmine Wasi's grouped contents index alongside Younus and Aritra; verified the last-two-years average of 3.82 in the current PDF CV. Prepared grouped and condensed original layout previews for owner review. No D2 production changes, commit, or deployment. |
| 2026-09-28 | R10 plan | Owner chose the condensed index and supplied a replacement two-page PhD CV. Audited both PDFs and the public GitHub repositories. Chose the two CV-backed Technical Projects for Projects, with thesis and supervised work in their own sections; drafted About wording, CV delivery, eight-link architecture, five implementation passes, and cross-agent handoff. No page or PDF replacement yet; `check.py` passes. |
| 2026-09-28 | About correction | Owner supplied exact About wording and Fall 2028 timing. Replaced the About paragraph on `index.html`, removed the superseded italic hero line, and updated page descriptions and handoff documents. Research Interests cards await reconciliation in R10b. `check.py` passes; no CV replacement or deployment. |
| 2026-09-28 | Hero tagline | Owner chose "I want to understand what AI models learn, why they make certain predictions, and where they fail." Added it beneath the role; trimmed the repeated sentence from About. `check.py` passes; no deployment. |
| 2026-09-28 | R10a-e local implementation | Replaced the stable CV PDF with the supplied two-page file and confirmed matching SHA-256, HTTP 200, and `application/pdf`; kept the Downloads source. Implemented the eight-link rail and thirteen-link narrow menu, group tracking, Education directly after Research Work with 3.82 average, compact four-interest controls matching the owner-supplied About, and two CV/GitHub-backed Projects. News shows three recent entries with an all-updates keyboard-scroll view; Blog has a one-post preview and archive link. Simulated five Blog previews to verify overflow and keyboard scrolling, then removed the temporary test page. Browser reviewed 375, 780, and 1100px in both themes, group and legacy anchors, menu and interest keyboard controls, 44px phone targets, and no horizontal overflow. Source HTML exposes all six updates without JS; print CSS expands hidden entries. `check.py`, JS syntax, `git diff --check`, local page requests, PDF page count, and colour-token contrast checks pass. The in-app browser's PDF viewer did not render the file, despite a valid PDF response and matching source hash; a standard-browser PDF viewing check remains for release review. No commit, push, or deployment. |
| 2026-09-28 | R11 design and plan | Owner selected editorial one-line interests, top navigation with Community grouping, standalone Experience with teaching and supervision, GitHub project cards without dates, fixed-height News and Updates without a view-all button, the current About text, a one-degree Education timeline, and Awards after Education. Selected coursework was checked against the current PDF CV. Updated the isolated mockup and defined R11a-f above. No production-page implementation, commit, push, or deployment. |
| 2026-09-28 | R11 copy refinement | Owner supplied a revised one-paragraph About with four emphasised interests and Fall 2028 intent. Replaced the five-course proposal with eight owner-provided course titles, confirming “Computer Networks”, and matched the thesis/coursework font sizes in the isolated mockup. R11c now includes the About change. No production-page implementation, commit, push, or deployment. |
| 2026-09-28 | R11a local implementation | Added the one-degree Education timeline, owner-supplied eight-course line, and separate two-entry Awards section. Removed awards duplicated under Education and Experience; updated `check.py` section order. Browser reviewed light/dark at 375, 780, and 1100px with no overflow; thesis and coursework computed at 15.04px. Direct `#awards` worked with and without JavaScript at 375px. `check.py` passed; screenshots saved as `planning/R11a-*.png`. Top nav remains R10 until R11b. No commit, push, or deployment. |
| 2026-09-28 | R11b local implementation | Replaced the desktop rail with top navigation, Community disclosure, and narrow-screen Sections menu on all eight pages. Updated CSS, JS active-section/progress tracking, and `check.py` nav map. Browser reviewed light/dark at 375/780/1100/1280px plus breakpoint checks at 1120/1160px, with no overflow. Community, keyboard, Escape, contact active state, full progress, and no-JS secondary-page Awards link worked. JS syntax and `check.py` pass; screenshots: `planning/R11b-*.png`. No commit, push, or deployment. |
| 2026-09-28 | R11c local implementation | Applied the exact owner About copy as one paragraph with five strong phrases; converted Research Interests to four visible names in an editorial list, with no intro or disclosure controls. Removed unused interest CSS and retained the research detail page. Browser checked light/dark at 375/780/1100/1280px: one desktop line, natural phone wrapping, no overflow. `#interests` worked with and without JS; print retained all four names. `check.py` passed; screenshots: `planning/R11c-*.png`. No commit, push, or deployment. |
| 2026-09-28 | R11d local implementation | Moved Experience before Projects and grouped Teaching and Supervision under the Lecturer role. Kept the `#teaching` and `#academic-work` aliases and teaching detail link. Replaced two dated timeline projects with quiet GitHub cards, without dates or research claims. Browser checked light/dark at 375/780/1100/1280px with no overflow; cards are equal height at tablet/desktop and stack on phones. `#teaching` works with and without JS; print retains the cards. `check.py` passed; screenshots: `planning/R11d-*.png`. No commit, push, or deployment. |
| 2026-09-29 | R11e local implementation | Made Community a direct News anchor without dropdown on all eight shared nav blocks. Kept direct News, Blog, and Contact links in mobile Sections. Replaced News toggle with an always-scrollable six-entry HTML region. Updated mockup, checker, and handoff docs. Browser checked light/dark at 375/780/1100/1280px, keyboard scroll, active Community through Contact, mobile and secondary-page anchors without JS, and print expansion. `check.py`, JS syntax, and `git diff --check` pass. No commit, push, or deployment. |

### R8 remaining checks

- [x] Apply and inspect the owner's content and visual feedback.
- [x] Complete visual and accessibility review across the required widths and both themes.
- [x] Check keyboard focus, reduced motion, print, links, and content consistency.
- [x] Prepare a final local preview for owner review before publishing.
- [x] Record owner feedback: further changes are requested in R9.
- [ ] Repeat release checks and obtain owner review after R9; then decide whether to publish.

## Next action

### R12: approved refinements, 29 September 2026

The owner approved these after R11e. Keep the homepage one-page and the four
research interests visible. The desktop nav and narrow Sections menu have one
**Research** anchor to `#research`, covering Research Interests, Publications,
and Research Work. Remove their other two nav entries, retain their headings and
direct hash destinations, and keep the Research active pill/current label through
all three sections. Community continues to cover News, Blog, and Contact.

The owner confirmed Dinajpur Education Board for both school-examination
scholarships. Add these below the 2025 and 2023 awards in the same compact list:

| Examination year shown | Award title | Supporting line |
|---|---|---|
| 2016 | General Scholarship | Secondary School Certificate (SSC) examination · Dinajpur Education Board |
| 2014 | Talentpool Scholarship | Junior School Certificate (JSC) examination · Dinajpur Education Board |

The years label the examinations, not necessarily the announcement dates. These
individual honours are owner-supplied; no result certificate has been supplied.
The board name is owner-confirmed and matches the board's official site.

On `research.html`, add a visible fixed link back to `index.html#research`
near the title. Keep **Research Work** as the section name for ongoing and
completed studies. There are no arXiv papers now. If one is added later, enter
it in Publications with a *Preprint* status; describe the underlying project in
Research Work only when that adds distinct context. Never imply a preprint is
peer reviewed or duplicate one record as two outputs.

Project cards become whole-card GitHub links. Use a restrained colour transition
on the icon tile, border, and action, matching hover and keyboard focus with
reduced-motion support. The hero's six profile actions keep visible labels;
place them in one compact line when desktop space permits, with natural wrapping
on narrower screens. No icon-only hover labels.

| Task | Status | Work and acceptance |
|---|---|---|
| R12a · grouped Research nav | Done locally | Identical nav on eight pages, scroll tracking, checker, direct and legacy hashes, no-JS mobile links. Research remains active through all three research sections. |
| R12b · awards and return path | Done locally | Two owner-supplied Dinajpur scholarship rows and a fixed research return link; no invented result URL. Direct entry and no-JS return checked. |
| R12c · project and hero interactions | Done locally | Each project card is a semantic GitHub anchor with matching hover and focus treatment. Six labelled hero links fit one row at 1100px and above and wrap on narrower widths. Both themes and reduced motion checked. |
| R12d · integrated review and handoff | Reviewed locally | Checker, JS syntax, whitespace, hashes, no-JS navigation, print, browser console, responsive layout, project focus and hover, and PDF HTTP response checked. Local screenshots saved; owner visual review and release decision remain. |

**R12 validation, 29 September 2026:** `check.py`, JS syntax, and whitespace
checks passed. Browser checks at 375, 780, 1100, and 1280px in light and dark
themes found no horizontal overflow. Research stays active across Research
Interests, Publications, and Research Work; Education and Community select
their own links. Both repository URLs and keyboard focus work. JavaScript-off
mobile navigation and the research return link work. Print retains the project
cards and complete news list. The browser console had no page errors. The CV
link returned HTTP 200 with `application/pdf`; automated PDF rendering in the
local browser did not complete, so visual PDF viewing remains for owner review.
Screenshots: `planning/R12-1280-light.png`, `planning/R12-375-dark.png`,
`planning/R12-projects-light.png`, and `planning/R12-projects-dark.png`.

### R13: Experience and closing-section refinement, 29 September 2026

The owner selected concept A from
`planning/R13-experience-contact-mockups.html`: a role-led Experience layout,
with Teaching and Supervision as concise rows under the Lecturer appointment,
plus a separate AMIR Lab Research Intern role. The internship dates must read
**May 2025 – Dec 2025**. The owner described screening and analysing studies
for a PRISMA-guided review of self-supervised learning in cancer imaging and
drafting manuscript sections and figures. State that contribution succinctly;
the manuscript is in preparation and belongs in Research Work for fuller status.
AMIR Lab's site gives its full name as Advanced Machine Intelligence Research
Lab. The latest supplied CV omits AMIR; the owner separately confirmed this
role for HTML. The 29 September PDF replacement removes the earlier ELITE
Research Lab entry.

The owner also selected compact Contact concept A and equal-weight hero actions
in the order Email, CV, Google Scholar, ORCID, GitHub, LinkedIn. Keep all six
existing icons and the desktop one-row layout; wrap naturally on narrow
screens. Add contextual return links from the Teaching detail page to
Experience and from the individual Blog post to the homepage Blog section.
The research detail page already has its fixed return link. The stable
same-site CV PDF now contains the exact owner-supplied 29 September file from
Downloads; its URL is unchanged. Do not claim the PDF includes AMIR.

| Task | Status | Acceptance |
|---|---|---|
| R13a · Experience | Done locally | Two distinct roles, exact internship dates, short labelled Teaching and Supervision rows, owner-supplied AMIR contribution and lab link, old `#teaching` anchor preserved. |
| R13b · Contact and hero | Done locally | Compact Contact without the tall panel; six labelled, icon-bearing hero actions in approved order, equal weight and one desktop row. |
| R13c · return paths and CV | Done locally | Teaching and Blog post return to relevant homepage sections; exact supplied PDF replaces the old same-site file and its link works. |
| R13d · review and handoff | Reviewed locally | Checker, responsive light/dark layout, no-JS links, print, PDF bytes/render/response, screenshots, contrast, and owner preview. |

**Release task:** The owner authorised GitHub publication on 29 September
2026. Run `check.py`, JavaScript syntax and Git whitespace checks; confirm the
site PDF hash matches the new Downloads file; inspect the PDF and release diff;
then commit and push `main`. Verify the GitHub Actions deploy and the live
homepage and CV URL. Record the deployed commit and remaining issues here.

**Release verification, 29 September 2026:** Commit `0764bc4` was pushed to
`main`. GitHub Actions run `36523267175` passed the consistency check and
Pages deployment. The public homepage returned HTTP 200 with the AMIR role and
Research Interests. The public CV returned HTTP 200 as `application/pdf`,
184,919 bytes, SHA-256
`f662a07588f12554b75664a3ae71fa708f84876af4c90b95b47e8c2d2cead652`,
matching the supplied 29 September replacement. Both pages rendered legibly
before publication. This handoff-status update follows the verified release.

**R13 validation, 29 September 2026:** `check.py`, JavaScript syntax, and
`git diff --check` pass. Browser checks at 375, 780, 1100, and 1280px in
both themes found no horizontal overflow or page errors. The six hero links
retain six icons, follow the approved order, and occupy one row at 1100px and
above. The two Experience roles and full AMIR dates are visible; Contact is
106px high at desktop width and wraps accessibly on phones. New text pairs
exceed 5:1 contrast in both themes. Without JavaScript, the Teaching, Blog,
and Research return links reach `#experience`, `#blog`, and `#research`;
the old `#teaching` target works. Print retains AMIR. The CV matches the
supplied file's SHA-256, rendered legibly on two pages, and returns HTTP 200
with `application/pdf` from the stable site URL. Screenshots:
`planning/R13-experience-1280-light.png`,
`planning/R13-experience-375-dark.png`, `planning/R13-contact-1280-light.png`,
`planning/R13-contact-375-dark.png`, and `planning/R13-hero-1280-light.png`.

**Next task:** Review the public homepage and CV. Record any specific content
or layout corrections before another implementation pass. There is no arXiv
record to add now; follow the R12 preprint rule if one becomes available.

**1 October 2026 correction and CV replacement:** The owner corrected the
exact last-two-years average to 3.79/4.00 and chose 3.8/4.0 for the website.
The homepage and web CV now show that rounded value. The owner supplied a new
two-page PDF CV with 3.8 and the AMIR Lab internship; it replaced the previous
file at the same site path. Earlier 3.82 references above record the historical
source and review, not the current academic fact. The replacement and HTML
changes were pushed to `main` in commit `3a53856` on 1 October 2026.

**2 October 2026 display and CV update:** The owner requested 3.80 in place
of 3.8 and supplied `Md_Forhan_Shahriar_Fahim_CV_PHD_01_10_26_.pdf`.
The homepage and web CV display 3.80/4.00, and the supplied two-page PDF
replaces the previous asset at its stable URL. The exact owner-confirmed
average remains 3.79/4.00; 3.80 is the chosen display of the rounded value.
