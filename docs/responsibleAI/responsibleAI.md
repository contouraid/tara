# 11: Responsible AI, Regulation, and Security

Earlier chapters describe how to build, validate, integrate, and quality-assure specific AI tools. This chapter is the cross-cutting counterpart: it names who is accountable, what evidence and approvals a tool needs across its whole life, how patients and their data are protected, how a connected model is defended from attack, and how the answers change with jurisdiction. These concerns appear in fragments throughout the book—fairness in [validation](../validation/validation.md), governance in [workflow](../workflow/workflow.md), the regulatory frame in [quality assurance](../qa/qa.md), and prompt-injection risk in [vision–language models](../fundamentalAI/vlm.md)—but they are one subject and are treated canonically here. Those chapters supply operational detail; this chapter supplies the framework they hang on.

Two cautions apply throughout. First, this is orientation, not legal advice: the applicable law and standards for a specific tool must be determined with institutional regulatory, legal, and information-security expertise. Second, regulation moves, so **every regulatory statement below names its jurisdiction, source, and effective or review date**; a claim without those three is not actionable and should be checked before it is relied on.

## Six Kinds of "Must"

A recurring source of confusion is treating every requirement as if it had the same force. It does not. Six distinct kinds of obligation govern clinical AI, and a responsible program can state, for any given control, which kind it is answering to:

| Kind | Force | Examples |
|---|---|---|
| **Binding law** | Legally enforceable within its jurisdiction | EU AI Act; EU Medical Device Regulation; GDPR; US HIPAA |
| **Regulator guidance** | Not itself law; states how a regulator interprets and applies the law | US FDA guidance documents (e.g., predetermined change control plans) |
| **Consensus and professional guidance** | Persuasive, sometimes a standard of care; not binding law | WHO; ASTRO, ESTRO, AAPM position statements and task-group reports |
| **Technical standards** | Voluntary unless a law or contract references them | IEC 62304; ISO 14971; ISO/IEC 42001 |
| **Institutional policy** | Binding within the organization that issues it | Local model-governance policy; data-handling and access rules |
| **Ethics** | Judgment where rules are silent or conflict | Weighing an efficiency gain against unequal benefit across patient groups |

The distinction is practical, not academic. A vendor claim that a product "meets IEC 62304" describes a voluntary software-lifecycle standard, not regulatory clearance and not local clinical validation. A department that has an institutional policy but no legal obligation still must follow the policy. And ethics is not a residual category to invoke when the others run out; it is what decides how much benefit is enough, for whom, and at what cost—questions the other five kinds rarely answer on their own.

## The Responsible-AI Lifecycle

Responsibility is easiest to lose in the gaps between stages. A model is validated by one group, procured by another, commissioned by a third, and updated by a vendor, and no single record says what was decided, on what evidence, by whom. A lifecycle view closes those gaps by attaching, to each stage, a named activity, the evidence it produces, who approves it, and what would reverse it.

1. **Intended use.** State the users, patient population, inputs, output, the clinical decision supported, and the degree of automation. Everything downstream is scoped to this statement. See {ref}`validation <start-with-the-intended-use>`.
2. **Risk classification.** Determine the device/AI risk class under the applicable regime (see below) and the local hazard analysis. Risk class sets the required evidence and controls, not the other way around.
3. **Development controls.** Data provenance, versioning, and de-identification follow the [radiotherapy data and informatics foundations](../medicalImaging/medicalImaging.md); software lifecycle and risk management follow standards such as IEC 62304 and ISO 14971.
4. **Clinical evaluation.** Technical, silent, reader, and prospective evaluation, with subgroup and calibration analysis, are defined in [validation](../validation/validation.md). Evidence must match the claimed role.
5. **Procurement.** Contractual due diligence on evidence, security, data processing, model provenance, update policy, and exit terms (see *Third-Party, Cloud, and Vendor Risk* below).
6. **Commissioning.** Local acceptance and baseline characterization for the specific site, scanners, protocols, and population, as in {ref}`quality assurance <commissioning>`. Clearance elsewhere does not replace local commissioning.
7. **Change control.** Any modification—model, threshold, dependency, or interface—is a clinical change with documented reason, validation, training impact, release, rollback, and monitoring window. See {ref}`workflow <manage-versions-as-clinical-changes>`.
8. **Post-market monitoring.** Input drift, output and override distributions, subgroup performance, latency, and downstream safety, each tied to a defined response, as in {ref}`validation <post-deployment-monitoring>`.
9. **Incident response.** A route to recognize, report, investigate, and remediate a safety event, including regulatory reporting obligations and communication to affected clinicians and patients.
10. **Retirement.** A deliberate decision to withdraw a tool, with data retention, record continuity, and a validated fallback workflow.

