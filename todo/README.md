# TARA Content To-Do Tracker

This folder is the authoritative record of all known content gaps in this book — missing chapters, structural defects, and per-chapter literature-currency needs. Every item here represents work required to keep TARA complete, correct, and current, but not yet done.

**Do not use this folder for code bugs or build-tooling requests unrelated to book content.** Those belong in the repository's GitHub issue tracker. This folder tracks gaps in the *book itself* only.

This folder — together with [`../GUIDE.md`](../GUIDE.md) — is what makes the monthly autonomous literature-review process possible. The agent doing that review has no memory of prior runs; this folder and the review log are its only persistent state.

---

## How to Use This Folder

- **Open a new todo** when you identify a missing chapter section, a structural defect, or a literature-currency gap. Create a new file following the format below.
- **Close a todo** by deleting the file in the same pull request that adds the fix or content to the correct chapter. The PR description must reference the todo filename it resolves.
- **Update a todo** if scope or priority changes. Do not let todo files go stale — if a gap is no longer relevant, delete the file and note why in the PR description.
- **Review all todos** at the start of each monthly cycle, per the process in `GUIDE.md`.

---

## Filename Convention

```
p0-<slug>.md   Critical — a chapter has no real content, or the book fails to build
p1-<slug>.md   High     — a written chapter has a structural defect or missing required section
p2-<slug>.md   Medium   — chapter content is complete but literature is stale
p3-<slug>.md   Low      — polish: extra examples, diagrams, cross-links
```

`review-log.md` is a standing log, not a closeable todo — no priority prefix. It is appended to, never deleted.

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

---

## Priority Definitions

| Priority | Definition |
|---|---|
| **Critical** | A chapter promised by `docs/index.md` has no real content, or a defect breaks the published site. Resolve before the next monthly cycle completes. |
| **High** | A written chapter is missing a section required by `GUIDE.md` (Recent Advances / Recap / References), or has a verified structural defect. Target: next monthly cycle. |
| **Medium** | Chapter is structurally complete but its "Current Research and Recent Advances" section predates known developments in the sub-field. Target: addressed opportunistically as the monthly literature scan covers that chapter. |
| **Low** | Nice to have; improves clarity or navigation but blocks nothing. |

---

## Current Open Todos

Sorted by priority prefix (p0 → p3), then alphabetically within each tier.
`review-log.md` is a standing log, not a closeable todo — no priority prefix.
Last reconciled against the `tara` `main` branch on **2026-07-10**.

| File | Section | Priority | Status |
|---|---|---|---|
| [p0-write-stub-chapters.md](p0-write-stub-chapters.md) | `fundamentalRO/`, `registration/`, `qa/`, `validation/`, `workflow/`, `fundamentalAI/vlm.md` | P0 Critical | 🔴 Six chapters/sub-pages are title-only stubs |
| [p1-fix-broken-toc-anchors.md](p1-fix-broken-toc-anchors.md) | `intro/`, `fundamentalAI/`, `medicalImaging/`, `contouring/`, `treatmentPlanning/` | P1 High | 🔴 145 Sphinx build warnings from hand-written GitHub-style TOC blocks |
| [p2-literature-currency-intro.md](p2-literature-currency-intro.md) | `intro/` | P2 Medium | 🔴 No "Recent Advances" section yet |
| [p2-literature-currency-fundamentalAI.md](p2-literature-currency-fundamentalAI.md) | `fundamentalAI/` | P2 Medium | 🔴 No "Recent Advances" section yet |
| [p2-literature-currency-medicalImaging.md](p2-literature-currency-medicalImaging.md) | `medicalImaging/` | P2 Medium | 🔴 References are general, not RT-AI-specific or recent |
| [p2-literature-currency-contouring.md](p2-literature-currency-contouring.md) | `contouring/` | P2 Medium | 🔴 No coverage of foundation-model-based segmentation |
| [p2-literature-currency-treatmentPlanning.md](p2-literature-currency-treatmentPlanning.md) | `treatmentPlanning/` | P2 Medium | 🔴 No coverage of diffusion-model dose prediction or LLM-assisted planning |
