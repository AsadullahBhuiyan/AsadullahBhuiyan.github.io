# Redesign verification — September 18, 2026

## Build and content checks

- Jekyll 3.10.0 / GitHub Pages 232 builds using Ruby 3.2.2 and Bundler 2.7.1.
- Pinned lockfile resolves for arm64 macOS and x86_64 Linux. Local build executed on macOS; the prepared GitHub check workflow has not been run remotely.
- Production build is separate from the local preview. Production canonical and sharing URLs use `https://asadullahbhuiyan.github.io`.
- Built HTML audit: 13 pages including redirects; 126 local link/asset references checked; no missing local targets or anchors; one h1 per page; no duplicate IDs.
- Five journal articles, one preprint, and one manuscript in preparation are present. Both flagship projects have contribution sections and two figures each.
- All four extracted figures were visually inspected for clipping, labels, and axes. Images are faithful crops from the supplied paper PDFs; larger versions are linked.
- Selected public CV is byte-identical to the existing general academic CV. SHA-256: `9b4fea8c70c45f76a66770653db3770e8896b32dc90698373b7bdd54dc06ce86`.
- Main page and navigation copy contains no leftover friend identity. Hyejin Kim appears only as a legitimate coauthor or design attribution.
- Only the approved CV is shipped as a PDF. Internal documents, provenance records, scripts, and dependency files are excluded from the built site.

## Browser review

- Inspected desktop homepage, research figures, and About, and mobile homepage, Research, Publications, Talks, and About.
- All five main pages checked at 320, 768, and 1280 CSS pixels: document width equals viewport width; five navigation links remain available; one h1 on each page. The 390-pixel mobile layout was also inspected.
- Keyboard: Tab from Research focuses Publications with a visible 3px outline. Enter on Skip to content focuses the main landmark and sets `#main`.
- Navigation is accessible without a hamburger menu or JavaScript. Entrance animations were removed to make page changes immediate. Reduced-motion preference disables smooth scrolling.
- Paper images have alternative text, explanatory captions, source links, and full-size links.

## External links and limits

The external-link check results are recorded in `external-link-check.json`. The flagship paper/preprint, both code repositories, both APS programs, Scholar, and the theme/design links returned successful responses. AIP and MDPI returned 403 responses and LinkedIn returned 999 to the automated client. Their source-verified URLs are retained; successful automated access to these three destinations is not claimed. The Springer DOI resolves but may show a cookie requirement.

Both APS program pages were also read to confirm the talk titles, presenter, and dates. No genuine public slide files were found in the original repository; its slide PDFs were template samples. Private presentation decks were not published.

## Deployment state

The original remote master remains the baseline `ec01a77130944f5c95fe89543f9b9b4546331872`. Repository settings were read, not changed: legacy GitHub Pages, master branch, root directory, no custom domain. Redesign and backup tag are local; no changes have been pushed or deployed. The check workflow has read-only permissions and no deployment step.

Publication follows the user's review. Preserve the backup tag and merge the reviewed redesign into master; verify the resulting Pages build and live routes afterward.
