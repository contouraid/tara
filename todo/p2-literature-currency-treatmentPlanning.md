# TODO: Literature Currency — Treatment Planning Chapter

**Section:** `treatmentPlanning/`
**Priority:** Medium
**Owner:** (unassigned)
**Opened:** 2026-07-10

## Gap

`treatmentPlanning/treatmentPlanning.md` has zero citation-like references anywhere in the chapter despite covering dose prediction models, knowledge-based planning, and reinforcement-learning approaches to beam angle selection — all areas with substantial recent published work. There is a "Current Research in Treatment Planning Prediction" section, but every claim in it is unsourced. This is the chapter with the largest gap between claimed scope and citation support.

## What Is Needed

1. Add a `## References` section (currently entirely absent) and cite sources for every specific technique or claim already in the chapter body, not just new additions.
2. Add a `## Current Research and Recent Advances` section per the Chapter Content Standard in `GUIDE.md`.
3. Run the searches below (last 18 months, verified per the Sourcing Rules):
   - "diffusion model dose prediction radiotherapy"
   - "deep learning knowledge based planning VMAT dose prediction clinical validation"
   - "reinforcement learning beam angle optimization radiotherapy"
   - "large language model treatment planning assistance radiotherapy"
4. Add verified, cited entries covering: diffusion-model-based dose prediction approaches (a shift from the direct-regression framing the chapter currently implies), and any clinical (not just retrospective-dataset) validation of knowledge-based planning systems now in commercial or research use.

## Acceptance Criteria

- [ ] Chapter has a `## References` section with citations for existing body claims, not only new additions
- [ ] Chapter has a "Current Research and Recent Advances" section with at least 3 verified, dated citations
- [ ] At least one entry addresses diffusion-model-based dose prediction specifically
- [ ] `todo/review-log.md` has an entry recording the searches run and sources found/rejected for this chapter
