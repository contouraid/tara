# TODO: Establish Research Synthesis and Evidence Grading

**Section:** Root (cross-cutting)
**Priority:** Medium
**Owner:** (unassigned)
**Opened:** 2026-07-11

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

- [ ] `GUIDE.md` defines a reproducible review and evidence-maturity method in addition to recency rules
- [ ] Every AI application chapter contains an evidence table using the same core fields and maturity labels
- [ ] Research summaries distinguish model performance, external validity, workflow effect, patient outcome, regulatory clearance, and real-world adoption
- [ ] Each sub-area includes limitations, contradictory or negative evidence where available, and explicit unanswered questions
- [ ] Search dates, query families, inclusion decisions, and rejected sources are recorded in `todo/review-log.md`
- [ ] Dated recent-paper entries are periodically converted into durable synthesis without erasing the audit history
