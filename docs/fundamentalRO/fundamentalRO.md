# 3: Fundamentals of Radiation Oncology

## Before you begin

**Prerequisites:** None beyond [Chapter 1](../intro/intro.md). The [cross-book glossary](../resources/glossary.md) defines clinical and technical terms.

**Learning objectives:** After this chapter, you should be able to:

1. distinguish treatment intent, prescription, fractionation, dose distribution, modality, and biological response;
2. trace a patient from consultation and simulation through planning, delivery, follow-up, and possible adaptation;
3. explain how targets, organs at risk, imaging, dose, motion, and uncertainty constrain a treatment;
4. compare the purposes of major external-beam, brachytherapy, and radiopharmaceutical modalities; and
5. identify the responsible roles, handoffs, independent barriers, and stop authority around an artificial intelligence (AI)-supported step.

**Reading route:** Complete beginners and technical readers should read this before the application chapters. Clinicians may scan familiar sections and focus on roles, uncertainty, and AI consequences. {ref}`Cases A–C <recurring-cases>` instantiate the curative, stereotactic, and adaptive pathways described here.

Radiation oncology uses ionizing radiation to control or eradicate cancer, prevent recurrence, or relieve symptoms while limiting injury to normal tissue. It is both a clinical specialty and a tightly coupled technical system. A useful plan must express the right clinical intent, represent the right anatomy, calculate a defensible dose, be deliverable by the commissioned equipment, and remain appropriate as the patient and disease change.

AI applications discussed elsewhere in this book operate inside that system. Their outputs are not abstract labels or arrays: they can alter a target, a dose distribution, a treatment interruption, or a patient conversation. This chapter supplies the clinical mental model needed to understand those consequences.

## Intent, Prescription, Technique, and Response

Several concepts that are often blurred together answer different questions:

| Concept | Question it answers | Example |
|---|---|---|
| **Treatment intent** | Why is radiation being given? | cure, durable local control, prevention of recurrence, symptom relief |
| **Prescription** | What treatment has the radiation oncologist authorized? | target, total dose, dose per fraction, number and frequency of fractions, technique or modality requirements, and sometimes dose constraints |
| **Fractionation** | How is the total course divided over time? | 60 Gy in 30 daily fractions or 30 Gy in 10 fractions |
| **Dose distribution** | Where is absorbed dose expected to go in this patient model? | target coverage and dose-volume values for organs at risk |
| **Delivery modality and technique** | How will that distribution be produced? | photon volumetric modulated arc therapy (VMAT), proton pencil-beam scanning, electron field, brachytherapy applicator |
| **Biological response** | What happens to tumor and normal tissue over time? | local control, acute mucositis, late fibrosis, symptom relief |

Intent is established from diagnosis, stage, prognosis, competing health risks, patient goals, and alternative treatments. **Definitive** radiotherapy is the primary local treatment; **neoadjuvant** treatment precedes another therapy; **adjuvant** treatment follows it; **salvage** treatment addresses persistent or recurrent disease; and **palliative** treatment prioritizes symptom relief or prevention of morbidity. These categories describe purpose, not automatically dose or quality. Palliative treatment still requires accurate identification, prescription, planning, delivery, and follow-up.

A prescription is more than a total number of gray. It binds dose and time to a specified target and clinical purpose. The same total physical dose delivered in different fraction sizes or overall times can have a different biological effect. Conversely, two techniques can implement the same prescription with different dose distributions, robustness, treatment times, costs, and burdens. NCI's treatment overview distinguishes external-beam, brachytherapy, and systemic radiopharmaceutical therapy and emphasizes that modality choice depends on tumor, location, nearby normal tissues, health, and other treatment [[4]](https://www.cancer.gov/about-cancer/treatment/types/radiation-therapy).

(complete-radiotherapy-pathway)=
## The Complete Radiotherapy Pathway

The exact workflow varies by disease, modality, institution, and country, but the major clinical purposes are stable. ASTRO's multidisciplinary safety framework treats quality as a property of the complete process rather than one final machine check [[5]](https://www.astro.org/practice-support/quality-and-safety/safety-is-no-accident).

