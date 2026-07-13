# Language Models, Generative AI, and Agents

## Before you begin

**Prerequisites:** Read [Chapter 1](../intro/intro.md) and the transformer section of [Chapter 2](index.md). Use the [cross-book glossary](../resources/glossary.md) for shared artificial intelligence (AI) definitions.

**Learning objectives:** After this page, you should be able to:

1. distinguish natural language processing, large language models, chatbots, retrieval-augmented generation, tools, and agents;
2. trace clinical text through tokenization, adaptation, prompting, retrieval, inference, structured output, and review;
3. identify hallucination, omission, provenance, prompt-injection, privacy, drift, and automation-bias failure modes;
4. match task-constrained, generated, and human-workflow evaluations to a stated intended use; and
5. define a bounded, source-grounded, permission-limited deployment with abstention and escalation.

**Reading route:** Read this after the Chapter 2 transformer material. Clinicians may focus on system types, clinical workflow, failure modes, and evaluation; technical readers should include retrieval, tools, and agents. The recurring cases can use language systems for extraction or drafting, but none treats fluent text as a treatment decision.

Natural language processing (NLP) turns free text into information or produces text for a defined purpose. In radiation oncology, the text may be a consultation note, pathology report, prescription, treatment summary, guideline, patient message, incident report, or research paper. Language systems range from narrow extractors to generative assistants that retrieve documents and call software tools.

Fluent output is not evidence of clinical reasoning. A language model predicts text; a clinically integrated product adds data sources, prompts, retrieval, tools, permissions, validation, user interfaces, and human accountability. The safety and evidence claim belongs to that complete system for one intended use—not to the model name or chat demonstration.

## What Kind of System Is It?

These terms describe different layers and should not be used interchangeably:

| Term | Meaning | Example output |
|---|---|---|
| **NLP** | The broad field of computational methods for human language | a diagnosis code extracted from a note |
| **Discriminative language model** | Maps text to a constrained label, span, score, or embedding | toxicity present/absent; the exact dose phrase |
| **Large language model (LLM)** | A high-capacity model pretrained on large text collections and adaptable to many language tasks | generated or scored token sequences |
| **Generative AI** | A wider category of models that create text, images, audio, code, or other content | a draft treatment summary |
| **Chatbot** | A conversational interface that maintains a dialogue; it may use an LLM, rules, retrieval, or all three | a multi-turn question-and-answer exchange |
| **Retrieval-augmented generation (RAG)** | Retrieves external passages and supplies them to a generator at inference time | an answer grounded in a named guideline section |
| **Tool use** | Lets a model request a defined function or API with structured arguments | `get_prescription(patient_id)` |
| **Agent** | Uses a model in a loop to choose actions, inspect results, maintain task state, and pursue a goal | collect chart fields, detect missing data, then prepare a review queue |
| **Vision-language model (VLM)** | Couples visual and textual representations | an answer grounded in an image region |

An LLM is therefore not automatically a chatbot, a search engine, an agent, or a medical device. A RAG system can use a small model; an agent can use deterministic planning; and a chatbot can expose no tools at all. Systems that directly consume images belong in [Vision Language Models](vlm.md), which is the canonical home for multimodal architecture, volumetric imaging, visual grounding, and image-specific evaluation.

## From Clinical Text to Model Input

### Tokens and Embeddings

A tokenizer divides text into **tokens**: words, parts of words, punctuation, or bytes represented by integer identifiers. One clinical term may occupy several tokens, and token boundaries do not necessarily follow medical meaning. Token counts determine cost and whether content fits into the model's context.

An **embedding** maps a token, passage, or document to a vector. Token embeddings are internal model representations. Passage embeddings are often used for semantic retrieval: items with related meaning may be close even when their wording differs. Similarity is not truth or clinical equivalence; “no evidence of recurrence” and “evidence of recurrence” share vocabulary and require models that preserve negation.

### Pretraining, Adaptation, and Instruction Tuning

