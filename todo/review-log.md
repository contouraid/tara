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

## 2026-07-12 research-synthesis-and-evidence-grading closure

**Chapters reviewed:** `contouring/`, `registration/`, `treatmentPlanning/`, `clinicalPrediction/`, `qa/`, and `workflow/`
**Todos closed:** `p2-establish-research-synthesis-and-evidence-grading.md` (moved to `todo/done/`)
**Todos opened:** none

### Searches run
- scope and existing evidence: chapter-by-chapter searches for `Current Research and Recent Advances`, application evidence claims, table fields, maturity terms, limitations, and reference records across all six source files — all currently cited synthesis candidates reviewed.
- contouring: `"Assessment of manual adjustment" patients Brouwer 2020`, exact-title/DOI checks for the contour-editing study, and `MedSAM modalities image-mask pairs` (PubMed Central / publisher / DOI) — two table studies included; metric-consensus guidance retained as context.
- registration: `Seq2Morph planning CT weekly CBCT radiotherapy`, `4D-CT deformable image registration unsupervised recursive cascaded patients`, and exact PMID checks (PubMed) — three table studies included.
- treatment planning: `OpenKBP 340 patients challenge`, `Beam field guided diffusion model liver cancer dose prediction patients dataset`, and exact DOI checks (publisher / DOI) — two table studies included; adaptive-planning review retained as context.
- clinical prediction: `Decoding tumour phenotype 1019 patients seven cohorts`, `IBSI standardized radiomics 169 features 51 patients`, and exact DOI checks (PubMed Central / publisher / DOI) — three table studies included.
- QA: `Understanding machine learning classifier decisions automated radiotherapy QA dataset` and exact PMID checks (PubMed) — one system study included; TG-218 and FDA change-control guidance retained as context.
- workflow: exact-title and DOI checks for `Adoption of AI-driven automation and adaptive radiotherapy national survey Italy departments 2026`, plus WHO readiness/governance source checks (PubMed / WHO / DOI) — one adoption study included; two WHO reports retained as context.

### Added
- `GUIDE.md`: reproducible search, selection, deduplication, verification, extraction, stopping, audit, maturity-grading, and durable-synthesis rules.
- all six application chapters: a common eight-field evidence table and durable synthesis distinguishing performance, external validity, workflow, outcomes, regulatory status, and adoption.
- contouring and QA: corrected the verified bibliographic record for the Brouwer contour-editing study and Chen et al. explainable-QA study, respectively.

### Rejected
- FDA predetermined-change-control-plan guidance was not graded as `Regulatory status`: it is a framework, not authorization of a named product for a specified intended use.
- WHO readiness and ethics reports, TG-218, metric-selection consensus, and the adaptive-planning narrative review were not assigned system maturity labels: they inform interpretation but do not validate a specific application system at that level.
- The BeamDiff patient count was not inferred because it was not reported in the accessible abstract; the table records that limitation instead of guessing.
- Search results for unrelated CBCT dose calculation, newer uncited planning or QA models, vendor pages, patents, secondary books, and preprints were not added because this closure synthesized the verified in-book evidence set; new literature belongs to the open chapter-specific currency todos.
- No duplicate cohorts were counted as independent validations in the table rows.

### Notes for next cycle
- Stopping rule for this cross-cutting closure: every application chapter and every source already cited in its durable/recent synthesis was reviewed, exact bibliographic uncertainties were resolved where possible, and no unresolved item changed a maturity rating. No broad currency search was run, to avoid duplicating the open chapter-specific todos.
- Future currency cycles must run the new query families and saturation rule, record rejected and cohort-linked studies, and promote stable conclusions into `Evidence Synthesis` without deleting dated recent-advances entries.

## 2026-07-12 radiotherapy-clinical-foundations closure

**Chapters reviewed:** `fundamentalRO/`
**Todos closed:** `p1-strengthen-radiotherapy-clinical-foundations.md` (moved to `todo/done/`)
**Todos opened:** none