| Step | Purpose | Typical output or decision | Why an error matters downstream |
|---|---|---|---|
| **1. Consultation and diagnosis review** | confirm pathology, history, symptoms, fitness, prior treatment, and patient goals | indication and preliminary intent | treating the wrong disease context can make every later technical step internally consistent but clinically inappropriate |
| **2. Staging and multidisciplinary decision** | establish disease extent and compare radiation with surgery, systemic therapy, observation, or combined care | treatment strategy and sequencing | incomplete staging can miss metastatic disease or change a curative plan into an unsuitable local intervention |
| **3. Consent and preparation** | explain expected benefit, alternatives, acute and late effects, logistics, and uncertainties | informed decision; preparation instructions | misunderstanding can impair consent, adherence, pregnancy precautions, medication management, or supportive care |
| **4. Simulation** | reproduce the treatment position and acquire planning data over the correct anatomy and motion state | planning images, immobilization, reference marks, motion strategy | a poor patient model propagates into contours, dose calculation, and daily setup |
| **5. Image registration and contouring** | align relevant studies and define targets, organs at risk, and auxiliary structures | reviewed structure set with provenance | a geometric or semantic error changes what is optimized and evaluated |
| **6. Prescription and planning directive** | translate clinical intent into target dose, fractionation, priorities, constraints, and delivery requirements | signed prescription and plan goals | ambiguity can produce the wrong dose, target, schedule, or trade-off |
| **7. Dose calculation and optimization** | design a deliverable distribution on the patient model | candidate plan, dose, DVHs, robustness results | algorithm, density, geometry, or optimization errors can underdose tumor or overdose normal tissue |
| **8. Review, approval, and pretreatment verification** | confirm clinical acceptability, deliverability, data integrity, and independent checks | approved plan and verified treatment parameters | an unchallenged upstream error may otherwise repeat across every fraction |
| **9. Image guidance and delivery** | identify the patient, reproduce anatomy, apply approved corrections, and deliver the authorized fields or source sequence | treatment record for each fraction | wrong-patient, wrong-site, setup, motion, or transfer errors directly affect delivered dose |
| **10. On-treatment assessment and adaptation** | manage symptoms, interruptions, weight/anatomy change, tumor response, and technical deviations | supportive care, continue/hold decision, or revised plan | continuing an obsolete plan or adapting without adequate checks can shift the therapeutic balance |
| **11. Completion, follow-up, and survivorship** | document delivered treatment, assess response and toxicity, coordinate surveillance and late-effect care | treatment summary, outcome and toxicity record, survivorship plan | missing longitudinal information impairs care, outcome interpretation, and future retreatment |

The process is iterative rather than a simple one-way pipeline. A contouring concern can trigger new imaging; a planning trade-off can change a prescription; daily imaging can trigger resimulation; toxicity can interrupt or modify treatment. Every loop needs an explicit owner and a new approval state.

## Ionizing Radiation and Absorbed Dose

