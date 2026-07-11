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
│   ├── fundamentalAI/index.md, vlm.md        # 2: Fundamentals of AI through Deep Learning (+ VLM sub-page)
│   ├── fundamentalRO/fundamentalRO.md        # 3: Fundamentals of Radiation Oncology
│   ├── medicalImaging/medicalImaging.md      # 4: Medical Imaging in Radiation Oncology
│   ├── contouring/contouring.md              # 5: AI for Contouring
│   ├── registration/registration.md          # 6: AI in Image Registration and Fusion
│   ├── treatmentPlanning/treatmentPlanning.md# 7: AI for Treatment Planning
│   ├── qa/qa.md                              # 8: AI for Quality Assurance and Safety
│   ├── validation/validation.md              # 9: Validation and Evaluation of AI Models
│   ├── workflow/workflow.md                  # 10: Integration of AI into Clinical Workflow
│   └── responsibleAI/responsibleAI.md        # 11: Responsible AI, Regulation, and Security
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
4. **`## Recap`** — a short summary paragraph.
5. **`## References`** — numbered list, one entry per source cited anywhere in the chapter, each with a resolvable Markdown link (DOI, PubMed, arXiv, or publisher link). Numbered in-text citations must also be clickable, using the visible form `[[1]](https://...)`; do not leave citation markers such as `[1]` or reference URLs as plain text.

A chapter that has only a title and no body is a **Critical** gap, not a Medium one. The original six-stub gap and its resolution are retained in `todo/done/p0-write-stub-chapters.md`.

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
