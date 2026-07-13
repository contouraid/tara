# 1: Introduction

## Before you begin

**Prerequisites:** None. New readers may keep the [cross-book glossary](../resources/glossary.md) open; it is the canonical source for artificial intelligence (AI) and other terms used throughout ART101.

**Learning objectives:** After this chapter, you should be able to:

1. outline the radiotherapy pathway and identify where AI can affect it;
2. distinguish artificial intelligence, machine learning, and deep learning;
3. trace a clinical AI system from question and data through retirement;
4. distinguish training, validation, and inference and explain why patients must be separated across data splits; and
5. separate technical performance, clinical validity, clinical utility, and lifecycle safety when reading a claim.

**Reading route:** Everyone should read this chapter first. Complete beginners should next read Chapters 3 and 4 before Chapter 2; clinicians may continue to Chapter 2 or their application of interest; technical readers should continue to Chapters 3 and 4. {ref}`Cases A–C <recurring-cases>` establish the clinical threads used later.

## What Radiation Oncology Does

Radiotherapy uses ionizing radiation to damage cellular targets while limiting injury to surrounding normal tissue. It may be delivered from outside the body, with external-beam techniques, or from sources placed in or near a target, as in brachytherapy. Population-based estimates indicate that roughly half of people with cancer have an evidence-based indication for radiotherapy at some point in their care, although access and actual use vary by health system [[1]](https://doi.org/10.1016/S1470-2045%2815%2900222-3).

A treatment course connects clinical decisions, simulation images, target and organ-at-risk contours, a prescription, an optimized treatment plan, physics and clinical quality assurance, image-guided delivery, and follow-up. The [radiation-oncology fundamentals](../fundamentalRO/fundamentalRO.md) chapter explains this pathway; the [medical-imaging and informatics](../medicalImaging/medicalImaging.md) chapter explains how its data objects remain linked.

The planning objective is not simply to maximize target dose. Clinicians balance tumor control, normal-tissue risk, delivery uncertainty, treatment burden, and patient goals. Target-volume concepts and margin terminology are standardized internationally, but their clinical application remains disease- and technique-specific [[2]](https://doi.org/10.1093/jicru/10.1.Report83).

## What AI Means in This Book

**Artificial intelligence (AI)** is an umbrella term for computational systems designed to perform tasks associated with perception, prediction, language, decision support, or action. **Machine learning (ML)** is a family of approaches in which model behavior is estimated from data rather than exhaustively specified by hand. **Deep learning** uses multilayer neural networks to learn representations and task outputs jointly [[3]](https://doi.org/10.1038/nature14539).

These labels do not establish clinical value. A model may perform well on a retrospective benchmark yet fail at another institution, under a changed imaging protocol, or when embedded in a real workflow. Readers should therefore separate four questions:

1. **Technical performance:** Does the model predict the reference labels on representative data?
2. **Clinical validity:** Does the output correspond to a clinically meaningful state or endpoint?
3. **Clinical utility:** Does using the system improve decisions, workflow, safety, outcomes, or resource use?
4. **Lifecycle safety:** Can performance, versions, failures, and changes be monitored after deployment?

The distinction matters because reviews of medical-imaging AI have repeatedly found high risk of bias, limited external validation, and weak evidence of prospective clinical impact despite strong reported discrimination [[4]](https://doi.org/10.1136/bmj.m1328).

## Where AI Enters the Radiotherapy Pathway

AI methods have been studied across imaging, contouring, registration, treatment planning, quality assurance, outcome modeling, and workflow orchestration [[5]](https://doi.org/10.1088/1361-6560/ac678a). Examples include:

- segmenting targets or organs at risk, followed by expert review;
- registering images acquired at different times or with different modalities;
- predicting achievable dose distributions or optimization objectives;
- detecting unusual plans, contours, machine behavior, or workflow states;
- extracting structured variables from reports; and
- estimating risks to support, but not replace, a clinical decision.

Each task has a dedicated chapter. This introduction establishes the shared vocabulary and the standard of evidence used to read those chapters.

(common-ai-lifecycle)=
## The Common Clinical AI Lifecycle

An AI system begins before a model architecture is chosen and continues after the model stops being used. The same lifecycle applies to {ref}`Case A's autocontour <recurring-cases>`, Case B's quality-assurance alert, and Case C's adaptive-workflow service.

| Stage | Novice question | Required output before moving on |
|---|---|---|
| **1. Clinical question and intended use** | Who will use what output, for which patients, to support which decision? | a bounded claim, accountable user, expected benefit, and unacceptable harms |
| **2. Data and labels** | What observations become inputs, and how was the reference output created? | cohort definition, provenance, label protocol, missingness analysis, and data-governance basis |
| **3. Development split** | Which cases may influence fitting and choices, and which remain untouched? | patient-level training, validation, and test sets; when needed, external, temporal, or site-separated evaluation |
| **4. Training** | What does the model learn from examples? | frozen preprocessing, parameters, software and data versions, and reproducible training record |
| **5. Validation** | Does the frozen system work for its intended use and failure costs? | technical, clinical, subgroup, robustness, human-factors, and workflow evidence proportionate to risk |
| **6. Inference** | How does a new case become an output? | specified inputs, quality checks, uncertainty or abstention behavior, review, and audit trail |
| **7. Deployment** | How does the tested system enter real work? | local commissioning, integration, training, downtime path, escalation, approval, and version control |
| **8. Monitoring and change** | Does benefit persist as patients, users, equipment, and software change? | performance and safety indicators, drift thresholds, incident review, revalidation, and change control |
| **9. Retirement** | When and how is use stopped? | stop criteria, removal and fallback plan, record retention, communication, and successor validation |

**Data** are recorded observations such as images, dose, notes, or outcomes. A **label** is the reference target used for learning or evaluation, such as a clinician contour or observed toxicity; it may be uncertain or biased rather than ground truth. A **feature** is a model input derived from the data. **Training** estimates model parameters. **Validation** can mean both the development set used to choose a model and the broader evidence that a frozen system is fit for use; the context must make clear which meaning applies. **Inference** applies the frozen pipeline to a new case.

The lifecycle is not a one-way permission slip. Failure at validation returns the team to the question, data, or design; monitoring can trigger restriction, retraining, rollback, or retirement. A model is only one component inside a clinical AI system that also includes data pipelines, interfaces, people, policies, and safety barriers.

## Learning Paradigms

### Supervised Learning

Supervised learning estimates a mapping from inputs to labeled outputs. Classification predicts categories, regression predicts quantities, and segmentation predicts spatial labels. The label is a reference standard, not automatically truth: contours can vary between experts, outcomes can be missing or inconsistently defined, and historical approvals may encode local preference.

### Unsupervised and Self-supervised Learning

Unsupervised learning seeks structure without task labels, for example through clustering or lower-dimensional representations. Self-supervised learning constructs a training signal from the data themselves, such as predicting masked content or matching related views. These approaches can use large unlabeled collections, but downstream clinical validity still requires task-specific evaluation [[6]](https://doi.org/10.1109/CVPR42600.2020.00975).

### Semi-supervised Learning

Semi-supervised learning combines a smaller labeled set with a larger unlabeled set. It is attractive where expert annotation is expensive, but performance depends on whether the unlabeled cases represent the intended population and whether erroneous pseudo-labels reinforce model bias.

### Reinforcement Learning

Reinforcement learning estimates a policy for sequential actions using a reward signal. In radiotherapy research, the environment is generally a simulator or planning system rather than a patient. A reward based on dose metrics is only a proxy for clinical benefit, so a successful simulation does not by itself justify autonomous clinical use [[7]](https://mitpress.mit.edu/9780262039246/reinforcement-learning/).

## Training and Evaluation Basics

Development data are used to fit parameters; validation data guide model selection; test data estimate performance after choices are fixed. Splits must occur at the unit that can leak information—usually the patient, and sometimes the institution or time period—not at the image slice or treatment fraction. External evaluation tests transport to a meaningfully different setting. The [validation chapter](../validation/validation.md) covers metrics, calibration, subgroup analysis, study design, and post-deployment monitoring.

Metric choice follows intended use. Accuracy can conceal failure in an uncommon class; overlap scores can conceal clinically important boundary errors; and mean dose error can conceal a localized hot spot. A useful evaluation therefore connects technical metrics to the failure modes and consequences of the actual task. TRIPOD+AI provides reporting guidance for prediction models that use regression or machine-learning methods [[8]](https://doi.org/10.1136/bmj-2023-078378).

## Reading Claims About Clinical AI

Treat evidence as a ladder rather than a binary label:

- **Development or benchmark evidence** shows feasibility on selected data.
- **External retrospective evidence** tests performance in data separated by place, time, or population.
- **Silent prospective evaluation** observes performance in the live data stream without influencing care.
- **Interventional evaluation** measures how the human-AI system changes decisions, workload, safety, or patient outcomes.
- **Post-deployment surveillance** tests whether benefit and safety persist as data, users, and software change.

Randomization is not appropriate for every technical question, but claims of clinical benefit require evidence that measures clinical use. Reporting should also make clear whether a study was single-center, retrospective, benchmark-only, or not specific to radiotherapy.

## Limitations and Responsible Use

Models learn associations present in their development data. They may exploit shortcuts, reproduce inequities, become miscalibrated under distribution shift, or encourage automation bias. Privacy protection, security, usability, accountability, and change control are therefore part of system performance rather than optional additions. WHO guidance frames health AI around autonomy, well-being and safety, transparency, accountability, inclusiveness, and sustainability [[9]](https://www.who.int/publications/i/item/9789240029200).

Clinical responsibility remains with appropriately qualified people and organizations. The right level of automation depends on intended use, failure consequence, detectability, time pressure, and the strength of independent checks.

## Current Research and Recent Advances

- **General-purpose and multimodal models:** Biomedical models increasingly combine images and language across multiple tasks. Their breadth does not establish radiotherapy utility; evaluation still has to cover volumetric RT data, treatment context, external sites, and consequential errors [[10]](https://doi.org/10.1038/s41591-024-03185-2). _(added: 2026-07)_
- **AI-specific reporting guidance:** TRIPOD+AI and PROBAST+AI make reporting, risk of bias, fairness, and applicability more explicit for prediction models, shifting attention from headline performance to evidence quality [[8]](https://doi.org/10.1136/bmj-2023-078378) [[11]](https://doi.org/10.1136/bmj-2024-082505). _(added: 2026-07)_
- **Lifecycle governance:** International good-machine-learning-practice principles emphasize representative data, human-AI team performance, clear user information, and monitoring of deployed models rather than one-time validation alone [[12]](https://www.fda.gov/medical-devices/software-medical-device-samd/good-machine-learning-practice-medical-device-development-guiding-principles). _(added: 2026-07)_

## Recap

- **Objective 1:** Radiotherapy is a linked clinical and technical process in which AI may support perception, prediction, optimization, or quality control.
- **Objective 2:** AI is the umbrella field, machine learning estimates behavior from data, and deep learning uses multilayer neural networks.
- **Objective 3:** A clinical AI system moves from an intended question through data, splitting, training, validation, inference, deployment, monitoring, change, and retirement; failed evidence can send it backward.
- **Objective 4:** Training fits parameters, development validation guides choices, a held-out test estimates frozen performance, and inference applies the pipeline to a new case. Patient separation prevents one person's information leaking between those roles.
- **Objective 5:** A technical score is not clinical benefit. Claims must separately support technical performance, clinical validity, clinical utility, and lifecycle safety.

**Important limitation and misconception:** A label is not automatically truth, a test set is not automatically external validation, and a high retrospective score does not authorize clinical use.

## References

1. Atun R, Jaffray DA, Barton MB, et al. Expanding global access to radiotherapy. *The Lancet Oncology*. 2015. [DOI](https://doi.org/10.1016/S1470-2045%2815%2900222-3)
2. International Commission on Radiation Units and Measurements. Prescribing, recording, and reporting photon-beam intensity-modulated radiation therapy (IMRT): ICRU Report 83. *Journal of the ICRU*. 2010. [DOI](https://doi.org/10.1093/jicru/10.1.Report83)
3. LeCun Y, Bengio Y, Hinton G. Deep learning. *Nature*. 2015. [DOI](https://doi.org/10.1038/nature14539)
4. Nagendran M, Chen Y, Lovejoy CA, et al. Artificial intelligence versus clinicians: systematic review of design, reporting standards, and claims of deep learning studies. *BMJ*. 2020. [DOI](https://doi.org/10.1136/bmj.m1328)
5. Barragán-Montero AM, Javaid U, Valdés G, et al. Artificial intelligence and machine learning for medical imaging: a technology review. *Physics in Medicine & Biology*. 2021. [DOI](https://doi.org/10.1088/1361-6560/ac678a)
6. He K, Fan H, Wu Y, Xie S, Girshick R. Momentum contrast for unsupervised visual representation learning. *CVPR*. 2020. [DOI](https://doi.org/10.1109/CVPR42600.2020.00975)
7. Sutton RS, Barto AG. *Reinforcement Learning: An Introduction*. 2nd ed. MIT Press; 2018. [Publisher](https://mitpress.mit.edu/9780262039246/reinforcement-learning/)
8. Collins GS, Moons KGM, Dhiman P, et al. TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods. *BMJ*. 2024. [DOI](https://doi.org/10.1136/bmj-2023-078378)
9. World Health Organization. *Ethics and Governance of Artificial Intelligence for Health*. 2021. [WHO](https://www.who.int/publications/i/item/9789240029200)
10. Tu T, Azizi S, Driess D, et al. Towards generalist biomedical AI. *Nature Medicine*. 2024. [DOI](https://doi.org/10.1038/s41591-024-03185-2)
11. Moons KGM, Damen JAA, Kaul T, et al. PROBAST+AI: an updated quality, risk of bias, and applicability assessment tool for prediction models. *BMJ*. 2025. [DOI](https://doi.org/10.1136/bmj-2024-082505)
12. US Food and Drug Administration, Health Canada, Medicines and Healthcare products Regulatory Agency. Good machine learning practice for medical device development: guiding principles. 2021. [FDA](https://www.fda.gov/medical-devices/software-medical-device-samd/good-machine-learning-practice-medical-device-development-guiding-principles)
