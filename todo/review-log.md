# Literature Review Log

This is a standing log of every monthly autonomous review cycle. It is append-only — never delete or rewrite a past entry. Its purpose is to give the next review cycle (which starts with no memory of this one) a record of what was searched, what was found, what was rejected, and why, so work isn't repeated and rejected sources aren't re-proposed without new evidence.

Append one entry per cycle, in the format below, at the **top** of the log (newest first).

```markdown
## <YYYY-MM-DD> review

**Chapters reviewed:** <list>
**Todos closed:** <list, or "none">
**Todos opened:** <list, or "none">

### Searches run
- <chapter>: "<query>" (Semantic Scholar / Google Scholar / arXiv / PubMed) — <N candidates found>

### Added
- <chapter>: <one-line description of what was added, with citation>

### Rejected
- <candidate paper/claim>: <reason — e.g., "single preprint, no citations, no code">

### Notes for next cycle
- <anything the next run should know — e.g., a search that returned nothing useful, an ambiguity that needs a human call>
```

---

## Log

No review cycles have run yet. This repository was set up for autonomous literature-tracking on 2026-07-10 — see `../GUIDE.md` for the process and `README.md` for open todos. The first cycle should start with `p0-write-stub-chapters.md` and `p1-fix-broken-toc-anchors.md`, since both block the "Current Research" mechanism the later P2 literature-currency todos depend on.
