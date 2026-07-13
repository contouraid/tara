AI in RadioTherapy 101
===================================

**ART101 (Artificial Intelligence in Radiotherapy 101)** is a set of notes on how artificial intelligence is used across the radiotherapy workflow today — what it does well, where the evidence is thin, and how to read a claim critically. It is written for radiation oncologists, medical physicists, dosimetrists, and the engineers and data scientists who build tools alongside them. No single background is assumed: the early chapters build the shared vocabulary, and later chapters apply it to specific steps in the clinical pathway.

A guiding theme runs through every chapter: **a model's technical score is not the same as clinical benefit.** Each topic is therefore presented with its methods *and* the standard of evidence needed to trust it in practice.

## Audience, assumed knowledge, and proficiency

ART101 is for three overlapping audiences: clinicians and clinical trainees who assess or use artificial intelligence (AI), medical physicists and dosimetrists who commission and supervise technical systems, and engineers or data scientists who build them. Complete beginners are also welcome. The book assumes only secondary-school mathematics, comfort reading a technical diagram, and willingness to follow links when a term is unfamiliar. It does **not** assume programming, machine-learning, imaging, or radiotherapy experience.

After completing the route appropriate to their role, a proficient reader should be able to:

1. map an AI use case to the radiotherapy pathway, its data, accountable users, and potential patient consequence;
2. explain training, validation, inference, deployment, monitoring, and retirement without confusing a model with the complete clinical system;
3. distinguish technical performance, clinical validity, clinical utility, and lifecycle safety;
4. identify leakage, weak reference standards, distribution shift, automation bias, and missing workflow controls in a study or product claim;
5. ask for the evidence, governance, and independent checks appropriate to an intended use; and
6. communicate across clinical and technical roles using the [cross-book glossary](resources/glossary.md).

## Choose a reader route

The routes are recommendations, not gates. Every chapter begins with its own prerequisites, learning objectives, and route note, so readers can enter selectively and return to missing foundations.

| Route | Start with | Recommended order | You are ready to branch when... |
|---|---|---|---|
| **Complete beginner** | No prior domain knowledge | Chapters 1 → 3 → 4 → 2, then 5–12 in order | you can narrate the radiotherapy and AI lifecycles and distinguish data, labels, features, model outputs, and clinical decisions |
| **Clinician or clinical trainee** | Basic clinical training; no coding required | Chapters 1 → 2 (concepts and architectures selectively) → 4 → 5–9 → 10 → 11 → 12; use Chapter 3 to fill radiotherapy gaps | you can state an intended use, challenge a validation claim, and name the human review and escalation needed for a model output |
| **Physicist, engineer, or data scientist** | Basic quantitative reasoning; programming helps but is not required | Chapters 1 → 3 → 4 → 2 → 5–10 → 11 → 12 | you can trace clinical intent into data and labels, prevent patient-level leakage, and connect technical failure to workflow and patient risk |

Readers evaluating a single application may read Chapters 1, 3, 4, the relevant application chapter, and Chapters 10–12 as a minimum safe route. A route is complete only when its reader can meet the proficiency statements above; finishing pages is not itself proficiency.

(recurring-cases)=
## Recurring cases

Three deliberately simplified cases recur throughout the book. They give every role the same patient and system context while the chapter-specific question changes. Their fixed anatomy, metadata, failure injections, safe responses, and capstone are in the [Synthetic Casebook and Capstone](resources/cases.md).

| Case | Clinical thread | Questions to carry forward |
|---|---|---|
| **Case A — Head-and-neck curative course** | Planning computed tomography (CT) and magnetic resonance imaging (MRI), target and organ-at-risk contours, intensity-modulated radiotherapy plan, image guidance, and toxicity follow-up | Can images and structures be registered safely? Are autocontours acceptable? Does a dose or toxicity prediction change a decision? |
| **Case B — Lung stereotactic treatment** | Four-dimensional CT, respiratory motion, a small target, stereotactic planning, pretreatment checks, and on-treatment anatomy | How do motion and geometry affect labels, uncertainty, dose, quality assurance, and stop rules? |
| **Case C — Pelvic adaptive workflow** | Daily imaging, anatomy change, propagated contours, re-optimization, rapid review, delivery, and longitudinal monitoring | Which steps may be automated, who approves each transition, and what happens when inputs drift or the service is unavailable? |

These are synthetic learning devices, not protocols or patient-specific recommendations. Each chapter's opening route note points to the cases it develops, and each chapter ends with a five-question knowledge check with reasoned answers.

## How this book is organized

The chapters move from foundations, to the imaging data everything depends on, to AI applied at each stage of care, and finally to the cross-cutting concerns of validation and clinical integration.

### Foundations

**[1: Introduction](intro/intro.md)** — Establishes the shared vocabulary (AI, machine learning, deep learning), the learning paradigms, and the "ladder of evidence" used to judge clinical AI claims. Read this first; every later chapter leans on its framing of technical performance versus clinical utility.

