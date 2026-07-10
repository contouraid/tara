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
