# Asadullah Bhuiyan — research website

Jekyll site for https://asadullahbhuiyan.github.io. A single homepage contains the introduction, two research highlights, complete publication record, and talks in CV format, in that order. Navigation is Research · Publications · Talks · CV; the first three jump to homepage sections, and CV opens the PDF.

## Preview locally

Use Ruby 3.2.2 and Bundler 2.7.1, as recorded in the version files and lockfile.

```sh
gem install bundler -v 2.7.1
bundle install
./scripts/preview.sh
```

Open http://127.0.0.1:4000. Run these commands inside this repository. The preview listens only on the local computer.

To build and check the production site:

```sh
JEKYLL_ENV=production bundle exec jekyll build
python3 scripts/check_site.py _site --production
```

The theme styles are vendored from the reference repository at a recorded commit, so the build does not fetch a moving theme branch. `github-pages` 232 and the complete dependency graph are pinned in the Gemfile and lockfile.

## Update the site

| Change | Location |
|---|---|
| Homepage / About introduction | `index.html` |
| Compact homepage bibliography layout | `_includes/bibliography.html` |
| Two concise research highlights | `_includes/research-highlights.html` |
| Publications, authors, venues, and statuses | `_data/publications.json` |
| Homepage talks, dates, and program links | `_data/talks.json` (layout: `_includes/talks.html`) |
| Education, thesis, teaching, mentoring, and outreach | Maintain these in the CV PDF |
| CV download | Replace `assets/files/Asadullah_Bhuiyan_CV.pdf`, keeping its name |
| Figure images, captions, and source links | `assets/images/research/` and `_data/figures.json` |
| Homepage photo | Replace `assets/images/asad-hiking.jpg`; the full image is displayed without cropping |
| Sharing / legacy portrait | Replace `assets/images/headshot.jpg`; also update `images/Headshot.jpg` to preserve the old URL |
| Name, description, and profile links | `_config.yml` |
| Profile icons and link labels | `_includes/profile-links.html` and `_includes/icons/` |
| Navigation | `_data/navigation.yml` |
| Visual styling | `assets/css/main.scss` |

CV buttons automatically include a build timestamp so that updated PDFs are requested fresh instead of reusing a previously cached download. The underlying PDF address remains stable.

The publication data are JSON; preserve valid quoting and commas. Edit titles, authors, venues, statuses, and paper/code links only in `_data/publications.json`. Author strings allow `<strong>` markup for the site owner's name. The bibliography lists papers in group order and then paper order; empty groups and manuscripts in preparation are hidden. The six published articles are numbered 1–6 automatically. Do not duplicate citations in the research highlights.

Each paper's `project` identifier is stable. The highlight link include (`_includes/research-links.html`) uses `learning` or `quantum` to obtain the main `url` and the link labeled `Research code` from the same publication data. Once published, use the final title, journal details, and DOI as the main URL; arXiv can remain in supplemental links. New publication entries require an update to the expected record in `scripts/check_site.py`.

The highlights follow the introduction, whose only action button opens the CV. Each has two explanatory paragraphs, one figure, and paper/code links. Use `learning_robustness` and `quantum_classification` from `_data/figures.json`; keep scientific scope and experimental settings clear. Captions, source links, alt text, and full-size images are managed there. Historical figure files remain available for previously shared direct image URLs, but are not rendered as extra figures. Contribution lists and other project descriptions belong in the CV rather than on the homepage.

Talks appear directly below the homepage bibliography in the order listed in `_data/talks.json` (newest first). Keep the venue, ISO date, display date, and title current. The optional `url` links the title to its official program; `note` is for brief labels such as an invited seminar.

Voice: follow the learning-theory CV's direct, result-first wording. Use “we” for collective paper results and “I” for documented personal contributions. Keep exploratory interests and ongoing results distinct from completed work. Avoid promotional taglines and inflated claims.

## Review and publication

The live site publishes from `master` at the repository root. The check workflow builds and validates with read-only permissions; GitHub Pages performs deployment separately.

Build and check locally, inspect desktop and mobile layouts, then commit the intended changes and push `master`. Verify both GitHub workflows and the live sections, redirect targets, and CV. Compare the downloaded CV to the supplied PDF when replacing it.

The annotated record in `docs/PROVENANCE.md` identifies the baseline and reference commits. Backup tag: `before-redesign-2026-09-18`. Before publication, preserve that tag remotely with the reviewed changes. To roll back a published squash merge, revert that merge commit and push the revert, retaining history rather than force-pushing.

## Compatibility and credits

`/publications/` redirects to `/#publications`, `/about/` to the homepage, and `/talks/` and `/talkmap.html` to `/#talks`. `/research/` redirects to `/#research`; a small local redirect script forwards its `#learning` and `#quantum` fragments to the matching homepage highlights, with all other fragments falling back to `#research`. Without JavaScript, it falls back to the research overview. `/year-archive/` also redirects to `/#research`. `/cv/` remains a compatibility landing page; `/teaching/`, `/resume`, `/resume/`, and `/cv-json/` lead there. The underlying PDF and legacy portrait URLs remain available.

The design is adapted from Hyejin Kim's site and the MIT-licensed Minimal Mistakes theme by Michael Rose and contributors. Source provenance is retained in this repository; the visible design-adaptation credit was removed at the owner's request. Preserve the theme license. Profile icons come from Bootstrap Icons v1.13.1; their MIT license is included in `_includes/profile-links.html`. Research figures belong to their respective paper authors; links identify the source papers. This site contains no comments, analytics, contact-form backend, or externally loaded JavaScript.