Ionizing radiation carries enough energy to remove electrons from atoms. In tissue it transfers energy directly and through secondary charged particles, damaging cellular molecules and creating reactive chemical species. The IAEA radiation-oncology physics handbook provides the foundational treatment of interactions, machines, dosimetry, planning, and protection used throughout this chapter [[1]](https://www-pub.iaea.org/MTCD/Publications/PDF/Pub1196_web.pdf).

Absorbed dose is energy imparted per unit mass:

$$D = \frac{dE}{dm}$$

Its SI unit is the gray (Gy), equal to one joule per kilogram. Dose is not a machine setting or an image intensity. It depends on beam or source properties, geometry, patient composition, field modulation, motion, and the calculation or measurement method.

### Photons and Secondary Electrons

Megavoltage photons used in external-beam radiotherapy interact mainly through Compton scattering over much of the clinically relevant range. Energy transferred to secondary electrons is then deposited along their paths. Photon fluence, electron transport, and absorbed dose are therefore related but not interchangeable.

Photon beams have an entrance dose, a build-up region, and dose beyond a deep target. Combining fields from several directions and modulating their fluence can concentrate dose, but it cannot make the path through normal tissue disappear.

### Charged Particles and Range

Electrons lose energy and scatter over a finite useful depth, which makes them valuable for many superficial targets but less suitable for deep disease. Protons and heavier ions deposit increasing energy near the end of their range. Multiple energies cover a volume, potentially reducing exit dose compared with photons.

That finite range is also a vulnerability. Computed tomography (CT)-to-stopping-power conversion, setup, anatomical change, implants, gas, and motion can move the distal edge. Robust particle planning tests uncertainty scenarios; a sharp gradient is useful only if its position is reliable.

## Modalities and Delivery Techniques

**Modality** describes the radiation or source class. **Technique** describes how it is shaped, positioned, and delivered. One modality supports several techniques, and no technique is best for every patient.

### External-Beam Photons and Electrons

A medical linear accelerator can produce megavoltage photons and, on many systems, electrons. Three-dimensional conformal radiotherapy shapes several fields to the target. Intensity-modulated radiotherapy (IMRT) varies fluence across fields, while VMAT delivers modulated radiation during gantry rotation. These methods can improve conformality but create steep gradients and many interdependent parameters. They remain sensitive to contouring, calculation, setup, motion, and machine performance. The National Cancer Institute (NCI) provides a stable introductory comparison of photon, electron, proton, conformal, IMRT, image-guided radiotherapy (IGRT), and stereotactic external-beam techniques [[4]](https://www.cancer.gov/about-cancer/treatment/types/radiation-therapy).

Electrons have a useful finite depth but broad lateral scatter and sensitivity to surface contour and heterogeneity. Bolus may deliberately bring dose toward the surface. Photon/electron selection depends on target depth, shape, nearby structures, energy, field arrangement, and local equipment—not the label “superficial” alone.

### Proton and Heavy-Ion Therapy

Protons can reduce integral dose or dose beyond a target in selected geometries. Pencil-beam scanning paints dose spot by spot and layer by layer; passive-scattering techniques shape a broader field. Heavy ions such as carbon have different physical and biological properties and much more limited availability.

Particle therapy is not automatically safer or superior. Range and motion uncertainty, variable biological effectiveness, complex planning and quality assurance (QA), capital cost, access, and the strength of comparative clinical evidence all matter. A favorable dose comparison is a planning result; it is not by itself proof of better patient outcome.

### Brachytherapy

Brachytherapy places sealed radioactive sources in or near the target using applicators, catheters, needles, or permanent seeds. The steep fall-off can deliver high local dose while sparing more distant tissue, but small geometric errors near a source can cause large dose changes.

**Low-dose-rate** techniques deliver continuously over a longer period; **high-dose-rate** afterloaders move a high-activity source through programmed dwell positions for shorter treatments; **pulsed-dose-rate** delivery uses repeated pulses. Applicator placement, reconstruction, source calibration, dwell sequence, channel connection, imaging, organ motion, and emergency procedures are integral to safety. IAEA TRS-492 provides the current international code of practice for brachytherapy source dosimetry [[11]](https://www.iaea.org/publications/15202/dosimetry-in-brachytherapy-an-international-code-of-practice-for-secondary-standards-dosimetry-laboratories-and-hospitals).

### Stereotactic Radiosurgery and Body Radiotherapy

Stereotactic radiosurgery (SRS) and stereotactic body radiotherapy (SBRT/SABR) use highly conformal small fields and steep dose gradients, commonly in one or a few high-dose fractions. “Radiosurgery” does not require an incision. The value comes from precise localization and dose concentration; the risk comes from the same high dose and gradient when localization, motion, small-field dosimetry, or contouring is wrong.

Stereotactic practice requires appropriate case selection, immobilization, image guidance, motion control, small-field commissioning, end-to-end testing, and delivery verification. ICRU Report 91 supplies a common framework for target definition, prescribing, recording, small-field dosimetry, planning, QA, and image guidance [[10]](https://www.icru.org/report/icru-report-91-prescribing-recording-and-reporting-of-stereotactic-treatments-with-small-photon-beams-2/).

### Radiopharmaceutical Therapy

Radiopharmaceutical therapy administers an unsealed radioactive drug whose biological distribution delivers radiation internally. Unlike external-beam and most brachytherapy, activity moves through the body, is taken up and cleared over time, and can expose multiple organs and body fluids. The prescribed quantity may be administered activity, an absorbed-dose objective, or a protocol-defined regimen depending on the treatment and jurisdiction.

Imaging, activity calibration, pharmacokinetics, organ segmentation, time-activity integration, absorbed-dose calculation, contamination control, release instructions, laboratory monitoring, and coordination with nuclear medicine are central. IAEA's 2024 dosimetry text explains why identical administered activities can produce different tumor and organ absorbed doses between patients [[12]](https://www.iaea.org/publications/15002/dosimetry-for-radiopharmaceutical-therapy). Radiopharmaceutical therapy is therefore not simply “systemic external beam”; its data, dosimetry, logistics, and radiation-protection pathway differ.

## Simulation, Immobilization, and Motion

### Building the Patient Model

Simulation places the patient in a treatment position that is both clinically appropriate and reproducible. The scan must cover the relevant anatomy and include devices, contrast phases, breathing states, and acquisition settings needed for planning. Immobilization may use masks, vacuum cushions, body molds, bite blocks, breast boards, indexed supports, or internal/external markers. Comfort matters because an intolerable position is not reproducible over a course.

Planning CT supplies patient geometry and material information for many external-beam calculations. Magnetic resonance imaging (MRI), positron emission tomography (PET), diagnostic CT, ultrasound, or pathology may refine target definition but must be linked to the correct patient, time, position, and coordinate system. The imaging/data model is treated in [Chapter 4](../medicalImaging/medicalImaging.md); transformation and fusion are treated in [Chapter 6](../registration/registration.md).

### Target Volumes and Organs at Risk

The **gross tumor volume (GTV)** represents visible or otherwise demonstrable disease. The **clinical target volume (CTV)** includes tissue requiring treatment for demonstrated or suspected microscopic disease. The **planning target volume (PTV)** is a geometrical concept used to make adequate CTV dose sufficiently likely despite defined setup and internal-motion uncertainties. ICRU Report 50 established these core target-volume concepts for photon therapy [[6]](https://www.icru.org/report/prescribing-recording-and-reporting-photon-beam-therapy-report-50/).

An **organ at risk (OAR)** is a normal structure whose radiation sensitivity can influence planning or prescription. A planning-risk volume may add a margin to an OAR where appropriate. Target and OAR contours represent clinical judgments under uncertainty, not naturally occurring sharp borders. Margins do not repair the wrong diagnosis, an unrecognized registration error, or an unsuitable image.

### Respiratory and Organ Motion

Anatomy moves between fractions (**interfraction motion**) and during a fraction (**intrafraction motion**). Causes include respiration, cardiac motion, swallowing, bladder and rectal filling, peristalsis, weight change, tumor response, discomfort, and relaxation. Motion can blur images, alter apparent target extent, change density, and create an interplay with scanned or modulated delivery.

Management options include motion-encompassing imaging such as 4D CT, internal-target volumes, breath-hold, respiratory gating, abdominal compression, tracking, fiducials, and repeated imaging. Each has failure modes: an irregular trace, changed breathing pattern, surrogate–tumor mismatch, marker migration, or poor patient tolerance. AAPM Task Group 76 describes the clinical and QA principles for respiratory-motion management [[8]](https://doi.org/10.1118/1.2349696).

## Prescription, Planning, and Dose Calculation

### From Clinical Directive to Objectives

The radiation oncologist's prescription identifies the target and fractionation and communicates the clinical priorities. Planning objectives translate that directive into measurable target coverage, homogeneity or conformality goals, and OAR dose-volume constraints. Constraints may be hard safety limits, protocol requirements, or optimization goals; they are not interchangeable.

A dose-volume histogram (DVH) summarizes how much of a structure receives at least a given dose but discards spatial location. Two plans can have similar DVHs and different hotspots, gradients, robustness, or clinical implications. ICRU Report 83 standardizes core concepts for prescribing, recording, and reporting IMRT and emphasizes precise three-dimensional target and normal-tissue definition [[7]](https://www.icru.org/report/prescribing-recording-and-reporting-intensity-modulated-photon-beam-therapy-imrticru-report-83/).

### Calculation and Optimization

The treatment planning system converts patient and machine models into an estimated three-dimensional dose. Algorithms differ in how they represent scatter, heterogeneity, interfaces, small fields, charged-particle transport, and biological quantities. A calculation is valid only within the commissioned conditions and declared grid, material, and algorithm assumptions.

**Forward planning** adjusts fields and weights directly, often for simpler arrangements. **Inverse planning** starts with objectives and lets an optimizer search machine parameters. Optimization produces a mathematical compromise; it does not know which clinical trade-off is acceptable unless the objectives, priorities, and review encode that judgment. The canonical AI planning discussion is in [Chapter 7](../treatmentPlanning/treatmentPlanning.md).

Commissioning compares the planning system with measurements and known cases before clinical use; periodic QA and change control maintain that evidence. IAEA TRS-430 describes commissioning and quality assurance for computerized treatment-planning systems and documents why incorrect configuration or use can produce serious systematic errors [[13]](https://www-pub.iaea.org/MTCD/Publications/PDF/TRS430_web.pdf).

## Review, Verification, Image Guidance, and Delivery

### Plan Review and Independent Checks

Clinical plan review asks whether target coverage, OAR exposure, spatial dose, robustness, and technique match the prescription and patient. Physics review asks whether the machine, calculation, data transfer, and plan parameters are technically valid. These perspectives overlap but are not substitutes.

Independent checks should avoid sharing the same failure mode where practical. Examples include a secondary dose or monitor-unit calculation, patient-specific measurement, collision review, image-registration review, checklist, time-out, and end-to-end test. AAPM Task Group 219 describes independent calculation-based verification for IMRT/VMAT as one component of a comprehensive QA program [[14]](https://doi.org/10.1002/mp.15069). Agreement with a second algorithm does not prove the prescription, contour, or patient identity is correct.

### Image-Guided Radiotherapy

Initial setup uses indexed devices, room lasers, surface marks, or other references. IGRT then compares treatment-day anatomy with a reference using planar imaging, cone-beam CT, surface guidance, ultrasound, MRI, implanted markers, or other systems. The user must know what anatomy is visible, what registration was used, which degrees of freedom can be corrected, and when a mismatch requires escalation rather than a couch shift.

Online correction can reduce setup error but may introduce wrong-registration, wrong-reference, or wrong-direction errors. A target aligned perfectly to the wrong dataset is not safe. Imaging dose, frequency, latency, and the possibility of anatomical change should be part of the protocol.

### Delivery and Record

Before beam or source delivery, the team confirms patient, site, prescription, plan, fraction, setup, imaging decision, accessories, and special instructions. The oncology information or record-and-verify system transfers and records parameters; the treatment unit applies interlocks and reports delivery. A treatment record documents what the system says occurred, which still requires interpretation when there are interruptions, overrides, partial fractions, or machine faults.

Radiation therapists monitor the patient and machine and can interrupt delivery. “Beam on” is only a small part of the appointment; identification, positioning, imaging, review, correction, documentation, and response to exceptions dominate many workflows.

## Adaptive Radiotherapy

Adaptive radiotherapy changes the treatment in response to observed anatomy, biology, dose, or clinical status. **Offline adaptation** creates a revised plan for later fractions. **Online adaptation** performs imaging, contour review, replanning, QA, approval, and delivery while the patient remains in position. A plan library selects among preapproved alternatives.

Adaptation can address weight loss, tumor regression, organ filling, target motion, or systematic setup change. It is not simply rerunning optimization. The team must decide whether the observed difference is real and important, whether accumulated dose is meaningful, what remains of the prescription, and whether the revised plan has adequate independent checks. The NRG review summarizes contemporary adaptive strategies and their technical dependencies [[3]](https://doi.org/10.1016/j.ijrobp.2020.10.021).

## Toxicity, Outcomes, Follow-up, and Survivorship

Radiotherapy outcomes include tumor response, local or regional control, progression, survival, symptom relief, organ function, patient-reported quality of life, treatment burden, and adverse effects. A technically conformal plan is a surrogate, not a patient outcome.

**Acute effects** occur during or soon after treatment, often in rapidly renewing tissues; examples include skin reaction, mucositis, nausea, fatigue, and marrow suppression depending on the treated region. **Late effects** may emerge months or years later and include fibrosis, vascular injury, endocrine dysfunction, organ impairment, fracture, cognitive effects, and second malignancy. Timing alone does not determine mechanism or reversibility. NCI provides an accessible organ-specific overview of radiation side effects and their management [[17]](https://www.cancer.gov/about-cancer/treatment/types/radiation-therapy/side-effects).

On-treatment review checks symptoms, nutrition, medications, laboratory results where relevant, treatment adherence, and the need to hold or modify treatment. Completion documentation should state the treated site, intent, modality/technique, dates, dose/fractionation, delivered deviations, concurrent therapy, acute effects, and follow-up plan.

Follow-up evaluates response, recurrence, toxicity, function, psychosocial needs, and coordination with the broader oncology team. Survivorship can extend for decades; late effects and retreatment decisions depend on an accurate prior dose and treatment record. Outcome labels used for AI are only as reliable as these definitions, schedules, adjudication, and missing-follow-up processes, as discussed in [Clinical Prediction, Radiomics, and Causal Inference](../clinicalPrediction/clinicalPrediction.md).

## Three Classes of Uncertainty

Uncertainty is not one margin or one confidence score. The IAEA consensus on accuracy and uncertainty covers clinical, radiobiological, dosimetric, technical, and physical contributions across external beam and brachytherapy [[9]](https://www.iaea.org/publications/10668/accuracy-requirements-and-uncertainties-in-radiotherapy).

- **Physical uncertainty** concerns the patient and radiation in space and time: setup, motion, deformation, range, source position, and machine geometry.
- **Dosimetric uncertainty** concerns the estimate or measurement of absorbed dose: calibration, detector response, dose algorithm, material assignment, grid resolution, data transfer, and accumulated-dose mapping.
- **Biological and clinical uncertainty** concerns what should be treated and what dose will achieve the desired balance: microscopic spread, radiosensitivity, fractionation response, competing risks, endpoint definitions, and the patient's evolving goals.

These classes interact but cannot substitute for one another. A larger PTV may address a quantified geometric uncertainty but can increase normal-tissue dose; it cannot correct the wrong CTV. A more accurate dose engine cannot determine whether escalation benefits the patient. A well-calibrated outcome model cannot rescue corrupted geometry.

## Professional Roles, Handoffs, and Safety Barriers

Titles, scopes, staffing, and legal accountability differ by jurisdiction. Some countries use “radiation therapist,” others “therapeutic radiographer” or “radiation therapy technologist”; dosimetry may be a distinct profession or part of another role. The local license, regulation, credentialing, and institutional policy govern. The role map below describes common functions, not universal legal assignments. The IAEA programme guide and ASTRO safety framework both emphasize a qualified multidisciplinary service [[16]](https://www-pub.iaea.org/MTCD/Publications/PDF/pub1296_web.pdf) [[5]](https://www.astro.org/practice-support/quality-and-safety/safety-is-no-accident).

| Professional function | Common responsibilities | Critical handoffs and independent contributions |
|---|---|---|
| **Radiation oncologist** | indication, intent, consent, target/OAR definition, prescription, plan approval, on-treatment and follow-up decisions | communicates clinical directive; reviews image guidance/adaptation within scope; owns clinical acceptability |
| **Medical physicist** | equipment acceptance/commissioning, reference and clinical dosimetry, TPS and imaging validation, technical plan review, QA, incident analysis | independently tests calculation/delivery chain; defines action levels and technical release criteria |
| **Medical dosimetrist or planner** | beam/arc/applicator modeling workflow, optimization, dose evaluation, planning documentation | translates prescription into candidate plans; escalates conflicting or unachievable objectives |
| **Radiation therapist/radiographer/technologist** | simulation, immobilization, daily identification/setup, imaging, delivery, observation, treatment record | detects day-of-treatment mismatch or patient change; pauses and escalates unsafe delivery |
| **Radiologist and nuclear-medicine specialist** | diagnostic interpretation, staging imaging, tracer selection/interpretation, radiopharmaceutical therapy responsibilities where applicable | communicates diagnostic certainty, disease extent, imaging limitations, and radionuclide pathway decisions |
| **Nurse and allied health team** | assessment, education, symptom and skin care, nutrition/rehabilitation coordination, psychosocial support | identifies toxicity, adherence, medication, and functional changes that may require clinical review |
| **Informatics, IT, and engineering staff** | interfaces, identity, access, data integrity, cybersecurity, backups, versioning, uptime | maintain controlled data flow and auditability; do not decide clinical acceptability unless separately qualified |

A handoff is a safety-critical transformation: diagnosis to intent, intent to prescription, prescription to plan, plan to delivery, daily image to correction, and delivered course to follow-up record. Read-back, structured fields, status controls, checklists, independent review, and stop authority reduce ambiguity. “The computer accepted it” is not an independent barrier.

Risk-based quality management maps the real workflow, identifies how failures propagate, and places controls where likelihood, severity, and lack of detectability combine. AAPM Task Group 100 formalizes process mapping, failure-modes analysis, fault trees, and risk-informed QA for radiotherapy [[15]](https://doi.org/10.1118/1.4947547).

## AI Roles in Their Clinical Context

The accountable user is the person authorized and competent to make the clinical or technical decision—not the model developer, software vendor, or “AI.” Local roles may differ, but they must be named before deployment.

| AI-supported task | Decision supported | Accountable/reviewing professional | Plausible model failure | Downstream consequence | Independent safety controls |
|---|---|---|---|---|---|
| image reconstruction, denoising, or synthetic imaging | whether an image is adequate for contouring, registration, or calculation | radiologist, radiation oncologist, physicist, or therapist according to use | invented/removed anatomy; wrong quantitative values | wrong target, density, or setup reference | source-image comparison, quantitative phantom tests, fallback acquisition |
| target or OAR segmentation | which anatomy is included in optimization and evaluation | radiation oncologist for targets; designated clinician for OARs | missed disease, wrong laterality, boundary error | geographic miss or unrecognized OAR overdose | protocol-based human review, display on source images, geometric/dose checks |
| image registration | how information or dose is transferred between images | radiation oncologist/physicist depending purpose | plausible but wrong transform or direction | misplaced contour, dose, or adaptation decision | landmark/overlap review, transform provenance, task-specific QA |
| dose or DVH prediction | what distribution is achievable or worth optimizing toward | dosimetrist, physicist, radiation oncologist | reproduces poor historical practice; misses small critical structure | biased objectives or false reassurance | dose engine, constraint evaluation, comparison with clinical baseline |
| automated planning/optimization | which deliverable parameters implement the prescription | radiation oncologist approves clinical plan; physicist verifies technical validity | wrong priorities, non-robust or undeliverable plan | undercoverage, toxicity, treatment delay | independent calculation/measurement, robustness, plan and chart review |
| plan, machine, or chart QA | whether a case is released or escalated | physicist and/or authorized clinical user | false pass, shared failure with system checked, alert fatigue | error reaches one or many fractions | deterministic rules, independent measurements/calculations, stop policy |
| outcome/toxicity prediction | whether risk information changes counseling or supportive care | radiation oncologist and relevant care team | miscalibration, subgroup failure, causal overinterpretation | inappropriate reassurance, escalation, or treatment selection | external/local validation, calibration, decision policy, prospective impact study |
| documentation, retrieval, or agent workflow | what information is summarized, routed, or written | author/approver of the clinical record or workflow action | fabricated source, omitted exception, wrong patient, excessive tool action | misinformation, privacy breach, unauthorized order or delay | source display, least privilege, structured validation, confirmation before write |

AI should be evaluated at the decision boundary. A segmentation score is incomplete without editing and dose consequences; a QA classifier is incomplete without clinically important fault detection; a fluent note is incomplete without source-grounded correctness and omission review. [Chapter 10](../validation/validation.md) develops those evaluation principles, while [Chapter 9](../qa/qa.md) and [Chapter 11](../workflow/workflow.md) cover safety and integration.

## Current Research and Recent Advances

- **Biology-guided personalization:** Research increasingly combines spatial dose with imaging, molecular, and longitudinal response data to move beyond population-level constraints. These models remain sensitive to endpoint definition, confounding, and dataset shift, so prospective clinical utility must be demonstrated rather than inferred from retrospective discrimination alone [[2]](https://doi.org/10.1038/s41571-020-0417-8). _(added: 2026-07)_
- **Online adaptive radiotherapy:** Integrated imaging, automated contour propagation or segmentation, rapid replanning, and on-couch review are turning adaptation into a fraction-level workflow. The opportunity is tighter personalization; the safety challenge is validating every compressed step under time pressure [[3]](https://doi.org/10.1016/j.ijrobp.2020.10.021). _(added: 2026-07)_
- **Automation as a sociotechnical system:** Contemporary radiation oncology AI guidance emphasizes data quality, representative evaluation, human factors, and lifecycle monitoring rather than benchmark performance alone [[2]](https://doi.org/10.1038/s41571-020-0417-8). _(added: 2026-07)_

## Recap

- **Objective 1:** Intent states why treatment is given; a prescription authorizes target, dose, fractionation, and constraints; planning estimates spatial dose; modality and technique define delivery; response is observed afterward.
- **Objective 2:** The pathway links consultation, simulation, contouring, prescription, planning, review, image guidance, delivery, and follow-up, with reassessment and adaptation when appropriate.
- **Objective 3:** Targets and organs at risk, imaging fidelity, anatomy and motion, calculation and delivery uncertainty, and patient change jointly constrain safe treatment.
- **Objective 4:** Photons, electrons, charged particles, brachytherapy, stereotactic techniques, and radiopharmaceutical therapy differ in how dose is produced, localized, verified, and managed.
- **Objective 5:** Safe AI support requires an accountable qualified user, explicit handoffs, plausible-failure analysis, independent barriers, escalation, and stop authority.

**Important limitation and misconception:** A technically deliverable dose distribution is not automatically clinically appropriate, and AI output does not transfer professional accountability to the model.

## References

1. Podgorsak EB, ed. *Radiation Oncology Physics: A Handbook for Teachers and Students*. International Atomic Energy Agency; 2005. [IAEA publication](https://www-pub.iaea.org/MTCD/Publications/PDF/Pub1196_web.pdf)
2. Huynh E, Hosny A, Guthier C, et al. Artificial intelligence in radiation oncology. *Nature Reviews Clinical Oncology*. 2020;17:771-781. [DOI](https://doi.org/10.1038/s41571-020-0417-8)
3. Glide-Hurst CK, Lee P, Yock AD, et al. Adaptive radiation therapy (ART) strategies and technical considerations: a state of the ART review from NRG Oncology. *International Journal of Radiation Oncology, Biology, Physics*. 2021;109(4):1054-1075. [DOI](https://doi.org/10.1016/j.ijrobp.2020.10.021)
4. National Cancer Institute. Radiation Therapy to Treat Cancer. Reviewed 2025. [NCI](https://www.cancer.gov/about-cancer/treatment/types/radiation-therapy)
5. American Society for Radiation Oncology. *Safety Is No Accident: A Framework for Quality Radiation Oncology Care*. 2019. [ASTRO](https://www.astro.org/practice-support/quality-and-safety/safety-is-no-accident)
6. International Commission on Radiation Units and Measurements. *ICRU Report 50: Prescribing, Recording, and Reporting Photon Beam Therapy*. 1993. [ICRU](https://www.icru.org/report/prescribing-recording-and-reporting-photon-beam-therapy-report-50/)
7. International Commission on Radiation Units and Measurements. *ICRU Report 83: Prescribing, Recording, and Reporting Intensity-Modulated Photon-Beam Therapy*. 2010. [ICRU](https://www.icru.org/report/prescribing-recording-and-reporting-intensity-modulated-photon-beam-therapy-imrticru-report-83/)
8. Keall PJ, Mageras GS, Balter JM, et al. The management of respiratory motion in radiation oncology: report of AAPM Task Group 76. *Medical Physics*. 2006;33(10):3874-3900. [DOI](https://doi.org/10.1118/1.2349696)
9. International Atomic Energy Agency. *Accuracy Requirements and Uncertainties in Radiotherapy*. Human Health Series No. 31. 2016. [IAEA publication](https://www.iaea.org/publications/10668/accuracy-requirements-and-uncertainties-in-radiotherapy)
10. International Commission on Radiation Units and Measurements. *ICRU Report 91: Prescribing, Recording, and Reporting of Stereotactic Treatments with Small Photon Beams*. 2017. [ICRU](https://www.icru.org/report/icru-report-91-prescribing-recording-and-reporting-of-stereotactic-treatments-with-small-photon-beams-2/)
11. International Atomic Energy Agency. *Dosimetry in Brachytherapy: An International Code of Practice for Secondary Standards Dosimetry Laboratories and Hospitals*. Technical Reports Series No. 492. 2023. [IAEA publication](https://www.iaea.org/publications/15202/dosimetry-in-brachytherapy-an-international-code-of-practice-for-secondary-standards-dosimetry-laboratories-and-hospitals)
12. International Atomic Energy Agency. *Dosimetry for Radiopharmaceutical Therapy*. 2024. [IAEA publication](https://www.iaea.org/publications/15002/dosimetry-for-radiopharmaceutical-therapy)
13. International Atomic Energy Agency. *Commissioning and Quality Assurance of Computerized Planning Systems for Radiation Treatment of Cancer*. Technical Reports Series No. 430. 2004. [IAEA publication](https://www-pub.iaea.org/MTCD/Publications/PDF/TRS430_web.pdf)
14. Zhu TC, Stathakis S, Clark JR, et al. Report of AAPM Task Group 219 on independent calculation-based dose/MU verification for IMRT. *Medical Physics*. 2021;48(10):e808-e829. [DOI](https://doi.org/10.1002/mp.15069)
15. Huq MS, Fraass BA, Dunscombe PB, et al. The report of Task Group 100 of the AAPM: application of risk analysis methods to radiation therapy quality management. *Medical Physics*. 2016;43(7):4209-4262. [DOI](https://doi.org/10.1118/1.4947547)
16. International Atomic Energy Agency. *Setting Up a Radiotherapy Programme: Clinical, Medical Physics, Radiation Protection and Safety Aspects*. 2008. [IAEA publication](https://www-pub.iaea.org/MTCD/Publications/PDF/pub1296_web.pdf)
17. National Cancer Institute. Radiation Therapy Side Effects. Reviewed 2025. [NCI](https://www.cancer.gov/about-cancer/treatment/types/radiation-therapy/side-effects)
