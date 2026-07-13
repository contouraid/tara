# DONE: Add Worked Cases and Formative Assessment

**Section:** Root (cross-cutting)
**Priority:** Low
**Owner:** Codex
**Opened:** 2026-07-11
**Completed:** 2026-07-13

## Gap

Most chapters explain concepts descriptively but do not let readers practice applying them. The index promises case studies for contouring and treatment planning, yet those chapters contain no fully worked clinical cases. A reader can finish the book knowing vocabulary without demonstrating that they can recognize leakage, choose an appropriate metric, critique a paper, identify a safety hazard, or plan a responsible local evaluation.

Worked examples and formative assessment are particularly important for novices because they expose misunderstandings that fluent prose can conceal.

## What Is Needed

1. Develop two or three de-identified synthetic longitudinal cases that recur across imaging, contouring, registration, planning, QA, validation, and workflow chapters.
2. Include at least one failure-focused case involving dataset shift, incorrect geometry/metadata, misleading aggregate performance, automation bias, or unsafe integration.
3. Add short knowledge checks to each chapter, mixing terminology, interpretation, calculation, paper critique, and clinical-safety questions.
4. Provide answers with reasoning and links back to the relevant section; avoid trivia or questions answerable only by memorizing a paper.
5. Add a capstone in which readers specify an intended use, dataset, validation plan, workflow, risk controls, monitoring plan, and evidence threshold for one RT-AI tool.
6. Clearly label all cases as synthetic/educational and avoid presenting them as patient-specific medical advice.

## Acceptance Criteria

- [x] At least two coherent cases recur across three or more chapters and preserve consistent anatomy, task, metadata, and clinical context
- [x] Contouring and treatment-planning chapters contain the case studies promised by `docs/index.md`
- [x] Every chapter has at least five formative questions spanning recall, interpretation, and application
- [x] Answer explanations identify why plausible alternatives are wrong or unsafe
- [x] At least one case demonstrates a high metric score alongside poor clinical utility or safety
- [x] A capstone rubric assesses intended use, data, evidence, human factors, governance, and monitoring
- [x] Cases are explicitly synthetic, accessible to novices, and reviewed for clinical plausibility

## What Was Done

1. Created `docs/resources/cases.md` as the canonical synthetic casebook. It fixes the anatomy, imaging, frames/metadata, AI tasks, role ownership, failure injection, and safe response for head-and-neck, lung stereotactic, and pelvic adaptive cases.
2. Added an explicit educational-use statement and an internal clinical-plausibility check against Chapter 3's pathway, roles, handoffs, and barriers. Numerical values are labeled as synthetic record details rather than recommendations.
3. Added worked-case sections to medical imaging, contouring, registration, treatment planning, QA, validation, and workflow, plus linked the clinical-prediction worked example to Case A.
4. Made high aggregate performance versus poor safety concrete: Case A has mean Dice 0.91 with a cord discontinuity and wrong laterality; Case C retains mean Dice 0.90 while omitting field-edge bowel after a software shift.
5. Added exactly five formative questions to all 12 numbered chapters and both Chapter 2 companion pages: 70 questions total spanning recall, interpretation, calculation where appropriate, paper/claim critique, and clinical-safety application.
6. Added concise reasoned answers to every question, each linking to the relevant teaching section and explaining why a plausible shortcut or alternative is wrong or unsafe.
7. Added a capstone requiring intended use, data, evidence thresholds, human factors, governance/risk, and monitoring. Its 18-point rubric requires at least 14 overall and no safety-domain score below 2 for educational peer review, while explicitly stating that the score is not clinical authorization.
8. Updated `GUIDE.md`, the landing page, resources page, and Sphinx configuration so future chapters preserve the assessment standard, use the canonical cases, and support validated section backlinks.

## Verification

- Mechanically confirmed that all 14 chapter/companion pages contain exactly one `Knowledge Check` with exactly five numbered questions.
- Confirmed Cases A and C each appear across at least medical imaging, contouring, registration/treatment planning, QA/validation, and workflow contexts without changing their fixed record.
- Confirmed contouring and treatment planning have explicit worked-case headings, every case page states its synthetic educational status, and the capstone rubric contains all six required domains.
- Ran `git diff --check` successfully.
- Ran a strict Sphinx HTML build with warnings treated as errors: `make -C docs html SPHINXOPTS='-W --keep-going' BUILDDIR=_build/strict`.
