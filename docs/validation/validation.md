# 9: Validation and Evaluation of AI Models

Validation asks whether an AI system is fit for a defined purpose in a defined setting. It is not one calculation performed at the end of model development. It begins with the clinical question, continues through data design and technical evaluation, and extends to workflow impact and post-deployment monitoring.

A high benchmark score can coexist with poor clinical value. Performance may fall under distribution shift, a threshold may be poorly chosen, probabilities may be miscalibrated, or the output may arrive too late to affect care. Validation must therefore connect statistical performance to the complete clinical use case.

(start-with-the-intended-use)=
## Start with the Intended Use

Before selecting a metric, specify:

- the target population and exclusions;
- the clinical setting and users;
- the input data and acquisition conditions;
- the output and its units or meaning;
- the decision or task the output supports;
- the comparator and current standard of care;
- the cost and severity of false positives, false negatives, and unavailable results;
- the required human review and downstream action.

The same model may be suitable for prioritizing review but unsuitable for autonomous rejection. Validation evidence must match the claimed role.

## Data for Development and Evaluation

Use [Radiotherapy Data and Informatics Foundations](../medicalImaging/medicalImaging.md) for the canonical RT object model, cohort manifest, longitudinal identity, label provenance, missingness, de-identification, and preprocessing controls. The sections below focus on how those curated data support an unbiased evaluation.

### Separate the Data Splits

Training data estimate model parameters. Validation data support model and hyperparameter selection. Test data estimate final performance after development decisions are frozen. Repeatedly consulting the test set turns it into development data and produces optimistic results.

Splits should prevent leakage. In longitudinal radiotherapy data, images or fractions from one patient must not be divided between training and test sets. Near-duplicate plans, propagated contours, repeated reconstructions, and institutional templates can create less obvious leakage.

### Internal and External Validation

**Internal validation** evaluates new observations drawn from substantially the same source as development data. Cross-validation and bootstrapping can estimate optimism efficiently but do not test transport to a new institution.

**Temporal validation** uses later patients from the same setting and can reveal changes in practice or equipment. **Geographical external validation** uses another site or system and better tests transportability. A convincing evidence package often includes both.

External data should not be silently used to tune the model and still be called an untouched external test. Any recalibration or adaptation should be reported, with performance before and after the change.

### Reference Standards

The target label may be uncertain. Contours vary between experts; toxicity may be under-recorded; plan approval reflects local preferences; delivered dose is estimated rather than directly observed. Validation should describe who produced the reference, what information they saw, how disagreement was resolved, and whether adjudicators were blinded to model output.

Where no unique ground truth exists, use multiple readers, consensus methods, repeated measurement, or outcome-based endpoints. Report inter-observer or test-retest variability so model error has a meaningful clinical context.

## Classification Metrics

For a binary classifier, predictions at a chosen threshold form true positives (TP), false positives (FP), true negatives (TN), and false negatives (FN).

### Accuracy

$$Accuracy = \frac{TP + TN}{TP + TN + FP + FN}$$

Accuracy is intuitive but can be misleading when classes are imbalanced. If a serious error occurs in 1% of plans, a classifier that always predicts "no error" is 99% accurate and clinically useless.

### Sensitivity and Specificity

$$Sensitivity = \frac{TP}{TP + FN}$$

$$Specificity = \frac{TN}{TN + FP}$$

Sensitivity measures the fraction of positive cases detected; specificity measures the fraction of negative cases correctly excluded. They should be accompanied by confidence intervals and evaluated at a threshold chosen for the intended clinical trade-off.

### Predictive Values

$$PPV = \frac{TP}{TP + FP}, \qquad NPV = \frac{TN}{TN + FN}$$

Positive and negative predictive values depend on prevalence. A model can retain sensitivity and specificity yet produce a different PPV when deployed in a population with a different event rate.

### ROC and Precision-Recall Curves

The receiver operating characteristic (ROC) curve plots sensitivity against false-positive rate across thresholds. Area under the ROC curve summarizes discrimination but does not select a threshold and can look favorable for rare events.

The precision-recall curve focuses on positive predictive value and sensitivity and is often more informative for rare positives. Both curves summarize ranking, not calibration or clinical benefit.

### F1 Score and Balanced Accuracy

The F1 score is the harmonic mean of precision and recall. Balanced accuracy averages sensitivity and specificity. These can help with imbalance, but they encode particular trade-offs and should not replace reporting the underlying confusion matrix.

## Segmentation Metrics

### Dice Similarity Coefficient

For predicted voxel set $P$ and reference set $G$:

$$DSC = \frac{2|P \cap G|}{|P| + |G|}$$

Dice measures overlap from 0 to 1. It is sensitive to structure size: a small boundary displacement can greatly reduce Dice for a tiny organ while having little effect for a large organ. Dice also provides no direct location of the disagreement.

### Hausdorff and Surface Distances