### Searches run
- clinical pathway and team: "radiotherapy process of care clinical team safety" (ASTRO and IAEA) — multidisciplinary pathway, roles, handoffs, and programme requirements verified.
- terminology and prescription: "ICRU target volumes prescription reporting photon IMRT stereotactic" (ICRU Reports 50, 83, and 91) — GTV/CTV/PTV, IMRT reporting, and stereotactic concepts verified.
- modalities: "NCI external beam radiation photon electron proton stereotactic", "IAEA brachytherapy dosimetry", and "IAEA radiopharmaceutical therapy dosimetry" — modality purpose, limitations, and distinct dosimetry pathways verified.
- motion, calculation, and verification: "AAPM TG-76 respiratory motion", "IAEA treatment planning commissioning", and "AAPM TG-219 independent dose verification" — motion strategies, TPS commissioning, and independent-check principles verified.
- uncertainty and safety: "IAEA accuracy requirements uncertainties radiotherapy" and "AAPM TG-100 risk analysis" — uncertainty classes and risk-based quality-management framework verified.
- toxicity and follow-up: "NCI radiation therapy side effects" — stable organ-specific patient guidance verified.

### Added
- fundamentalRO: complete consultation-to-survivorship pathway; intent/prescription/fractionation distinctions; modality comparisons; simulation, motion, planning, verification, IGRT, adaptation, toxicity, follow-up, and uncertainty foundations.
- fundamentalRO: jurisdiction-aware team and handoff map plus an eight-row AI clinical-accountability matrix tying every task to its decision, professional owner, failure consequence, and independent controls.
- fundamentalRO: 14 new authoritative references, bringing the chapter total to 17 while preserving the separate recent-research section.

### Rejected
- Vendor descriptions and institution-specific role assignments were not used for stable clinical foundations.
- Technique-specific outcome superiority was not inferred from favorable dosimetry or modality physics alone.
- Fast-moving research claims were not added to the foundational body; the existing `p2-literature-currency-fundamentalRO.md` remains the home for the dedicated recent-literature cycle.

### Notes for next cycle
- Chapter 3 is now the canonical clinical mental model for later application chapters; downstream content should link rather than re-explain the full pathway or role map.
- Clean strict Sphinx build completed with zero warnings; all 17 citation numbers and URLs matched the reference list.

## 2026-07-12 language-model and agent closure

**Chapters reviewed:** `fundamentalAI/` (new `llm.md`, plus `index.md` and `vlm.md` cross-links), `qa/`, and `workflow/`
**Todos closed:** `p1-cover-language-models-generative-ai-and-agents.md` (moved to `todo/done/`)
**Todos opened:** none

### Searches run
- language-model foundations: "BERT pretraining", "instruction tuning human feedback", "retrieval augmented generation", and "Toolformer" (ACL and NeurIPS primary pages) — discriminative, generative, RAG, and tool-use foundations verified.
- security: "indirect prompt injection LLM-integrated applications" (ACM AISec) — peer-reviewed attack model and DOI verified.
- healthcare evaluation: "large language models clinical knowledge" and "testing evaluation healthcare LLM systematic review" (Nature and JAMA) — benchmark limitations and the 519-study evidence map verified.
- radiation oncology: "LLM radiation oncology patient care questions" and "LLM ACR radiation oncology examination" (JAMA Network Open and AI in Precision Oncology) — peer-reviewed task-specific results and limitations verified.
- attribution: "fabricated citations ChatGPT" (Scientific Reports) — peer-reviewed reference-fabrication analysis verified.

### Added
- fundamentalAI/llm: canonical novice-level language-model, RAG, tool-use, and agent foundations; a source-to-reviewed-output pipeline; radiotherapy use-case maturity table; security and human-factors controls; and clinically weighted evaluation with 11 verified sources.
- fundamentalAI index and VLM: sibling navigation and explicit canonical boundaries between text-only and multimodal content.
- QA and workflow: links from chart checking, drafting, and automation to the language-model chapter's source, permission, validation, and review controls.

