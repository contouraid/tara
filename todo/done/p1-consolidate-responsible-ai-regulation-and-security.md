# DONE: Consolidate Responsible AI, Regulation, and Security

**Section:** Root (cross-cutting)
**Priority:** High
**Owner:** Codex
**Opened:** 2026-07-11
**Completed:** 2026-07-11

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

## What Was Done

1. Added a canonical chapter, `docs/responsibleAI/responsibleAI.md`, covering the six kinds of obligation, the full responsible-AI lifecycle, jurisdiction-specific regulation and privacy, fairness, transparency, security, vendor risk, governance, and retirement.
2. Added primary regulator and standards-body sources with jurisdiction and date labels, including a final verification of the current HHS HIPAA and FDA predetermined-change-control guidance pages.
3. Added a deployment governance checklist and a RACI responsibility map with named accountable roles, escalation, suspension, incident-response, and retirement responsibilities.
4. Linked the QA, validation, VLM, and workflow chapters to stable, explicit section targets in the canonical chapter and replaced duplicated framing where appropriate.
5. Added the chapter to the book landing page, Sphinx toctree, and repository guide.
6. Fixed all cross-document MyST warnings by using explicit labels and Sphinx-native references.

## Acceptance Criteria

- [x] Readers can distinguish law, regulator guidance, consensus guidance, technical standards, institutional policy, and ethics
- [x] Every regulatory statement identifies jurisdiction, source, and effective/review date
- [x] The full AI lifecycle from intended use through retirement has named evidence, approval, monitoring, and change-control activities
- [x] Fairness covers data, model, workflow, access, and outcome mechanisms rather than metric parity alone
- [x] Cybersecurity includes read/write permissions, auditability, third-party dependencies, adversarial inputs, downtime, and recovery
- [x] A governance checklist and responsibility map identify accountable roles and escalation paths
- [x] QA, validation, VLM, and workflow chapters link to this canonical content without contradictory duplication

## Verification

- `git diff --check` passed.
- Clean strict Sphinx build: `../.venv/bin/sphinx-build -b html -W -n . _build/strict` completed with zero warnings across all 14 source files.
- HHS and FDA regulatory dates and guidance status were checked against their primary pages on 2026-07-11.
