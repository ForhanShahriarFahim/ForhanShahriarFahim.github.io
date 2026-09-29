#!/usr/bin/env python3
"""Consistency checker for the site.

Because the site is plain HTML with no build step, the shared nav and footer are
duplicated across pages on purpose. This script is what keeps that safe: it
catches drift and broken references before they ship.

Run it after any edit:

    python check.py

Exit code 0 means everything passed; 1 means something needs fixing.

It can also regenerate sitemap.xml from the indexable pages on disk, which is
the easiest way to keep it correct after adding a page:

    python check.py --write-sitemap
"""

import glob
import html as html_lib
import json
import os
import re
import sys

# Root pages plus every post under blog/. Paths are normalised to forward
# slashes so the script behaves identically on Windows and Linux (CI).
PAGES = sorted(
    p.replace(os.sep, "/")
    for p in glob.glob("*.html") + glob.glob("blog/*.html")
)

SITE = "https://forhanshahriarfahim.github.io/"
# The publications page is a legacy route to the canonical homepage list.
INDEXABLE = [p for p in PAGES if p not in ("404.html", "publications.html")]


def slug(page):
    return "" if page == "index.html" else page


def write_sitemap():
    """Regenerate sitemap.xml from indexable pages on disk."""
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    # Homepage first, then the rest alphabetically.
    ordered = sorted(INDEXABLE, key=lambda p: (p != "index.html", p))
    for page in ordered:
        lines.append(f"  <url><loc>{SITE}{slug(page)}</loc></url>")
    lines.append("</urlset>")
    with open("sitemap.xml", "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(lines) + "\n")
    print(f"Wrote sitemap.xml with {len(INDEXABLE)} entries.")


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def normalise(fragment):
    """Collapse whitespace, drop the current-page marker, and make root-absolute
    URLs comparable with the relative ones used by pages at the site root."""
    fragment = fragment.replace(' aria-current="page"', "")
    fragment = fragment.replace('href="./#', 'href="#')
    fragment = fragment.replace('href="/', 'href="').replace('src="/', 'src="')
    return re.sub(r"\s+", " ", fragment).strip()


def extract(html, start_marker, end_marker):
    i = html.find(start_marker)
    if i == -1:
        return None
    j = html.find(end_marker, i)
    return html[i : j + len(end_marker)]


def main():
    problems = []
    sources = {p: read(p) for p in PAGES}
    ids = {p: set(re.findall(r'\sid="([^"]+)"', h)) for p, h in sources.items()}

    # --- 1. Internal links, anchors, and assets all resolve -------------------
    for page, html in sources.items():
        for href in re.findall(r'href="([^"]+)"', html):
            if href.startswith(("http://", "https://", "mailto:")):
                continue
            if href.startswith("#"):
                if len(href) > 1 and href[1:] not in ids[page]:
                    problems.append(f"{page}: dead anchor {href}")
                continue
            target, _, fragment = href.partition("#")
            if target in ("./", "/"):
                if fragment and fragment not in ids["index.html"]:
                    problems.append(f"{page}: dead homepage anchor -> {href}")
                continue
            target = target.split("?", 1)[0].lstrip("/")
            if not target:
                continue
            if not os.path.exists(target):
                problems.append(f"{page}: link to missing file -> {href}")
            elif fragment and target.endswith(".html"):
                if fragment not in ids.get(target, set()):
                    problems.append(f"{page}: dead cross-page anchor -> {href}")

        for src in re.findall(r'src="([^"]+)"', html):
            if src.startswith(("http://", "https://", "data:")):
                continue
            if not os.path.exists(src.split("?", 1)[0].lstrip("/")):
                problems.append(f"{page}: missing asset -> {src}")

    # --- 2. Shared nav and footer have not drifted ---------------------------
    def shared(page, start, end):
        block = extract(sources[page], start, end)
        return None if block is None else normalise(block)

    for label, start, end in [
        ("nav", '<nav class="site-nav"', "</nav>"),
        ("footer", '<footer class="site-footer"', "</footer>"),
    ]:
        baseline = shared("index.html", start, end)
        if baseline is None:
            problems.append(f"index.html: no {label} found")
            continue
        for page in PAGES:
            block = shared(page, start, end)
            if block is None:
                problems.append(f"{page}: no {label} found")
            elif block != baseline:
                problems.append(f"{page}: {label} has drifted from index.html")

    # The complete homepage map must remain reachable in both nav layouts.
    section_map = [
        "about", "research", "publications", "research-work", "education",
        "awards", "experience", "projects", "updates", "blog", "contact",
    ]
    primary_map = [
        "research", "education", "awards", "experience", "projects", "updates",
    ]
    menu_map = [
        "research", "education", "awards", "experience", "projects",
        "updates", "blog", "contact",
    ]
    home_sections = re.findall(r'<section id="([^"]+)"', sources["index.html"])
    if home_sections != section_map:
        problems.append("index.html: homepage section order differs from the navigation map")
    for nav_class, end_marker, expected in (
        ("site-nav__links", '<details class="site-nav__menu"', primary_map),
        ("site-nav__menu-links", '</div>', menu_map),
    ):
        nav_group = extract(sources["index.html"], f'<div class="{nav_class}"', end_marker)
        link_ids = re.findall(r'<a(?: class="[^"]+")? href="[^"]*#([^"]+)">', nav_group) if nav_group else []
        if link_ids != expected:
            problems.append(f"index.html: {nav_class} differs from the navigation map")
    if '<a class="site-nav__community" href="./#updates">Community</a>' not in sources["index.html"] or '<details class="site-nav__community">' in sources["index.html"]:
        problems.append("index.html: Community must link directly to News and Updates")
    if '<a href="./#research">Research</a>' not in sources["index.html"]:
        problems.append("index.html: Research must link directly to Research Interests")
    for group_id in ("academic-work", "news-blog"):
        if group_id not in ids["index.html"]:
            problems.append(f"index.html: group #{group_id} is missing")
    for old_id in ("interests", "news", "background", "teaching"):
        if old_id not in ids["index.html"]:
            problems.append(f"index.html: legacy #{old_id} bookmark is missing")

    # --- 3. Every page carries the required head plumbing --------------------
    required = [
        ('localStorage.getItem("theme")', "inline theme init (prevents theme flash)"),
        ("assets/css/style.css", "stylesheet link"),
        ("assets/js/main.js", "main.js script"),
        ('class="theme-toggle"', "theme toggle button"),
        ('class="skip-link"', "skip link"),
        ('lang="en"', 'lang="en" attribute'),
        ('name="viewport"', "viewport meta"),
        ("<title>", "title"),
        ('name="description"', "meta description"),
        ('id="year"', "footer year span"),
    ]
    for page, html in sources.items():
        for needle, label in required:
            if needle not in html:
                problems.append(f"{page}: missing {label}")
        for tag in re.findall(r"<img [^>]*>", html):
            if "alt=" not in tag:
                problems.append(f"{page}: <img> without alt text")

        if page != "404.html":
            canonical_url = SITE if page == "publications.html" else SITE + slug(page)
            canonical = re.findall(r'<link rel="canonical" href="([^"]+)"', html)
            og_url = re.findall(r'<meta property="og:url" content="([^"]+)"', html)
            if canonical != [canonical_url]:
                problems.append(f"{page}: canonical URL must be {canonical_url}")
            if og_url != [canonical_url]:
                problems.append(f"{page}: og:url must be {canonical_url}")
            for prop in ("og:title", "og:description"):
                if not re.search(rf'<meta property="{prop}" content="[^"]+"', html):
                    problems.append(f"{page}: missing {prop}")
            noindex = bool(re.search(r'<meta name="robots" content="[^"]*noindex', html))
            if noindex != (page == "publications.html"):
                problems.append(f"{page}: incorrect noindex status")

    # --- 4. Homepage papers and legacy publication routes agree -------------
    def publication_records(page):
        return re.findall(
            r'<article class="pub" id="(pub-[^"]+)">(.*?)</article>',
            sources[page], re.S,
        )

    home_records = publication_records("index.html")
    home_ids = [pub_id for pub_id, _ in home_records]
    if not home_records or len(home_ids) != len(set(home_ids)):
        problems.append("index.html: publication records are missing or have duplicate IDs")
    if publication_records("publications.html"):
        problems.append("publications.html: full paper records belong on index.html")
    if '<body data-legacy-publications>' not in sources["publications.html"]:
        problems.append("publications.html: missing legacy-route marker")

    bridge_records = re.findall(
        r'<div class="pub" id="(pub-[^"]+)" data-canonical-target="([^"]+)">'
        r'\s*<h3 class="pub__title"><a href="index.html#([^"]+)">(.*?)</a></h3>',
        sources["publications.html"], re.S,
    )
    if [pub_id for pub_id, _, _, _ in bridge_records] != home_ids:
        problems.append("publications.html: legacy paper IDs/order differ from index.html")
    for (pub_id, article), (bridge_id, target, href_id, title) in zip(home_records, bridge_records):
        if bridge_id != pub_id or target != pub_id or href_id != pub_id:
            problems.append(f"publications.html: {pub_id} does not route to its homepage anchor")
        home_title = re.search(r'<h3 class="pub__title">(.*?)</h3>', article, re.S)
        visible_title = html_lib.unescape(re.sub(r"<[^>]+>", "", home_title.group(1))).strip() if home_title else ""
        if html_lib.unescape(title).strip() != visible_title:
            problems.append(f"publications.html: {pub_id} title differs from index.html")
    for old_id, target in {
        "accepted": "pub-raaicon-2026",
        "y2026": "publications",
        "in-progress": "research-work",
    }.items():
        section = re.search(rf'<section id="{old_id}" data-canonical-target="([^"]+)"', sources["publications.html"])
        if not section or section.group(1) != target or target not in ids["index.html"]:
            problems.append(f"publications.html: legacy #{old_id} route is missing or incorrect")

    def item_lists(page):
        lists = []
        scripts = re.findall(
            r'<script type="application/ld\+json">(.*?)</script>',
            sources[page], re.S,
        )
        for script in scripts:
            try:
                data = json.loads(script)
            except json.JSONDecodeError as exc:
                problems.append(f"{page}: invalid JSON-LD ({exc})")
                continue
            if data.get("@type") == "ItemList":
                lists.append(data)
        return lists

    home_lists = item_lists("index.html")
    if len(home_lists) != 1:
        problems.append("index.html: expected one publication ItemList JSON-LD block")
    if item_lists("publications.html"):
        problems.append("publications.html: publication ItemList belongs on index.html")
    if len(home_lists) == 1:
        items = home_lists[0].get("itemListElement", [])
        if len(items) != len(home_records):
            problems.append("index.html: ItemList count differs from visible papers")
        for position, ((pub_id, article), entry) in enumerate(
            zip(home_records, items), start=1
        ):
            item = entry.get("item", {})
            if entry.get("position") != position:
                problems.append(f"index.html: {pub_id} has wrong ItemList position")

            def visible(pattern):
                match = re.search(pattern, article, re.S)
                if not match:
                    return ""
                without_tags = re.sub(r"<[^>]+>", "", match.group(1))
                return re.sub(r"\s+", " ", html_lib.unescape(without_tags)).strip()

            if item.get("name") != visible(r'<h3 class="pub__title">(.*?)</h3>'):
                problems.append(f"index.html: {pub_id} title differs from ItemList")
            year = visible(r'<span class="pub__year">(.*?)</span>')
            expected_year = item.get("datePublished") or pub_id.rsplit("-", 1)[-1]
            if year != expected_year:
                problems.append(f"index.html: {pub_id} visible year differs from its record")
            status = visible(r'<span class="pub__status[^\"]*">(.*?)</span>')
            expected_status = "Published" if item.get("datePublished") else "Accepted"
            if status != expected_status:
                problems.append(f"index.html: {pub_id} visible status differs from its record")
            authors = visible(r'<p class="pub__authors">(.*?)</p>').split(", ")
            listed_authors = [author.get("name") for author in item.get("author", [])]
            if authors != listed_authors:
                problems.append(f"index.html: {pub_id} author order differs from ItemList")
            venue = visible(r'<p class="pub__venue">(.*?)</p>')
            listed_venue = item.get("isPartOf", {}).get("name", "")
            if not listed_venue or listed_venue not in venue:
                problems.append(f"index.html: {pub_id} venue differs from ItemList")
            doi = re.search(r'href="(https://doi\.org/[^"]+)"', article)
            if (doi.group(1) if doi else None) != item.get("sameAs"):
                problems.append(f"index.html: {pub_id} DOI differs from ItemList")
            title_link = re.search(r'<h3 class="pub__title"><a href="([^"]+)"', article)
            if (title_link.group(1) if title_link else None) != item.get("sameAs"):
                problems.append(f"index.html: {pub_id} title link differs from ItemList")
            if 'class="pub__actions"' in article or 'class="bibtex"' in article:
                problems.append(f"index.html: {pub_id} still has a DOI/BibTeX action row")

    # --- 5. Every page appears in sitemap.xml -------------------------------
    if os.path.exists("sitemap.xml"):
        sitemap = read("sitemap.xml")
        listed = set(re.findall(r"<loc>([^<]+)</loc>", sitemap))
        expected = {f"{SITE}{slug(page)}" for page in INDEXABLE}
        for missing in sorted(expected - listed):
            problems.append(f"sitemap.xml: missing entry for {missing}")
        for extra in sorted(listed - expected):
            problems.append(f"sitemap.xml: lists a page that no longer exists: {extra}")
        if listed != expected:
            problems.append("fix both with: python check.py --write-sitemap")

    # --- 6. No CSS custom property used without being defined ---------------
    css_path = "assets/css/style.css"
    if os.path.exists(css_path):
        css = read(css_path)
        defined = set(re.findall(r"(--[a-z0-9-]+)\s*:", css))
        used = set(re.findall(r"var\((--[a-z0-9-]+)", css))
        for name in sorted(used - defined):
            problems.append(f"{css_path}: var({name}) is used but never defined")

    # --- 7. Text assets must be clean UTF-8 with no stray control bytes ----
    # A mangled escape sequence once wrote a literal NUL into the stylesheet,
    # which the browser then rendered as visible mojibake. Cheap to guard.
    nul = bytes([0])
    replacement_char = chr(0xFFFD)
    text_assets = (["assets/css/style.css", "assets/js/main.js"]
                   + sorted(glob.glob("*.md")) + PAGES)
    for asset in text_assets:
        if not os.path.exists(asset):
            continue
        with open(asset, "rb") as fh:
            raw_bytes = fh.read()
        if nul in raw_bytes:
            problems.append(f"{asset}: contains a NUL byte (broken escape sequence?)")
        try:
            text = raw_bytes.decode("utf-8")
        except UnicodeDecodeError as exc:
            problems.append(f"{asset}: is not valid UTF-8 ({exc})")
            continue
        if replacement_char in text:
            problems.append(f"{asset}: contains U+FFFD, so a character was lost")

    # --- Report -------------------------------------------------------------
    print(f"Checked {len(PAGES)} pages: {', '.join(PAGES)}")
    if problems:
        print(f"\n{len(problems)} problem(s) found:\n")
        for problem in problems:
            print("  x " + problem)
        return 1
    print("\nAll checks passed.")
    return 0


if __name__ == "__main__":
    if "--write-sitemap" in sys.argv:
        write_sitemap()
    sys.exit(main())