Transformers use attention to relate tokens across a sequence [[1]](https://proceedings.neurips.cc/paper/7181-attention-is-all-you-need). An encoder model such as BERT can be pretrained by reconstructing masked text and then fine-tuned for constrained tasks such as classification, span extraction, or named-entity recognition [[2]](https://doi.org/10.18653/v1/N19-1423). A decoder-style generative model is commonly pretrained to predict the next token given preceding tokens.

**Instruction tuning** adapts a pretrained model to follow task descriptions and examples. Preference tuning can make responses more helpful or aligned with annotator expectations; InstructGPT demonstrated that human preference data can materially change behavior while simple mistakes remain [[3]](https://proceedings.neurips.cc/paper_files/paper/2022/hash/b1efde53be364a73914f58805a001731-Abstract.html). Fine-tuning changes model parameters. Prompting and RAG instead change the information supplied at inference time.

### Context Windows, Prompts, and Inference

The **context window** is the bounded token sequence available for one inference. It may contain system instructions, the user's request, prior turns, retrieved passages, tool results, and an output schema. Fitting a document into the window does not ensure that every detail will be used correctly. Important content can be omitted, contradicted, or overwhelmed by irrelevant context.

A **prompt** is part of the system configuration. It should state the task, permitted evidence, output format, handling of missing or conflicting information, and abstention rule. Few-shot examples can clarify behavior but may also teach unintended shortcuts. Prompt development belongs inside the development set; repeatedly changing prompts after inspecting the final test set leaks evaluation information.

During **inference**, the model produces a distribution over possible next tokens. Decoding settings control how a sequence is selected. A lower temperature may improve repeatability but cannot make unsupported content true. Re-running the same prompt, asking the model to “be certain,” or reading confident wording is not a calibrated uncertainty estimate.

## Retrieval-Augmented Generation and Provenance

RAG separates some external knowledge from model parameters. The original RAG formulation combined a generator's parametric memory with retrieved passages from a searchable index [[4]](https://proceedings.neurips.cc/paper/2020/hash/6b493230-Abstract.html). In a clinical system, the corpus should be governed as carefully as a dataset:

1. define authoritative sources, owners, versions, effective dates, jurisdictions, and patient populations;
2. parse documents while preserving headings, tables, footnotes, page locations, and access controls;
3. split content into retrievable units and create lexical or embedding indexes;
4. retrieve candidate passages for the user's question and apply metadata filters;
5. provide only authorized passages to the model with explicit source identifiers;
6. generate a constrained answer that links each material claim to supporting text;
7. verify that cited passages exist and actually entail the claims before human review.

RAG can make knowledge easier to update and provenance easier to expose. It does not guarantee retrieval of the right passage, faithful use of that passage, or a correct answer. A system may retrieve obsolete guidance, miss a decisive exception, cite a relevant document that does not support the sentence, or combine recommendations for incompatible populations. Bibliographic-looking text generated from model memory is not a verified citation; fabricated and erroneous references have been documented even in newer general models [[10]](https://doi.org/10.1038/s41598-023-41032-5).

(source-to-reviewed-output)=
## From Source Document to Reviewed Clinical Output

The following pipeline illustrates one safe pattern for guideline navigation. Dashed boundaries are trust or permission boundaries, not merely software components.

```text
approved guideline/PDF
        │  owner, version, effective date, access policy
        ▼
validated parser ──► versioned passages ──► retrieval index
                                              │
clinician question ──► identity/role check ───┤
                                              ▼
                              retrieved passages + source locations
                                              │  untrusted content boundary
                                              ▼
                                   constrained LLM prompt
                                              ▼
                                    structured draft answer
                                              │
                    schema + citation + claim-support validation
                                              ▼
                         clinician reviews answer beside sources
                                              ▼
                              approve / edit / reject / escalate
                                              │
                               audit log; no silent chart write
```

The model is one box in this pipeline. Retrieval recall, document currency, permissions, validators, display, and review behavior can dominate safety. Store the source version, query, retrieved passages, model and prompt versions, generated output, validation results, edits, reviewer, and final disposition.

## Structured Outputs, Tools, Memory, and Agents

### Structured Outputs and Tool Calling

A schema can require fields such as `{finding, evidence_location, confidence_state}` and reject malformed output. This improves interface reliability but not semantic correctness: a perfectly valid JSON field can contain the wrong dose.

Tool calling lets a model propose a function and arguments rather than fabricate the result in prose. Research systems such as Toolformer showed that language models can learn when and how to invoke external APIs [[5]](https://proceedings.neurips.cc/paper/2023/hash/d842425e4bf79ba039352da0f658a906-Abstract-Conference.html). In a clinical system, every tool needs a narrow contract, input validation, patient-context checks, least privilege, timeouts, idempotency where possible, and auditable results. Deterministic software—not the LLM—should perform arithmetic, DICOM parsing, dose calculation, constraint comparison, and database enforcement.

### Memory and Workflow Agents

**Conversation history** contains recent turns. **Task state** records explicit facts such as which chart was opened, which checks ran, and which approvals remain. **Long-term memory** stores information across sessions. These are different risk surfaces. A summary generated by the model is not an authoritative patient record, and memories must have provenance, access control, retention rules, correction, and deletion.

An agent repeatedly observes state, selects an action, receives a result, and decides what to do next. This can help orchestrate multi-step research or administrative work, but errors compound across steps. More autonomy also expands the impact of prompt injection, wrong-patient selection, stale state, duplicated actions, and data exfiltration.

Useful deterministic guardrails include:

- an allow-list of tools, arguments, records, and destinations;
- read-only access by default and separate authorization for every write;
- explicit patient and encounter binding outside the language model;
- maximum steps, time, cost, and retry limits;
- typed workflow states and prohibited transitions;
- independent validation of tool inputs and outputs;
- human confirmation immediately before consequential or irreversible action;
- a complete audit trail and a tested stop, rollback, and downtime path.

## Radiotherapy Use Cases and Evidence Maturity

The relevant question is not “Can an LLM produce something plausible?” but “What evidence supports this exact role, and what happens when it is wrong?”

| Use case | Evidence maturity | Important failure modes | Minimum oversight before clinical use |
|---|---|---|---|
| **Documentation drafting**: consultation, on-treatment, or completion summaries assembled from verified fields | General-health deployment evidence is emerging; RT-specific impact evidence is limited | omitted toxicity, copied-forward error, wrong fraction or stage, polished contradiction | source-linked fields, constrained template, mandatory author review, edit and omission monitoring |
| **Information extraction and cohort discovery**: stage, treatment, dose, toxicity, or eligibility from notes | Classical discriminative NLP is established; generative extraction is mostly retrospective | negation and temporality errors, hidden missingness, data leakage, biased exclusions | task-specific labeled validation, patient-level splits, structured output, manual sample audit; no direct cohort enrollment |
| **Guideline and policy retrieval** | RAG is technically mature as a method; prospective RT decision evidence is thin | stale or wrong-jurisdiction source, missed exception, unsupported synthesis, fabricated attribution | approved versioned corpus, source passage beside every claim, date/population filters, clinician decision ownership |
| **Plan and chart checking** | Early concept or retrospective prototype for LLM-based components; deterministic checks are more mature | arithmetic error, wrong-patient context, missed hard constraint, narrative overriding a rule | rules and dose engines remain authoritative, read-only silent testing, realistic fault set, physicist review, no autonomous approval |
| **Patient-facing communication** | One peer-reviewed cross-sectional RT study compared 115 answers with professional sources; two responses were rated potentially harmful and readability was worse [[9]](https://doi.org/10.1001/jamanetworkopen.2024.4630) | unsafe reassurance, omitted emergency advice, unsuitable reading level, unsupported personalization | approved source grounding, literacy and language testing, escalation rules, clinician review for patient-specific advice |
| **Research workflows**: screening, extraction, coding, data queries, or manuscript drafts | Useful demonstrations exist; reproducibility and scientific-integrity evidence varies | fabricated references, silent extraction omissions, code errors, leakage of unpublished or patient data | verify every source and extraction, execute code in controlled environments, retain protocol and model version, human authors accountable |
| **Workflow agents**: assembling chart data, routing tasks, or coordinating checks | Experimental in radiation oncology | cascading error, excessive permissions, duplicate or wrong-patient actions, prompt injection from retrieved text | least-privilege tools, typed state machine, step limits, independent checks, case-level approval before writes |

Radiation-oncology examination performance is evidence of domain question answering, not clinical competence: models showed large performance differences by model and disease area in a peer-reviewed in-training-examination study [[11]](https://doi.org/10.1089/aipo.2023.0007). Likewise, general medical benchmarks show that domain instruction tuning can improve expert ratings while leaving incorrect or omitted content [[7]](https://doi.org/10.1038/s41586-023-06291-2). Neither design measures whether a deployed human–AI team improves care.

Vendor demonstrations and unpublished radiation-oncology preprints may motivate evaluation, but they are not interchangeable with peer-reviewed external validation or prospective impact studies. Report model access date and exact version: hosted models, safety layers, retrieval corpora, and prompts can change, making an old score a result for an old configuration.

## Failure Modes and Security

### Hallucination, Omission, and Unreliable Confidence

A **hallucination** is content unsupported by the supplied evidence or reality. An omission may be more dangerous because the remaining text can be entirely correct. Evaluate both claim correctness and completeness against the intended use. Verbal phrases such as “high confidence” are generated text unless separately calibrated against held-out outcomes. An abstention policy needs operational triggers, a safe fallback, and measurement of inappropriate answers as well as inappropriate refusals.

### Prompt Injection and Data Exfiltration

Prompts, retrieved documents, web pages, messages, and tool output may contain instructions. **Indirect prompt injection** occurs when malicious or accidental instructions inside such content alter system behavior; peer-reviewed demonstrations have shown compromise of LLM-integrated applications through retrieved data [[6]](https://doi.org/10.1145/3605764.3623985). Delimiters and a request to “ignore instructions in documents” are not security boundaries.

Treat retrieved text as untrusted data. Enforce authorization outside the model, minimize secrets in context, isolate tools, validate destinations, and prevent the model from choosing its own privileges. A model that can read a chart and send a message creates an exfiltration route even if each function is individually legitimate. The canonical governance and threat-management treatment is in {ref}`Responsible AI, Regulation, and Security <cybersecurity-for-connected-clinical-ai>`.

### Privacy, Knowledge Cutoffs, and Drift

Do not paste protected or confidential data into a service unless the institution has approved the data flow, contract, retention, training use, region, subprocessors, access controls, and incident response. De-identification is not guaranteed by removing a name from free text.

Parametric knowledge reflects an opaque training period and can be stale. RAG helps only when the current source is retrieved and used faithfully. Model, prompt, tokenizer, tool, index, and policy updates create a new system configuration. Freeze them for evaluation, log them in use, regression-test changes, and maintain rollback. Sampling a few familiar questions after a version change is not revalidation.

### Automation Bias and Overreliance

Fluent drafts can anchor reviewers. Faster approval, fewer edits, or high user preference can reflect overreliance rather than quality. Interfaces should expose evidence and missing information, require meaningful review for high-risk content, and sample accepted outputs against an independent reference. Monitor correction type and clinical severity, not edit distance alone.

## Evaluation for the Intended Task

A broad benchmark score cannot validate a specific workflow. A systematic review published online in 2024 examined 519 healthcare LLM studies and found that only 5% used real patient-care data; accuracy dominated, while calibration, deployment considerations, fairness, bias, and toxicity were much less commonly assessed [[8]](https://doi.org/10.1001/jama.2024.21700). Evaluation should progress from frozen component tests to the real human–AI system.

### Constrained and Extraction Tasks

For labels or spans, report sensitivity, specificity, precision, recall, F1, calibration where probabilities drive action, and exact or partial span agreement. Stratify by institution, note type, disease site, language, subgroup, negation, temporality, missing fields, and rare but serious cases. Compare against rules and smaller task-specific models; a larger generator is not automatically the best extractor.

### Generated and Retrieved Answers

Evaluate at the claim level:

- factual correctness and clinically important omissions;
- whether each claim is supported, contradicted, or not addressed by its cited passage;
- retrieval recall for the decisive source, not only ranking similarity;
- source authority, currency, jurisdiction, population, and version;
- correct attribution and resolvable identifiers;
- harmful action, delay, reassurance, or escalation, weighted by severity;
- readability, language quality, and preservation of uncertainty;
- reproducibility across repeated runs and frozen prompt variants;
- appropriate answering and abstention on answerable and unanswerable cases.

BLEU, ROUGE, embedding similarity, and user preference can supplement this assessment but cannot replace it. Different wording may be clinically equivalent, while nearly identical wording can reverse meaning through negation, dose, laterality, or timing.

### Human–AI and Prospective Evaluation

Measure the intended users with and without the system: correctness and omission severity after review, time, editing burden, source consultation, overrides, inappropriate acceptance, escalation, subgroup effects, and downstream decisions. Use representative prevalence and account for repeated users and cases. Silent evaluation should precede influence on care; consequential uses require prospective comparison and monitoring of near misses and patient outcomes where relevant.

Prespecify acceptance thresholds by error severity. A system can have excellent mean factuality and still fail because one unsupported dose or missed cord constraint is unacceptable. The reviewer study must reflect the actual interface, time pressure, permissions, and fallback—not an isolated chat window.

## Current Research and Recent Advances

- **Medical evaluation remains benchmark-heavy:** A large systematic review found that most healthcare LLM evaluations focused on question answering and accuracy, with limited real patient-care data, calibration, or deployment analysis [[8]](https://doi.org/10.1001/jama.2024.21700). _(added: 2026-07)_
- **Radiation-oncology evidence is task-specific:** Peer-reviewed patient-question and examination studies demonstrate useful domain behavior alongside harmful answers, readability problems, and substantial model/domain variation; they do not establish clinical workflow benefit [[9]](https://doi.org/10.1001/jamanetworkopen.2024.4630) [[11]](https://doi.org/10.1089/aipo.2023.0007). _(added: 2026-07)_
- **Tools increase capability and attack surface:** Language models can learn to call external tools, but retrieved content can also inject instructions into an application. Clinical agents therefore require system-enforced permissions and validation rather than prompt-only controls [[5]](https://proceedings.neurips.cc/paper/2023/hash/d842425e4bf79ba039352da0f658a906-Abstract-Conference.html) [[6]](https://doi.org/10.1145/3605764.3623985). _(added: 2026-07)_

## Knowledge Check

1. **Recall:** What does retrieval-augmented generation add to a language model?
   - **Answer and reasoning:** It retrieves selected source material and supplies it as context for generation; it does not guarantee that retrieval is complete or the answer faithful. Treating retrieval as an automatic truth filter is wrong. Review [Retrieval-Augmented Generation and Provenance](#retrieval-augmented-generation-and-provenance).
2. **Interpretation:** A generated treatment summary cites the correct chart but states the wrong fraction number. Has provenance solved the problem?
   - **Answer and reasoning:** No. Provenance makes checking possible, but the claim is still incorrect and requires field-level validation and human review. A source link beside a false claim is not safety. Review [From Source Document to Reviewed Clinical Output](#from-source-document-to-reviewed-clinical-output).
3. **Security:** Why should retrieved text be treated as untrusted data?
   - **Answer and reasoning:** It can contain malicious or accidental instructions that redirect model behavior or tools. Asking the model to ignore attacks is weaker than enforcing permissions and data/tool isolation outside it. Review [Failure Modes and Security](#failure-modes-and-security).
4. **Application:** What endpoint should evaluate an LLM that drafts notes for clinician approval?
   - **Answer and reasoning:** Measure claim correctness, omissions, attribution, clinically weighted errors, edit burden, review behavior, and workflow effects. Fluency or user preference alone can reward persuasive errors and automation bias. Review [Evaluation for the Intended Task](#evaluation-for-the-intended-task).
5. **Governance:** An agent may read charts and send messages. Is a final “Are you sure?” prompt an adequate control?
   - **Answer and reasoning:** No. Use least privilege, explicit destinations, deterministic validation, audit logs, approval boundaries, and safe failure states. A confirmation prompt can be habituated or manipulated. Review [Structured Outputs, Tools, Memory, and Agents](#structured-outputs-tools-memory-and-agents).

## Recap

- **Objective 1:** Natural language processing is the field; a large language model is a model; a chatbot is an interface; retrieval-augmented generation supplies retrieved context; tools expose functions; and an agent chooses actions over steps.
- **Objective 2:** Tokens and embeddings enter a pretrained or adapted model under prompts and context; retrieval and tools add external state; decoding or structured output produces a candidate that still needs validation and review.
- **Objective 3:** Fluent systems can hallucinate, omit, lose provenance, follow injected instructions, expose data, drift, and encourage overreliance.
- **Objective 4:** Constrained tasks need field-level errors; generated answers need claim-level factuality, attribution, and clinically weighted harms; deployment claims need prospective human-workflow evidence.
- **Objective 5:** Safer roles are narrow, source-grounded, least-privilege, auditable, and read-only where possible, with validation, abstention, escalation, and accountable review.

**Important limitation and misconception:** Retrieval and structured output improve control but do not guarantee truth, and a language model's apparent explanation or confidence is not a calibrated account of clinical reasoning.

## References

1. Vaswani A, Shazeer N, Parmar N, et al. Attention is all you need. *Advances in Neural Information Processing Systems*. 2017. [Proceedings](https://proceedings.neurips.cc/paper/7181-attention-is-all-you-need)
2. Devlin J, Chang MW, Lee K, Toutanova K. BERT: pre-training of deep bidirectional transformers for language understanding. *NAACL-HLT*. 2019:4171-4186. [DOI](https://doi.org/10.18653/v1/N19-1423)
3. Ouyang L, Wu J, Jiang X, et al. Training language models to follow instructions with human feedback. *Advances in Neural Information Processing Systems*. 2022;35. [Proceedings](https://proceedings.neurips.cc/paper_files/paper/2022/hash/b1efde53be364a73914f58805a001731-Abstract.html)
4. Lewis P, Perez E, Piktus A, et al. Retrieval-augmented generation for knowledge-intensive NLP tasks. *Advances in Neural Information Processing Systems*. 2020;33. [Proceedings](https://proceedings.neurips.cc/paper/2020/hash/6b493230-Abstract.html)
5. Schick T, Dwivedi-Yu J, Dessì R, et al. Toolformer: language models can teach themselves to use tools. *Advances in Neural Information Processing Systems*. 2023;36. [Proceedings](https://proceedings.neurips.cc/paper/2023/hash/d842425e4bf79ba039352da0f658a906-Abstract-Conference.html)
6. Abdelnabi S, Greshake K, Mishra S, et al. Not what you've signed up for: compromising real-world LLM-integrated applications with indirect prompt injection. *Proceedings of the 16th ACM Workshop on Artificial Intelligence and Security*. 2023:79-90. [DOI](https://doi.org/10.1145/3605764.3623985)
7. Singhal K, Azizi S, Tu T, et al. Large language models encode clinical knowledge. *Nature*. 2023;620:172-180. [DOI](https://doi.org/10.1038/s41586-023-06291-2)
8. Bedi S, Liu Y, Orr-Ewing L, et al. Testing and evaluation of health care applications of large language models: a systematic review. *JAMA*. 2025;333(4):319-328. Published online 2024. [DOI](https://doi.org/10.1001/jama.2024.21700)
9. Yalamanchili A, Sengupta B, Song J, et al. Quality of large language model responses to radiation oncology patient care questions. *JAMA Network Open*. 2024;7(4):e244630. [DOI](https://doi.org/10.1001/jamanetworkopen.2024.4630)
10. Walters WH, Wilder EI. Fabrication and errors in the bibliographic citations generated by ChatGPT. *Scientific Reports*. 2023;13:14045. [DOI](https://doi.org/10.1038/s41598-023-41032-5)
11. Thaker NG, Redjal N, Loaiza-Bonilla A, et al. Large language models encode radiation oncology domain knowledge: performance on the American College of Radiology standardized examination. *AI in Precision Oncology*. 2024;1(1). [DOI](https://doi.org/10.1089/aipo.2023.0007)
