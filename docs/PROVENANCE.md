# Redesign source record

- Date: September 18, 2026.
- User website baseline: `ec01a77130944f5c95fe89543f9b9b4546331872`.
- Backup tag: `before-redesign-2026-09-18`.
- Design reference: https://github.com/aadeliee22/aadeliee22.github.io at `ac46e0b9235f4d4e41e9b992482156ec8443a838`.
- Theme SCSS and the starting custom stylesheet are copied from that exact reference. The layouts/navigation are adapted for the new content and accessible, script-free navigation. The vendored files are the build source; no floating remote theme is used.
- Original MIT license retained. Visible footer credits Jekyll, Minimal Mistakes, and Hyejin Kim.
- The extra upstream 4.26.2 checkout used during inspection is not a build dependency and supplies no separately imported files.

## Content sources

- `Documents/LaTeX/postdoc_learning_cv.tex`, September 15 version: primary interests and current contribution wording.
- `Documents/PDFs/academic_cv.pdf`: unchanged public CV download; comprehensive record. Its SHA-256 is recorded in the verification report.
- `Documents/LaTeX/academic_cv.tex`: detailed contributions and earlier research.
- Flagship preprints already supplied in the workspace: arXiv:2606.11319v1 and arXiv:2507.13437v3. Figure extraction coordinates and PDF hashes are in `figure-provenance.json`.
- The research-profile and talk-evidence records corroborate contribution attribution and event dates. These private working documents are not copied into the site.
- Headshot explicitly provided by the user on September 18. Used without generative alterations; CSS controls display framing.

## Editorial decisions

- Lead with physics of learning and use the complete five-article, one-preprint, one-in-preparation record.
- Homepage and research pages use direct scientific prose aligned with the user's current CV.
- Distinguish ReLU/cross-entropy robustness experiments from erf/MSE theory validation. Identify the fitted centroid model.
- Distinguish ideal exponentially localized preparation from the finite-range protocol and trajectory-resolved from trajectory-averaged quantities.
- Manuscript in preparation: public title, authors, status, and a brief CV-grounded description only. No unpublished figure or manuscript included.
- The code linked from the quantum feature is explicitly labeled related follow-up code.
- APS event names/titles follow the verified official programs. No public slide deck was present in the existing repository: its three slide PDFs were Academic Pages samples. Private presentation files were not published. Talks link to official programs and relevant research instead.
- Do not copy the general CV's older research-interest wording over the newer learning-theory wording. The selected CV itself remains unchanged, as requested.

## Legacy routes

Preserved: `/`, `/publications/`, `/talks/`, `/cv/`, `/images/Headshot.jpg`.
Redirected: `/resume`, `/resume/`, `/cv-json/` → `/cv/`; `/teaching/` → `/about/`; `/year-archive/` → `/research/`; `/talkmap.html` → `/talks/`.
New: `/research/`, `/about/`, stable academic CV asset, four figure pairs.
The old collection entries and sample PDFs were unmodified Academic Pages placeholders. They are removed from the public build and remain recoverable in Git history.
