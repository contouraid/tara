# DONE: Establish Research Synthesis and Evidence Grading

**Section:** Root (cross-cutting)
**Priority:** Medium
**Owner:** Codex
**Opened:** 2026-07-11
**Completed:** 2026-07-12

## Gap

The chapter-level literature-currency todos will add recent papers, but recency alone will not produce a critical account of the state of research. Current recent-advances sections typically list three papers or themes without a reproducible search boundary, evidence hierarchy, comparison table, negative findings, or explicit distinction among technical feasibility, external validation, workflow benefit, patient benefit, and routine adoption.

To meet the book's academic purpose, readers need to understand not only what is new but how mature each sub-area is, where findings agree, where they conflict, and which evidence gaps remain.

## What Is Needed

1. Define a lightweight, reproducible synthesis protocol for each application area: databases, date range, query families, inclusion/exclusion criteria, deduplication, source verification, and stopping rule.
2. Adopt an evidence-maturity vocabulary that separates proof of concept, internal retrospective validation, external/multi-institution validation, silent prospective testing, human-factors/workflow evaluation, clinical impact, regulatory status, and routine adoption.
3. Add a compact evidence table to each AI application chapter with task, population/site, data scale, validation design, comparator, endpoint, principal limitation, and maturity.
4. Include systematic reviews, consensus statements, benchmark/challenge evidence, prospective studies, and informative negative or non-generalizing results; do not construct the state of a field from isolated high-performing papers.
5. Summarize agreement, heterogeneity, clinical relevance, open datasets/code, and unresolved gaps in prose. Keep dated paper entries as an audit trail but periodically synthesize durable conclusions into the main body.
6. Coordinate this protocol with the existing chapter-specific currency todos and `review-log.md` rather than duplicating searches.

## Acceptance Criteria

- [x] `GUIDE.md` defines a reproducible review and evidence-maturity method in addition to recency rules
- [x] Every AI application chapter contains an evidence table using the same core fields and maturity labels
- [x] Research summaries distinguish model performance, external validity, workflow effect, patient outcome, regulatory clearance, and real-world adoption
- [x] Each sub-area includes limitations, contradictory or negative evidence where available, and explicit unanswered questions
- [x] Search dates, query families, inclusion decisions, and rejected sources are recorded in `todo/review-log.md`
- [x] Dated recent-paper entries are periodically converted into durable synthesis without erasing the audit history

## What Was Done

1. Added a reproducible synthesis protocol to `GUIDE.md`: fixed search boundaries, required query families, eligibility and exclusion rules, DOI/PMID/title and cohort deduplication, source verification, common extraction fields, a two-page saturation stopping rule, and required review-log records.
2. Defined eight maturity labels from proof of concept through routine adoption, with explicit warnings that regulatory status and adoption do not prove local validity, effectiveness, or patient benefit.
3. Defined the six application chapters in scope: contouring, registration, treatment planning, clinical prediction, QA, and workflow. Added an `Evidence Synthesis` section to each before its dated recent-advances ledger.
4. Added the same eight table fields to all six chapters: task, population/site, data scale, validation design, comparator, endpoint, principal limitation, and maturity.
5. Added durable synthesis prose separating component performance, external validity, human-workflow effects, clinical or patient outcomes, named-product regulatory status, and routine adoption. Each chapter now states agreement, heterogeneity, clinical meaning, open-resource status, negative or limiting evidence, and unanswered questions.
6. Retained every dated `Current Research and Recent Advances` entry as the intake audit trail while converting stable conclusions into the main body.
7. Corrected two source-record errors found during extraction: the Brouwer contour-editing article's DOI/journal and the Chen et al. explainable-QA article's authorship/journal.
8. Recorded the cross-cutting verification searches, inclusion decisions, contextual sources not assigned a maturity grade, and stopping decision in `todo/review-log.md`. Chapter-specific currency searches remain in their existing open todos.

## Verification

- Confirmed mechanically that all six application chapters contain exactly one `Evidence Synthesis` heading and the identical eight-field table header.
- Confirmed all eight maturity labels are defined in `GUIDE.md` and that chapter prose explicitly addresses the six required evidence questions.
- Confirmed all dated recent-advances entries remain present and the review-log entry records the search date, query families, decisions, and stopping rule.
- Ran `git diff --check` successfully.
- Ran a strict Sphinx HTML build with warnings treated as errors: `make -C docs html SPHINXOPTS='-W --keep-going' BUILDDIR=_build/strict`.
