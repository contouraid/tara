# TODO: Consolidate Responsible AI, Regulation, and Security

**Section:** Root (cross-cutting)
**Priority:** High
**Owner:** (unassigned)
**Opened:** 2026-07-11

## Gap

Fairness, human factors, governance, privacy, regulation, and monitoring appear in several chapters, but only as brief fragments. There is no single novice-accessible account of responsible AI across the medical-device lifecycle, nor a clear distinction among legal requirements, standards, professional guidance, institutional policy, and ethical judgment. Cybersecurity and third-party/cloud risk are largely absent even though integrated AI can read from and write to safety-critical clinical systems.

Readers therefore lack a coherent framework for deciding who is accountable, what evidence is required, how changes are controlled, how patients and data are protected, and how jurisdiction affects the answer.

## What Is Needed

1. Create one canonical responsible-AI treatment covering intended use, risk classification, development controls, clinical evaluation, procurement, commissioning, change control, post-market monitoring, incident response, and retirement.
2. Explain fairness and health equity from dataset construction through access and clinical outcomes, including subgroup selection, intersectionality, measurement bias, accessibility, and unequal automation benefit.
3. Cover transparency, explainability, uncertainty, contestability, informed communication, patient/public involvement, accountability, liability boundaries, and conflicts of interest.
4. Introduce cybersecurity threat modeling for connected clinical AI: authentication and authorization, least privilege, audit logs, supply-chain/model risk, prompt injection, data poisoning, ransomware/downtime, cloud/vendor dependencies, and recovery.
5. Compare regulatory and privacy frameworks only from current primary regulator or standards-body sources. Label jurisdiction and effective date; distinguish binding law from guidance and voluntary standards.
6. Add a reusable governance checklist and RACI-style responsibility map, then replace duplicated fragments in QA, validation, VLM, and workflow chapters with links.

## Acceptance Criteria

- [ ] Readers can distinguish law, regulator guidance, consensus guidance, technical standards, institutional policy, and ethics
- [ ] Every regulatory statement identifies jurisdiction, source, and effective/review date
- [ ] The full AI lifecycle from intended use through retirement has named evidence, approval, monitoring, and change-control activities
- [ ] Fairness covers data, model, workflow, access, and outcome mechanisms rather than metric parity alone
- [ ] Cybersecurity includes read/write permissions, auditability, third-party dependencies, adversarial inputs, downtime, and recovery
- [ ] A governance checklist and responsibility map identify accountable roles and escalation paths
- [ ] QA, validation, VLM, and workflow chapters link to this canonical content without contradictory duplication
