# 9: AI for Quality Assurance and Safety

## Before you begin

**Prerequisites:** Read Chapters 1, 3, and 4; know the artificial intelligence (AI) lifecycle, radiotherapy pathway, data objects, intended use, distribution shift, and the distinction between quality assurance and quality control. Use the [cross-book glossary](../resources/glossary.md).

**Learning objectives:** After this chapter, you should be able to:

1. distinguish acceptance testing, commissioning, routine quality control, patient-specific verification, and end-to-end testing;
2. map an AI check to the hazard, process stage, detection opportunity, and independent safety layers it supports;
3. explain rare-event, shared-dependency, false-alarm, automation-bias, and drift limitations of learned anomaly detection;
4. define evidence and human-factors evaluation for machine, patient-specific, plan, chart, or workflow QA; and
5. specify ownership, configuration control, monitoring, escalation, and change controls for an AI QA tool.

**Reading route:** All readers deploying AI should read this chapter. Clinicians may emphasize plan/chart checks and automation bias; physicists and engineers should include commissioning, machine and patient-specific QA, and lifecycle controls. Case B centers the layered checks around stereotactic treatment; Case C tests rapid adaptive checks and safe fallback.

Quality assurance (QA) in radiation oncology is the planned set of activities used to establish confidence that equipment, software, data, and clinical processes will perform as intended. Quality control (QC) is the operational testing within that system. Safety is the outcome sought: preventing, detecting, and mitigating errors before they harm a patient.

AI can increase the reach and speed of QA by learning patterns across images, plans, log files, and workflow events. It can also create new failure modes. A model may share a hidden dependency with the system it checks, fail silently after a software update, or automate a weak surrogate rather than the clinically important hazard. AI-based QA must therefore be one layer in a broader safety architecture, not the sole source of assurance.

The canonical [radiotherapy data and informatics foundations](../medicalImaging/medicalImaging.md) explain how images, structures, plans, dose, registrations, treatment records, and clinical outcomes connect, and how their identity, units, provenance, and versions should be checked. This chapter treats those checks as inputs to a layered QA system.

## Why Radiotherapy Requires Layered QA

Radiotherapy links many specialized systems over days or weeks. Simulation images, contours, prescriptions, plan parameters, dose distributions, treatment records, and machine instructions move between people and software. A defect may be introduced early but become visible only at delivery.

Useful safety layers include:

- standardized procedures and role definitions;
- equipment commissioning and preventive maintenance;
- independent calculations and measurements;
- peer review and structured checklists;
- record-and-verify constraints and machine interlocks;
- incident learning and corrective action;
- competency assessment and continuing education.

The layers should be diverse. Two checks driven by the same input, algorithm, or assumption may fail together.

## The QA Lifecycle

### Acceptance Testing

Acceptance testing determines whether a newly installed system meets contractual and specified performance requirements. It should be based on agreed tests, tolerances, and documentation. For software, acceptance includes interfaces, data integrity, configuration, access control, and representative end-to-end workflows—not only whether the application starts.

(commissioning)=
### Commissioning

Commissioning establishes how a system behaves in the local clinical environment and creates baseline data for future comparison. A treatment machine is characterized across energies, field sizes, accessories, and delivery modes. A treatment planning system is tested across representative geometries and algorithms. An AI tool should likewise be evaluated across intended anatomical sites, scanners, protocols, populations, and difficult cases before clinical release.

Commissioning is local because risk depends on local use. A contouring model commissioned only for draft generation under mandatory review has a different role from a model whose output automatically drives planning.

### Routine Quality Control

Routine QC checks stability against the commissioned baseline. Frequencies are chosen according to risk, expected drift, manufacturer recommendations, professional guidance, and regulatory requirements. Tests may be daily, monthly, annual, after maintenance, or triggered by a change.

For AI, calendar-based checks should be supplemented by event-based checks after:

- model, operating system, driver, or application updates;
- scanner or reconstruction changes;
- treatment planning system upgrades;
- data-interface or Digital Imaging and Communications in Medicine (DICOM)-routing changes;
- a new patient population, disease site, or protocol;
- a safety signal or unexpected output pattern.

### End-to-End Testing

