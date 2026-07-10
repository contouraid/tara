# TODO: Add Worked Cases and Formative Assessment

**Section:** Root (cross-cutting)
**Priority:** Low
**Owner:** (unassigned)
**Opened:** 2026-07-11

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

- [ ] At least two coherent cases recur across three or more chapters and preserve consistent anatomy, task, metadata, and clinical context
- [ ] Contouring and treatment-planning chapters contain the case studies promised by `docs/index.md`
- [ ] Every chapter has at least five formative questions spanning recall, interpretation, and application
- [ ] Answer explanations identify why plausible alternatives are wrong or unsafe
- [ ] At least one case demonstrates a high metric score alongside poor clinical utility or safety
- [ ] A capstone rubric assesses intended use, data, evidence, human factors, governance, and monitoring
- [ ] Cases are explicitly synthetic, accessible to novices, and reviewed for clinical plausibility