**[2: Fundamentals of AI through Deep Learning](fundamentalAI/index.md)** — Covers the machine-learning and deep-learning ideas that recur throughout the book: model training and evaluation, neural networks, convolutional architectures, language models, generative AI, agents, and vision-language models. Included so that readers can follow *how* the clinical tools in later chapters actually work, rather than treating them as black boxes.

**[3: Fundamentals of Radiation Oncology](fundamentalRO/fundamentalRO.md)** — A compact primer on radiation physics, radiobiology, and how a course of treatment is delivered. Included so that readers from a computing background understand the clinical problem AI is being asked to help with, and why safety margins matter.

### The data foundation

**[4: Medical Imaging in Radiation Oncology](medicalImaging/medicalImaging.md)** — Imaging modalities (computed tomography, magnetic resonance imaging, and positron emission tomography), acquisition and reconstruction, and Digital Imaging and Communications in Medicine (DICOM) / DICOM radiotherapy (DICOM-RT) objects that tie a treatment course together. Included because almost every AI method in radiotherapy is built on this imaging data, and its structure and quality set the ceiling on what any model can achieve.

### AI across the workflow

These chapters follow the treatment pathway in order, each pairing the methods with case studies and their evidence base.

**[5: AI for Contouring](contouring/contouring.md)** — Automated delineation of targets and organs at risk with U-Net-style and foundation segmentation models. Included as the most clinically mature application of AI in radiotherapy, and a useful lens on the shift from *producing* contours to *reviewing* them.

**[6: AI in Image Registration and Fusion](registration/registration.md)** — Aligning images across modalities and time points, and the learning-based methods that improve on classical registration. Included because registration underpins multimodal planning, adaptive therapy, and much of the contouring and dose work in the surrounding chapters.

**[7: AI for Treatment Planning](treatmentPlanning/treatmentPlanning.md)** — Dose prediction, knowledge-based and automated planning, and optimization for intensity-modulated radiotherapy (IMRT) and volumetric modulated arc therapy (VMAT). Included because planning is among the most time-consuming steps in the workflow and one where AI's efficiency gains are most tangible.

**[8: Clinical Prediction, Radiomics, and Causal Inference](clinicalPrediction/clinicalPrediction.md)** — Clinical endpoints, radiomics and dosiomics, toxicity and control modeling, longitudinal and multimodal biomarkers, and the distinction between prognosis, treatment-effect prediction, and causal claims. Included because estimating risk is not the same as knowing which treatment will improve an outcome.

**[9: AI for Quality Assurance and Safety](qa/qa.md)** — Automated error detection, plan and contour checking, and the regulatory context for AI tools. Included because quality assurance (QA) is where AI both helps *and* introduces new failure modes, making it central to safe deployment.

### Getting it into the clinic

**[10: Validation and Evaluation of AI Models](validation/validation.md)** — Performance metrics, clinical validation, subgroup analysis, and post-deployment monitoring. Included as the practical companion to the introduction's evidence framing — the "how do I actually check this?" chapter.

**[11: Integration of AI into Clinical Workflow](workflow/workflow.md)** — Workflow analysis, user training and acceptance, and change management. Included because a model only creates value once it is embedded in real clinical practice, and most implementation failures are organizational rather than technical.

### Responsibility across the lifecycle

**[12: Responsible AI, Regulation, and Security](responsibleAI/responsibleAI.md)** — The cross-cutting counterpart to the workflow chapters: accountability, the AI lifecycle from intended use to retirement, fairness and health equity, transparency and liability, cybersecurity for connected clinical systems, and how regulation and privacy law differ by jurisdiction. Included as the canonical home for governance, regulatory, and security concerns that the earlier chapters touch locally and link to here, distinguishing binding law from voluntary standards and professional guidance.

## Resources and further reading

A companion **[Resources](resources/index.md)** page collects open-source software for working with radiotherapy data (image I/O, visualization, treatment planning systems, and QA tools) along with external courses and workshops on AI in radiation therapy.

The **[Cross-book Glossary](resources/glossary.md)** is the canonical vocabulary for AI, statistics, imaging, DICOM-RT, radiotherapy, validation, safety, deployment, and regulation. Chapters expand abbreviations at first use and link there instead of maintaining local glossaries.

The **[Synthetic Casebook and Capstone](resources/cases.md)** preserves the fixed facts for Cases A–C, injects clinically consequential failures, and provides a six-domain capstone rubric for planning a responsible local evaluation.

Each chapter closes with its own numbered **References** section, with a weblink to every cited source.

```{toctree}
:maxdepth: 2
:caption: Contents
:hidden:
intro/intro
fundamentalAI/index
fundamentalRO/fundamentalRO
medicalImaging/medicalImaging
contouring/contouring
registration/registration
treatmentPlanning/treatmentPlanning
clinicalPrediction/clinicalPrediction
qa/qa
validation/validation
workflow/workflow
responsibleAI/responsibleAI
resources/index
resources/glossary
resources/cases
```
