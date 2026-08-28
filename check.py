#!/usr/bin/env python3
"""Consistency checker for the site.

Because the site is plain HTML with no build step, the shared nav and footer are
duplicated across pages on purpose. This script is what keeps that safe: it
catches drift and broken references before they ship.

Run it after any edit:

    python check.py

Exit code 0 means everything passed; 1 means something needs fixing.
"""

import glob
import os
import re
import sys

PAGES = sorted(p for p in glob.glob("*.html"))
ROOT_RELATIVE = "404.html"  # served from any depth, so it uses absolute paths


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def normalise(fragment):
    """Collapse whitespace and drop the per-page current-page marker."""
    fragment = fragment.replace(' aria-current="page"', "")
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
            target = target.lstrip("/")
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
            if not os.path.exists(src.lstrip("/")):
                problems.append(f"{page}: missing asset -> {src}")

    # --- 2. Shared nav and footer have not drifted ---------------------------
    def shared(page, start, end):
        block = extract(sources[page], start, end)
        if block is None:
            return None
        block = normalise(block)
        if page == ROOT_RELATIVE:
            block = block.replace('href="/', 'href="').replace('src="/', 'src="')
        return block

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

    # --- 4. Publication titles on the homepage match publications.html -------
    def titles(page):
        return set(
            re.sub(r"\s+", " ", t).strip()
            for t in re.findall(r'<h3 class="pub__title">(.*?)</h3>', sources[page], re.S)
        )

    home, full = titles("index.html"), titles("publications.html")
    for title in sorted(home - full):
        problems.append(
            "index.html lists a publication missing from publications.html: "
            + title[:70]
        )

    # --- 5. Every page appears in sitemap.xml -------------------------------
    if os.path.exists("sitemap.xml"):
        sitemap = read("sitemap.xml")
        for page in PAGES:
            if page == "404.html":
                continue
            slug = "" if page == "index.html" else page
            if f"/{slug}<" not in sitemap:
                problems.append(f"sitemap.xml: missing entry for {page}")

    # --- 6. No CSS custom property used without being defined ---------------
    css_path = "assets/css/style.css"
    if os.path.exists(css_path):
        css = read(css_path)
        defined = set(re.findall(r"(--[a-z0-9-]+)\s*:", css))
        used = set(re.findall(r"var\((--[a-z0-9-]+)", css))
        for name in sorted(used - defined):
            problems.append(f"{css_path}: var({name}) is used but never defined")

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
    sys.exit(main())