### Rejected
- Vendor claims and general chatbot demonstrations were not treated as evidence of radiation-oncology clinical capability.
- Unpublished radiation-oncology preprints were not used to support clinical claims; peer-reviewed task-specific evidence was available for the claims retained.
- Examination and question-answer scores were not described as evidence of clinical competence, autonomous use, or patient benefit.

### Notes for next cycle
- `fundamentalAI/llm.md` is the canonical home for text-only LLMs, RAG, tools, and agents; `fundamentalAI/vlm.md` remains canonical for visual-language architectures, volumetric inputs, grounding, and image-specific evaluation.
- Clean strict Sphinx build completed with zero warnings; citation numbering and links were reconciled separately.

## 2026-07-12 clinical-prediction closure

**Chapters reviewed:** new `clinicalPrediction/` chapter plus cross-links in `fundamentalRO/`, `medicalImaging/`, `treatmentPlanning/`, and `validation/`
**Todos closed:** `p1-cover-clinical-prediction-radiomics-and-causal-inference.md` (moved to `todo/done/`)
**Todos opened:** none

### Searches run
- radiomics standards: "Image Biomarker Standardisation Initiative radiomics standardized feature calculation" (RSNA, PubMed, and IBSI) — consensus definitions, reference values, and publication metadata verified.
- radiomics evidence: "Aerts radiomics lung head neck validation" and "Welch vulnerabilities radiomic signature tumor volume" (Nature, PubMed, and publisher pages) — influential external-validation result and later safeguard analysis verified.
- longitudinal and outcome modeling: "delta-radiomics NSCLC outcomes", "Fine Gray competing risk", "decision curve analysis", and "QUANTEC NTCP" (PubMed and publisher pages) — representative methods and radiotherapy applications verified.
- causal inference and reporting: "target trial Hernán Robins", "TRIPOD+AI", and "PROBAST+AI" (PubMed and BMJ) — target-trial framework and current prediction-study guidance verified.

### Added
- clinicalPrediction: canonical novice-oriented chapter covering clinical endpoints, survival and competing-risk outcomes, TCP/NTCP, radiomics/dosiomics, deep and longitudinal biomarkers, multimodal models, calibration, decision utility, causal interpretation, and prospective impact, with ten verified references.
- clinicalPrediction: worked xerostomia-risk example from endpoint definition through frozen external validation and decision analysis, followed by a counterexample explaining why modality selection requires comparative causal evidence.
- index and related chapters: new Chapter 8 navigation, renumbered later chapters, and links from radiobiology, imaging, planning, and validation.
- site configuration: removed the redundant theme-generated author footer line while retaining copyright and licensing attribution.

### Rejected
- Association-only radiomics results were not presented as evidence for dose escalation, de-escalation, modality selection, or treatment benefit.
- Preprints and secondary summaries were not used where peer-reviewed primary studies, standards, or reporting guidance were available.

### Notes for next cycle
- Chapter 8 is the single canonical home for outcome prediction, radiomics/dosiomics, and prediction-versus-causality concepts; other chapters should link rather than duplicate it.
- Strict Sphinx build completed with zero warnings, and the generated footer retained copyright while omitting the separate author line.

## 2026-07-11 responsible-AI closure

**Chapters reviewed:** new `responsibleAI/` chapter plus cross-links in `fundamentalAI/vlm.md`, `qa/`, `validation/`, and `workflow/`
**Todos closed:** `p1-consolidate-responsible-ai-regulation-and-security.md` (moved to `todo/done/`)
**Todos opened:** none

### Searches run
- US regulation: "HIPAA Security Rule compliance date" (HHS primary pages) — Security Rule effective and compliance dates verified.
- US FDA guidance: "predetermined change control plan final guidance artificial intelligence-enabled device software functions" (FDA primary pages) — current final-guidance status and August 2025 update verified.

### Added
- responsibleAI: a canonical novice-accessible treatment of obligation types, the full AI lifecycle, regulation and privacy by jurisdiction, fairness, transparency, cybersecurity, third-party risk, governance checklist, and RACI responsibility map with 14 sources.
- QA, validation, VLM, and workflow: stable Sphinx-native cross-references to the canonical governance, regulatory, fairness, and security sections.

