# TODO: Cover Clinical Prediction, Radiomics, and Causal Inference

**Section:** Root (cross-cutting)
**Priority:** High
**Owner:** (unassigned)
**Opened:** 2026-07-11

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

- [ ] Diagnostic, prognostic, treatment-predictive, and causal questions are defined with radiotherapy examples
- [ ] Time-to-event data, censoring, competing risks, calibration, discrimination, and decision utility are explained for novices
- [ ] The complete radiomics/dosiomics workflow and its major reproducibility failure modes are covered
- [ ] The text explicitly prevents causal or prescriptive interpretation of association-only models
- [ ] At least one worked example follows a model from endpoint definition through external validation and a treatment decision
- [ ] Both successful and non-replicating or externally degraded examples are used to present a balanced state of evidence
- [ ] Content has one canonical home and is cross-linked from radiobiology, imaging, planning, and validation chapters
