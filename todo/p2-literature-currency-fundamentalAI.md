# TODO: Literature Currency — Fundamentals of AI Chapter

**Section:** `fundamentalAI/`
**Priority:** Medium
**Owner:** (unassigned)
**Opened:** 2026-07-10

## Gap

`fundamentalAI/index.md` is the longest and most detailed chapter (925 lines: perceptrons, activation functions, feedforward networks, loss functions, backpropagation, initialization, and more), but it has only 5 citation-like references in the entire body and no "Current Research and Recent Advances" section. Its "Further Reading" list at the bottom includes only classic/foundational references (Attention Is All You Need, nnU-Net 2021, a 2022 survey) — nothing tracking what's changed since 2023. Its `vlm.md` sub-page is a placeholder (tracked separately in `p0-write-stub-chapters.md`), but once written, VLM content and this chapter's core deep-learning content need to stay coherent with each other.

## What Is Needed

1. Add a `## Current Research and Recent Advances` section per the Chapter Content Standard in `GUIDE.md`.
2. Run the searches below (last 18 months, verified per the Sourcing Rules):
   - "foundation model medical image analysis 2025"
   - "self-supervised pretraining radiology deep learning"
   - "parameter efficient fine-tuning medical imaging"
   - "vision transformer medical image segmentation benchmark"
3. Add verified, cited entries on: the shift from task-specific CNNs (the chapter's current implicit framing) toward foundation-model / fine-tuning paradigms; any major architecture or training-technique advances since the 2022 survey currently cited.
4. Once `fundamentalAI/vlm.md` is written (see `p0-write-stub-chapters.md`), cross-check that this chapter's "Current Research" section and the VLM sub-page don't duplicate the same citations — link instead of repeating.

## Acceptance Criteria

- [ ] Chapter has a "Current Research and Recent Advances" section with at least 3 verified, dated citations from 2024 or later
- [ ] "Further Reading" / references list includes at least one source newer than the current newest (2022)
- [ ] No duplicated citation content between this chapter and `fundamentalAI/vlm.md` once both are current
- [ ] `todo/review-log.md` has an entry recording the searches run and sources found/rejected for this chapter