### Rejected
- File-plus-fragment Markdown links were not retained for cross-document section references because MyST did not resolve generated heading fragments with `heading_anchors=0`; explicit labels and `{ref}` roles were used instead.

### Notes for next cycle
- Clean strict build `../.venv/bin/sphinx-build -b html -W -n . _build/strict`: **zero warnings**, all 14 source files.
- Regulatory summaries remain orientation rather than legal advice. Recheck jurisdiction, effective date, and primary regulator status before relying on them in future cycles.

## 2026-07-11 strict-build closure

**Chapters reviewed:** all ten numbered chapters, `fundamentalAI/vlm.md` (verification pass only, no content rewrites)
**Todos closed:** `p1-audit-evidence-citations-and-claims.md` (moved to `todo/done/`)
**Todos opened:** none

### Searches run
- None — this cycle verified the prior "2026-07-11 evidence audit" cycle's claims rather than sourcing new content. No new literature search was performed.

### Added
- medicalImaging: fixed one dead citation URL (NIBIB's `.../science-topics/x-rays` now 404s on NIH's own site) by pointing both the in-text citation and reference-list entry to the current `.../science-topics/medical-x-rays` page (verified live, `200`).

### Rejected
- N/A — no new content proposed this cycle.

### Notes for next cycle
- Ran `sphinx-build -W --keep-going -b html docs <out>` (the build the prior cycle couldn't run in its sandbox) via a `uv`-managed Python 3.13 venv with `docs/requirements.txt` installed: **zero warnings**, all 12 source files.
- Independently cross-checked in-text `[n]` markers against each chapter's numbered `References` list (Sphinx doesn't validate this — these are plain Markdown links, not docutils citation roles). All 11 pages had an exact one-to-one match.
- Live-checked all 67 unique URLs cited across the book. Several Wiley/AAPM, BMJ, ACM, Oxford Academic, MIT Press, and IEEE Xplore DOIs return `403`/`202` to a plain HTTP client — verified with a headless browser that these are Cloudflare/WAF bot-challenges, not dead links; each resolves to the correct article/book page for a human visitor. Only the NIBIB link above was genuinely dead.
- If a future cycle re-runs a link check and hits `403`/`202` on a DOI, don't treat that as broken by default — confirm with a real browser first, since major publishers block scripted clients.

## 2026-07-11 evidence audit

**Chapters reviewed:** `intro/`, `fundamentalAI/` (including `vlm.md`), `fundamentalRO/`, `medicalImaging/`, `contouring/`, `registration/`, `treatmentPlanning/`, `qa/`, `validation/`, `workflow/`
**Todos closed:** none (`p1-audit-evidence-citations-and-claims.md` remains open pending a strict Sphinx build)
**Todos opened:** none

### Searches run
- contouring: "U-Net biomedical image segmentation", "V-Net volumetric medical image segmentation", "Metrics Reloaded image analysis validation", and "Segment Anything in Medical Images" (DOI/Crossref metadata) — canonical architecture, evaluation, clinical-editing, and foundation-model sources checked
- treatmentPlanning: "OpenKBP dose prediction challenge", "predicting dose-volume histograms knowledge-based planning", "automation IMRT treatment planning review", "multiobjective radiotherapy Pareto", and "diffusion model radiotherapy dose prediction" (DOI/Crossref metadata) — foundational KBP/MCO sources and one 2025 peer-reviewed diffusion study checked
- cross-cutting: DOI, publisher, PMLR, WHO, FDA, DICOM, TCIA, and PubMed links used by all 11 pages were reconciled against each chapter's numbered reference list on 2026-07-11

