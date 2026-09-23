# Project context

Last reviewed against the repository: 23 September 2026.

Read this file at the start of work in this repository, then read `AGENTS.md` for
the binding rules. This is an orientation map, not a substitute for the current
source files. Re-read the relevant page or asset before editing it. If a durable
fact, page, workflow, or design decision changes, update this file in the same
change. Do not treat the review date or a page's fallback "Last updated" text
as proof that a real-world fact is still current.

## Purpose and audience

This is the personal academic website of Md. Forhan Shahriar Fahim, at
<https://forhanshahriarfahim.github.io/>. It supports applications to US AI PhD
programmes for Fall 2027. Faculty and admissions committees are the main
audience. The presentation should be quiet, factual, fast, and recognisably a
researcher's page.

The research narrative asks how to make deep models legible and label-efficient
enough to trust where mistakes are costly. Its three threads are AI safety and
interpretability, computer vision, and health and medical AI. Large language
models are a research interest within the first and third threads. The three
published 2026 vulnerability-detection papers belong to interpretability: they
use LIME, explainable multi-task transformers, and CWE categorisation. The
accepted patch-generation paper is related software-security work, with a
different research claim. Preserve these distinctions when editing the site.

## Current site content

These statements describe what the repository currently publishes. Check the
named source before changing or repeating an exact record.

- **Appointment:** Lecturer, Department of Computer Science & Engineering,
  Pundra University of Science & Technology, since March 2025.
- **Education:** B.Sc. in Computer Science & Engineering, University of
  Rajshahi, 2019 to 2024, CGPA 3.66/4.00. Undergraduate thesis on
  force-invariant surface EMG pattern recognition with a hybrid CNN–LSTM model.
- **Publications:** Three published papers, all dated 2026: a journal paper on
  explainable multi-task transformers for cross-language source-code
  vulnerability detection, a QPAIN paper on CWE-categorised Android
  vulnerabilities, and an ICECTE paper on transformer models with LIME for
  JavaScript vulnerability detection. A fourth paper, VulPatchNet, is accepted
  at RAAICON 2026; it is not yet presented as published and has no DOI on the
  site. `publications.html` is canonical for exact records and status. The
  homepage and web CV repeat summaries and must stay consistent.
- **Research status:** A PRISMA-guided review of self-supervised learning for
  label-efficient cancer imaging (MRI, CT, and histopathology) ran from August
  2025 to September 2026. Its manuscript remains in preparation. The former
  YOLO crop-disease project is no longer pursued and has been removed.
- **Teaching and supervision:** Current courses are Design and Analysis of
  Algorithms and Machine Learning; previous courses include Web Engineering,
  Structured Programming, and Simulation and Modelling. More than ten
  undergraduate research students are supervised. Check `teaching.html` and
  `cv.html` for precise descriptions.
- **Blog:** One post, "The Machine Learning Pipeline, and Where It Usually
  Breaks", dated 28 August 2026. `blog.html` is the index.
- **Public contact and profiles:** Email
  `forhan.shahriar.fahim@gmail.com`; ORCID `0009-0006-8705-4598`; Google
  Scholar user `jkZQkCYAAAAJ`; GitHub `ForhanShahriarFahim`; LinkedIn
  `forhanshahriarfahim`. Do not add a phone number, home address, or referees'
  contact details to the site. The PDF CV has fuller contact information.

The current PDF CV includes an internship that the owner has chosen to add to
the HTML site later. Do not surface it in HTML until explicitly requested. The
web CV is a curated academic page, not a complete transcription of the PDF.

## Where to find the source of truth

| Need | Read |
|---|---|
| Binding agent rules and verification | `AGENTS.md` |
| Why a design or content choice was made | `DECISIONS.md` |
| How to add news, publications, posts, or routine CV content | `CONTENT-GUIDE.md` |
| Bio, current application wording, news, selected papers | `index.html` |
| Research framing, threads, and project status | `research.html` |
| Exact paper records and structured data | `publications.html` |
| Teaching and supervision | `teaching.html` |
| Web CV and PDF link | `cv.html` and `assets/cv/` |
| Blog index and post content | `blog.html` and `blog/` |
| Colours, typography, spacing, responsive and print rules | `assets/css/style.css` |
| Theme, date, news, BibTeX, and back-to-top behaviour | `assets/js/main.js` |
| Validation and sitemap logic | `check.py` |
| Deployment gate | `.github/workflows/deploy.yml` |

`404.html` is the not-found page. `sitemap.xml` lists indexable HTML pages.
`_source/` contains local originals, is ignored by Git, and must not be used as
the public site's source of truth.

## Architecture and working rules

- Static HTML, a single CSS file, and one small vanilla JavaScript file. There
  is no build step, package manager, framework, or CDN script or stylesheet.
  Google Fonts is the only external page request and has local fallback stacks.
- Navigation and footer markup is deliberately duplicated on every HTML page
  for no-JavaScript rendering and search indexing. Edit every copy together.
  Blog posts and `404.html` use root-absolute asset and navigation paths.
- The light, system-dark, and manually selected dark palettes must all remain
  coherent. Keep text contrast at 4.5:1 or better. Persist a theme preference
  only after an explicit click.
- JavaScript injects the back-to-top control, BibTeX copy buttons, and the
  earlier-news toggle after six items. It also updates the footer year and
  "Last updated" date from the page's `Last-Modified` header.
- Use British spelling, understated claims, and no em dashes. Web-development
  projects and competitive-programming ratings belong at the bottom of
  `cv.html`, not on the homepage or research page.
- Run `python check.py` after every change. It checks links, anchors, shared
  markup, metadata, publication title sync, sitemap coverage, and text asset
  integrity. After adding or removing a page, run
  `python check.py --write-sitemap`, then check again. Preview with
  `python -m http.server 4173`. Review layout changes in both themes at phone,
  tablet, and desktop widths, including 375px, 780px, and 1100px.
- Push to `main` to deploy through GitHub Actions. The workflow runs the
  checker before publishing to GitHub Pages. Pages must use GitHub Actions as
  its source.

## Settled choices and open items

`DECISIONS.md` records the full history. In particular, do not reintroduce a
build system, a scrollable news box, JavaScript-injected navigation, or the
reverted narrow prose measure. The owner prefers the fuller text column. The
section label is **Blog**, chosen after considering Notes and Writing.

The portrait and possible font change are open taste decisions. Per-paper PDF
or arXiv links need actual preprint URLs. Do not infer that an open item is
authorised for implementation merely because it is mentioned here.

## Keeping this context current

1. At the start of a task, read this file and `AGENTS.md`, then the relevant
   source files. For a design change, also read `DECISIONS.md`; for routine
   content work, read `CONTENT-GUIDE.md`.
2. When content changes, update its canonical HTML source and any repeated
   summaries first. When the change alters a durable fact or project state,
   update the matching summary above and the review date. Record new rationale
   in `DECISIONS.md` when a settled choice changes.
3. Run the checker after the complete change and resolve failures. Keep
   `CONTEXT.md`, `AGENTS.md`, and assistant entry files as short pointers where
   possible, so facts do not drift between instruction files.

No repository file can force an arbitrary LLM client to read local files.
Assistant integrations that recognise repository instruction files are directed
here; for other clients, supply `AGENTS.md` and `CONTEXT.md` with the task.
