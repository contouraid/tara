# 8: Clinical Prediction, Radiomics, and Causal Inference

Clinical prediction models estimate an outcome for a defined patient at a defined time. In radiation oncology, the outcome might be two-year local control, grade 2 or worse xerostomia by 12 months, pathological complete response, or survival after treatment. Images, dose, clinical variables, laboratory measurements, and molecular data may all contribute.

Prediction is not the same as choosing treatment. A model can identify patients with poor outcomes while being unable to say whether escalation, de-escalation, another modality, or no change would help them. This chapter is the canonical home for outcome-modeling questions: what is predicted, how radiomic and multimodal predictors are constructed, how time and competing events are handled, and what additional assumptions are required before a prediction supports a causal or prescriptive claim.

(four-clinical-questions)=
## Four Different Clinical Questions

The word *predictive* is used loosely in clinical AI. Before evaluating a model, rewrite its aim as one of four questions:

| Question | What the model estimates | Radiotherapy example | What it does **not** establish |
|---|---|---|---|
| **Diagnostic** | A condition that is present at the index time | Is a new enhancing lesion recurrence or radiation necrosis? | future course or benefit from a treatment |
| **Prognostic** | A future outcome under the mixture of care represented in the data | What is this patient's two-year local-control risk after the current standard pathway? | which treatment changes that outcome |
| **Treatment-predictive** | How outcome differs with treatment choice; statistically, treatment-effect heterogeneity or an interaction | Is the benefit of dose escalation larger for biomarker-positive than biomarker-negative patients? | causality unless treatment comparisons are valid |
| **Causal** | A counterfactual contrast between well-defined interventions | What would the difference in two-year local control be if this patient received 60 Gy rather than 54 Gy, with all else specified? | transport to patients or interventions outside the target question |

A variable can be prognostic without being treatment-predictive. Large tumors may have worse control after either of two regimens but receive the same absolute benefit from both. Conversely, a treatment-effect modifier is defined by a difference between treatments, not by a significant association within only one treatment group. Calling a risk model “predictive” in the general machine-learning sense must not be read as evidence that it predicts treatment benefit.

## Define the Endpoint Before the Model

A usable endpoint specifies the event, starting time, prediction time, horizon, assessment method, and competing events. “Toxicity” is not an endpoint; “first clinician-graded grade 2 or worse xerostomia within 12 months of completing radiotherapy” is closer. Even then, the grading system, baseline symptoms, assessment schedule, patient-reported outcomes, retreatment, and death need rules.

### Endpoint Quality and Follow-up

Outcome labels are measurements, not automatic truth. Recurrence can require pathology, imaging consensus, or a composite definition. Toxicity grades vary between observers and may be absent because a patient was well, treated elsewhere, too ill to attend, or never asked. Tumor response depends on the assessment system and time point. Overall survival is comparatively unambiguous but may be too remote or nonspecific for the intended decision.

For every model, record:

- the index time and the latest information allowed as input;
- the event definition, severity threshold, adjudication, and blinding;
- the prediction horizon and why a decision at that horizon matters;
- baseline status and whether recurrent events or recovery are represented;
- follow-up distribution, assessment schedule, data source, and linkage method;
- missing outcomes and reasons, including differences by site and subgroup.

Excluding everyone without complete follow-up can select a healthier or more locally connected cohort. Treating an undocumented toxicity as “none” can train the model to recognize documentation patterns. Sensitivity analyses should test plausible missing-outcome mechanisms; linkage or prospective collection may be needed when missingness cannot be repaired analytically.

### Time-to-Event Outcomes, Censoring, and Competing Risks

Binary labels such as “alive at two years” discard information and can misclassify a patient whose last follow-up was at six months. Survival methods instead represent the time from a defined origin to an event. **Right censoring** means the event was not observed before follow-up ended; it does not mean the event never occurred. Standard analyses assume censoring is sufficiently independent of the event after accounting for modeled information. Loss to follow-up related to health or access can violate that assumption.

