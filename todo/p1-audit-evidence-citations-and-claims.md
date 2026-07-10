# TODO: Audit Evidence, Citations, and Clinical Claims

**Section:** Root (cross-cutting)
**Priority:** High
**Owner:** (unassigned)
**Opened:** 2026-07-11

## Gap

The book does not yet have a consistent academic evidence base. Citation density and style vary sharply: `intro/intro.md` uses many inline author-date links, several newer chapters support broad bodies of content with only three or four references, and `treatmentPlanning/treatmentPlanning.md` contains no citations. `contouring/contouring.md` ends with a literal `- ...` reference placeholder. Four chapters also do not end with the distinct `Current Research and Recent Advances`, `Recap`, and `References` sections required by `GUIDE.md`.

This prevents a novice from distinguishing established knowledge, expert interpretation, emerging evidence, and speculation. It also makes claims difficult to verify and undermines the book's stated role as a citable introduction.

## What Is Needed

1. Build a claim-to-source audit for every chapter, prioritizing numerical claims, comparative performance claims, statements about clinical benefit or adoption, safety and regulatory claims, and descriptions of named methods.
2. Add authoritative foundational sources for stable concepts and verified primary, consensus, or systematic-review sources for clinical and research claims. Replace a preprint with its peer-reviewed version when one exists and label any retained preprint.
3. Standardize clickable numbered in-text citations and numbered reference lists according to `GUIDE.md`; remove malformed, duplicated, dead, indirect-PDF, and placeholder references.
4. Separate evidence from outlook language. Qualify claims when evidence is retrospective, single-center, benchmark-only, or not radiotherapy-specific.
5. Bring `intro/intro.md`, `fundamentalAI/index.md`, `contouring/contouring.md`, and `treatmentPlanning/treatmentPlanning.md` into the required closing-section structure without duplicating the chapter-specific literature-currency todos.
6. Record source-verification dates and decisions in `todo/review-log.md` so later reviews do not repeat the audit.

## Acceptance Criteria

- [ ] Every substantive, quantitative, comparative, clinical, regulatory, or safety claim has a nearby verified citation or is explicitly framed as an illustrative statement
- [ ] Every chapter uses the citation and reference format defined in `GUIDE.md`
- [ ] Every cited source appears once in its chapter's `References` list, every numbered citation resolves to that source, and no placeholder reference remains
- [ ] All ten numbered chapters and the VLM page have distinct `Current Research and Recent Advances`, `Recap`, and `References` sections
- [ ] Preprints are labeled and are not used when a corresponding peer-reviewed publication is available
- [ ] A clean strict Sphinx build completes without citation-related or cross-reference warnings
- [ ] `todo/review-log.md` records the chapters audited, links checked, and major sourcing decisions
