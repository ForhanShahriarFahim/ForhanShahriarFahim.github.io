# Decision log

Why this site looks and works the way it does. `AGENTS.md` holds the rules;
this file holds the reasoning, including things that were tried and rejected.
Read it before proposing a change that contradicts something here.

Last updated: 29 August 2026.

---

## Who this is for

Md. Forhan Shahriar Fahim, Lecturer in CSE at Pundra University of Science &
Technology, applying to **AI PhD programmes in the United States for Fall 2027**.
The audience is faculty and admissions committees. Every design decision is
judged by one question: does this help a busy academic reader find the research,
or does it make the page look like a developer portfolio?

## The research narrative (do not flatten this)

The three published papers are all software-vulnerability detection, while the
stated interests are interpretability, computer vision, and health AI. These are
not separate: the papers apply LIME and explainable multi-task transformers, so
they *are* applied interpretability in a high-stakes domain. The site states one
question, "how do we make deep models legible and label-efficient enough to be
trusted when the cost of a mistake is high", and shows three settings for it.
Anyone rewriting the About or Research copy must preserve that thread.

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
| Plain HTML, one CSS file, one small JS file, no build step | Content volume is three papers and one post. A content-collection system is machinery without payoff, and nothing can break during application season. |
| Nav and footer duplicated across every page | Injecting them with JS would hide them from search engines and break no-JS rendering. `check.py` detects drift, which makes the duplication safe. |
| `writing/` pages and `404.html` use root-absolute paths | They are served from a different depth. `check.py` normalises this before comparing navigation. |
| Deploy through GitHub Actions, not branch deploy | It lets `check.py` gate the deploy, so a broken edit fails the build instead of taking the live site down. |
| Screenshots captured with headless Chrome | The preview pane scales and sometimes returns mid-paint frames. Chrome gives real resolution. Note it enforces a ~500px minimum window width, so 390px shots must be rendered inside a 390px iframe and cropped. |

## Rejected alternatives

- **Jekyll / academicpages**: dated visuals, jQuery-heavy, painful Ruby setup on
  Windows, and instantly recognisable as a template.
- **Hugo Blox**: content coupled to remotely-versioned modules, three breaking
  rebrands, growing paid-tier push. Built for labs with 1,000+ papers.
- **Astro**: needs Node plus a build step for content that does not justify it.
- **A scrollable news box** (as on some faculty pages): traps touch scrolling on
  phones, hides items below its own fold, clips when printed, and needs
  `tabindex` plus a label for keyboard access. `main.js` collapses entries past
  the sixth behind a toggle instead.
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
- ~~Renaming "Notes" to "Writing".~~ **Done on 29 August 2026.** "Notes"
  promised short technical jottings, but the section carries reflections and
  life events too. "Writing" covers all three without promising any, and it is
  standard on faculty pages. Done while nothing linked to the old URL yet.
  "Journal" was rejected as actively confusing next to a Publications page
  listing journal articles; "Blog" as the label committees associate with
  developer portfolios.
- **Adding PDF or arXiv links per paper.** A content task; needs preprint URLs.
- The homepage shows DOI only while `publications.html` shows DOI and BibTeX.
  This is intentional: the homepage is a teaser, and duplicating BibTeX blocks
  would double the two-file sync burden.

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
