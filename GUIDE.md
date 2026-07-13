# ART101 Content Guide

This is the canonical reference for how this repository is organized, what standard every chapter must meet, and — critically — the rules an autonomous agent must follow when it updates this book on a recurring basis. When in doubt about where content goes or whether a change is safe to make, consult this file first.

---

## Philosophy

ART101 ("AI in RadioTherapy 101") is a living textbook giving an overview of how AI is used and impacting the radiotherapy workflow today, published to [contouraid.github.io/art101](https://contouraid.github.io/art101/). It is not a project-status document or a product roadmap — it is a reference a clinician, physicist, or engineer reads to learn the field.

The intended reader is someone with a technical or clinical background who wants a structured, citable, up-to-date grounding in a specific sub-topic (contouring, registration, treatment planning, etc.) without having to survey the primary literature themselves.

**This repository is designed to be self-evolving.** Roughly monthly, an autonomous agent (Claude, run by the maintainer) reviews recent literature and updates the book. That agent has no memory of previous runs beyond what is written down here and in `todo/`. Every rule in this file exists to make that unattended process safe, auditable, and consistent with the style of content a human already wrote. **If a rule here seems overly strict, assume it exists because unattended edits are riskier than human edits, not because the topic is unimportant.**

---

## Structure

```
art101/
├── GUIDE.md                      # This document — organization and update rules
├── README.md                     # One-paragraph repo snapshot and link to the published book
├── .github/workflows/docs.yml    # Builds docs/ with Sphinx and deploys to GitHub Pages on push to main
│
├── docs/
│   ├── conf.py, requirements.txt, Makefile   # Sphinx book build (sphinx_book_theme + myst_parser)
│   ├── index.md                  # Book cover page, tool/course links, root toctree
│   ├── intro/intro.md                        # 1: Introduction
│   ├── fundamentalAI/index.md, llm.md, vlm.md # 2: Fundamentals of AI (+ language/agent and VLM sub-pages)
│   ├── fundamentalRO/fundamentalRO.md        # 3: Fundamentals of Radiation Oncology
│   ├── medicalImaging/medicalImaging.md      # 4: Medical Imaging in Radiation Oncology
│   ├── contouring/contouring.md              # 5: AI for Contouring
│   ├── registration/registration.md          # 6: AI in Image Registration and Fusion
│   ├── treatmentPlanning/treatmentPlanning.md# 7: AI for Treatment Planning
│   ├── clinicalPrediction/clinicalPrediction.md # 8: Clinical Prediction, Radiomics, and Causal Inference
│   ├── qa/qa.md                              # 9: AI for Quality Assurance and Safety
│   ├── validation/validation.md              # 10: Validation and Evaluation of AI Models
│   ├── workflow/workflow.md                  # 11: Integration of AI into Clinical Workflow
│   └── responsibleAI/responsibleAI.md        # 12: Responsible AI, Regulation, and Security
│
└── todo/                         # Open content gaps, completed archive, and review log
    └── done/                    # Completed todos retained as an audit trail
```

**Two governing rules apply everywhere:**
1. A topic lives in exactly one chapter. If another chapter needs it, link to the chapter — never duplicate the explanation.
2. The root level is navigation and process only: `README.md`, `GUIDE.md`, `todo/`. All book content lives under `docs/`.

---

## Chapter Content Standard

Every chapter file (`docs/<folder>/<name>.md`) must contain, in this order:

1. **Numbered title** matching `docs/index.md` (e.g., `# 5: AI for Contouring`).
2. **Body sections** using MyST Markdown headers (`##`, `###`). No manual "table of contents" block of hand-written `[text](#anchor)` links at the top of the file — see Rule 3 below for why this is forbidden, not just discouraged.
3. **`## Current Research and Recent Advances`** — the section the monthly literature-review process maintains. Each entry is one bullet or short paragraph, ends with a citation, and is tagged with the review cycle that added it: `_(added: 2026-07)_`. Never delete an entry here without moving its claim into the main body first or confirming (via a todo, see below) that it's been superseded.
4. **`## Knowledge Check`** — at least five formative questions spanning recall, interpretation, and application, each followed by a reasoned answer and a link to the relevant section. Explanations must identify why a plausible shortcut, alternative, or unsafe interpretation fails.
5. **`## Recap`** — a short summary paragraph.
6. **`## References`** — numbered list, one entry per source cited anywhere in the chapter, each with a resolvable Markdown link (DOI, PubMed, arXiv, or publisher link). Numbered in-text citations must also be clickable, using the visible form `[[1]](https://...)`; do not leave citation markers such as `[1]` or reference URLs as plain text.

A chapter that has only a title and no body is a **Critical** gap, not a Medium one. The original six-stub gap and its resolution are retained in `todo/done/p0-write-stub-chapters.md`.

### Cases and formative assessment

`docs/resources/cases.md` is the canonical record for the synthetic recurring cases and capstone. Chapter worked steps must link to that record rather than changing anatomy, identifiers, geometry, task, role ownership, or clinical context locally. All case content must say it is synthetic and educational, avoid patient-specific advice, expose missing or conflicting information rather than silently repair it, and identify the accountable decision maker and safe fallback.

At least two cases must recur across three or more chapters. Contouring and treatment planning must contain explicit worked-case sections. At least one case must show why a favorable aggregate metric, confidence score, or smooth output can coexist with poor clinical utility or safety. When a clinical parameter is included for realism, label it as part of the fixed synthetic record—not a recommendation.

Knowledge checks are formative, not certification. Questions should mix terminology, interpretation, calculation where appropriate, paper or claim critique, and clinical-safety application. Do not ask for trivia available only by memorizing a citation. Answers should state the reasoning, name the tempting but wrong alternative, and link back to the teaching section. The capstone must assess intended use, data, evidence, human factors, governance, and monitoring; its score never authorizes clinical use.

---

## Sourcing Rules for Autonomous Updates

These rules govern how the monthly agent finds and adds content. They exist to prevent two specific failure modes: citing a paper that doesn't exist, and adding content that reads as marketing rather than evidence.

1. **Primary search tools:** [Semantic Scholar](https://www.semanticscholar.org) (via its public API, `api.semanticscholar.org`, where available) and [Google Scholar](https://scholar.google.com). Use [arXiv](https://arxiv.org) and [PubMed](https://pubmed.ncbi.nlm.nih.gov) for direct source lookup once a candidate paper is identified.
2. **Search scope per chapter:** use the chapter's own section headers and the "Current Research" subsection titles as the query terms (e.g., for `contouring.md`: "deep learning organ at risk segmentation", "foundation model medical image segmentation radiotherapy"). Restrict to publications from the **last 18 months** relative to the review date, unless backfilling a chapter's foundational references.
3. **What counts as "really innovative" and worth adding:**
   - A new state-of-the-art result on a recognized benchmark or challenge (e.g., a segmentation challenge leaderboard).
   - A method that has been clinically validated (multi-institution, prospective, or retrospective clinical cohort), not just demonstrated on a public dataset.
   - A widely-cited survey or consensus/guideline paper that reframes the sub-field.
   - A new open dataset, open-source tool, or foundation model that changes what's practical to build (e.g., a segmentation foundation model, a new public RT dataset).
   - Evidence of adoption: FDA clearance, inclusion in a commercial TPS, or a professional-society guideline update (ASTRO, ESTRO, AAPM).
4. **What must NOT be added:**
   - A single preprint with no citations, no code, and no independent replication — note it in `todo/` instead of adding it to the book.
   - Vendor marketing material or unreviewed blog posts, except as an entry in `docs/index.md`'s "Open Source Software tools" or "Further reading" lists, which are explicitly link collections, not cited claims.
   - Any preprint added must be explicitly labeled `(preprint, not yet peer-reviewed)` in the citation.
5. **Verification is mandatory before citing.** A citation may only be added if the agent has confirmed — via the Semantic Scholar API, a resolvable DOI, or a live arXiv/PubMed page — that the paper exists and the resolvable link is included in `## References`. **Never fabricate a citation, author list, venue, or metric.** If a claim cannot be verified this way, do not add it to the chapter body; open or update a `todo/` file describing what needs checking instead.
6. **Prefer peer-reviewed venues** (IEEE TMI, Medical Physics, Red Journal/IJROBP, Radiotherapy & Oncology, MICCAI, and similar) over preprints when both exist for the same result.

---

## Research Synthesis and Evidence Maturity

The recency scan identifies candidates; it does not by itself establish the state of a field. The six AI application chapters—contouring, registration, treatment planning, clinical prediction, QA, and workflow—must maintain a compact `Evidence Synthesis` section before `Current Research and Recent Advances`. Vision-language models and language models retain task-specific maturity tables in their fundamental-AI pages; they link to the relevant application chapter rather than duplicating an application synthesis.

### Reproducible review protocol

For each application area, the reviewer must use and record this protocol:

1. **Fix the boundary before searching.** Record the review date, databases searched, date range, application tasks, populations, modalities, and intended clinical roles. The routine currency window is the last 18 months; older systematic reviews, consensus statements, benchmarks, and pivotal validation or negative studies may be included when needed to interpret maturity.
2. **Run query families, not one preferred phrase.** Combine the chapter's task and section terms with `radiotherapy` or a relevant disease/site and each of: method synonyms; `systematic review` or `consensus`; `benchmark`, `challenge`, `dataset`, or `code`; `external validation` or `multi-institution`; `prospective`, `silent`, `workflow`, or `human factors`; `clinical impact` or `patient outcome`; `negative`, `failure`, `bias`, `generalization`, or `distribution shift`; and `regulatory` or `adoption`. Search at least two discovery databases from the Sourcing Rules and verify included records against a primary publisher, DOI, PubMed, arXiv, regulator, standards body, or professional-society page.
3. **Apply explicit eligibility rules.** Include sources that define the field or materially change a maturity judgment: systematic reviews, consensus or reporting guidance, recognized benchmarks/challenges, verified open datasets or code, comparative validation, prospective studies, workflow/human-factors studies, clinical-impact studies, regulatory records, adoption studies, and informative negative or non-generalizing results. Exclude unverifiable records, marketing claims, duplicates, off-task populations or endpoints, papers outside the date window that add no foundational value, and isolated preprints without code or independent support. A preprint that is retained must be labeled as such.
4. **Deduplicate and verify.** Deduplicate by DOI or PMID first, then normalized title and study cohort. Link secondary analyses of the same cohort rather than counting them as independent validation. Verify title, authorship, venue, year, study design, population/site, scale, comparator, endpoint, and source URL before extraction.
5. **Extract comparable fields.** Every evidence table uses: task; population/site; data scale; validation design; comparator; endpoint; principal limitation; and maturity. Use `not reported` rather than guessing. Record whether data and code are open in the surrounding synthesis when that fact affects reproducibility.
6. **Use a reproducible stopping rule.** Stop only after every planned query family has been run, backward/forward checks of included reviews or consensus sources add no new eligible evidence, and two consecutive result pages per discovery database add no study that changes the synthesis or maturity rating. A search can stop earlier when the database reports no further results. Record the stopping reason.
7. **Keep the audit trail.** At the top of `todo/review-log.md`, record search dates, databases, exact query families, candidate counts when available, inclusion decisions, rejected sources with reasons, deduplication or cohort links, the stopping decision, and todos opened or closed. Chapter-specific literature-currency todos remain the search work queue; do not repeat their searches in a cross-cutting todo.

### Evidence-maturity vocabulary

Assign the highest level directly supported for the stated system, population, site, and endpoint. Do not promote a study because the underlying model or a different product is more mature.

| Label | Evidence required |
|---|---|
| **Proof of concept** | Technical feasibility on development data, a benchmark, simulation, phantom, or narrowly selected retrospective sample; no independent clinical validation. |
| **Internal retrospective validation** | A frozen method evaluated on held-out retrospective data from the development institution or an equivalent single-system setting. |
| **External/multi-institution validation** | Evaluation on meaningfully independent institutions, scanners, populations, or a multi-institution cohort, with transportability assessed rather than assumed. |
| **Silent prospective testing** | Prospectively collected cases processed in the intended workflow without the AI output changing care; failures and operational reliability are measured. |
| **Human-factors/workflow evaluation** | Intended users and interfaces are evaluated on endpoints such as time, edits, overrides, workload, trust, or consequential error in a representative workflow. |
| **Clinical impact** | Prospective comparative evidence shows an effect on clinical decisions, safety, quality of care, toxicity, disease control, survival, or another patient-relevant endpoint. |
| **Regulatory status** | A named product has a verified authorization or clearance for a specified jurisdiction, version, and intended use. This is a parallel status, not proof of superiority, local validity, or patient benefit. |
| **Routine adoption** | Representative usage evidence shows sustained use in ordinary practice, with the jurisdiction, denominator, workflow, and monitoring context stated. Adoption does not establish effectiveness. |

### Writing the synthesis

Each evidence synthesis must explicitly separate six questions: (1) model or component performance, (2) external validity, (3) effect on the human workflow, (4) patient outcome or clinical impact, (5) regulatory clearance for a named intended use, and (6) real-world adoption. A favorable geometric, accuracy, dose, or benchmark endpoint must not be described as workflow or patient benefit.

The prose around the table must state where evidence agrees, where methods, populations, comparators, or endpoints are heterogeneous, what the result means clinically, whether important data or code are open, and which questions remain unanswered. Include contradictory, null, harmful, or non-generalizing evidence when available; if none was found, say that the search found none rather than implying it does not exist. Build conclusions from the evidence set, prioritizing systematic reviews, consensus statements, benchmarks, prospective studies, and informative negative findings over isolated high-performing papers.

`Current Research and Recent Advances` remains the dated intake ledger. During each substantive review, compare its entries with the main body. When multiple entries support a stable conclusion, revise the durable `Evidence Synthesis` prose and table, but retain the dated entries as the audit history. If an entry is superseded or contradicted, add a dated update and explain the decision in `todo/review-log.md`; never erase the historical record silently.

---

## The Monthly Update Process

When the agent is run to update this book, it must, in order:

1. Read this file and `todo/README.md` in full before touching any chapter.
2. Work chapter by chapter. For each chapter with open literature-currency todos (see `todo/`), run the searches described in Sourcing Rules above.
3. Draft additions only to the `## Current Research and Recent Advances` section and `## References`, unless a `todo/` item explicitly calls for restructuring the body (e.g., the stub chapters, or the broken-anchor fix).
4. Never delete existing verified content. If new evidence contradicts something already written, add a dated note rather than silently rewriting history (`_(update, 2026-07): later work suggests X; original claim retained for context._`).
5. Update `todo/` per the lifecycle rules in `todo/README.md` — archive satisfied todos with completion notes under `todo/done/`, and open new ones for gaps discovered along the way.
6. Append one entry to `todo/review-log.md` summarizing: which chapters were reviewed, what search queries were run, what was added, what was rejected and why, and which todos were opened or closed. This is the audit trail — without it, the next run has no way to know what was already tried.
7. **Open a pull request; never push directly to `main`.** The PR description must list the todo filenames addressed and the sources consulted. A human reviews and merges. Once merged, `.github/workflows/docs.yml` rebuilds and republishes the site automatically — no manual deploy step is needed or should be taken.

---

## Rules

1. **One home per topic.** If content belongs conceptually to two chapters (e.g., vision-language models touch both `fundamentalAI` and `contouring`), it lives in the more fundamental chapter and the other links to it. Never duplicate an explanation across chapters.

2. **Root level is navigation and process only.** `README.md`, `GUIDE.md`, and `todo/` are the only permitted top-level content outside `docs/` and repository tooling (`.github/`, `.gitignore`).

3. **No hand-written GitHub-style TOC blocks inside chapters.** `sphinx_book_theme` already renders a full navigation sidebar from the document's actual headers. A manual `- [Title](#slug)` block duplicates that and can silently break under MyST's header-slug rules when a heading is renamed. The original 145-warning defect and its resolution are recorded in `todo/done/p1-fix-broken-toc-anchors.md`. If in-page navigation is wanted, use MyST's `{contents}` directive, which regenerates correctly.

4. **Every substantive chapter ends with `## Recap` and `## References`.** No exceptions once a chapter is out of stub state.

5. **No dates in filenames.** Use the `_(added: YYYY-MM)_` inline tag convention for recent-advances entries described above, and let git track file history otherwise.

6. **Cross-references use relative doc paths** (e.g., `../contouring/contouring.md`), never absolute filesystem paths or bare chapter numbers.

7. **Tool, course, and dataset links belong in `docs/index.md`**, under "Open Source Software tools" or "Further reading" — not repeated inside individual chapters.

8. **Chapters are authoritative, not aspirational.** Write what is established and cited, not what might be true or what a vendor claims. If evidence is thin, say so explicitly rather than smoothing it over.

9. **This file is the last word.** If a chapter's content or an update's scope is ambiguous, the answer is here. If this file doesn't resolve it, update this file (in its own reviewable change) before proceeding.

---

## What Is Missing

All known open content gaps are tracked as individual files directly under [`todo/`](todo/); completed work is retained under [`todo/done/`](todo/done/). See [`todo/README.md`](todo/README.md) for the current list and lifecycle rules, and [`todo/review-log.md`](todo/review-log.md) for the history of past autonomous review runs.

Do not maintain a gap list in this file. `todo/` is the single source of truth for open work.