Hausdorff distance measures the largest nearest-surface discrepancy. Because one outlier can dominate, the 95th-percentile Hausdorff distance (HD95) is often reported. Mean or average symmetric surface distance summarizes typical boundary disagreement.

Surface Dice measures the proportion of surfaces within a specified tolerance. The tolerance must be clinically justified and reported; changing it changes the result.

### Volume and Clinical Impact

Relative volume difference can reveal systematic over- or under-segmentation. More importantly, segmentation should be evaluated through its use: editing time, frequency of major edits, missed critical boundaries, and effect on dose-volume metrics or treatment decisions.

An average score can hide a catastrophic tail. Report per-structure distributions, low-performing cases, missing structures, and failure rates—not only the mean.

## Regression and Dose-Prediction Metrics

Mean absolute error (MAE) retains the units of the target and is relatively robust to outliers. Root mean squared error (RMSE) penalizes larger deviations more heavily. Neither shows whether the model systematically overpredicts or underpredicts, so signed error and agreement plots are useful.

For three-dimensional dose prediction, voxel-wise MAE should be complemented by clinically meaningful measures:

- target coverage and hotspot metrics;
- organ-at-risk mean and maximum doses;
- dose-volume histogram differences;
- spatial gamma or distance-to-agreement where justified;
- plan deliverability and optimization performance when the prediction guides planning.

A dose model can have low global voxel error while missing a small serial organ or blurring a steep gradient. Evaluation should stratify by region and clinical objective.

(calibration-and-probabilistic-predictions)=
## Calibration and Probabilistic Predictions

Discrimination asks whether higher-risk patients tend to have events more often. Calibration asks whether predicted probabilities correspond to observed frequencies. A model can discriminate well and still predict risks that are systematically too high or low.

Useful calibration analyses include:

- calibration plots with uncertainty;
- calibration-in-the-large or intercept;
- calibration slope;
- Brier score;
- subgroup and temporal calibration.

