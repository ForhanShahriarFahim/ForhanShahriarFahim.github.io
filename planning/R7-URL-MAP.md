# R7 URL and link map

The homepage is the complete academic profile and the canonical publication
list. Existing detail URLs remain reachable for readers who have bookmarks or
find them in older material. This map records how they behave after R7.

| URL | Role after R7 | Canonical and sitemap |
|---|---|---|
| `/` and `/index.html` | Complete scrollable profile and publication source | Canonical `/`; listed as `/`. |
| `/publications.html` | Legacy route to the homepage publication anchors; a readable link list when JavaScript is off | Canonical `/`, `noindex,follow`; omitted from sitemap. |
| `/research.html` | Optional deeper research statement and project notes | Self-canonical; listed. |
| `/teaching.html` | Optional course, supervision, and mentoring detail | Self-canonical; listed. |
| `/cv.html` | Web CV and PDF link | Self-canonical; listed. |
| `/blog.html` | Blog index | Self-canonical; listed. |
| `/blog/ml-pipeline-common-mistakes.html` | Complete article | Self-canonical; listed. |
| `/404.html` | Not-found help | `noindex`; omitted from sitemap. |

## Publication bookmark targets

The old page preserves these fragment IDs. With JavaScript, it replaces the URL
with the matching homepage fragment. Without JavaScript, it shows a title link
to the same destination.

| Old fragment | Homepage target |
|---|---|
| no fragment | `/#publications` |
| `#accepted` | `/#pub-raaicon-2026` |
| `#y2026` | `/#publications` |
| `#pub-raaicon-2026` | `/#pub-raaicon-2026` |
| `#pub-jcst-2026` | `/#pub-jcst-2026` |
| `#pub-qpain-2026` | `/#pub-qpain-2026` |
| `#pub-icecte-2026` | `/#pub-icecte-2026` |
| `#in-progress` | `/#research-work` |

Internal paper links from the research page and web CV should point directly to
the homepage. The blog article's research link should do the same. The 404 page
should offer the homepage publication section rather than the legacy route.
The primary navigation already points to homepage sections on every page.
