# TODO: Literature Currency — Contouring Chapter

**Section:** `contouring/`
**Priority:** Medium
**Owner:** (unassigned)
**Opened:** 2026-07-10

## Gap

`contouring/contouring.md` has a "Current Research in Auto-contouring" section covering OAR contouring and tumor volume delineation, but only 2 citation-like references in the whole chapter, and its architecture coverage stops at U-Net/V-Net/attention-based segmentation — it does not mention segmentation foundation models (e.g., SAM-style promptable segmentation adapted to medical imaging, or general-purpose medical segmentation models trained across many organs/modalities), which represent the most significant architectural shift in this sub-field since the chapter's current content was written.

## What Is Needed

1. Expand the existing `### Organ-at-Risk (OAR) Contouring` and `### Tumor Volume Delineation` subsections, or add a new subsection, to cover foundation-model-based segmentation approaches, per the Chapter Content Standard in `GUIDE.md`.
2. Run the searches below (last 18 months, verified per the Sourcing Rules):
   - "segment anything model medical image segmentation radiotherapy"
   - "foundation model organ at risk segmentation multi-organ"
   - "auto-contouring clinical validation radiotherapy multi-institution"
   - "segmentation challenge leaderboard head and neck radiotherapy"
3. Add verified, cited entries on: promptable/foundation-model segmentation approaches and how they compare to the U-Net-family baselines the chapter currently treats as state of the art; any recent multi-institution clinical validation studies (not just public-dataset benchmarks) for auto-contouring adoption.
4. Cross-check against `p2-literature-currency-fundamentalAI.md` — if a foundation-model architecture is described generically there, link to it here rather than re-explaining the architecture.

## Acceptance Criteria

- [ ] Chapter covers at least one segmentation foundation-model approach with a verified citation
- [ ] At least one added citation is a multi-institution or prospective clinical validation study, not just a public-benchmark result
- [ ] `## References` section exists (add if not already present) and includes the newly-added sources
- [ ] `todo/review-log.md` has an entry recording the searches run and sources found/rejected for this chapter