End-to-end testing follows representative data from acquisition through planning and delivery. It can expose interface, coordinate, transfer, and workflow failures that component tests miss. For an AI-assisted workflow, the test should include preprocessing, model execution, display, editing, approval, export, and downstream use.

## Machine Quality Assurance

Machine QA evaluates whether the treatment unit produces the intended radiation and geometry. Common domains include:

- output constancy and beam quality;
- flatness, symmetry, and profile constancy;
- mechanical and imaging isocenter accuracy;
- gantry, collimator, couch, and multileaf collimator positioning;
- imaging-treatment coordinate coincidence;
- safety interlocks, audiovisual systems, and collision protections;
- specialized tests for stereotactic, gating, tracking, and adaptive modes.

Trend analysis is often more informative than isolated pass/fail results. A parameter that remains inside tolerance but drifts monotonically may warrant preventive action.

### AI for Machine QA

Models can analyze time series of QC measurements, delivery logs, and images to identify drift or anomalous combinations. Potential methods include control charts, change-point detection, autoencoders, one-class classifiers, and supervised fault classifiers.

The output should support diagnosis: the measurement involved, deviation from baseline, trend duration, comparable historical events, and recommended escalation. A single unexplained anomaly score is difficult to act on safely.

Training data present a challenge because serious faults are rare. Synthetic fault injection can improve coverage but may not represent the coupled behavior of real hardware. False positives can create alarm fatigue, while false negatives can create misplaced confidence.

## Patient-Specific QA

Patient-specific QA asks whether an individual plan is correctly calculated, transferred, and deliverable. The program may include secondary dose calculation, data-transfer checks, measurement-based verification, delivery-log analysis, and structured plan review.

