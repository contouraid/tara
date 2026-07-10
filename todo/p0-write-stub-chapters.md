# TODO: Write Stub Chapters

**Section:** `fundamentalRO/`, `registration/`, `qa/`, `validation/`, `workflow/`, `fundamentalAI/vlm.md`
**Priority:** Critical
**Owner:** (unassigned)
**Opened:** 2026-07-10

## Gap

`docs/index.md` promises ten chapters plus a Vision Language Models sub-page under Chapter 2, each with a bullet-point description of what it covers. Six of these currently contain only a title line and, for the sub-page, one placeholder sentence:

- `fundamentalRO/fundamentalRO.md` — "3. Fundamentals of Radiation Oncology" (title only)
- `registration/registration.md` — "6: AI in Image Registration and Fusion" (title only)
- `qa/qa.md` — "8: AI for Quality Assurance and Safety" (title only)
- `validation/validation.md` — "9: Validation and Evaluation of AI Models" (title only)
- `workflow/workflow.md` — "10: Integration of AI into Clinical Workflow" (title only)
- `fundamentalAI/vlm.md` — "Vision Language Models" + "Example text for vision language models." (placeholder)

This is more than half the book's chapter list. A reader following the table of contents in `docs/index.md` hits a blank page for 5 of 10 numbered chapters and one linked sub-page. Until these are written, the per-chapter literature-currency process described in `GUIDE.md` has nothing to build on for these topics — there is no body content to add a "Recent Advances" section to.

## What Is Needed

For each stub, write a chapter matching the depth and structure of the existing complete chapters (`intro/intro.md`, `fundamentalAI/index.md`, `medicalImaging/medicalImaging.md`, `contouring/contouring.md`, `treatmentPlanning/treatmentPlanning.md` — roughly 250–950 lines, organized into `##`/`###` sections), and following the Chapter Content Standard in `GUIDE.md` (body, Current Research and Recent Advances, Recap, References).

Use the bullet points already promised in `docs/index.md` as the required scope for each:

1. **`fundamentalRO/fundamentalRO.md`** — Radiation physics in medicine; radiobiology basics for treating cancer with high-energy radiation; history, current state, and future of radiation oncology as a field.
2. **`registration/registration.md`** — Concepts of image registration (rigid, deformable, multimodal); AI-enhanced/learning-based registration methods; clinical applications integrating multimodal imaging (e.g., MR-CT registration for target delineation, 4D-CT registration for motion management).
3. **`qa/qa.md`** — Quality assurance processes in radiation therapy; AI applications in QA (automated error detection, machine QA, patient-specific QA); regulatory considerations (FDA, IEC 62304-adjacent context) for AI tools in the QA workflow.
4. **`validation/validation.md`** — Performance metrics for AI model validation (accuracy, sensitivity, specificity, Dice/Hausdorff for segmentation, calibration for dose prediction); clinical validation pathway from research to practice; continuous/post-deployment monitoring.
5. **`workflow/workflow.md`** — Workflow analysis for AI integration points; user training and clinical acceptance strategies; change management for introducing AI into an existing radiation oncology department.
6. **`fundamentalAI/vlm.md`** — Vision-language models as a sub-topic of Chapter 2: what they are, how they differ from vision-only CNNs/transformers, and why they're relevant to radiation oncology (e.g., report generation, multimodal reasoning over images + clinical text).

Each new chapter must be added to (or confirmed already present in) the relevant `toctree` block, matching the pattern already used by the five complete chapters.

## Acceptance Criteria

- [ ] All six stubs have real body content matching the Chapter Content Standard in `GUIDE.md`
- [ ] Each new chapter has a "Current Research and Recent Advances", "Recap", and "References" section
- [ ] `docs/index.md`'s WIP notice at the top is reassessed once this todo and `p1-fix-broken-toc-anchors.md` are both closed
- [ ] No new chapter introduces a hand-written GitHub-style TOC block (see `p1-fix-broken-toc-anchors.md`)
- [ ] A `p2-literature-currency-*.md` todo is opened for each newly-written chapter once it lands, mirroring the ones already open for the five complete chapters
