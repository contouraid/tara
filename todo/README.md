# ART101 Content To-Do Tracker

This folder is the authoritative record of content work for this book. Files directly under `todo/` are open gaps; completed work is retained under `todo/done/` as an audit trail.

**Do not use this folder for code bugs or build-tooling requests unrelated to book content.** Those belong in the repository's GitHub issue tracker. This folder tracks gaps in the *book itself* only.

This folder — together with [`../GUIDE.md`](../GUIDE.md) — is what makes the monthly autonomous literature-review process possible. The agent doing that review has no memory of prior runs; this folder and the review log are its only persistent state.

---

## How to Use This Folder

- **Open a new todo** when you identify a missing chapter section, a structural defect, or a literature-currency gap. Create a new file following the format below.
- **Complete a todo** by updating it with a `**Completed:** <YYYY-MM-DD>` field, a concise `## What Was Done` section, checked acceptance criteria, and verification notes. Then move it to `todo/done/` in the same pull request as the completed work. Do not delete completed todos.
- **Update an open todo** if scope or priority changes. Do not let todo files go stale. If a gap is no longer relevant, explain why in the file, mark it completed, and archive it under `todo/done/`.
- **Review all todos** at the start of each monthly cycle, per the process in `GUIDE.md`.

---

## Filename Convention

```
p0-<slug>.md   Critical — a chapter has no real content, or the book fails to build
p1-<slug>.md   High     — a written chapter has a structural defect or missing required section
p2-<slug>.md   Medium   — chapter content is complete but literature is stale
p3-<slug>.md   Low      — polish: extra examples, diagrams, cross-links
```

`review-log.md` is a standing log, not a closeable todo — no priority prefix. It is appended to, never deleted. The `done/` directory contains completed todos using their original filenames.

---

## Todo File Format

Every file in this folder must follow this exact format. Filename must begin with the priority prefix followed by a short kebab-case slug (e.g., `p1-fix-broken-toc-anchors.md`).

```markdown
# TODO: <Title>

**Section:** <docs/ chapter folder this belongs to, or "Root (cross-cutting)">
**Priority:** <Critical | High | Medium | Low>
**Owner:** <name or "(unassigned)">
**Opened:** <YYYY-MM-DD>

## Gap

One to three paragraphs describing what is missing and why it matters. Be specific about
the consequence — what a reader can't learn, what the book claims to cover but doesn't,
or what breaks in the build.

## What Is Needed

A numbered or bulleted list of the specific content, sections, or fixes required to close
the gap. Each item should be concrete enough that the monthly review agent — or a human
contributor — can act on it without further clarification. For literature-currency todos,
list the search queries to run per the Sourcing Rules in `GUIDE.md`.

## Acceptance Criteria

A checklist of conditions that must be true for this todo to be considered closed.
Each criterion should be objectively verifiable.

- [ ] Criterion one
- [ ] Criterion two
```

When the work is complete, change the title prefix from `TODO` to `DONE`, add `**Completed:**`, document the implementation and verification, check the satisfied criteria, and move the file to `todo/done/`.

---

## Priority Definitions

| Priority | Definition |
|---|---|
| **Critical** | A chapter promised by `docs/index.md` has no real content, or a defect breaks the published site. Resolve before the next monthly cycle completes. |
| **High** | A written chapter is missing a required section, an essential prerequisite or major promised topic is absent, or the book has a verified structural or evidence-integrity defect. Target: next monthly cycle. |
| **Medium** | A chapter is structurally complete but its literature is stale, or a cross-cutting evidence-synthesis improvement is needed. Target: addressed opportunistically as the monthly literature scan covers that chapter. |
| **Low** | Nice to have; improves clarity or navigation but blocks nothing. |

---

## Current Open Todos

Sorted by priority prefix (p0 → p3), then alphabetically within each tier.
`review-log.md` is a standing log, not a closeable todo — no priority prefix.
Last reconciled against the working tree on **2026-07-12** (research-synthesis-and-evidence-grading closure).

| File | Section | Priority | Status |
|---|---|---|---|
| [p2-literature-currency-contouring.md](p2-literature-currency-contouring.md) | `contouring/` | P2 Medium | 🔴 No coverage of foundation-model-based segmentation |
| [p2-literature-currency-fundamentalAI.md](p2-literature-currency-fundamentalAI.md) | `fundamentalAI/` | P2 Medium | 🔴 No "Recent Advances" section yet |
| [p2-literature-currency-fundamentalRO.md](p2-literature-currency-fundamentalRO.md) | `fundamentalRO/` | P2 Medium | 🔴 Initial chapter needs a current adaptive and biology-guided literature review |
| [p2-literature-currency-intro.md](p2-literature-currency-intro.md) | `intro/` | P2 Medium | 🔴 No "Recent Advances" section yet |
| [p2-literature-currency-medicalImaging.md](p2-literature-currency-medicalImaging.md) | `medicalImaging/` | P2 Medium | 🔴 References are general, not RT-AI-specific or recent |
| [p2-literature-currency-qa.md](p2-literature-currency-qa.md) | `qa/` | P2 Medium | 🔴 Initial chapter needs current fault-detection and regulatory evidence |
| [p2-literature-currency-registration.md](p2-literature-currency-registration.md) | `registration/` | P2 Medium | 🔴 Initial chapter needs current learning-based clinical validation evidence |
| [p2-literature-currency-treatmentPlanning.md](p2-literature-currency-treatmentPlanning.md) | `treatmentPlanning/` | P2 Medium | 🔴 No coverage of diffusion-model dose prediction or LLM-assisted planning |
| [p2-literature-currency-validation.md](p2-literature-currency-validation.md) | `validation/` | P2 Medium | 🔴 Initial chapter needs ongoing standards and monitoring review |
| [p2-literature-currency-vlm.md](p2-literature-currency-vlm.md) | `fundamentalAI/vlm.md` | P2 Medium | 🔴 Fast-moving VLM evidence needs a dedicated currency review |
| [p2-literature-currency-workflow.md](p2-literature-currency-workflow.md) | `workflow/` | P2 Medium | 🔴 Initial chapter needs current real-world implementation evidence |
| [p3-add-worked-cases-and-formative-assessment.md](p3-add-worked-cases-and-formative-assessment.md) | Root (cross-cutting) | P3 Low | 🔴 Few worked cases or opportunities to test applied understanding |

## Completed Todos

Completed work is retained in [`done/`](done/). The archive currently includes:

- [p0-write-stub-chapters.md](done/p0-write-stub-chapters.md)
- [p1-add-radiotherapy-data-and-informatics-foundations.md](done/p1-add-radiotherapy-data-and-informatics-foundations.md)
- [p1-audit-evidence-citations-and-claims.md](done/p1-audit-evidence-citations-and-claims.md)
- [p1-cover-clinical-prediction-radiomics-and-causal-inference.md](done/p1-cover-clinical-prediction-radiomics-and-causal-inference.md)
- [p1-cover-language-models-generative-ai-and-agents.md](done/p1-cover-language-models-generative-ai-and-agents.md)
- [p1-consolidate-responsible-ai-regulation-and-security.md](done/p1-consolidate-responsible-ai-regulation-and-security.md)
- [p1-establish-novice-learning-architecture.md](done/p1-establish-novice-learning-architecture.md)
- [p1-fix-broken-toc-anchors.md](done/p1-fix-broken-toc-anchors.md)
- [p1-strengthen-radiotherapy-clinical-foundations.md](done/p1-strengthen-radiotherapy-clinical-foundations.md)
- [p2-establish-research-synthesis-and-evidence-grading.md](done/p2-establish-research-synthesis-and-evidence-grading.md)
