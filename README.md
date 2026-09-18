# Asadullah Bhuiyan — research website

Jekyll site for https://asadullahbhuiyan.github.io. The redesign emphasizes the physics of learning while presenting the complete quantum and earlier research record.

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
| Homepage introduction and featured projects | `index.html` |
| Research descriptions and personal contributions | `_pages/research.html` |
| Publications, authors, venues, and statuses | `_data/publications.json` |
| Talks and program links | `_pages/talks.html` |
| Biography, education, teaching, and outreach | `_pages/about.html` |
| CV download | Replace `assets/files/Asadullah_Bhuiyan_CV.pdf`, keeping its name |
| Figure images, captions, and source links | `assets/images/research/` and `_data/figures.json` |
| Portrait | Replace `assets/images/headshot.jpg`; also update `images/Headshot.jpg` to preserve the old URL |
| Name, description, and profile links | `_config.yml` |
| Profile icons and link labels | `_includes/profile-links.html` and `_includes/icons/` |
| Navigation | `_data/navigation.yml` |
| Visual styling | `assets/css/main.scss` |

CV buttons automatically include a build timestamp so that updated PDFs are requested fresh instead of reusing a previously cached download. The underlying PDF address remains stable.

The publication data are JSON; preserve valid quoting and commas. Author strings allow simple `<strong>` markup for the site owner's name. Update statuses consistently on the homepage, research page, and publications data. Research figures have display and larger versions; maintain their aspect ratios and retain readable axes and labels. The figure link opens the larger version directly.

Voice: follow the learning-theory CV's direct, result-first wording. Use “we” for collective paper results and “I” for documented personal contributions. Keep exploratory interests and ongoing results distinct from completed work. Avoid promotional taglines and inflated claims.

## Review and publication

The `redesign` branch contains the reviewed redesign. The existing live site publishes from `master` at the repository root. The check workflow only builds and validates; it cannot deploy and has read-only permissions. No Pages settings were changed.

To publish future changes, commit any corrections, merge the reviewed branch into `master`, and push `master` to publish through the existing GitHub Pages configuration. Verify the GitHub Pages build, navigation, CV, and figures on the live domain. Do not publish merely to obtain a preview.

The annotated record in `docs/PROVENANCE.md` identifies the baseline and reference commits. Backup tag: `before-redesign-2026-09-18`. Before publication, preserve that tag remotely with the reviewed changes. To roll back a published squash merge, revert that merge commit and push the revert, retaining history rather than force-pushing.

## Compatibility and credits

Existing `/publications/`, `/talks/`, and `/cv/` routes remain. `/resume`, `/resume/`, and `/cv-json/` lead to the CV page; `/teaching/` leads to About; `/year-archive/` leads to Research; `/talkmap.html` leads to Talks. The old portrait URL remains available. Removed example posts, fake CV entries, and sample paper/slide PDFs were template content, not the owner's research.

The design is adapted from Hyejin Kim's site and the MIT-licensed Minimal Mistakes theme by Michael Rose and contributors. Source provenance is retained in this repository; the visible design-adaptation credit was removed at the owner's request. Preserve the theme license. Profile icons come from Bootstrap Icons v1.13.1; their MIT license is included in `_includes/profile-links.html`. Research figures belong to their respective paper authors; links identify the source papers. This site contains no comments, analytics, contact-form backend, or externally loaded JavaScript.
