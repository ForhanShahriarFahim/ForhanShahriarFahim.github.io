# Project context

Last reviewed against the repository: 29 September 2026.

Read this with `AGENTS.md` at the start of a task. This file describes the
current local site; `ONE-PAGE-ROADMAP.md` holds the staged history and status.
Check the source file before changing or repeating an exact claim.

## Purpose and current state

This is Md. Forhan Shahriar Fahim's academic site for US AI PhD applications
beginning in Fall 2028. Faculty and admissions committees should be able to
read the research profile, all paper records, education, teaching, and contact
on one scrollable homepage. The design is quiet, factual, fast, and static.
R10a-e, R11a-e, R12a-c, and R13a-c are implemented locally and owner reviewed.
Integrated checks are recorded in `ONE-PAGE-ROADMAP.md`. The owner approved
publication on 29 September 2026; deployment verification is the current task.
The owner has approved the **R11 target design**. R11a Education and Awards and
R11b top navigation, R11c About and Research Interests, R11d Experience
and Projects, and R11e Community and News are complete locally. R12a-c add
grouped Research navigation, two school scholarships, a research return link,
whole-card GitHub actions, and compact labelled hero links. R12d is the
integrated review. R13 adds the owner-reviewed Experience and Contact layouts,
equal-weight profile links, contextual returns, and the exact supplied CV.
The reviewed R11 mockup is
`planning/top-nav-community-news-mockup.html`; the ordered tasks and checks
are in the R11 section of `ONE-PAGE-ROADMAP.md`. The owner's later Community
correction replaces the mockup's dropdown with a direct News anchor.
Do not mistake the mockup for the deployed or local site.

The About text and Fall 2028 timing on `index.html` were supplied by the
owner after the original R10 plan. Do not substitute the older proposed
Fall 2027 paragraph. The hero question is: "I want to understand what AI
models learn, why they make certain predictions, and where they fail."
For R11, the owner supplied a further revised About paragraph. Its exact
one-paragraph copy and emphasis are in the R11 target rules of
`ONE-PAGE-ROADMAP.md` and now on `index.html`.

## Verified facts and content boundaries

- Lecturer, Department of Computer Science & Engineering, Pundra University
  of Science & Technology, since March 2025.
- B.Sc. CSE, University of Rajshahi, January 2019 to December 2024.
  CGPA 3.66/4.00; last two years average 3.82/4.00. The undergraduate
  force-invariant surface-EMG thesis belongs to Education and the research
  detail page, never homepage Projects.
- The R11 homepage Selected coursework line is owner-provided: Artificial
  Intelligence, Digital Image Processing, Algorithms, Data Structure,
  Database, Operating System, Computer Networks, and Cryptography and Network
  Security. “Computer Networks” was confirmed by the owner. This supersedes
  the previous five-course proposal; do not claim all eight are PDF-verified.
  Match its font size to the Undergraduate thesis line in the R11 design.
- Three published 2026 papers and one accepted 2026 conference paper. The
  accepted VulPatchNet paper has no verified DOI or public paper URL. Complete
  visible records and ItemList JSON-LD are on `index.html`; the old
  `publications.html` URL is a bookmark bridge.
- There is no arXiv preprint now. A future preprint belongs in Publications
  with its status explicit; Research Work may describe its underlying study
  when that adds distinct context.
- The PRISMA-guided systematic review of self-supervised learning in cancer
  imaging ran August 2025 to September 2026. It is complete; its manuscript
  is in preparation, not published.
- The owner confirmed a Research Intern role at AMIR Lab (Advanced Machine
  Intelligence Research Lab), May 2025 to December 2025. During it he screened
  and analysed studies for the cancer-imaging review and drafted manuscript
  sections and figures. This owner-supplied role is absent from the current PDF.
- Four interests: AI safety and interpretability, computer vision, large
  language models, and vision-language models. The last two are future
  research interests, not claims of completed work. The three published
  vulnerability-detection papers are interpretability work; the accepted
  patch-generation paper has a different claim.
- Homepage Projects contains two CV-backed built systems in GitHub cards:
  CSE Academic Operations Hub and BookHive, linked to their public repositories.
  Do not imply the Hub was officially deployed. Undergraduate medical-imaging
  student projects are under Teaching & Supervision, not Projects.
- Awards includes the 2025 faculty award, 2023 Dean's Award, and two
  owner-supplied Dinajpur Education Board scholarships. The 2016 SSC General
  Scholarship and 2014 JSC Talentpool Scholarship use examination years,
  which need not equal announcement dates. Individual result certificates
  have not been supplied.
