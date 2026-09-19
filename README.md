# Asadullah Bhuiyan — research website

Jekyll site for https://asadullahbhuiyan.github.io. The homepage is About; Research combines project descriptions with the complete publication record. Navigation is Research · Talks · CV · About.

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
| Research descriptions and personal contributions | `_pages/research.html` |
| Publications, authors, venues, and statuses | `_data/publications.json` |
| Talks and program links | `_pages/talks.html` |
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

The publication data are JSON; preserve valid quoting and commas. Author strings allow simple `<strong>` markup for the site owner's name. Each paper has a unique `project` identifier matching an include in `_pages/research.html`, for example `{% include project-citation.html project="learning" %}`. Edit citation titles, complete authorship, venues, and notes only in `_data/publications.json`; their status comes from the enclosing group. Move an accepted paper from the preprint group to the journal group and update its venue. The `url` is the paper-title link; optional `links` entries provide additional arXiv or code links. Keep each project citation include exactly once and do not duplicate metadata in research prose. The homepage bibliography reads the same data through `_includes/bibliography.html`: editing a citation updates both pages. It shows authors, linked title, venue/year, and any status note, without research summaries, figures, or code links. Groups and papers appear in their JSON order, matching the CV: preprint first, then journal articles, then the manuscript in preparation. Numbering continues across the preprint and journal groups (currently 1–6); in-preparation entries are unnumbered. Do not type citation copies or list numbers into `index.html`. New papers need a unique project identifier, a matching include, and an update to the expected publication records in `scripts/check_site.py`. Research figures have display and larger versions; maintain their aspect ratios and retain readable axes and labels. The figure link opens the larger version directly.

Voice: follow the learning-theory CV's direct, result-first wording. Use “we” for collective paper results and “I” for documented personal contributions. Keep exploratory interests and ongoing results distinct from completed work. Avoid promotional taglines and inflated claims.

## Review and publication

The `content-reorganization` branch contains the local page-consolidation preview. Review it before publishing. The existing live site publishes from `master` at the repository root. The check workflow only builds and validates; it cannot deploy and has read-only permissions. No Pages settings were changed.

To publish future changes, commit any corrections, merge the reviewed branch into `master`, and push `master` to publish through the existing GitHub Pages configuration. Verify the GitHub Pages build, navigation, CV, and figures on the live domain. Do not publish merely to obtain a preview.

The annotated record in `docs/PROVENANCE.md` identifies the baseline and reference commits. Backup tag: `before-redesign-2026-09-18`. Before publication, preserve that tag remotely with the reviewed changes. To roll back a published squash merge, revert that merge commit and push the revert, retaining history rather than force-pushing.

## Compatibility and credits

`/publications/` redirects to `/research/`, `/about/` redirects to the homepage, and `/teaching/` redirects to `/cv/`. `/talks/` and `/cv/` remain. `/resume`, `/resume/`, and `/cv-json/` lead to the CV page; `/year-archive/` leads to Research; `/talkmap.html` leads to Talks. The old portrait URL remains available. Removed example posts, fake CV entries, and sample paper/slide PDFs were template content, not the owner's research.

The design is adapted from Hyejin Kim's site and the MIT-licensed Minimal Mistakes theme by Michael Rose and contributors. Source provenance is retained in this repository; the visible design-adaptation credit was removed at the owner's request. Preserve the theme license. Profile icons come from Bootstrap Icons v1.13.1; their MIT license is included in `_includes/profile-links.html`. Research figures belong to their respective paper authors; links identify the source papers. This site contains no comments, analytics, contact-form backend, or externally loaded JavaScript.