A **competing risk** prevents the event of interest. Death before late xerostomia, for example, prevents later observation of that toxicity. Simply censoring deaths and applying one-minus-Kaplan–Meier can overstate absolute toxicity risk. Use the cumulative incidence function for real-world event probability. Cause-specific hazards address the instantaneous event rate among those still event-free, whereas Fine–Gray subdistribution models relate predictors to cumulative incidence; the estimand must match the clinical question [[1]](https://doi.org/10.1080/01621459.1999.10474144).

Longitudinal response adds repeated, irregularly timed measurements. Define whether the target is the next measurement, a trajectory, time to progression, or a landmark prediction updated at each visit. Inputs recorded after a landmark cannot be used to predict from that landmark. Registration, segmentation, scanner, and interval variability can otherwise masquerade as biological change.

## Classical Outcome Models in Radiotherapy

Tumor-control probability (TCP) and normal-tissue complication probability (NTCP) models connect dose and other covariates to outcomes. They can compare plans or communicate population-level dose–response relationships, but parameter values depend on endpoint, fractionation, dose representation, organ definition, treatment technique, population, and follow-up. QUANTEC highlighted limitations in endpoint consistency, statistical methods, external validity, and uncertainty that still apply to higher-dimensional AI models [[2]](https://doi.org/10.1016/j.ijrobp.2009.09.040).

Modern toxicity or control models may combine dose-volume summaries with spatial **dosiomics**, clinical covariates, genetics, and imaging. Added complexity is justified only if it improves performance and utility beyond a credible simpler baseline. A high-dimensional model should be compared with standard clinical factors, tumor or organ volume, and established TCP/NTCP variables—not only with another complex model.

(radiomics-workflow)=
## The Radiomics and Dosiomics Workflow

Radiomics converts a defined image region into quantitative descriptors. Handcrafted features describe shape, intensity distributions, and spatial texture; deep imaging biomarkers learn representations directly from pixels or voxels. Dosiomics applies related spatial descriptors to three-dimensional planned or accumulated dose. The arithmetic is easy to automate; making the measurement stable, clinically meaningful, and externally valid is the hard part.

### 1. Lock the Clinical Design

Specify population, index time, outcome, horizon, intended use, comparator, and analysis plan before feature screening. Estimate the required sample size from the number of events and anticipated model complexity, not the number of images or patches. Partition by patient and protect an untouched temporal or geographical external test set. The canonical RT object model, geometry, provenance, and leakage controls are in [Medical Imaging in Radiation Oncology](../medicalImaging/medicalImaging.md).

### 2. Control Acquisition and Reconstruction

Scanner, sequence, tracer uptake interval, reconstruction kernel, slice thickness, voxel size, motion, contrast, and dose calculation algorithm can alter features without changing biology. Record these factors and test repeatability with same-patient repeat scans or appropriate phantoms. Restricting protocols can improve internal consistency but narrow applicability; including heterogeneous protocols requires enough data to estimate and validate that robustness.

### 3. Define and Test the Region

Segmentation determines which voxels contribute. Record the structure definition, annotators, software, editing, and whether contours were created with knowledge of outcome. Perturbations or repeat contours can reveal segmentation-sensitive features. Whole-tumor, habitat, organ, peritumoral, and dose regions answer different questions and must be prespecified. A contour generated after treatment is unavailable to a pretreatment model.

### 4. Freeze Preprocessing and Feature Calculation

Declare interpolation grid, resampling, intensity normalization, discretization or bin width, filtering, partial-volume handling, and feature definitions. These choices form part of the biomarker. The Image Biomarker Standardisation Initiative (IBSI) supplies consensus definitions and reference values for reproducible feature calculation [[3]](https://doi.org/10.1148/radiol.2020191145). Software name alone is insufficient: save versions, parameters, code, and a test case with expected values.

For dose, preserve units, fractionation assumptions, grid geometry, registration, and whether the array represents planned, fraction, accumulated, or biologically transformed dose. A texture feature from a misregistered or interpolated dose grid can be reproducible and wrong.

### 5. Screen Stability Before Association

Reject or flag features unstable to plausible acquisition, reconstruction, segmentation, registration, and preprocessing changes. Check correlations with simple quantities such as volume and mean intensity. A complex texture signature that is merely a proxy for tumor volume has not demonstrated added imaging information. Stability criteria and all exclusions must be learned in development data, not selected for favorable test performance.

### 6. Reduce Dimension and Fit Without Leakage

Radiomics often begins with far more candidate features than outcome events. Filtering, imputation, scaling, harmonization, dimensionality reduction, feature selection, hyperparameter tuning, and calibration must occur inside each training resample. Univariate screening on the complete dataset leaks outcomes into evaluation. Repeated patches or time points from one patient remain clustered within that patient's partition.

Harmonization methods can reduce site or protocol effects, but parameters must be fitted without the test set and cannot recover information never acquired. If site is entangled with outcome or treatment, removing a “batch effect” can remove clinical signal or preserve confounding. Report performance by site and protocol before and after harmonization.

### 7. Validate the Frozen Pipeline

External validation reruns the complete frozen pipeline—from source objects and contours through preprocessing to prediction—on patients from another place or time. Report exclusions and failures, not just successfully processed cases. If recalibration, feature replacement, or harmonization is refitted, show performance before and after and label the result as model updating rather than untouched validation.

## Deep, Longitudinal, and Multimodal Biomarkers

**Deep imaging biomarkers** can learn features or an end-to-end outcome model, reducing dependence on handcrafted definitions but not on acquisition, segmentation, leakage, sample size, or external validation. Saliency maps do not by themselves validate biological mechanism. Self-supervised or foundation representations still require evaluation for the exact modality, anatomy, endpoint, and population.

**Delta-radiomics** uses change between baseline and later images. A longitudinal feature requires consistent acquisition, time windows, registration, regions, and handling of disappearing or splitting lesions. In a retrospective NSCLC study, changes in CT radiomic features were associated with outcomes, illustrating the approach but not establishing a treatment rule [[4]](https://doi.org/10.1038/s41598-017-00665-z). Landmarking must prevent immortal-time bias: a patient must survive and remain observed long enough to supply the later scan.

**Multimodal models** may combine CT, MRI, PET, dose, clinical data, pathology, laboratory results, patient-reported outcomes, genomics, or other omics. Each modality needs a declared measurement time and missing-data policy. More modalities can shrink the eligible cohort and create site-specific missingness. Compare the combined model against each component and a clinical baseline; use ablation studies and external validation to show that added complexity contributes transportable information.

## Evaluation: From Accuracy to Decisions

Evaluation must match the endpoint and intended decision. [Validation and Evaluation of AI Models](../validation/validation.md) gives the general framework; outcome models add time and treatment-specific requirements.

### Discrimination and Error

Discrimination asks whether patients with earlier or more frequent events receive higher risk. For a fixed binary horizon, ROC AUC or precision–recall measures may be suitable. For censored outcomes, use a clearly defined concordance index or time-dependent AUC with methods that account for censoring. Report uncertainty and performance at clinically relevant horizons. One global c-index cannot show whether two-year risks are numerically correct.

### Calibration

Calibration compares predicted and observed risk. Show calibration-in-the-large, slope, and a curve at each important horizon, with uncertainty. Recalibration may repair a shifted baseline risk but not poor ranking or a wrong endpoint. Assess calibration by site, period, and clinically relevant subgroup, especially when treatment or follow-up differs.

### Clinical Utility and Decision Curves

A threshold probability expresses when the expected benefit of acting is worth the expected harm. Decision-curve analysis compares a model's net benefit across plausible thresholds with strategies such as act on everyone or no one [[5]](https://doi.org/10.1177/0272989X06295361). It does not prove that clinicians will use the model correctly, that the modeled action causes benefit, or that all relevant harms are included. Prospective impact studies must test the human–model pathway against current care and measure decisions, treatment, toxicity, control, workload, failures, and inequity.

## Association Is Not a Treatment Recommendation

Historical treatment choice is not random. Frailer patients may receive lower dose; patients with aggressive disease may receive escalation; newer technology may coincide with better supportive care. A model trained on these data can learn **treatment-selection bias** and confounding. Conditioning on post-treatment variables can introduce further bias. High accuracy does not remove any of these problems.

A causal question defines the population, interventions, assignment strategy, time zero, follow-up, outcome, and causal contrast. **Target-trial thinking** makes these elements explicit before observational analysis and helps avoid misaligned eligibility, treatment assignment, and follow-up [[6]](https://doi.org/10.1093/aje/kwv254). Estimating an individual or conditional treatment effect additionally requires assumptions such as:

- **consistency:** the observed outcome under the received intervention corresponds to the intervention as defined;
- **exchangeability:** after measured adjustment, treatment groups are comparable for the counterfactual outcomes;
- **positivity:** each relevant patient type could plausibly receive each compared treatment;
- correct handling of time-varying treatment, confounders, censoring, interference, and measurement.

Randomized trials address treatment assignment most directly, although subgroup effects still need prespecification, adequate power, and validation. Observational causal methods—standardization, propensity approaches, weighting, g-methods, or doubly robust estimators—can be useful, but their credibility depends on design, measured confounders, diagnostics, negative controls or sensitivity analyses, and subject-matter knowledge. No algorithm can adjust for an important unmeasured confounder merely by fitting a more flexible prediction function.

> **Interpretation rule:** A diagnostic or prognostic association-only model may support measurement or risk communication. It must not be described as selecting, escalating, de-escalating, or prescribing treatment unless valid comparative-effect evidence and prospective decision evaluation support that claim.

(worked-example-outcome-to-decision)=
## Worked Example: From Endpoint to a Treatment Decision

Suppose a team wants to use baseline CT, planned dose, and clinical variables to identify head-and-neck patients for an intensified xerostomia-prevention program.

1. **Intended use:** before treatment, estimate 12-month grade 2 or worse xerostomia to offer extra supportive care—not to reduce tumor dose. The endpoint uses a named grading scale, baseline symptom rule, scheduled assessments, death as a competing event, and registry linkage for follow-up.
2. **Data and pipeline:** patients are split by institution. Acquisition, parotid contours, dose alignment, feature definitions, missingness, and protocol are recorded. Stability screening, harmonization, selection, fitting, and calibration occur inside development folds. The model is compared with baseline symptoms, mean parotid dose, and a standard clinical model.
3. **Frozen external validation:** the untouched site runs the packaged pipeline on every eligible patient. The report includes processing failures, cumulative-incidence calibration and discrimination at 12 months, subgroup results, and confidence intervals. A performance drop triggers investigation rather than test-set feature replacement.
4. **Decision analysis:** clinicians specify risk thresholds at which the burden of extra supportive care is justified. Decision curves compare model-guided referral with referring everyone or no one. If net benefit is absent, the model stops even if its AUC is respectable.
5. **Prospective impact:** a controlled study tests whether showing risk changes referrals and improves patient-reported symptoms without unacceptable workload or inequity. Because the action is supportive care, the study does not claim the model estimates benefit from changing radiotherapy.

Now imagine using the same risk score to choose proton rather than photon therapy. That is a different question. High predicted xerostomia risk under historical mixed care does not estimate the counterfactual difference between modalities. The team needs a defined comparative-effect estimand, defensible trial or causal design, modality-specific dose and outcome data with adequate overlap, and validation of the treatment policy. The original prognostic model cannot make that leap.

## A Balanced Reading of the Evidence

The 2014 study by Aerts and colleagues extracted 440 CT features from 1,019 lung and head-and-neck cancer patients and validated a four-feature prognostic signature in independent cohorts, an influential demonstration of multi-cohort radiomics [[7]](https://doi.org/10.1038/ncomms5006). It showed feasibility and external association, not that using the signature improves treatment decisions.

Later stress testing exposed why external performance alone is not enough. Welch and colleagues reconstructed a related signature and found similar concordance from randomized image intensities and from tumor volume alone; three of four features were strongly volume-related [[8]](https://doi.org/10.1016/j.radonc.2018.10.027). This does not make all radiomics invalid. It demonstrates the need for simple baselines, perturbation and negative-control tests, transparent pipelines, and biological restraint.

The field has responded with standardization and reporting frameworks. IBSI addresses feature definitions and reference values [[3]](https://doi.org/10.1148/radiol.2020191145); TRIPOD+AI specifies transparent reporting for regression and machine-learning prediction studies [[9]](https://doi.org/10.1136/bmj-2023-078378); and PROBAST+AI assesses development quality, evaluation bias, and applicability [[10]](https://doi.org/10.1136/bmj-2024-082505). Reporting compliance is not proof of low bias, reproducibility, utility, or causality, but it makes those properties more inspectable.

## Current Research and Recent Advances

- **Standardized quantitative imaging:** IBSI consensus definitions and reference values make feature calculations testable across software implementations, while acquisition and clinical transportability remain separate validation problems [[3]](https://doi.org/10.1148/radiol.2020191145). _(added: 2026-07)_
- **Longitudinal and multimodal modeling:** Delta-radiomics, spatial dose, deep representations, and clinical or molecular data broaden the signal available to models, but add timing, missingness, harmonization, and sample-size failure modes [[4]](https://doi.org/10.1038/s41598-017-00665-z). _(added: 2026-07)_
- **Prediction-study governance:** TRIPOD+AI and PROBAST+AI strengthen expectations for transparent development, evaluation, fairness, risk-of-bias assessment, and applicability across classical and machine-learning models [[9]](https://doi.org/10.1136/bmj-2023-078378) [[10]](https://doi.org/10.1136/bmj-2024-082505). _(added: 2026-07)_

## Recap

Clinical outcome modeling begins with a precise endpoint, prediction time, horizon, follow-up process, and intended decision. Censoring, competing risks, repeated measurements, and missing outcomes determine what can be learned. Radiomics and dosiomics require a frozen, leakage-safe chain from acquisition and segmentation through standardized calculation, stability testing, dimension reduction, fitting, and true external validation. Discrimination must be accompanied by calibration, decision utility, subgroup evaluation, and prospective impact. Most importantly, diagnostic or prognostic association does not estimate treatment benefit: prescribing treatment requires a valid comparative causal question and evidence design.

## References

1. Fine JP, Gray RJ. A proportional hazards model for the subdistribution of a competing risk. *Journal of the American Statistical Association*. 1999;94(446):496-509. [DOI](https://doi.org/10.1080/01621459.1999.10474144)
2. Bentzen SM, Constine LS, Deasy JO, et al. Quantitative Analyses of Normal Tissue Effects in the Clinic (QUANTEC): an introduction to the scientific issues. *International Journal of Radiation Oncology, Biology, Physics*. 2010;76(3 Suppl):S3-S9. [DOI](https://doi.org/10.1016/j.ijrobp.2009.09.040)
3. Zwanenburg A, Vallières M, Abdalah MA, et al. The Image Biomarker Standardization Initiative: standardized quantitative radiomics for high-throughput image-based phenotyping. *Radiology*. 2020;295(2):328-338. [DOI](https://doi.org/10.1148/radiol.2020191145)
4. Fave X, Zhang L, Yang J, et al. Delta-radiomics features for the prediction of patient outcomes in non-small cell lung cancer. *Scientific Reports*. 2017;7:588. [DOI](https://doi.org/10.1038/s41598-017-00665-z)
5. Vickers AJ, Elkin EB. Decision curve analysis: a novel method for evaluating prediction models. *Medical Decision Making*. 2006;26(6):565-574. [DOI](https://doi.org/10.1177/0272989X06295361)
6. Hernán MA, Robins JM. Using big data to emulate a target trial when a randomized trial is not available. *American Journal of Epidemiology*. 2016;183(8):758-764. [DOI](https://doi.org/10.1093/aje/kwv254)
7. Aerts HJWL, Rios Velazquez E, Leijenaar RTH, et al. Decoding tumour phenotype by noninvasive imaging using a quantitative radiomics approach. *Nature Communications*. 2014;5:4006. [DOI](https://doi.org/10.1038/ncomms5006)
8. Welch ML, McIntosh C, Haibe-Kains B, et al. Vulnerabilities of radiomic signature development: the need for safeguards. *Radiotherapy and Oncology*. 2019;130:2-9. [DOI](https://doi.org/10.1016/j.radonc.2018.10.027)
9. Collins GS, Moons KGM, Dhiman P, et al. TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods. *BMJ*. 2024;385:e078378. [DOI](https://doi.org/10.1136/bmj-2023-078378)
10. Moons KGM, Damen JAA, Kaul T, et al. PROBAST+AI: an updated quality, risk of bias, and applicability assessment tool for prediction models using regression or artificial intelligence methods. *BMJ*. 2025;388:e082505. [DOI](https://doi.org/10.1136/bmj-2024-082505)