### Added
- intro: replaced a duplicated author-date link collection with an evidence-led introduction distinguishing technical performance, clinical validity, utility, and lifecycle safety; added 12 verified numbered sources.
- fundamentalAI: added primary citations for the perceptron, backpropagation, initialization, batch normalization, CNNs, LSTM, GANs, transformers, U-Net, and nnU-Net; added the required closing sections.
- contouring: removed the literal placeholder reference, qualified overlap and clinical-acceptability claims, and added seven primary, systematic-review, or validation sources.
- treatmentPlanning: removed the unsupported universal dose-error claim, distinguished prediction from calculation and deliverability, qualified KBP/MCO/outcome claims, and added seven verified sources.
- medicalImaging and VLM: added the missing recent-advances structure, removed indirect general-imaging links, reconciled dataset citation URLs, and replaced the CLIP arXiv link with its peer-reviewed ICML/PMLR version.

### Rejected
- Legacy introduction links that pointed to direct PDFs, secondary summaries, mislabeled papers, or unreviewed RO-LMM/ROND preprints were removed rather than carried into the normalized reference list.
- A universal claim that dose-prediction models achieve less than 5% prescription-dose error was removed because normalization, evaluated region, beam inputs, dataset, and aggregation differ between studies.
- Benchmark performance was not presented as evidence of clinical benefit; benchmark-only, retrospective, and transfer claims are labeled in the revised prose.

### Notes for next cycle
- A mechanical audit found sequential reference numbering on every page, one-to-one citation/reference URL mappings, no orphaned references, and all three required closing headings on all ten chapters plus `vlm.md`.
- `sphinx-build -W --keep-going -b html docs /tmp/tara-sphinx-evidence-audit` could not run because Sphinx is not installed. Installing `docs/requirements.txt` in a temporary virtual environment failed under restricted DNS; the required elevated network request was then denied because the environment reported its current usage limit. Run the strict build once dependencies are available, fix any warnings, then close and archive `p1-audit-evidence-citations-and-claims.md`.

## 2026-07-11 review

**Chapters reviewed:** `medicalImaging/`, `contouring/`, `registration/`, `treatmentPlanning/`, `qa/`, `validation/`, `workflow/`
**Todos closed:** `p1-add-radiotherapy-data-and-informatics-foundations.md`
**Todos opened:** none

### Searches run
- medicalImaging: "radiotherapy DICOM RT Structure Set Segmentation RT Plan RT Dose treatment record registration objects" (DICOM Standard) — current standard, WG-07, and second-generation RT materials reviewed
- medicalImaging: "radiotherapy collection license RTSTRUCT RTDOSE CT dataset" (TCIA) — NSCLC-Radiomics, LCTSC, Head-Neck-PET-CT, HNSCC, and RADCURE candidates reviewed
- medicalImaging: "OpenKBP dataset official license CT dose structures" (publisher and challenge sources) — peer-reviewed dataset paper verified
- medicalImaging: "FAIR principles", "Datasheets for Datasets", and "federated learning medicine multi-institutional" (publisher and PubMed sources) — foundational documentation and distributed-learning sources verified

### Added
- medicalImaging: canonical patient-level RT data model, geometry and units, cohort construction, leakage prevention, provenance, privacy, dataset documentation, public datasets, and federated-learning foundations with 11 new verified references.
- application chapters: concise links to the canonical data foundations from contouring, registration, treatment planning, QA, validation, and workflow.

### Rejected
- Dataset summaries without authoritative access/license information were not used; collection landing pages or the peer-reviewed dataset publication were required.
- Search results that were preprints, secondary summaries, or unrelated datasets were not cited where a primary standard, collection page, or peer-reviewed source was available.

### Notes for next cycle
- The separate `p2-literature-currency-medicalImaging.md` todo remains open; this review backfilled foundational informatics rather than performing the chapter's recent-advances scan.

### Initialization note (2026-07-10)

At setup time, no review cycles had run. This repository was set up for autonomous literature-tracking on 2026-07-10 — see `../GUIDE.md` for the process and `README.md` for open todos. The first cycle was expected to start with `p0-write-stub-chapters.md` and `p1-fix-broken-toc-anchors.md`, since both blocked the "Current Research" mechanism the later P2 literature-currency todos depend on.
