# TODO: Fix Broken TOC Anchor Links

**Section:** `intro/`, `fundamentalAI/`, `medicalImaging/`, `contouring/`, `treatmentPlanning/`
**Priority:** High
**Owner:** (unassigned)
**Opened:** 2026-07-10

## Gap

All five currently-written chapters open with a hand-written, GitHub-flavored-Markdown table of contents: a nested bullet list of `[Section Title](#section-slug)` links placed directly under the chapter title. This pattern does not resolve under MyST/Sphinx's own header-slug rules, and building the book with `sphinx-build` currently produces **145 `myst.xref_missing` warnings**, distributed as:

| File | Warnings |
|---|---|
| `fundamentalAI/index.md` | 55 |
| `medicalImaging/medicalImaging.md` | 25 |
| `intro/intro.md` | 24 |
| `contouring/contouring.md` | 23 |
| `treatmentPlanning/treatmentPlanning.md` | 18 |

Every one of these links is dead in the built HTML — clicking them does nothing, since the anchors MyST generates don't match GitHub's slugification (e.g., duplicate headers like "Clinical Uses in Radiation Oncology" get suffixed `-1`, `-2`, etc. by GitHub's renderer but not necessarily the same way by MyST). This is also pure duplication: `sphinx_book_theme` already renders a complete, correctly-linked navigation sidebar from the same headers, so the hand-written block adds no value even when it does resolve — it's a leftover from content that was drafted for a plain GitHub Markdown viewer, not for this Sphinx build.

## What Is Needed

1. Remove the hand-written TOC bullet-list block from the top of each of the five files listed above.
2. If in-page (not sidebar) navigation is desired, replace it with MyST's `{contents}` directive, which regenerates correctly from actual headers and can't go stale.
3. Rebuild with `sphinx-build -b html docs docs/_build/html` and confirm the warning count drops from 145 to (ideally) 0 for this class of warning.
4. Add the rule already stated in `GUIDE.md` Rule 3 to any chapter-writing checklist used going forward, so new chapters (see `p0-write-stub-chapters.md`) don't reintroduce this pattern.

## Acceptance Criteria

- [ ] Zero `myst.xref_missing` warnings referencing hand-written anchor links in a clean `sphinx-build` run
- [ ] No chapter contains a hand-written `- [Text](#slug)` navigation block
- [ ] The GitHub Actions docs workflow (`.github/workflows/docs.yml`) run for the fixing PR completes with a visibly lower warning count in the build log