- The owner's supplied two-page PDF CV is at
  `assets/cv/Md_Forhan_Shahriar_Fahim_CV.pdf`. The site opens it in a new
  tab via a stable same-site URL. Its bytes match the owner's Downloads file.
  The owner's 29 September replacement removes the ELITE Research Lab entry.
  It still omits AMIR, which the owner separately supplied and approved for
  HTML. Fuller contact details remain PDF-only. Do not add phone, address, or
  referees' details to HTML unless explicitly asked.
- Teaching, current and previous courses, awards, and public profile links
  should be checked in `index.html`, `teaching.html`, and `cv.html` before
  changing exact wording. Web-development and competitive-programming details
  remain low on `cv.html`; the two selected Projects are an owner-approved
  exception for the homepage.

## Current architecture

Plain HTML, one CSS file, one small vanilla JavaScript file. No build step,
dependencies, framework, or CDN code. Google Fonts is the only external page
request and has local fallbacks.

The homepage section order is About, Research Interests, Publications,
Research Work, Education, Awards & Recognition, Experience, Projects,
News and Updates, Blog, Contact. The sticky top bar links directly to
Research (`#research`), Education, Awards, Experience, and Projects. Research
stays active through Publications and Research Work. Community is a direct
`#updates` link without a dropdown, and
its active state continues through Blog and Contact. Below 1120px, a Sections disclosure exposes the same
destinations. On phones its row sits below the name and theme toggle. About
stays on the page without a nav link. Experience has separate Lecturer and
AMIR Lab Research Intern roles; Teaching and Supervision remain concise rows
under Lecturer. There is no separate homepage
Teaching section. All eleven section IDs remain addressable, and old
`#teaching`, `#interests`, `#news`, `#background`,
`#academic-work`, and `#news-blog` bookmarks still resolve. JS highlights the
current nav group or section and shows page progress; ordinary
scrolling and native anchors work without JS.

The homepage Research Interests section now shows four names on one editorial
line at tablet/desktop widths and wraps on phones. It has no introduction or
expansion controls; `research.html` retains the longer explanations.
Projects follows Experience as two undated, whole-card GitHub links; the EMG
thesis stays in Education. The fuller course and supervision records remain on
`teaching.html`. The six hero actions keep visible labels and fit on one row at
1100px and wider, wrapping naturally below that. Their order is Email, CV,
Google Scholar, ORCID, GitHub, LinkedIn, with icons and equal label weight.
Contact is a compact email and public-profile strip. `research.html` has a
fixed return link to Research Interests; `teaching.html` returns to Experience
and the Blog post returns to the homepage Blog section.

News keeps all six current entries in a fixed-height, keyboard-focusable and
touch-scrollable list. There is no view-all control. All entries remain in
HTML without JS, and print expands the region. Blog currently has one post, no scrollbar,
and a "View all posts" link to `blog.html`. Once more than three homepage
post previews exist, JS makes the preview scrollable.

Shared navigation and footer are duplicated intentionally across all HTML
pages. Root pages use relative paths; `blog/` and `404.html` use root-absolute
paths. `check.py` validates markup parity, links, anchor map, publication
bridge, metadata, JSON-LD, sitemap, and text integrity. Run it after every
change.

## Source map and handoff

| Need | Source |
|---|---|
| Binding rules | `AGENTS.md` |
| Active status, staged history, next task | `ONE-PAGE-ROADMAP.md` |
| Design rationale and superseded choices | `DECISIONS.md` |
| Routine content editing | `CONTENT-GUIDE.md` |
| Current homepage and publication records | `index.html` |
| Research detail | `research.html` |
| Teaching detail | `teaching.html` |
| Web CV and current PDF | `cv.html`, `assets/cv/` |
| Blog index and post | `blog.html`, `blog/` |
| Style and behaviour | `assets/css/style.css`, `assets/js/main.js` |
| Validation and deployment | `check.py`, `.github/workflows/deploy.yml` |

For Claude or another agent, read `AGENTS.md`, this file, and the roadmap's
Current task/R11/Next action first. Read `DECISIONS.md` when considering a
design reversal and `CONTENT-GUIDE.md` for a routine edit. `CLAUDE.md` and
`GEMINI.md` are pointers, not parallel sources of facts. Begin with R12d;
do not repeat the earlier R10 implementation.

The local preview is `http://localhost:4177/` while its server is running.
After any edit, run the bundled Python executable or `python check.py`.
Before publishing, inspect both themes, 375/780/1100px widths, navigation,
news scrolling, blog link, PDF, no-JS content, print, and the browser console.
Publishing uses GitHub Actions on a push to `main`; this task has not pushed.
