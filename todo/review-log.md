# Literature Review Log

This is a standing log of every monthly autonomous review cycle. It is append-only — never delete or rewrite a past entry. Its purpose is to give the next review cycle (which starts with no memory of this one) a record of what was searched, what was found, what was rejected, and why, so work isn't repeated and rejected sources aren't re-proposed without new evidence.

Append one entry per cycle, in the format below, at the **top** of the log (newest first).

```markdown
## <YYYY-MM-DD> review

**Chapters reviewed:** <list>
**Todos closed:** <list, or "none">
**Todos opened:** <list, or "none">

### Searches run
- <chapter>: "<query>" (Semantic Scholar / Google Scholar / arXiv / PubMed) — <N candidates found>

### Added
- <chapter>: <one-line description of what was added, with citation>

### Rejected
- <candidate paper/claim>: <reason — e.g., "single preprint, no citations, no code">

### Notes for next cycle
- <anything the next run should know — e.g., a search that returned nothing useful, an ambiguity that needs a human call>
```

---

## Log

## 2026-07-11 responsible-AI closure

**Chapters reviewed:** new `responsibleAI/` chapter plus cross-links in `fundamentalAI/vlm.md`, `qa/`, `validation/`, and `workflow/`
**Todos closed:** `p1-consolidate-responsible-ai-regulation-and-security.md` (moved to `todo/done/`)
**Todos opened:** none

### Searches run
- US regulation: "HIPAA Security Rule compliance date" (HHS primary pages) — Security Rule effective and compliance dates verified.
- US FDA guidance: "predetermined change control plan final guidance artificial intelligence-enabled device software functions" (FDA primary pages) — current final-guidance status and August 2025 update verified.

### Added
- responsibleAI: a canonical novice-accessible treatment of obligation types, the full AI lifecycle, regulation and privacy by jurisdiction, fairness, transparency, cybersecurity, third-party risk, governance checklist, and RACI responsibility map with 14 sources.
- QA, validation, VLM, and workflow: stable Sphinx-native cross-references to the canonical governance, regulatory, fairness, and security sections.

### Rejected
- File-plus-fragment Markdown links were not retained for cross-document section references because MyST did not resolve generated heading fragments with `heading_anchors=0`; explicit labels and `{ref}` roles were used instead.

### Notes for next cycle
- Clean strict build `../.venv/bin/sphinx-build -b html -W -n . _build/strict`: **zero warnings**, all 14 source files.
- Regulatory summaries remain orientation rather than legal advice. Recheck jurisdiction, effective date, and primary regulator status before relying on them in future cycles.

## 2026-07-11 strict-build closure

**Chapters reviewed:** all ten numbered chapters, `fundamentalAI/vlm.md` (verification pass only, no content rewrites)
**Todos closed:** `p1-audit-evidence-citations-and-claims.md` (moved to `todo/done/`)
**Todos opened:** none

### Searches run
- None — this cycle verified the prior "2026-07-11 evidence audit" cycle's claims rather than sourcing new content. No new literature search was performed.

### Added
- medicalImaging: fixed one dead citation URL (NIBIB's `.../science-topics/x-rays` now 404s on NIH's own site) by pointing both the in-text citation and reference-list entry to the current `.../science-topics/medical-x-rays` page (verified live, `200`).

### Rejected
- N/A — no new content proposed this cycle.

### Notes for next cycle
- Ran `sphinx-build -W --keep-going -b html docs <out>` (the build the prior cycle couldn't run in its sandbox) via a `uv`-managed Python 3.13 venv with `docs/requirements.txt` installed: **zero warnings**, all 12 source files.
- Independently cross-checked in-text `[n]` markers against each chapter's numbered `References` list (Sphinx doesn't validate this — these are plain Markdown links, not docutils citation roles). All 11 pages had an exact one-to-one match.
- Live-checked all 67 unique URLs cited across the book. Several Wiley/AAPM, BMJ, ACM, Oxford Academic, MIT Press, and IEEE Xplore DOIs return `403`/`202` to a plain HTTP client — verified with a headless browser that these are Cloudflare/WAF bot-challenges, not dead links; each resolves to the correct article/book page for a human visitor. Only the NIBIB link above was genuinely dead.
- If a future cycle re-runs a link check and hits `403`/`202` on a DOI, don't treat that as broken by default — confirm with a real browser first, since major publishers block scripted clients.

## 2026-07-11 evidence audit

**Chapters reviewed:** `intro/`, `fundamentalAI/` (including `vlm.md`), `fundamentalRO/`, `medicalImaging/`, `contouring/`, `registration/`, `treatmentPlanning/`, `qa/`, `validation/`, `workflow/`
**Todos closed:** none (`p1-audit-evidence-citations-and-claims.md` remains open pending a strict Sphinx build)
**Todos opened:** none

