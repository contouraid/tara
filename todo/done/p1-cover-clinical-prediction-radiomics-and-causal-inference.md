# DONE: Cover Clinical Prediction, Radiomics, and Causal Inference

**Section:** Root (cross-cutting)
**Priority:** High
**Owner:** Codex
**Opened:** 2026-07-11
**Completed:** 2026-07-12

## Gap

Outcome prediction is named in the introduction and treatment-planning chapter, but the book does not teach it as a distinct AI domain. There is no coherent treatment of radiomics, toxicity and tumor-control prediction, time-to-event outcomes, longitudinal response, biomarkers, multimodal/omics data, or patient selection. Most importantly, the text does not clearly separate prediction from prognosis, treatment-effect estimation, and causal claims.

This omission leaves readers poorly equipped to assess a large part of radiation-oncology AI research and at risk of interpreting association or discrimination as evidence that a model improves treatment decisions.

## What Is Needed

1. Create a canonical section or chapter covering clinical endpoints, endpoint quality, competing risks, censoring, follow-up, missing outcomes, and clinically meaningful prediction horizons.
2. Explain the radiomics pipeline: acquisition variability, segmentation, preprocessing, feature extraction, feature stability, dimensionality reduction, model fitting, harmonization, and external validation.
3. Cover deep imaging biomarkers, delta-radiomics, dosiomics, clinical/genomic/multimodal models, toxicity prediction, TCP/NTCP modeling, response assessment, and patient selection.
4. Distinguish diagnostic, prognostic, predictive, and causal questions; explain confounding, treatment-selection bias, target-trial thinking, counterfactual treatment effects, and why a predictive model does not by itself prescribe treatment.
5. Connect evaluation to calibration, decision-curve analysis, clinical utility, survival metrics, subgroup performance, and prospective impact studies.
6. Review reporting and reproducibility guidance and use representative positive and negative/failed validation studies to show the field's maturity.

## Acceptance Criteria

- [x] Diagnostic, prognostic, treatment-predictive, and causal questions are defined with radiotherapy examples
- [x] Time-to-event data, censoring, competing risks, calibration, discrimination, and decision utility are explained for novices
- [x] The complete radiomics/dosiomics workflow and its major reproducibility failure modes are covered
- [x] The text explicitly prevents causal or prescriptive interpretation of association-only models
- [x] At least one worked example follows a model from endpoint definition through external validation and a treatment decision
- [x] Both successful and non-replicating or externally degraded examples are used to present a balanced state of evidence
- [x] Content has one canonical home and is cross-linked from radiobiology, imaging, planning, and validation chapters

## What Was Done

1. Added `docs/clinicalPrediction/clinicalPrediction.md` as a new canonical Chapter 8 and renumbered the later chapters and book navigation.
2. Defined diagnostic, prognostic, treatment-predictive, and causal questions with radiotherapy examples and an explicit rule against prescribing from association-only models.
3. Added novice-oriented coverage of endpoint design, missing outcomes, follow-up, time-to-event data, censoring, competing risks, longitudinal response, TCP/NTCP, discrimination, calibration, decision curves, subgroup performance, and prospective impact evaluation.
4. Documented the complete radiomics and dosiomics workflow from clinical design and acquisition through segmentation, preprocessing, standardized feature calculation, stability screening, leakage-safe model fitting, harmonization, and frozen external validation.
5. Covered deep imaging biomarkers, delta-radiomics, spatial dose, clinical/genomic/multimodal inputs, toxicity and tumor-control prediction, response assessment, and patient selection.
6. Added a worked xerostomia-risk example that proceeds from endpoint definition through external validation and supportive-care referral, then shows why changing radiotherapy modality requires a separate comparative causal design.
7. Balanced the influential multi-cohort Aerts radiomics result with the Welch reanalysis showing that randomized intensities and tumor volume could reproduce similar discrimination.
8. Cross-linked the canonical chapter from the radiation-oncology foundations, medical-imaging, treatment-planning, and validation chapters.
9. Removed the Sphinx theme's redundant `By Amith Kamath` footer line while retaining the copyright attribution and license footer.

## Verification

- Verified all ten new references against DOI, PubMed, publisher, or official guideline pages.
- Confirmed that every acceptance criterion is represented in Chapter 8 and that the four required chapters link to it.
- Ran `git diff --check`, a reference/citation consistency check, and a clean strict Sphinx build with warnings treated as errors.
- Confirmed the generated footer no longer contains `By Amith Kamath` and still contains the copyright attribution.
