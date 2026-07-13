# Synthetic Casebook and Capstone

(casebook-safety)=
## Educational-use statement

Every person, image, identifier, measurement, plan, model result, and event on this page is **synthetic and deliberately simplified for education**. Nothing here describes a real patient, prescribes care, or replaces local protocols, qualified clinical judgment, commissioning, or patient-specific review. Numerical values make the reasoning concrete; they are not treatment recommendations.

The cases were checked for internal consistency against the pathway, roles, handoffs, and safety barriers in [Chapter 3](../fundamentalRO/fundamentalRO.md). The plausibility check confirmed that each record has a coherent disease site, imaging sequence, geometry, contouring task, planning task, accountable reviewer, QA route, and fallback. Deliberate failures are marked as failures; no learner should copy them into practice.

## How to use the cases

Read the fixed case record here before solving a chapter's worked step. Do not silently repair missing or conflicting data. State what is known, what must be verified, who owns the decision, and the safe fallback. The same case can support different intended uses, but changing the intended use changes the evidence and controls required.

(case-a)=
## Case A — Head-and-neck curative course

**Fixed synthetic record:** An adult with a right-sided oropharyngeal primary and ipsilateral nodal disease is planned for a curative intensity-modulated course. The planning CT is contrast-enhanced, has 1.0 × 1.0 × 2.0 mm voxels, and uses frame of reference `HN-A-PLAN`. A T2-weighted MRI acquired in treatment position has 0.8 × 0.8 × 2.0 mm voxels and is imported for target review. The prescribed synthetic plan is 70 Gy in 35 fractions to the high-dose target with lower-dose elective volumes. Required structures include target volumes, spinal cord, brainstem, parotids, mandible, oral cavity, and optic structures. The radiation oncologist owns target and organ-at-risk approval; the planning and physics team owns plan and technical verification.

**AI tasks:** MRI-to-CT registration, target and organ-at-risk autocontouring, plan-quality prediction, and 12-month xerostomia-risk estimation for additional supportive care.

**Deliberate failure:** The contouring validation report advertises mean Dice 0.91 across 20 structures. In this case the cord contour has a six-slice discontinuity near the high-dose region, and a small optic structure is assigned to the wrong side after an MRI export with inconsistent orientation metadata. The aggregate score is high because large, easy structures dominate. Clinical utility is poor until geometry and structure-specific errors are reviewed.

**Safe response:** Quarantine the MRI-derived outputs, verify patient/study/frame relationships and orientation, inspect high-consequence structures slice by slice, correct or redraw as required, and recalculate downstream dose after approval. Do not lower a dose or change modality from a prognostic risk score; that would require treatment-effect evidence.

(case-b)=
## Case B — Lung stereotactic treatment

**Fixed synthetic record:** An adult with a small peripheral right-upper-lobe lesion undergoes a ten-phase four-dimensional CT in frame of reference `LUNG-B-4D`. Reconstructed phases use 1.2 × 1.2 × 2.0 mm voxels. A respiratory trace and maximum-intensity projection support motion review. The synthetic prescription is 54 Gy in three fractions. The gross target moves 9 mm superior–inferior across the recorded cycle. Required decisions include motion-envelope construction, planning tradeoffs, pretreatment patient-specific QA, image guidance, and a treatment-day stop rule.

**AI tasks:** phase sorting, motion-aware target propagation, dose prediction, virtual QA triage, and detection of treatment-day anatomy outside the planned envelope.

**Deliberate failure:** Two phase labels are duplicated after an export, making the apparent motion range 4 mm. A model trained on correctly sorted studies returns a confident contour and the predicted plan meets aggregate dose–volume goals. Confidence and dosimetry cannot rescue the invalid temporal input.

**Safe response:** Stop automated propagation and planning, reconcile the respiratory trace with image timestamps and phase identifiers, reconstruct or reacquire according to local policy, and repeat contour, plan, and QA review. A human should not approve because the output looks smooth.

(case-c)=
## Case C — Pelvic adaptive workflow

**Fixed synthetic record:** An adult receiving a fractionated pelvic course has planning CT frame `PELVIS-C-PLAN`, approved target/bladder/rectum/bowel structures, and a baseline volumetric-modulated arc plan. Daily cone-beam CT (CBCT) is acquired for a bounded online-adaptive workflow. The synthetic service may propagate contours, propose an adapted plan, run independent technical checks, and present both scheduled and adapted options. The radiation oncologist approves target and organ-at-risk contours and the treatment choice; the physicist approves the technical plan/QA state; radiation therapists verify identity, setup, and delivery readiness.

**AI tasks:** CT-to-CBCT registration, propagated contour review, rapid re-optimization, plan/record checks, orchestration, and longitudinal monitoring.