### Searches run
- contouring: "U-Net biomedical image segmentation", "V-Net volumetric medical image segmentation", "Metrics Reloaded image analysis validation", and "Segment Anything in Medical Images" (DOI/Crossref metadata) — canonical architecture, evaluation, clinical-editing, and foundation-model sources checked
- treatmentPlanning: "OpenKBP dose prediction challenge", "predicting dose-volume histograms knowledge-based planning", "automation IMRT treatment planning review", "multiobjective radiotherapy Pareto", and "diffusion model radiotherapy dose prediction" (DOI/Crossref metadata) — foundational KBP/MCO sources and one 2025 peer-reviewed diffusion study checked
- cross-cutting: DOI, publisher, PMLR, WHO, FDA, DICOM, TCIA, and PubMed links used by all 11 pages were reconciled against each chapter's numbered reference list on 2026-07-11

### Added
- intro: replaced a duplicated author-date link collection with an evidence-led introduction distinguishing technical performance, clinical validity, utility, and lifecycle safety; added 12 verified numbered sources.
- fundamentalAI: added primary citations for the perceptron, backpropagation, initialization, batch normalization, CNNs, LSTM, GANs, transformers, U-Net, and nnU-Net; added the required closing sections.
- contouring: removed the literal placeholder reference, qualified overlap and clinical-acceptability claims, and added seven primary, systematic-review, or validation sources.
- treatmentPlanning: removed the unsupported universal dose-error claim, distinguished prediction from calculation and deliverability, qualified KBP/MCO/outcome claims, and added seven verified sources.
- medicalImaging and VLM: added the missing recent-advances structure, removed indirect general-imaging links, reconciled dataset citation URLs, and replaced the CLIP arXiv link with its peer-reviewed ICML/PMLR version.

### Rejected
- Legacy introduction links that pointed to direct PDFs, secondary summaries, mislabeled papers, or unreviewed RO-LMM/ROND preprints were removed rather than carried into the normalized reference list.
- A universal claim that dose-prediction models achieve less than 5% prescription-dose error was removed because normalization, evaluated region, beam inputs, dataset, and aggregation differ between studies.
- Benchmark performance was not presented as evidence of clinical benefit; benchmark-only, retrospective, and transfer claims are labeled in the revised prose.

### Notes for next cycle
- A mechanical audit found sequential reference numbering on every page, one-to-one citation/reference URL mappings, no orphaned references, and all three required closing headings on all ten chapters plus `vlm.md`.
- `sphinx-build -W --keep-going -b html docs /tmp/tara-sphinx-evidence-audit` could not run because Sphinx is not installed. Installing `docs/requirements.txt` in a temporary virtual environment failed under restricted DNS; the required elevated network request was then denied because the environment reported its current usage limit. Run the strict build once dependencies are available, fix any warnings, then close and archive `p1-audit-evidence-citations-and-claims.md`.

## 2026-07-11 review

**Chapters reviewed:** `medicalImaging/`, `contouring/`, `registration/`, `treatmentPlanning/`, `qa/`, `validation/`, `workflow/`
**Todos closed:** `p1-add-radiotherapy-data-and-informatics-foundations.md`
**Todos opened:** none

### Searches run
- medicalImaging: "radiotherapy DICOM RT Structure Set Segmentation RT Plan RT Dose treatment record registration objects" (DICOM Standard) — current standard, WG-07, and second-generation RT materials reviewed
- medicalImaging: "radiotherapy collection license RTSTRUCT RTDOSE CT dataset" (TCIA) — NSCLC-Radiomics, LCTSC, Head-Neck-PET-CT, HNSCC, and RADCURE candidates reviewed
- medicalImaging: "OpenKBP dataset official license CT dose structures" (publisher and challenge sources) — peer-reviewed dataset paper verified
- medicalImaging: "FAIR principles", "Datasheets for Datasets", and "federated learning medicine multi-institutional" (publisher and PubMed sources) — foundational documentation and distributed-learning sources verified

### Added
- medicalImaging: canonical patient-level RT data model, geometry and units, cohort construction, leakage prevention, provenance, privacy, dataset documentation, public datasets, and federated-learning foundations with 11 new verified references.
- application chapters: concise links to the canonical data foundations from contouring, registration, treatment planning, QA, validation, and workflow.

### Rejected
- Dataset summaries without authoritative access/license information were not used; collection landing pages or the peer-reviewed dataset publication were required.
- Search results that were preprints, secondary summaries, or unrelated datasets were not cited where a primary standard, collection page, or peer-reviewed source was available.

### Notes for next cycle
- The separate `p2-literature-currency-medicalImaging.md` todo remains open; this review backfilled foundational informatics rather than performing the chapter's recent-advances scan.

### Initialization note (2026-07-10)

At setup time, no review cycles had run. This repository was set up for autonomous literature-tracking on 2026-07-10 — see `../GUIDE.md` for the process and `README.md` for open todos. The first cycle was expected to start with `p0-write-stub-chapters.md` and `p1-fix-broken-toc-anchors.md`, since both blocked the "Current Research" mechanism the later P2 literature-currency todos depend on.
