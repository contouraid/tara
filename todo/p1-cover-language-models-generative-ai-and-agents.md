# TODO: Cover Language Models, Generative AI, and Agents

**Section:** `fundamentalAI/`
**Priority:** High
**Owner:** (unassigned)
**Opened:** 2026-07-11

## Gap

The VLM page explains image-language systems, but the book lacks a foundation for text-only large language models, clinical NLP, retrieval-augmented generation, tool use, and agentic workflows. These systems are increasingly discussed for documentation, information retrieval, guideline navigation, coding, plan/chart checking, patient communication, and workflow orchestration. Readers need terminology and evidence standards that distinguish a language model, chatbot, search system, tool-using agent, and clinically integrated product.

Without this material, the book's terminology is incomplete and readers may overinterpret fluent output, benchmark scores, or demonstrations as reliable clinical reasoning.

## What Is Needed

1. Add novice-level explanations of tokenization, embeddings, pretraining, instruction tuning, context windows, prompting, inference, and the difference between discriminative NLP and generative language models.
2. Explain retrieval-augmented generation, citations and provenance, structured outputs, function/tool calling, memory, workflow agents, and deterministic guardrails.
3. Map radiotherapy use cases across documentation, information extraction, cohort discovery, guideline retrieval, plan/chart QA, patient-facing communication, and research workflows.
4. Cover hallucination, omission, prompt injection, data exfiltration, unreliable citations, knowledge cutoffs, model/version drift, overreliance, and the limits of verbalized confidence.
5. Teach task-appropriate evaluation: factuality, evidence attribution, extraction accuracy, calibration/abstention, clinical error severity, human editing burden, subgroup performance, and prospective human-AI outcomes.
6. Distinguish peer-reviewed clinical evidence from general-medical benchmarks, vendor claims, and radiation-oncology preprints; cross-link rather than duplicate VLM safety and evaluation content.

## Acceptance Criteria

- [ ] Readers can distinguish NLP, an LLM, a chatbot, RAG, tool use, an agent, and a VLM
- [ ] The generation and retrieval pipeline is illustrated from source document to reviewed clinical output
- [ ] At least four radiotherapy use cases are evaluated in terms of evidence maturity, failure modes, and required oversight
- [ ] Prompt injection, privacy leakage, fabricated attribution, version drift, and automation bias are addressed
- [ ] Evaluation includes source-grounded factuality and clinically weighted human-AI assessment, not only lexical similarity or preference
- [ ] Claims about clinical capability rely on verified evidence and preprints are clearly labeled
- [ ] Generic multimodal material is linked to `fundamentalAI/vlm.md` rather than duplicated