The lifecycle is a frame, not a duplicate: the *how* of each stage lives in the chapter linked from it. What this chapter adds is the requirement that every stage have a named owner, explicit evidence, an approval, and a reversal path—so that "who decided this, and on what basis?" always has an answer.

(regulatory-and-privacy-frameworks-by-jurisdiction)=
## Regulatory and Privacy Frameworks by Jurisdiction

The frameworks below are the ones most often relevant to AI in radiotherapy. Each entry names jurisdiction, source, and effective or review date, and marks whether it is binding law, regulator guidance, or a voluntary standard. Only the primary regulator or standards-body text is authoritative; secondary summaries (including this one) can lag.

### United States

- **HIPAA Security Rule** (binding law; United States; US Department of Health and Human Services; effective 21 April 2003, with compliance required from 20 April 2005 for most covered entities and 20 April 2006 for small health plans). The standards, codified at 45 CFR Part 164, Subpart C, require administrative, physical, and technical safeguards for electronic protected health information [[1]](https://www.hhs.gov/hipaa/for-professionals/security/index.html) [[13]](https://www.hhs.gov/hipaa/for-professionals/index.html).
- **FDA medical-device oversight** (binding law and regulator guidance; United States; US Food and Drug Administration; guidance status reviewed 11 July 2026). An AI function meeting the device definition may require FDA review through an applicable pathway; the details are treated in {ref}`quality assurance <regulatory-and-standards-context>`. FDA's *Good Machine Learning Practice* guiding principles (2021, jointly with Health Canada and the UK MHRA) and its final guidance on predetermined change control plans (originally issued December 2024 and updated August 2025) are regulator guidance, not statute [[2]](https://www.fda.gov/medical-devices/software-medical-device-samd/good-machine-learning-practice-medical-device-development-guiding-principles) [[14]](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/marketing-submission-recommendations-predetermined-change-control-plan-artificial-intelligence).

### European Union

- **Artificial Intelligence Act** (binding law; Regulation (EU) 2024/1689; adopted 13 June 2024, entered into force 1 August 2024, with obligations phasing in over the following months and years). The first horizontal AI law; it classifies AI systems by risk, and many medical AI systems fall in its high-risk category with attendant obligations that operate alongside, not instead of, medical-device law [[3]](https://eur-lex.europa.eu/eli/reg/2024/1689/oj).
- **Medical Device Regulation** (binding law; Regulation (EU) 2017/745; entered into force 2017, applicable from 26 May 2021). Governs placing medical devices, including software as a medical device, on the EU market [[4]](https://eur-lex.europa.eu/eli/reg/2017/745/oj).
- **General Data Protection Regulation** (binding law; Regulation (EU) 2016/679; applicable from 25 May 2018). Governs processing of personal data, including health data as a special category [[5]](https://eur-lex.europa.eu/eli/reg/2016/679/oj).

### International technical standards (voluntary unless referenced by law or contract)

- **IEC 62304** — medical device software lifecycle processes [[6]](https://webstore.iec.ch/en/publication/22794).
- **ISO 14971:2019** — application of risk management to medical devices [[7]](https://www.iso.org/standard/72704.html).
- **ISO/IEC 42001:2023** — requirements for an artificial-intelligence management system, the first management-system standard specific to AI [[8]](https://www.iso.org/standard/42001).

### Voluntary frameworks and consensus guidance

- **NIST AI Risk Management Framework** (AI RMF 1.0, NIST AI 100-1; United States; January 2023). A voluntary framework for governing, mapping, measuring, and managing AI risk; not law, but a widely used scaffolding for the governance activities described here [[9]](https://www.nist.gov/itl/ai-risk-management-framework).
- **WHO** *Ethics and Governance of Artificial Intelligence for Health* (2021). Consensus guidance framing health AI around autonomy, safety, transparency, accountability, inclusiveness, and responsiveness [[10]](https://www.who.int/publications/i/item/9789240029200).

Two failure modes recur when reading this landscape. The first is treating a voluntary standard or framework as if it were binding law; the second is treating a regulator clearance as if it discharged the local obligations of commissioning, validation, and monitoring. Neither substitution is safe.

(fairness-and-health-equity)=
## Fairness and Health Equity

Fairness in clinical AI is not achieved by equalizing a single metric. Harm can enter—and must be examined—at five points along the path from data to patient outcome:

- **Data.** Dataset construction determines who is represented. Subgroup selection, intersectionality (harms that appear only at the combination of attributes), and measurement bias (a label that means something different across groups) are decided here. A concentration of training data in a few institutions or modalities limits what the model has actually learned, as noted for {ref}`vision–language models <privacy-and-dataset-bias>`.
- **Model.** The choice of prediction *target* can encode bias even when the algorithm is neutral. A widely cited analysis showed that a health-care algorithm using predicted cost as a proxy for predicted need systematically underestimated the needs of Black patients, because less money had historically been spent on them at equal illness [[11]](https://doi.org/10.1126/science.aax2342). The label, not the model class, was the defect.
- **Workflow.** A tool can perform equitably in isolation yet be applied unevenly—triggered for some patients and not others, or reviewed more carefully for some groups.
- **Access.** Benefit reaches only patients whose data, devices, and care settings the tool supports. Accessibility, including for patients with disabilities or non-standard anatomy, is part of fairness.
- **Outcome.** The endpoint that matters is whether clinical outcomes and the benefits of automation are distributed fairly, not whether an intermediate score is balanced.

Subgroup evaluation—the mechanics of measuring performance across sex, age, anatomy, site, device, and institution—is detailed in {ref}`validation <subgroup-evaluation>`. This chapter's point is upstream of the metric: different error types carry different clinical harm, so fairness analysis must connect subgroup performance to data, model target, workflow, access, and outcome, rather than reporting metric parity alone.

## Transparency, Accountability, and Patients

- **Transparency and explainability.** Users should be able to learn what a tool checked and did not check, on what inputs, and with what known limitations. Explanations must themselves be validated for usefulness rather than assumed helpful.
- **Uncertainty.** A calibrated probability is not the same as free-form confidence language; calibration and its evaluation are covered in {ref}`validation <calibration-and-probabilistic-predictions>`.
- **Contestability.** There should be a defined, low-friction way for a clinician—or a patient—to question, override, and appeal an AI-influenced decision, with the override recorded and reviewed.
- **Informed communication and patient involvement.** Patients and the public have a legitimate interest in how AI is used in their care. Meaningful involvement in design and deployment improves both legitimacy and safety.
- **Accountability and liability.** Accountability rests with named people and the institution, never with "the model" or "the team." The boundary of responsibility among clinician, institution, and vendor should be explicit in advance, not discovered after an incident.
- **Conflicts of interest.** Financial and academic interests in a tool's adoption should be disclosed and managed, particularly when the same parties generate and interpret the supporting evidence.

(cybersecurity-for-connected-clinical-ai)=
## Cybersecurity for Connected Clinical AI

Integrated clinical AI is a security concern precisely because it is useful: to help, it must read from and often write to safety-critical systems—the oncology information system, the treatment planning system, the record-and-verify database. That read/write reach is also its attack surface. Threat modeling asks, for each connection, what an attacker could read, alter, delay, or destroy, and what the clinical consequence would be.

Core controls:

- **Authentication and authorization.** Strong authentication of users and services, with authorization scoped to role.
- **Least privilege.** A service that only needs to read images should not be able to write plans. Read and write permissions into clinical systems are granted narrowly and reviewed.
- **Audit logs.** Tamper-evident records of who and what accessed or changed clinical data, sufficient to reconstruct an incident.
- **Supply-chain and model risk.** Provenance and integrity of models, weights, dependencies, and container images; a compromised or silently swapped model breaks traceability just as a code compromise would.
- **Adversarial inputs.** Data poisoning during training and prompt injection at inference are recognized threats for connected and language-model-based systems; the OWASP Top 10 for LLM Applications (2025) catalogs these for LLM and agent deployments [[12]](https://genai.owasp.org/llm-top-10/), and the input-separation defenses are described for {ref}`vision–language models <protect-against-prompt-and-retrieval-risks>`.
- **Ransomware and downtime.** Radiotherapy has been disrupted by ransomware; availability is a clinical-safety property, not only an IT one. A tested downtime and manual-fallback workflow is a security control, covered operationally in {ref}`workflow <reliability-and-downtime>`.
- **Cloud and vendor dependencies.** A dependency on an external service is a dependency on its availability, security posture, and continued existence.
- **Recovery.** Backups, tested restoration, and a rehearsed incident-response plan determine how quickly safe operation resumes after a compromise or outage.

The NIST AI Risk Management Framework [[9]](https://www.nist.gov/itl/ai-risk-management-framework) provides a structure for mapping and managing these risks alongside the fairness and governance concerns above, rather than treating security as a separate silo.

## Third-Party, Cloud, and Vendor Risk

Most clinical AI is procured, not built in-house, which shifts part of the responsibility—but none of the accountability—to a vendor. Procurement is therefore a governance activity. Due diligence should establish, in the contract where possible:

- the evidence supporting the claimed intended use, and its independence;
- security posture, including data location, encryption, access controls, and breach notification;
- a data-processing agreement consistent with the applicable privacy law;
- model and dependency provenance, and the policy for updates and their revalidation;
- service-level commitments for availability and support, and their clinical adequacy;
- exit and portability terms: what happens to data, configurations, and continuity if the vendor or service ends.

A dependency the institution cannot inspect, monitor, or exit is a risk the institution nonetheless owns.

(a-governance-checklist-and-responsibility-map)=
## A Governance Checklist and Responsibility Map

Governance becomes real only when it is attached to named people, measures, and decision rights. The oversight group described in {ref}`workflow <governance>` should have the authority to approve deployment, restrict use, require corrective action, and suspend a system. The following checklist and responsibility map make that authority operational.

### Governance checklist

Before deployment and at each periodic review, confirm that:

- [ ] The intended use, users, population, and degree of automation are documented.
- [ ] The applicable legal regime and risk class are identified, with jurisdiction and effective dates.
- [ ] Clinical evaluation evidence matches the claimed role, including subgroup and calibration analysis.
- [ ] Fairness has been examined across data, model target, workflow, access, and outcome.
- [ ] A cybersecurity threat model covers read/write permissions, authentication, audit logging, adversarial inputs, third-party dependencies, downtime, and recovery.
- [ ] A change-control process treats any modification as a clinical change with revalidation.
- [ ] Post-market monitoring is defined, with thresholds tied to specific responses.
- [ ] An incident-response and regulatory-reporting route exists and has been tested.
- [ ] Named owners, escalation paths, and the authority to suspend are recorded.
- [ ] A retirement plan and validated fallback workflow exist before go-live.

### Responsibility map (RACI)

A responsibility-assignment matrix names, for each activity, who is **R**esponsible (does the work), **A**ccountable (answerable for the outcome—exactly one role), **C**onsulted, and **I**nformed. "The team" is not a role.

| Activity | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| Intended use and clinical evaluation | Clinical/physics lead | Clinical owner (e.g., lead radiation oncologist) | Data science, statistics | Governance committee |
| Commissioning and QA | Medical physicist | Clinical owner | Vendor, IT | Governance committee |
| Security and access control | IT / information security | Chief information security officer | Informatics, vendor | Clinical owner |
| Privacy and data processing | Data protection officer | Data protection officer | Legal, IT | Clinical owner |
| Change control and versioning | Informatics | Clinical owner | Physics, vendor, IT | All users |
| Monitoring and incident response | Informatics / QA | Clinical owner | Security, vendor | Governance committee |
| Suspension / retirement decision | Governance committee | Governance committee chair | Clinical owner, physics, legal | All users, patients where relevant |

The exact titles vary by institution; the requirement is that each row has a single accountable role and a working escalation path to the authority that can stop the system. This map replaces the scattered, implicit ownership that the QA, validation, VLM, and workflow chapters each touch locally, and those chapters link here rather than restating it.

## Current Research and Recent Advances

- **First horizontal AI law:** The EU Artificial Intelligence Act (Regulation (EU) 2024/1689) entered into force on 1 August 2024 with obligations phasing in over subsequent years. It classifies AI systems by risk and places many medical AI systems in its high-risk category, creating obligations that operate alongside existing medical-device and data-protection law rather than replacing them [[3]](https://eur-lex.europa.eu/eli/reg/2024/1689/oj). _(added: 2026-07)_
- **Management-system standards for AI:** ISO/IEC 42001:2023, the first AI-management-system standard, and the NIST AI Risk Management Framework (2023) give organizations voluntary, auditable structures for the governance, fairness, and security activities that clinical deployment requires—useful scaffolding, but not a substitute for device law or local validation [[8]](https://www.iso.org/standard/42001) [[9]](https://www.nist.gov/itl/ai-risk-management-framework). _(added: 2026-07)_
- **A named threat taxonomy for language-model systems:** The OWASP Top 10 for LLM Applications (2025) formalizes risks—prompt injection, sensitive-information disclosure, supply-chain and model poisoning, and excessive agency—that are directly relevant as retrieval- and agent-based tools reach into clinical systems [[12]](https://genai.owasp.org/llm-top-10/). _(added: 2026-07)_

## Recap

Responsible clinical AI is a single subject with many faces: accountability, evidence, equity, privacy, security, and jurisdiction. Six kinds of obligation—binding law, regulator guidance, consensus guidance, technical standards, institutional policy, and ethics—carry different force and must not be substituted for one another. The AI lifecycle, from intended use through retirement, works only when each stage has a named owner, explicit evidence, an approval, and a reversal path. Regulation is jurisdiction- and date-specific, so every regulatory claim must name its source and effective date and distinguish law from voluntary standards. Fairness spans data, model target, workflow, access, and outcome rather than metric parity alone. Cybersecurity is a clinical-safety property for systems that read from and write to safety-critical databases, covering permissions, auditability, adversarial inputs, third-party dependence, downtime, and recovery. A governance checklist and RACI-style responsibility map turn these principles into named roles and escalation paths—the point at which responsibility stops being an aspiration and becomes an assignment.

## References

1. U.S. Department of Health and Human Services. *HIPAA Security Rule* (Security Standards for the Protection of Electronic Protected Health Information; 45 CFR Part 164, Subpart C). [HHS](https://www.hhs.gov/hipaa/for-professionals/security/index.html)
2. U.S. Food and Drug Administration, Health Canada, Medicines and Healthcare products Regulatory Agency. *Good Machine Learning Practice for Medical Device Development: Guiding Principles*. 2021, updated 2025. [FDA guidance](https://www.fda.gov/medical-devices/software-medical-device-samd/good-machine-learning-practice-medical-device-development-guiding-principles)
3. European Parliament and Council. Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence (Artificial Intelligence Act). Adopted 13 June 2024; in force 1 August 2024. [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
4. European Parliament and Council. Regulation (EU) 2017/745 on medical devices (Medical Device Regulation). In force 2017; applicable from 26 May 2021. [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2017/745/oj)
5. European Parliament and Council. Regulation (EU) 2016/679 on the protection of natural persons with regard to the processing of personal data (General Data Protection Regulation). Applicable from 25 May 2018. [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
6. International Electrotechnical Commission. IEC 62304:2006+A1:2015, Medical device software—Software life cycle processes. [IEC publication](https://webstore.iec.ch/en/publication/22794)
7. International Organization for Standardization. ISO 14971:2019, Medical devices—Application of risk management to medical devices. [ISO](https://www.iso.org/standard/72704.html)
8. International Organization for Standardization / International Electrotechnical Commission. ISO/IEC 42001:2023, Information technology—Artificial intelligence—Management system. [ISO](https://www.iso.org/standard/42001)
9. National Institute of Standards and Technology. *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*, NIST AI 100-1. January 2023. [NIST](https://www.nist.gov/itl/ai-risk-management-framework)
10. World Health Organization. *Ethics and Governance of Artificial Intelligence for Health*. 2021. [WHO publication](https://www.who.int/publications/i/item/9789240029200)
11. Obermeyer Z, Powers B, Vogeli C, Mullainathan S. Dissecting racial bias in an algorithm used to manage the health of populations. *Science*. 2019;366(6464):447-453. [DOI](https://doi.org/10.1126/science.aax2342)
12. OWASP Foundation. *OWASP Top 10 for LLM Applications* (2025). [OWASP Gen AI Security Project](https://genai.owasp.org/llm-top-10/)
13. U.S. Department of Health and Human Services. *HIPAA for Professionals*. Security Rule effective 21 April 2003; compliance required from 20 April 2005 for most covered entities and 20 April 2006 for small health plans; content last reviewed 19 March 2026. [HHS](https://www.hhs.gov/hipaa/for-professionals/index.html)
14. U.S. Food and Drug Administration. *Marketing Submission Recommendations for a Predetermined Change Control Plan for Artificial Intelligence-Enabled Device Software Functions*. Final guidance originally issued December 2024; updated 18 August 2025. [FDA guidance](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/marketing-submission-recommendations-predetermined-change-control-plan-artificial-intelligence)
