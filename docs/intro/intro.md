# 1: Introduction

## Before you begin

**Prerequisites:** None. New readers may keep the [cross-book glossary](../resources/glossary.md) open; it is the canonical source for artificial intelligence (AI) and other terms used throughout ART101.

**Learning objectives:** After this chapter, you should be able to:

1. outline the radiotherapy pathway and identify where AI can affect it;
2. distinguish artificial intelligence, machine learning, and deep learning;
3. trace a clinical AI system from question and data through retirement, and distinguish lifecycle stages from readiness evidence;
4. distinguish training, validation, and inference and explain why patients must be separated across data splits; and
5. separate technical performance, clinical validity, clinical utility, and lifecycle safety when reading a claim.

**Reading route:** Everyone should read this chapter first. Complete beginners should next read Chapters 3 and 4 before Chapter 2; clinicians may continue to Chapter 2 or their application of interest; technical readers should continue to Chapters 3 and 4. {ref}`Cases A–C <recurring-cases>` establish the clinical threads used later.

## What Radiation Oncology Does

Radiotherapy uses ionizing radiation to damage cellular targets while limiting injury to surrounding normal tissue. It may be delivered from outside the body, with external-beam techniques, or from sources placed in or near a target, as in brachytherapy. Population-based estimates indicate that roughly half of people with cancer have an evidence-based indication for radiotherapy at some point in their care, although access and actual use vary by health system \[[Atun et al., 2015](https://doi.org/10.1016/S1470-2045%2815%2900222-3)\].

A treatment course connects clinical decisions, simulation images, target and organ-at-risk contours, a prescription, an optimized treatment plan, physics and clinical quality assurance, image-guided delivery, and follow-up. The [radiation-oncology fundamentals](../fundamentalRO/fundamentalRO.md) chapter explains this pathway; the [medical-imaging and informatics](../medicalImaging/medicalImaging.md) chapter explains how its data objects remain linked.

The planning objective is not simply to maximize target dose. Clinicians balance tumor control, normal-tissue risk, delivery uncertainty, treatment burden, and patient goals. Target-volume concepts and margin terminology are standardized internationally, but their clinical application remains disease- and technique-specific \[[ICRU, 2010](https://doi.org/10.1093/jicru/10.1.Report83)\].

## What AI Means in This Book

**Artificial intelligence (AI)** is an umbrella term for computational systems designed to perform tasks associated with perception, prediction, language, decision support, or action. **Machine learning (ML)** is a family of approaches in which model behavior is estimated from data rather than exhaustively specified by hand. **Deep learning** uses multilayer neural networks to learn representations and task outputs jointly \[[LeCun, Bengio, and Hinton, 2015](https://doi.org/10.1038/nature14539)\].

These labels do not establish clinical value. A model may perform well on a retrospective benchmark yet fail at another institution, under a changed imaging protocol, or when embedded in a real workflow. Readers should therefore separate four questions:

1. **Technical performance:** Does the model predict the reference labels on representative data?
2. **Clinical validity:** Does the output correspond to a clinically meaningful state or endpoint?
3. **Clinical utility:** Does using the system improve decisions, workflow, safety, outcomes, or resource use?
4. **Lifecycle safety:** Can performance, versions, failures, and changes be monitored after deployment?

The distinction matters because reviews of medical-imaging AI have repeatedly found high risk of bias, limited external validation, and weak evidence of prospective clinical impact despite strong reported discrimination \[[Nagendran et al., 2020](https://doi.org/10.1136/bmj.m1328)\].

## Where AI Enters the Radiotherapy Pathway

AI methods have been studied across imaging, contouring, registration, treatment planning, quality assurance, outcome modeling, and workflow orchestration \[[Barragán-Montero et al., 2022](https://doi.org/10.1088/1361-6560/ac678a)\]. Examples include:

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

### From a lifecycle map to readiness decisions

The lifecycle says **what work exists**; a readiness framework says **what evidence is sufficient to pass a gate**. These are related but not interchangeable. A model can be technically sophisticated while its labels are poorly justified, its clinical workflow is undefined, or its regulatory path is unresolved. Progress should therefore be recorded as a set of evidence-backed readiness decisions, not as time spent on a project or a single headline score.

Three complementary tools help teams ask different questions:

| Tool | Question it answers | What it contributes | What it does **not** establish |
|---|---|---|---|
| **Machine Learning Technology Readiness Levels (MLTRL)** | Is the ML technology engineered and evidenced well enough to move from research toward operation? | Levels 0–9, gated reviews, requirements and risk records, progressive testing, TRL cards, and monitoring; the system inherits the readiness of its least-ready component \[[Lavin et al., 2022](https://doi.org/10.1038/s41467-022-33128-9)\] | clinical benefit, local workflow fitness, regulatory authorization, or commercial viability |
| **Model card** | What is this model version intended to do, where was it evaluated, and where should it not be used? | A concise, versioned record of intended and out-of-scope uses, evaluation conditions, subgroup performance, limitations, and relevant ethical considerations \[[Mitchell et al., 2019](https://doi.org/10.1145/3287560.3287596)\] | independent validation, a safety case, regulatory approval, or proof that users will benefit |
| **GAITS Healthcare Innovation Cycle** | Is the whole healthcare innovation maturing across the domains needed for adoption? | Ten Innovation Maturity Levels tracked in parallel across Clinical/Workflow, Market/Business, Regulatory, and Technical/Science domains \[[GAITS/CIMIT, n.d.](https://www.gaits.org/foundation)\] | ML-specific verification, model-level reporting, or permission to skip local commissioning |

#### MLTRL: readiness of the ML system

MLTRL adapts systems-engineering readiness levels to ML. It starts at level 0 with first principles and progresses through research, prototyping, productization, deployment, and level 9 operation. Movement between levels depends on reviewable evidence rather than model accuracy alone. Data pipelines, preprocessing, software, interfaces, and the model are treated as connected components; if one critical component remains immature, the assembled system is not made ready by the others. Reviews may also send a component back to an earlier level when evidence exposes a problem. This makes MLTRL useful for coordinating researchers, engineers, clinical specialists, and product owners without pretending that development is linear \[[Lavin et al., 2022](https://doi.org/10.1038/s41467-022-33128-9)\].

For a radiotherapy autocontouring system, for example, a strong segmentation model does not compensate for an untested DICOM import path or an unsafe hand-off to the treatment-planning system. Readiness evidence must cover the assembled workflow, its data dependencies, foreseeable failure modes, and operational monitoring.

#### Model cards: a durable description of one model version

A model card travels with a released model. At minimum, it should identify the model and version; intended users, patients, tasks, and settings; uses that are unsupported or out of scope; training and evaluation context; metrics and clinically relevant subgroup results; known limitations; and the conditions under which human review, abstention, or escalation is expected. The original proposal emphasizes evaluation across conditions and groups relevant to the intended application, not a generic declaration that a model is fair or safe \[[Mitchell et al., 2019](https://doi.org/10.1145/3287560.3287596)\].

The card should point to, rather than duplicate, the full data, validation, safety, and change-control records. It must be revised when a material model, preprocessing, input, intended-use, or evidence change creates a new version. A model card is therefore a communication and accountability artifact, not a substitute for testing.

#### GAITS: readiness of the healthcare innovation

GAITS implements CIMIT's Healthcare Innovation Cycle. Its ten Innovation Maturity Levels run from defining a clinical need through proof of concept, feasibility, value, clinical trials, validation, approval and launch, routine clinical use, and standard-of-care adoption. At every level, work is considered across four parallel domains: Clinical/Workflow, Market/Business, Regulatory, and Technical/Science \[[GAITS/CIMIT, n.d.](https://www.gaits.org/foundation)\].

This wider view exposes a common failure pattern: technical work races ahead while the clinical need, workflow, approvals, or route to sustainable delivery remains immature. For an AI contouring product, a credible technical prototype may still be far from adoption if no one has established who reviews edits, how errors are escalated, what evidence a regulator requires, or how deployment and support will be sustained.

#### How to use the tools together

Do not average the frameworks into one readiness score. Use the clinical lifecycle as the project map, MLTRL to gate the ML system's engineering maturity, a model card to communicate a particular model version, and GAITS to reveal cross-domain gaps in the healthcare innovation. Good machine learning practice adds total-product-lifecycle principles such as representative datasets, independence between training and test sets, evaluation of the human-AI team, clear user information, and monitoring of deployed models \[[FDA, Health Canada, and MHRA, 2021](https://www.fda.gov/media/153486/download)\].

A practical gate review should leave a traceable evidence pack: an intended-use statement; cohort, provenance, and label documentation; a reproducible model and software record; a current model card; technical, clinical, subgroup, robustness, and human-factors validation; a risk and fallback record; and deployment, monitoring, change, and retirement plans. The evidence pack grows and changes with the system. No single document proves readiness, and readiness in one institution or model version does not automatically transfer to another.

## Learning Paradigms

### Supervised Learning

Supervised learning estimates a mapping from inputs to labeled outputs. Classification predicts categories, regression predicts quantities, and segmentation predicts spatial labels. The label is a reference standard, not automatically truth: contours can vary between experts, outcomes can be missing or inconsistently defined, and historical approvals may encode local preference.

### Unsupervised and Self-supervised Learning

Unsupervised learning seeks structure without task labels, for example through clustering or lower-dimensional representations. Self-supervised learning constructs a training signal from the data themselves, such as predicting masked content or matching related views. These approaches can use large unlabeled collections, but downstream clinical validity still requires task-specific evaluation \[[He et al., 2020](https://doi.org/10.1109/CVPR42600.2020.00975)\].

### Semi-supervised Learning

Semi-supervised learning combines a smaller labeled set with a larger unlabeled set. It is attractive where expert annotation is expensive, but performance depends on whether the unlabeled cases represent the intended population and whether erroneous pseudo-labels reinforce model bias.

### Reinforcement Learning

Reinforcement learning estimates a policy for sequential actions using a reward signal. In radiotherapy research, the environment is generally a simulator or planning system rather than a patient. A reward based on dose metrics is only a proxy for clinical benefit, so a successful simulation does not by itself justify autonomous clinical use \[[Sutton and Barto, 2018](https://mitpress.mit.edu/9780262039246/reinforcement-learning/)\].

## Training and Evaluation Basics

Development data are used to fit parameters; validation data guide model selection; test data estimate performance after choices are fixed. Splits must occur at the unit that can leak information—usually the patient, and sometimes the institution or time period—not at the image slice or treatment fraction. External evaluation tests transport to a meaningfully different setting. The [validation chapter](../validation/validation.md) covers metrics, calibration, subgroup analysis, study design, and post-deployment monitoring.

Metric choice follows intended use. Accuracy can conceal failure in an uncommon class; overlap scores can conceal clinically important boundary errors; and mean dose error can conceal a localized hot spot. A useful evaluation therefore connects technical metrics to the failure modes and consequences of the actual task. TRIPOD+AI provides reporting guidance for prediction models that use regression or machine-learning methods \[[Collins et al., 2024](https://doi.org/10.1136/bmj-2023-078378)\].

## Reading Claims About Clinical AI

Treat evidence as a ladder rather than a binary label:

- **Development or benchmark evidence** shows feasibility on selected data.
- **External retrospective evidence** tests performance in data separated by place, time, or population.
- **Silent prospective evaluation** observes performance in the live data stream without influencing care.
- **Interventional evaluation** measures how the human-AI system changes decisions, workload, safety, or patient outcomes.
- **Post-deployment surveillance** tests whether benefit and safety persist as data, users, and software change.

Randomization is not appropriate for every technical question, but claims of clinical benefit require evidence that measures clinical use. Reporting should also make clear whether a study was single-center, retrospective, benchmark-only, or not specific to radiotherapy.

## Limitations and Responsible Use

Models learn associations present in their development data. They may exploit shortcuts, reproduce inequities, become miscalibrated under distribution shift, or encourage automation bias. Privacy protection, security, usability, accountability, and change control are therefore part of system performance rather than optional additions. WHO guidance frames health AI around autonomy, well-being and safety, transparency, accountability, inclusiveness, and sustainability \[[WHO, 2021](https://www.who.int/publications/i/item/9789240029200)\].

Clinical responsibility remains with appropriately qualified people and organizations. The right level of automation depends on intended use, failure consequence, detectability, time pressure, and the strength of independent checks.

## Current Research and Recent Advances

- **General-purpose and multimodal models:** Biomedical models increasingly combine images and language across multiple tasks. Their breadth does not establish radiotherapy utility; evaluation still has to cover volumetric RT data, treatment context, external sites, and consequential errors \[[Tu et al., 2024](https://doi.org/10.1038/s41591-024-03185-2)\]. _(added: 2026-07)_
- **AI-specific reporting guidance:** TRIPOD+AI and PROBAST+AI make reporting, risk of bias, fairness, and applicability more explicit for prediction models, shifting attention from headline performance to evidence quality \[[Collins et al., 2024](https://doi.org/10.1136/bmj-2023-078378); [Moons et al., 2025](https://doi.org/10.1136/bmj-2024-082505)\]. _(added: 2026-07)_
- **Lifecycle governance:** International good-machine-learning-practice principles emphasize representative data, human-AI team performance, clear user information, and monitoring of deployed models rather than one-time validation alone \[[FDA, Health Canada, and MHRA, 2021](https://www.fda.gov/media/153486/download)\]. _(added: 2026-07)_

## Knowledge Check

1. **Recall:** What is the difference between a trained model and a clinical AI system?
   - **Answer and reasoning:** A model maps inputs to outputs; the clinical system also includes data sources, preprocessing, interface, users, policy, monitoring, and fallback. Calling the model the system hides failure points and accountability. Review [What AI Means in This Book](#what-ai-means-in-this-book).
2. **Interpretation:** A paper randomly splits images from the same patient between training and testing. Why is the reported test score optimistic?
   - **Answer and reasoning:** Patient-specific anatomy can leak across the split, so the test set is not independent. More images do not fix this; splitting by image is the tempting but wrong shortcut. Review [Training and Evaluation Basics](#training-and-evaluation-basics).
3. **Application:** An autocontouring model has excellent Dice but no workflow study. What claim is justified?
   - **Answer and reasoning:** Only task-specific technical performance in the evaluated data is supported. Time savings, safer care, or patient benefit require separate evidence; inferring them from Dice is unsafe. Review [Reading Claims About Clinical AI](#reading-claims-about-clinical-ai).
4. **Safety:** A team says that publishing a model card proves its autocontouring model is ready for clinical deployment. Why is that claim wrong?
   - **Answer and reasoning:** A model card communicates intended use, evaluation context, performance, and limitations for a particular version; it does not independently validate the system or authorize use. MLTRL can expose immature ML components, while GAITS can expose lagging clinical/workflow, regulatory, or business work. All three still require claim-specific evidence and local governance. Review [From a lifecycle map to readiness decisions](#from-a-lifecycle-map-to-readiness-decisions).
5. **Lifecycle:** A deployed system's input distribution shifts after a scanner update. Is retraining the automatic next step?
   - **Answer and reasoning:** No. First contain risk, investigate the change, assess performance and workflow impact, and decide whether rollback, recalibration, revalidation, or retirement is appropriate. Blind retraining can hide the cause and introduce new failure. Review [Limitations and Responsible Use](#limitations-and-responsible-use).

## Recap

- **Objective 1:** Radiotherapy is a linked clinical and technical process in which AI may support perception, prediction, optimization, or quality control.
- **Objective 2:** AI is the umbrella field, machine learning estimates behavior from data, and deep learning uses multilayer neural networks.
- **Objective 3:** A clinical AI system moves from an intended question through data, splitting, training, validation, inference, deployment, monitoring, change, and retirement; failed evidence can send it backward. MLTRL gates ML-system maturity, model cards communicate a model version, and GAITS tracks the wider healthcare innovation across four parallel domains.
- **Objective 4:** Training fits parameters, development validation guides choices, a held-out test estimates frozen performance, and inference applies the pipeline to a new case. Patient separation prevents one person's information leaking between those roles.
- **Objective 5:** A technical score is not clinical benefit. Claims must separately support technical performance, clinical validity, clinical utility, and lifecycle safety.

**Important limitation and misconception:** A label is not automatically truth, a test set is not automatically external validation, and a high retrospective score does not authorize clinical use.

## References

- Atun R, Jaffray DA, Barton MB, et al. Expanding global access to radiotherapy. *The Lancet Oncology*. 2015. [DOI](https://doi.org/10.1016/S1470-2045%2815%2900222-3)
- Barragán-Montero A, Bibal A, Huet-Dastarac M, et al. Towards a safe and efficient clinical implementation of machine learning in radiation oncology by exploring model interpretability, explainability and data-model dependency. *Physics in Medicine & Biology*. 2022. [DOI](https://doi.org/10.1088/1361-6560/ac678a)
- Collins GS, Moons KGM, Dhiman P, et al. TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods. *BMJ*. 2024. [DOI](https://doi.org/10.1136/bmj-2023-078378)
- FDA, Health Canada, and Medicines and Healthcare products Regulatory Agency. *Good Machine Learning Practice for Medical Device Development: Guiding Principles*. 2021. [Primary guidance](https://www.fda.gov/media/153486/download)
- GAITS/CIMIT. *The Healthcare Innovation Cycle*. n.d. [Primary framework](https://www.gaits.org/foundation)
- He K, Fan H, Wu Y, Xie S, Girshick R. Momentum contrast for unsupervised visual representation learning. *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*. 2020. [DOI](https://doi.org/10.1109/CVPR42600.2020.00975)
- International Commission on Radiation Units and Measurements. *Prescribing, Recording, and Reporting Photon-Beam Intensity-Modulated Radiation Therapy (IMRT): ICRU Report 83*. 2010. [DOI](https://doi.org/10.1093/jicru/10.1.Report83)
- Lavin A, Gilligan-Lee CM, Visnjic A, et al. Technology readiness levels for machine learning systems. *Nature Communications*. 2022;13:6039. [DOI](https://doi.org/10.1038/s41467-022-33128-9)
- LeCun Y, Bengio Y, Hinton G. Deep learning. *Nature*. 2015. [DOI](https://doi.org/10.1038/nature14539)
- Mitchell M, Wu S, Zaldivar A, et al. Model cards for model reporting. *Proceedings of the Conference on Fairness, Accountability, and Transparency*. 2019. [DOI](https://doi.org/10.1145/3287560.3287596)
- Moons KGM, Damen JAA, Kaul T, et al. PROBAST+AI: an updated quality, risk of bias, and applicability assessment tool for prediction models using regression or artificial intelligence methods. *BMJ*. 2025;388:e082505. [DOI](https://doi.org/10.1136/bmj-2024-082505)
- Nagendran M, Chen Y, Lovejoy CA, et al. Artificial intelligence versus clinicians: systematic review of design, reporting standards, and claims of deep learning studies. *BMJ*. 2020. [DOI](https://doi.org/10.1136/bmj.m1328)
- Sutton RS, Barto AG. *Reinforcement Learning: An Introduction*. 2nd ed. MIT Press; 2018. [Publisher](https://mitpress.mit.edu/9780262039246/reinforcement-learning/)
- Tu T, Azizi S, Driess D, et al. Towards generalist biomedical AI. *Nature Medicine*. 2024. [DOI](https://doi.org/10.1038/s41591-024-03185-2)
- World Health Organization. *Ethics and Governance of Artificial Intelligence for Health*. 2021. [Primary guidance](https://www.who.int/publications/i/item/9789240029200)
