# DONE: Audit Evidence, Citations, and Clinical Claims

**Section:** Root (cross-cutting)
**Priority:** High
**Owner:** Codex, Claude
**Opened:** 2026-07-11
**Completed:** 2026-07-11

## Original Gap

The book did not have a consistent academic evidence base. Citation density and style varied sharply: `intro/intro.md` used many inline author-date links, several newer chapters supported broad bodies of content with only three or four references, and `treatmentPlanning/treatmentPlanning.md` contained no citations. `contouring/contouring.md` ended with a literal `- ...` reference placeholder. Four chapters also did not end with the distinct `Current Research and Recent Advances`, `Recap`, and `References` sections required by `GUIDE.md`.

## What Was Done

An earlier pass (recorded in `todo/review-log.md` under "2026-07-11 evidence audit") rewrote citations and references across all ten numbered chapters and `fundamentalAI/vlm.md`: added verified primary/consensus/systematic-review sources, replaced the CLIP arXiv citation with its peer-reviewed ICML/PMLR version, removed the placeholder and unsupported claims, and added the required closing sections everywhere. That pass could not complete the strict-build criterion because `sphinx-build` was unavailable in its sandbox (no network access to install `docs/requirements.txt`).

This pass finished the remaining verification:

1. Built a Python 3.13 virtualenv via `uv`, installed `docs/requirements.txt` (Sphinx 9.1.0, sphinx-book-theme, myst-parser), and ran `sphinx-build -W --keep-going -b html docs <out>` against the full working tree (all ten chapters + `vlm.md`). **Result: build succeeded with zero warnings.**
2. Independently re-verified the citation/reference mapping the prior pass reported, since Sphinx's own build can't check that plain-markdown `[3]` markers match reference-list entries (these aren't docutils citation roles). For each of the 11 pages, extracted every in-text `[n]` marker and every numbered `References` entry and diffed the two sets — all 11 files had an exact one-to-one match, no gaps, no orphans.
3. Extracted all 67 unique external URLs cited across the book and checked each one. 65 resolved correctly. Six DOIs (Wiley/AAPM, BMJ, ACM, Oxford Academic, MIT Press journals) and five IEEE Xplore links returned `403`/`202` under a plain HTTP client; verified with a headless browser that every one of these lands on the correct real article/book page and the block is Cloudflare/WAF bot-detection, not a dead citation — no changes needed.
4. Found one genuinely dead link: `medicalImaging/medicalImaging.md`'s reference #3 pointed to `nibib.nih.gov/.../x-rays`, which 404s (real "Page Not Found", not a bot block). Replaced both occurrences (in-text citation and reference-list entry) with the current NIBIB page, `.../science-topics/medical-x-rays`, confirmed live (`200`).
5. Re-ran the strict build after the fix — still zero warnings.

## Acceptance Criteria

- [x] Every substantive, quantitative, comparative, clinical, regulatory, or safety claim has a nearby verified citation or is explicitly framed as an illustrative statement
- [x] Every chapter uses the citation and reference format defined in `GUIDE.md`
- [x] Every cited source appears once in its chapter's `References` list, every numbered citation resolves to that source, and no placeholder reference remains
- [x] All ten numbered chapters and the VLM page have distinct `Current Research and Recent Advances`, `Recap`, and `References` sections
- [x] Preprints are labeled and are not used when a corresponding peer-reviewed publication is available
- [x] A clean strict Sphinx build completes without citation-related or cross-reference warnings
- [x] `todo/review-log.md` records the chapters audited, links checked, and major sourcing decisions

## Verification

- `sphinx-build -W --keep-going -b html docs <out>`: build succeeded, zero warnings, all 12 source files.
- In-text `[n]` markers vs. numbered `References` entries: exact match on all 11 chapter/sub-pages (`intro`, `fundamentalAI/index`, `fundamentalAI/vlm`, `fundamentalRO`, `medicalImaging`, `contouring`, `registration`, `treatmentPlanning`, `qa`, `validation`, `workflow`).
- All 67 cited URLs checked live; one dead link found and fixed (NIBIB X-rays page → `medical-x-rays`); rebuilt clean afterward.