For intensity-modulated radiotherapy (IMRT) measurement-based verification, American Association of Physicists in Medicine (AAPM) Task Group 218 recommends defined tolerance and action limits and discusses standardized use of gamma analysis [[1]](https://doi.org/10.1002/mp.12810). Gamma pass rate combines dose difference and distance-to-agreement, but it is not a direct measure of clinical consequence. Results must be interpreted alongside the delivery technique, detector limitations, spatial failure pattern, and relevant anatomy.

### Independent Dose Calculation

An independent calculation uses a method sufficiently separate from the primary treatment planning calculation to detect important errors. Independence can be weakened if both systems use the same beam data, density mapping, or algorithmic assumptions. Agreement does not prove that both are correct.

### Measurement-Based Verification

Measurements may use ion chambers, films, diode arrays, electronic portal imaging devices, or other detector systems. Their resolution, energy response, setup sensitivity, and calibration affect what faults they can detect. Measurements should be selected according to the plan's risk and the failure modes of concern.

### Log-File Analysis

Machine logs contain recorded positions, dose delivery, and timing information. They enable high-resolution reconstruction and trend analysis but generally report what the control system believes occurred. They are not fully independent measurements and may not detect a shared sensor or calibration error.

### AI for Patient-Specific QA

Supervised models can predict QA results or classify plans likely to fail. Input features may include plan complexity, aperture geometry, modulation, dose-volume statistics, machine parameters, or predicted-versus-measured fluence. Unsupervised models can flag cases unlike the commissioned population.

Safe use requires a clear action policy. A prediction of "likely pass" should not automatically remove measurement unless the alternative workflow has been validated against relevant clinically significant errors. The key endpoint is fault detection and patient risk, not agreement with a historical gamma label.

## Automated Plan and Chart Checking

Automated plan checks can evaluate prescription consistency, laterality, contour naming, target coverage, organ-at-risk limits, collision risk, machine compatibility, and transfer integrity. Rule-based checks are valuable because their logic is explicit. ML methods can complement them by learning multivariate patterns that are difficult to enumerate.

Language-model chart checking adds free-text extraction and synthesis but does not replace deterministic arithmetic, DICOM parsing, dose engines, or explicit rules. See [Language Models, Generative AI, and Agents](../fundamentalAI/llm.md) for the canonical treatment of source-grounded outputs, tool permissions, prompt injection, evidence maturity, and human review.

### Error Detection

Useful error-detection datasets should include realistic near misses and deliberately introduced faults, not only routine accepted plans. Examples include:

- incorrect isocenter or image set;
- inconsistent prescription and fractionation;
- missing bolus or accessory;
- swapped or mislabeled structures;
- implausible multileaf collimator patterns;
- dose outside the calculation grid;
- unusual overrides or couch models;
- plan changes not reflected in treatment records.

A model trained only to reproduce historical plan approval may learn institutional preference rather than safety. Explainability methods can help reviewers understand automated QA classifications, but explanations must themselves be validated for usefulness [[2]](https://pubmed.ncbi.nlm.nih.gov/34844219/).

### Workflow Surveillance

Process mining and event-log analysis can find missing approvals, unusual task sequences, excessive delays, or repeated rework. These signals are useful for system improvement, but workforce monitoring must have transparent governance. Metrics intended for safety should not become unexamined measures of individual performance.

## Human Factors and Automation Bias

Automation changes how people work. A check that is usually correct can reduce vigilance, and a poorly timed alert can be ignored even when important. QA interface design should make the safe action easy and preserve access to underlying evidence.

Important human-factors questions include:

- Does the user know what the model checked and did not check?
- Are warnings prioritized by clinical severity?
- Can the user inspect the source data and rationale?
- Is override possible, documented, and reviewed?
- Does the workflow preserve an independent check?
- What happens when the model or network is unavailable?

The human and AI should be evaluated as a team. Measuring model accuracy outside the actual interface and time pressure is insufficient.

## Managing an AI QA Tool

### Intended Use and Hazard Analysis

The intended use should name the users, patient population, input data, output, clinical decision, and degree of automation. Hazard analysis then asks how the tool can contribute to harm: wrong output, delayed output, missing output, corrupted transfer, confusing display, inappropriate use, or failure to detect an error.

Controls can include input validation, hard stops, independent checks, confidence or applicability warnings, human approval, audit logs, rollback, and downtime procedures. Risk controls should be tested, not merely documented.

### Data and Model Configuration

The deployed model, preprocessing, thresholds, reference data, and software dependencies require version control. A checksum or immutable identifier should connect each clinical output with the exact model configuration. Silent replacement of a model breaks traceability.

### Monitoring

Monitoring should include input drift, missingness, output distributions, failure and override rates, latency, subgroup performance where appropriate, and downstream safety outcomes. Thresholds should trigger defined responses such as investigation, increased manual review, rollback, or suspension.

(regulatory-and-standards-context)=
## Regulatory and Standards Context

The canonical treatment of regulation, privacy law, standards, and how they differ by jurisdiction—and the distinction between binding law, regulator guidance, and voluntary standards—is in {ref}`Responsible AI, Regulation, and Security <regulatory-and-privacy-frameworks-by-jurisdiction>`. This section notes only what is specific to QA tools.

Regulation depends on jurisdiction and intended use. In the United States, an AI function that meets the definition of a medical device may require FDA review through an applicable pathway. Clearance or authorization addresses a specified intended use; it does not replace local acceptance, commissioning, training, and QA.

IEC 62304 defines a framework for medical-device software lifecycle processes, including development and maintenance [[3]](https://webstore.iec.ch/en/publication/22794). It is adjacent to the clinical QA workflow because a department may operate software built under such a lifecycle, but the standard is not a substitute for local clinical validation and does not by itself validate the final medical device.

Other relevant lifecycle concepts include quality management, risk management, usability engineering, cybersecurity, change control, complaint handling, and post-market surveillance. The precise applicable standards and laws should be determined with institutional regulatory and legal expertise.

### Adaptive Models and Change Control

An AI system that changes after deployment raises questions about what version is authorized, how modifications are bounded, and what evidence is required. FDA's 2025 final guidance on predetermined change control plans recommends describing planned modifications, the protocol for development, validation and implementation, and an impact assessment [[4]](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/marketing-submission-recommendations-predetermined-change-control-plan-artificial-intelligence). A local department should still know when a model has changed and whether local revalidation is required.

## Evidence Synthesis

The cited evidence agrees that QA should target clinically meaningful faults and use independent safety layers. A model that reproduces a conventional pass/fail label or explains its own classification has demonstrated component behavior, not that it detects the errors most likely to harm a patient. Evidence is heterogeneous across machine QA, measurement-based patient-specific QA, plan checking, chart checking, sites, injected faults, and institutional policies, so a high score in one setting cannot be generalized to the QA programme as a whole.

| Task | Population / site | Data scale | Validation design | Comparator | Endpoint | Principal limitation | Maturity |
|---|---|---|---|---|---|---|---|
| Explainable automated plan QA [[2]](https://pubmed.ncbi.nlm.nih.gov/34844219/) | Prostate and breast planning datasets from one center | Two retrospective site-specific datasets | Internal retrospective analysis of two existing classifiers | LIME versus team-based Shapley explanations; expert interpretation | Explanation consistency and classifier rationale | Explanations can rationalize a wrong classifier; no prospective user-decision or safety endpoint | **Internal retrospective validation** |

The evidence supports retrospective classifier analysis and cross-institution consensus principles, but not silent prospective performance, improved human decisions, fewer incidents, or patient outcomes for an AI QA system. FDA guidance defines a possible regulatory process; this chapter makes no claim that a named system is cleared. Representative routine-adoption evidence is absent. The cited explainability study explicitly concludes that its classifiers should confirm rather than replace expert QA, which is an informative limit on stronger automation claims. Data and code openness are not established for the clinical classifiers. Unanswered questions are sensitivity to rare consequential faults, common-mode failure with the primary system, prospective alert burden and automation bias, safe drift thresholds, and whether AI changes incident rates rather than only surrogate labels.

## Current Research and Recent Advances

- **Explainable automated QA:** Research is moving beyond binary plan flags toward explanations that identify influential regions or features. Early work shows feasibility, but explanation quality and the effect on reviewer decisions need direct evaluation [[2]](https://pubmed.ncbi.nlm.nih.gov/34844219/). _(added: 2026-07)_
- **Lifecycle regulation for evolving AI:** FDA's final predetermined-change-control-plan guidance formalizes a route for certain planned AI device modifications while retaining evidence and risk controls across the lifecycle [[4]](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/marketing-submission-recommendations-predetermined-change-control-plan-artificial-intelligence). _(added: 2026-07)_
- **From pass-rate prediction to risk-based QA:** Current work increasingly combines plan complexity, log data, dose reconstruction, and clinical context. The important validation target is sensitivity to meaningful faults and downstream dose impact, not reproduction of a conventional QA label [[1]](https://doi.org/10.1002/mp.12810). _(added: 2026-07)_

## Recap

- **Objective 1:** Acceptance verifies acquisition requirements, commissioning establishes supported clinical use, routine control checks continued performance, patient-specific verification tests a treatment, and end-to-end tests exercise the chain.
- **Objective 2:** A useful AI check names the hazard, where it enters, how the model can detect it, the clinical consequence, and independent prevention, detection, and mitigation layers.
- **Objective 3:** Rare faults provide few examples, shared data or logic can defeat both system and checker, false alarms change behavior, automation bias weakens review, and drift invalidates assumptions.
- **Objective 4:** Evaluation must match the QA task and include representative faults, clinically weighted errors, workflow timing, alert response, usability, overrides, and residual risk.
- **Objective 5:** Safe service needs a named owner, intended use, traceable data/model/configuration versions, thresholds, escalation, monitoring, incident learning, and controlled change.

**Important limitation and misconception:** An AI checker is not independent merely because it is separate software; shared inputs, training labels, calculations, or failure assumptions can create common-mode failure.

## References

1. Miften M, Olch A, Mihailidis D, et al. Tolerance limits and methodologies for IMRT measurement-based verification QA: Recommendations of AAPM Task Group No. 218. *Medical Physics*. 2018;45(4):e53-e83. [DOI](https://doi.org/10.1002/mp.12810)
2. Chen Y, Aleman DM, Purdie TG, McIntosh C. Understanding machine learning classifier decisions in automated radiotherapy quality assurance. *Physics in Medicine & Biology*. 2022;67(2). [PubMed](https://pubmed.ncbi.nlm.nih.gov/34844219/)
3. International Electrotechnical Commission. IEC 62304:2006+A1:2015, Medical device software—Software life cycle processes. [IEC publication](https://webstore.iec.ch/en/publication/22794)
4. U.S. Food and Drug Administration. *Marketing Submission Recommendations for a Predetermined Change Control Plan for Artificial Intelligence-Enabled Device Software Functions*. Final guidance; 2025. [FDA guidance](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/marketing-submission-recommendations-predetermined-change-control-plan-artificial-intelligence)