**Deliberate failure:** After a CBCT software update, voxel spacing is unchanged but intensity and field-of-view distributions shift. Mean propagated-structure Dice on the first 30 monitored fractions remains 0.90, yet one bowel loop entering the superior field edge is omitted. The interface preselects “approve adapted plan,” and a hurried reviewer initially follows the default.

**Safe response:** Trigger the exception path, cancel the default approval, inspect field-edge anatomy and source metadata, correct contours, repeat optimization and independent checks, and use the scheduled plan or defer treatment if the adapted route cannot meet its time and safety conditions. Open a change investigation and stratify monitoring by field edge, anatomy, software version, and consequence—not mean Dice alone.

## Cross-chapter trace

| Chapter | Case A | Case B | Case C |
|---|---|---|---|
| Medical imaging | verify CT/MRI identity, orientation, and frame | reconcile phase labels and respiratory trace | detect post-update CBCT shift |
| Contouring | review cord discontinuity and laterality | review motion-dependent target labels | find the omitted field-edge bowel loop |
| Registration | decide whether MRI-to-CT use is valid | assess phase-to-phase motion mapping | validate propagation for adaptation |
| Treatment planning | recalculate after corrected contours | reject a plan built on invalid phases | compare scheduled and adapted options |
| QA and validation | measure consequential structure errors | test sorting faults and stop rules | monitor version-stratified failures |
| Workflow and governance | preserve role-specific approval | exercise the exception pathway | resist unsafe defaults and manage change |

(capstone)=
## Capstone — Specify a safe RT-AI evaluation

Choose one bounded tool for Case A, B, or C. Examples include organ-at-risk autocontouring, phase-sorting QA, dose prediction, propagated-contour review, or adapted-plan triage. Submit a two-page protocol plus one workflow diagram. It must include:

1. **Intended use:** user, patient population, input, output, decision supported, setting, exclusions, and prohibited uses.
2. **Data:** source systems, unit of independence, inclusion/exclusion, reference standard, development/evaluation split, subgroup coverage, provenance, and leakage controls.
3. **Evidence and threshold:** technical, external, workflow, and—if claimed—clinical endpoints; comparators; uncertainty; failure cases; sample-size rationale; and the evidence threshold required before each deployment phase.
4. **Human factors:** interface, accountable approver, training, time pressure, automation-bias controls, overrides, exception route, and downtime fallback.
5. **Governance and risk:** hazard analysis, independent checks, privacy/security, vendor/change controls, approvals, incident handling, and a named owner for each control.
6. **Monitoring:** baseline, denominators, subgroup and version stratification, alert/action limits, audit sampling, drift response, rollback, revalidation, and retirement rule.

### Rubric

Score each dimension from 0 to 3. The capstone is ready for peer review only with at least 14/18 overall and no score below 2. This educational threshold is not a clinical authorization.

| Dimension | 0 — absent | 1 — incomplete | 2 — adequate | 3 — strong |
|---|---|---|---|---|
| **Intended use** | “AI for RT” only | task named but user/decision unclear | bounded user, population, input, output, decision, and exclusions | also defines prohibited use, failure consequence, and claim boundary |
| **Data** | convenience data with no provenance | cohort described but leakage/reference gaps remain | independent split, provenance, reference standard, subgroup coverage, and leakage controls | also justifies transportability and tests missingness/shift |
| **Evidence** | one aggregate metric | technical metrics without comparator or threshold | task-matched endpoints, comparator, uncertainty, failures, and phase threshold | also separates external, workflow, and patient claims with justified sample size |
| **Human factors** | “human in the loop” | reviewer named but interface/fallback vague | accountable approval, training, override, exception, and downtime path | also tests time pressure, reliance, workload, and usability prospectively |
| **Governance** | no hazard ownership | generic policy list | hazards, independent controls, privacy/security, change and incident owners | also maps residual risk, vendor evidence, escalation, and decision authority |
| **Monitoring** | accuracy checked occasionally | metric named without denominator/action | versioned baseline, denominators, strata, limits, response, and rollback | also includes audit sampling, revalidation triggers, and retirement criteria |

### Assessor reasoning prompts

- A protocol that reports Dice or area under the curve without a clinical failure analysis cannot score above 1 for evidence: aggregate discrimination is not a safety threshold.
- “A clinician reviews every output” cannot score above 1 for human factors unless the interface, time, competence, override, exception, and fallback are testable.
- Regulatory clearance or vendor validation cannot replace local data, workflow, or monitoring; treating it as sufficient caps governance at 1.
- Monitoring without denominators, model/software versions, subgroup strata, or an action owner cannot distinguish drift from noise and caps monitoring at 1.

Use [Chapter 10](../validation/validation.md) to design the evaluation, [Chapter 11](../workflow/workflow.md) to map implementation, and [Chapter 12](../responsibleAI/responsibleAI.md) to assign governance, regulatory, privacy, and security controls.