The commonly used Hosmer-Lemeshow test should not be the sole calibration assessment because results depend on grouping and sample size. Calibration should be examined graphically and quantitatively [[1]](https://doi.org/10.1093/jamia/ocz228).

Dose prediction is often deterministic, but uncertainty-aware models may produce intervals or distributions. Validate both coverage—how often the interval contains the outcome—and sharpness—whether intervals are narrow enough to be useful.

## Robustness, Generalization, and Fairness

### Distribution Shift

Performance can change with scanner vendor, reconstruction, contouring convention, treatment technique, disease prevalence, demographic mix, software version, or workflow. Stress testing should vary plausible nuisance factors and include corrupted, incomplete, and out-of-distribution inputs.

Robustness testing is not permission to deploy outside intended use. It identifies boundaries and informs safeguards.

(subgroup-evaluation)=
### Subgroup Evaluation

Report performance for clinically relevant subgroups where sample size permits: sex, age, anatomy, disease site, stage, device, institution, and acquisition protocol. Small groups require uncertainty intervals and careful interpretation. Comparing point estimates without adequate precision can create false assurance or false alarms.

Fairness is not achieved by equalizing one metric mechanically. Different error types may carry different clinical harm. The analysis should connect subgroup performance to access, workflow, and outcomes. The broader treatment of fairness across data, model target, workflow, access, and outcome—beyond the subgroup metrics measured here—is in {ref}`Responsible AI, Regulation, and Security <fairness-and-health-equity>`.

### Missing and Low-Quality Inputs

Validation must reproduce missingness and quality problems expected in practice. Define whether the system rejects invalid inputs, degrades gracefully, or produces an applicability warning. A model that always returns an answer may be less safe than one that abstains appropriately.

## From Technical to Clinical Validation

### Analytical or Technical Validation

Technical validation shows that the software correctly accepts inputs, executes reproducibly, and meets prespecified performance criteria. It includes interface testing, preprocessing verification, numerical reproducibility, cybersecurity, latency, and failure handling.

### Silent Evaluation

In a silent deployment, the system runs on current cases but does not influence care. This tests integration, data availability, latency, and local performance while limiting clinical risk. Silent evaluation still requires privacy, security, and governance review.

### Reader or User Studies

Reader studies compare clinicians with and without AI support. Use randomized case order, appropriate washout, representative prevalence, and analysis that accounts for repeated readers and cases. Measure decision accuracy, time, confidence, overrides, and error types. The model-alone result is not a substitute for human-AI team performance.

### Prospective Clinical Evaluation

A prospective study evaluates the system in the intended workflow with prespecified outcomes. Designs may include stepped-wedge, cluster-randomized, or controlled before-and-after studies. Outcomes should reflect the claim: reduced contour-editing time, fewer clinically important errors, faster planning, improved guideline adherence, or patient outcomes.

Surrogate efficiency gains should not be described as patient benefit without evidence. New workflow delays, rework, and inequities should be measured alongside intended benefits.

### Reporting and Risk-of-Bias Assessment

TRIPOD+AI provides updated reporting guidance for clinical prediction models using regression or machine learning [[2]](https://doi.org/10.1136/bmj-2023-078378). PROBAST+AI distinguishes quality of model development from risk of bias in performance evaluation and gives explicit attention to fairness and applicability [[3]](https://doi.org/10.1136/bmj-2024-082505). Using these frameworks early improves study design; using them only at manuscript submission cannot repair a weak evaluation.

## Statistical Planning

Validation protocols should prespecify primary endpoints, acceptable performance, sample size, threshold selection, subgroup analyses, and handling of missing data. Confidence intervals are essential because a metric from a finite sample is an estimate.

For clustered data—multiple structures, fractions, or plans per patient—analysis must account for within-patient dependence. Comparing multiple models or endpoints also raises multiplicity concerns. A statistically significant difference may be too small to matter clinically, while a clinically important difference may be imprecisely estimated in a small study.

(post-deployment-monitoring)=
## Post-Deployment Monitoring

Validation does not end at release. Monitoring should be linked to a response plan and include:

- input schema, completeness, and quality;
- changes in patient and acquisition distributions;
- output and confidence distributions;
- rejection, override, edit, and failure rates;
- latency and availability;
- sampled ground-truth performance when outcomes become available;
- subgroup performance and safety incidents;
- downstream workflow and clinical endpoints.

### Drift Detection

Data drift is a change in input distribution. Concept drift is a change in the relationship between inputs and outcomes. Label drift is a change in outcome prevalence. Drift signals prompt investigation; they do not prove performance has worsened.

Monitoring delayed clinical outcomes may require linkage months or years later. Near-term process measures can provide faster signals but should not replace eventual outcome assessment.

### Updating a Model

Possible responses include recalibrating probabilities, adjusting thresholds, retraining, narrowing intended use, or retiring the model. Every update creates a new configuration that requires proportional validation and traceability. FDA and international GMLP principles emphasize total-product-lifecycle management and real-world monitoring [[4]](https://www.fda.gov/medical-devices/software-medical-device-samd/good-machine-learning-practice-medical-device-development-guiding-principles).

### Governance and Stop Rules

Name the owner of the deployed system, the review frequency, escalation pathway, and authority to suspend use. The reusable governance checklist and responsibility (RACI) map that assign these roles are in {ref}`Responsible AI, Regulation, and Security <a-governance-checklist-and-responsibility-map>`. Predetermined stop rules might include severe incidents, sustained metric breach, data-pipeline corruption, or an unvalidated upstream change. A rollback path and downtime workflow should be tested before they are needed.

## Current Research and Recent Advances

- **AI-specific reporting guidance:** TRIPOD+AI updates prediction-model reporting for regression and machine-learning methods and strengthens expectations around protocol, data, evaluation, and open science [[2]](https://doi.org/10.1136/bmj-2023-078378). _(added: 2026-07)_
- **Updated risk-of-bias assessment:** PROBAST+AI separates development quality from evaluation bias and incorporates applicability and fairness throughout its domains, reflecting the broader evidence needed for clinical AI [[3]](https://doi.org/10.1136/bmj-2024-082505). _(added: 2026-07)_
- **Total-lifecycle evaluation:** International GMLP principles emphasize representative datasets, independent test sets, human-AI team performance, clear user information, and monitoring of deployed models [[4]](https://www.fda.gov/medical-devices/software-medical-device-samd/good-machine-learning-practice-medical-device-development-guiding-principles). _(added: 2026-07)_

## Recap

AI validation begins with a precise intended use and follows the system from data design through technical performance, human-AI workflow, prospective impact, and post-deployment monitoring. Accuracy alone is rarely adequate. Classification requires threshold-aware and prevalence-aware measures; segmentation needs overlap, boundary, tail, and clinical-impact evaluation; probabilistic outputs require calibration; and every task requires external validity, robustness, subgroup analysis, uncertainty, and governance for change.

## References

1. Huang Y, Li W, Macheret F, Gabriel RA, Ohno-Machado L. A tutorial on calibration measurements and calibration models for clinical prediction models. *Journal of the American Medical Informatics Association*. 2020;27(4):621-633. [DOI](https://doi.org/10.1093/jamia/ocz228)
2. Collins GS, Moons KGM, Dhiman P, et al. TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods. *BMJ*. 2024;385:e078378. [DOI](https://doi.org/10.1136/bmj-2023-078378)
3. Moons KGM, Damen JAA, Kaul T, et al. PROBAST+AI: an updated quality, risk of bias, and applicability assessment tool for prediction models using regression or artificial intelligence methods. *BMJ*. 2025;388:e082505. [DOI](https://doi.org/10.1136/bmj-2024-082505)
4. U.S. Food and Drug Administration. Good Machine Learning Practice for Medical Device Development: Guiding Principles. Updated 2025. [FDA guidance](https://www.fda.gov/medical-devices/software-medical-device-samd/good-machine-learning-practice-medical-device-development-guiding-principles)
