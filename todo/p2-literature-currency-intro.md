# TODO: Literature Currency — Introduction Chapter

**Section:** `intro/`
**Priority:** Medium
**Owner:** (unassigned)
**Opened:** 2026-07-10

## Gap

`intro/intro.md` covers AI/ML fundamentals (supervised/unsupervised/reinforcement/self-supervised learning, classic algorithms, model evaluation) and a "Current Landscape" framing for AI in radiation oncology, but has no dedicated "Current Research and Recent Advances" section per the `GUIDE.md` Chapter Content Standard, and its examples of "AI in Action" in radiation oncology are not dated or sourced to specific recent literature. As the front door to the book, this chapter should reflect the current state of adoption (regulatory clearances, clinical deployment maturity), not just foundational ML concepts.

## What Is Needed

1. Add a `## Current Research and Recent Advances` section before `## Recap`/`## References` (add those two sections too if not already present in final form).
2. Run the searches below per the Sourcing Rules in `GUIDE.md` (last 18 months, verified via Semantic Scholar/Google Scholar/PubMed):
   - "AI adoption radiation oncology clinical deployment survey"
   - "FDA cleared AI radiotherapy software"
   - "large language models radiation oncology clinical workflow"
   - "self-supervised learning medical imaging foundation model"
3. Add verified, cited entries covering: the current regulatory/adoption landscape (how many AI tools are FDA-cleared for RT use cases), and the emergence of foundation models / self-supervised pretraining as a shift from the task-specific supervised models the chapter currently describes exclusively.
4. Ensure every claim in "Examples of AI in Action" either gets a citation or is rephrased as a general statement without a specific unverified claim.

## Acceptance Criteria

- [ ] Chapter has a "Current Research and Recent Advances" section with at least 3 verified, dated citations
- [ ] Chapter ends with `## Recap` and `## References` per `GUIDE.md`
- [ ] No claim in "Examples of AI in Action" lacks either a citation or a rephrase to remove the unverified specificity
- [ ] `todo/review-log.md` has an entry recording the searches run and sources found/rejected for this chapter
