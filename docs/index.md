AI in RadioTherapy 101
===================================

**ART101 (AI in RadioTherapy 101)** is a set of notes on how artificial intelligence is used across the radiotherapy workflow today — what it does well, where the evidence is thin, and how to read a claim critically. It is written for radiation oncologists, medical physicists, dosimetrists, and the engineers and data scientists who build tools alongside them. No single background is assumed: the early chapters build the shared vocabulary, and later chapters apply it to specific steps in the clinical pathway.

A guiding theme runs through every chapter: **a model's technical score is not the same as clinical benefit.** Each topic is therefore presented with its methods *and* the standard of evidence needed to trust it in practice.

## How this book is organized

The chapters move from foundations, to the imaging data everything depends on, to AI applied at each stage of care, and finally to the cross-cutting concerns of validation and clinical integration.

### Foundations

**[1: Introduction](intro/intro.md)** — Establishes the shared vocabulary (AI, machine learning, deep learning), the learning paradigms, and the "ladder of evidence" used to judge clinical AI claims. Read this first; every later chapter leans on its framing of technical performance versus clinical utility.

**[2: Fundamentals of AI through Deep Learning](fundamentalAI/index.md)** — Covers the machine-learning and deep-learning ideas that recur throughout the book: model training and evaluation, neural networks, convolutional architectures, and the newer vision–language and foundation models. Included so that readers can follow *how* the clinical tools in later chapters actually work, rather than treating them as black boxes.

**[3: Fundamentals of Radiation Oncology](fundamentalRO/fundamentalRO.md)** — A compact primer on radiation physics, radiobiology, and how a course of treatment is delivered. Included so that readers from a computing background understand the clinical problem AI is being asked to help with, and why safety margins matter.

### The data foundation

**[4: Medical Imaging in Radiation Oncology](medicalImaging/medicalImaging.md)** — Imaging modalities (CT, MRI, PET), acquisition and reconstruction, and the DICOM/DICOM-RT data objects that tie a treatment course together. Included because almost every AI method in radiotherapy is built on this imaging data, and its structure and quality set the ceiling on what any model can achieve.

### AI across the workflow

These chapters follow the treatment pathway in order, each pairing the methods with case studies and their evidence base.

**[5: AI for Contouring](contouring/contouring.md)** — Automated delineation of targets and organs at risk with U-Net-style and foundation segmentation models. Included as the most clinically mature application of AI in radiotherapy, and a useful lens on the shift from *producing* contours to *reviewing* them.

**[6: AI in Image Registration and Fusion](registration/registration.md)** — Aligning images across modalities and time points, and the learning-based methods that improve on classical registration. Included because registration underpins multimodal planning, adaptive therapy, and much of the contouring and dose work in the surrounding chapters.

**[7: AI for Treatment Planning](treatmentPlanning/treatmentPlanning.md)** — Dose prediction, knowledge-based and automated planning, and optimization for IMRT/VMAT. Included because planning is among the most time-consuming steps in the workflow and one where AI's efficiency gains are most tangible.

**[8: AI for Quality Assurance and Safety](qa/qa.md)** — Automated error detection, plan and contour checking, and the regulatory context for AI tools. Included because QA is where AI both helps *and* introduces new failure modes, making it central to safe deployment.

### Getting it into the clinic

**[9: Validation and Evaluation of AI Models](validation/validation.md)** — Performance metrics, clinical validation, subgroup analysis, and post-deployment monitoring. Included as the practical companion to the introduction's evidence framing — the "how do I actually check this?" chapter.

**[10: Integration of AI into Clinical Workflow](workflow/workflow.md)** — Workflow analysis, user training and acceptance, and change management. Included because a model only creates value once it is embedded in real clinical practice, and most implementation failures are organizational rather than technical.

### Responsibility across the lifecycle

**[11: Responsible AI, Regulation, and Security](responsibleAI/responsibleAI.md)** — The cross-cutting counterpart to the workflow chapters: accountability, the AI lifecycle from intended use to retirement, fairness and health equity, transparency and liability, cybersecurity for connected clinical systems, and how regulation and privacy law differ by jurisdiction. Included as the canonical home for governance, regulatory, and security concerns that the earlier chapters touch locally and link to here, distinguishing binding law from voluntary standards and professional guidance.

## Resources and further reading

A companion **[Resources](resources/index.md)** page collects open-source software for working with radiotherapy data (image I/O, visualization, treatment planning systems, and QA tools) along with external courses and workshops on AI in radiation therapy.

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
qa/qa
validation/validation
workflow/workflow
responsibleAI/responsibleAI
resources/index
```
