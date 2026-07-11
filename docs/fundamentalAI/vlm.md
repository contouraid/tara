# Vision Language Models

Vision-language models (VLMs) learn relationships between visual information and language. Instead of mapping an image only to a fixed class or segmentation mask, a VLM can connect visual features with free-text concepts, questions, reports, or instructions. This makes VLMs relevant to radiation oncology, where clinical reasoning routinely combines volumetric images with reports, prescriptions, contours, dose distributions, and longitudinal notes.

This page extends [Chapter 2](index.md). It assumes familiarity with convolutional neural networks (CNNs), transformers, attention, and transfer learning.

## From Vision-Only Models to Vision and Language

### Vision-Only Models

A conventional image classifier learns a function from pixels or voxels to a predetermined label. A segmentation model maps each pixel or voxel to a class. A vision transformer converts image patches into tokens and uses self-attention, but it remains vision-only if its training objective and inputs contain no language.

These models are powerful when the task is fixed and annotated examples are available. Their output space is constrained by the labels defined during development. Adding a new concept usually requires a new head, new labels, or new training.

### Language Models

A language model learns patterns over text tokens. A large language model can generate, summarize, classify, or reason over text, but a text-only model does not directly observe an image. A textual description inserted into its prompt is an interpretation produced by someone or something else.

### Vision-Language Models

A VLM includes a mechanism for connecting visual and textual representations. Its possible outputs include:

- image-text similarity scores;
- retrieval of matching reports or images;
- classification using natural-language labels;
- answers to questions about an image;
- captions or reports;
- grounded text linked to image regions;
- multimodal dialogue.

The defining feature is not a chat interface. It is learned coupling between the visual and language modalities.

## Core Architectural Patterns

### Dual-Encoder Models

A dual-encoder model uses one network for images and another for text. Both produce embeddings in a shared space. Training encourages matched image-text pairs to be close and unmatched pairs to be farther apart.

CLIP demonstrated the scale and transfer potential of this contrastive approach using natural-language supervision [[1]](https://proceedings.mlr.press/v139/radford21a.html). After training, a text prompt such as "an image containing pleural effusion" can be embedded and compared with an image embedding. This enables retrieval and zero-shot classification without a task-specific output class learned in the usual supervised way.

Dual encoders are computationally efficient for search because image and text embeddings can be precomputed. Their global embeddings may, however, miss fine spatial relationships and are not naturally generative.

### Fusion or Cross-Attention Models

Fusion models allow image and text tokens to interact through cross-attention or shared transformer layers. They can answer detailed questions and model relationships between words and image regions. The additional interaction is computationally heavier but useful for tasks requiring fine-grained multimodal reasoning.

### Visual Encoder Plus Language Decoder

Generative VLMs connect a visual encoder to an autoregressive language model. A projection or adapter converts image features into tokens the language model can use. The decoder then generates text conditioned on both the image and prompt.

Some systems freeze most pretrained components and train only an adapter; others fine-tune part or all of the model. Parameter-efficient tuning can reduce compute and data requirements, but it does not eliminate the need for domain-specific validation.

### Generalist Biomedical Models

Generalist models train across heterogeneous biomedical images and text, sometimes including radiology, pathology, dermatology, and scientific figures. The goal is reusable multimodal representations rather than one narrow task. Generality can improve transfer, but breadth does not guarantee performance on radiotherapy-specific volumetric data or safety-critical outputs.

## How VLMs Learn

### Contrastive Pretraining

Given a batch of image-text pairs, contrastive learning raises similarity for true pairs and lowers it for mismatched pairs. Large collections of images and associated reports provide supervision without requiring a separate manual class label for every concept.

Clinical reports are imperfect labels. They may omit normal findings, refer to prior studies, contain copied text, or describe information not visible in the image. Pair construction and report preprocessing materially affect what the model learns.

### Image-Text Matching

An image-text matching objective predicts whether a specific image and text belong together. Unlike a pure dual-encoder similarity objective, it may use deeper token-level interaction. Hard negative pairs—plausible but incorrect matches—can teach finer distinctions.

### Captioning and Next-Token Prediction

Generative training asks the model to predict report or caption tokens conditioned on visual input. Token-level likelihood rewards fluent reproduction of training text but does not directly guarantee factual correctness. A clinically serious hallucination can occur in an otherwise fluent, high-scoring report.

### Instruction Tuning

Instruction tuning trains the model to respond to prompts for tasks such as description, question answering, or comparison. The training data may be human-written, template-generated, or produced by another model. Synthetic instructions expand scale but can propagate errors and stylistic artifacts.

## Medical and Radiotherapy Data Challenges

### Volumetric and Multiseries Imaging

Many general VLMs assume one or a few two-dimensional images. Radiation oncology uses three-dimensional CT, multiple MRI sequences, PET-CT, 4D-CT phases, daily CBCT, and dose volumes. Flattening these data into selected slices can omit a lesion or spatial relationship.

Volumetric approaches must manage far more visual tokens. Strategies include 3D encoders, slice sampling, hierarchical pooling, region selection, and separate encoders for each series. The chosen strategy determines which information the language model can access.

### Spatial Coordinates and Orientation

Radiotherapy questions are spatial: whether a target overlaps an organ, where a hotspot lies, or how anatomy changed. A VLM must retain patient coordinate systems, orientation, voxel spacing, and relationships between image, contour, and dose grids. A model that sees only rendered screenshots may lose this information.

### DICOM and Structured Objects

Clinical context includes metadata and DICOM-RT objects, not just pixels. RT Structure Sets encode contours, RT Plan objects encode beams and prescriptions, and RT Dose objects encode dose grids. A multimodal system may need dedicated encoders or structured representations for these inputs rather than converting everything to prose.

### Longitudinal Context

Planning and adaptive decisions depend on change over time. Comparing planning CT, daily images, prior contours, and delivered dose requires reliable temporal ordering and registration. The model should distinguish an observed change from an apparent difference caused by acquisition or alignment.

### Privacy and Dataset Bias

Image-report pairs contain protected health information. De-identification must address DICOM metadata, burned-in annotations, free text, and linked identifiers. Public datasets are concentrated in selected modalities and institutions; chest radiographs are much more available than radiotherapy planning datasets. A model can therefore appear medically capable while having little relevant experience with radiotherapy.

## Potential Applications in Radiation Oncology

### Report and Documentation Drafting

A VLM could draft structured descriptions of simulation images, on-treatment imaging, or adaptive changes. It could also help assemble documentation from verified structured inputs. Every generated statement should remain traceable to source evidence and undergo clinical review.

Radiology report-generation research shows both promise and persistent evaluation difficulty. A 2025 expert study of chest-radiograph reports found performance varied by clinical setting and that clinically significant errors occurred in both AI- and human-written reports [[2]](https://doi.org/10.1038/s41591-024-03302-1). This is evidence for careful human-AI workflow evaluation, not for direct transfer to radiotherapy reporting.

### Multimodal Search and Retrieval

Shared embeddings can retrieve prior cases using an image, phrase, or combination of both. A clinician might search for patients with similar anatomy and a specified planning issue. Retrieval systems need controls against leakage of protected information and should show why a case matched.

### Visual Question Answering

A VLM may answer questions such as "Which side contains the target?" or "Does today's image show increased pleural fluid?" In treatment planning, more ambitious questions could involve contour presence, plan objectives, or dose-anatomy relationships.

Answers should distinguish direct observation from inference and cite the relevant image, slice, structure, or structured field. Free-form confidence language is not a calibrated probability.

### Multimodal Quality Assurance

Many radiotherapy errors are inconsistencies across modalities: a left-sided diagnosis with a right-sided plan, a prescription that does not match plan metadata, or a note that conflicts with an image or structure set. A VLM could surface such inconsistencies for review.

Safety favors constrained outputs and explicit evidence over unconstrained narrative. Deterministic rules should remain the primary check when the inconsistency can be specified exactly.

### Decision Support and Education

VLMs may help users navigate a complex case by organizing image and text evidence, retrieving guidelines, or generating educational explanations. They should not invent patient-specific recommendations or substitute for multidisciplinary clinical judgment. Retrieval sources, version dates, and uncertainty should be visible.

## Evaluation

### Retrieval and Classification

Retrieval can be evaluated with recall at $k$, precision at $k$, and ranking measures. Zero-shot classification uses sensitivity, specificity, predictive values, calibration, and subgroup analysis. Prompt wording and prompt selection are part of the model configuration and must be frozen for final evaluation.

### Generated Text

Lexical measures such as BLEU or ROUGE compare generated and reference wording. Semantically similar reports can use different words, and a fluent report can contain a crucial false finding. Clinical evaluation should include:

- factual correctness and completeness;
- false positive and false negative findings;
- laterality and anatomical location;
- temporal comparisons;
- severity and clinical consequence of errors;
- reader preference and editing time;
- performance of the human-VLM team.

The 2024 review by Hartsock and Rasool highlights the lack of adequate standardized evaluation and limited medical VLM datasets [[3]](https://doi.org/10.3389/frai.2024.1430984).

### Grounding

If a model claims to ground text in an image, evaluate localization with bounding boxes, masks, landmarks, or expert assessment. Attention maps alone are not proof that the generated claim was based on the highlighted region.

### Hallucination and Abstention

Hallucination is generation not supported by the input or reliable external evidence. Test adversarial and incomplete cases, conflicting modalities, absent findings, unusual anatomy, and out-of-distribution inputs. A safe model should identify when required information is unavailable and abstain according to a defined policy.

### External and Prospective Evaluation

Performance should be tested across institutions, devices, protocols, patient groups, and disease sites. Retrospective model-alone evaluation is insufficient for deployment. Prospective studies should measure the full workflow: decision quality, time, corrections, reliance, and safety events.

## Safety and Governance

### Constrain the Task

Broad prompts invite broad failure. Define supported inputs, questions, outputs, and prohibited uses. Prefer structured fields for safety-critical information and require explicit confirmation before downstream action.

### Preserve Provenance

Record the model and prompt version, visual inputs, text context, retrieved sources, output, edits, approver, and timestamps. Generated text should not be copied into the clinical record without its review state being clear.

### Protect Against Prompt and Retrieval Risks

Clinical text can contain instructions that were never intended to control a model. Systems that retrieve external or internal documents must separate data from executable instructions, restrict tools and permissions, and validate outputs before writing to clinical systems.

### Monitor the Human-VLM System

Monitor edit distance, factual corrections, rejected outputs, unsupported claims, subgroup performance, latency, and safety reports. A decline in editing does not automatically mean improvement; it may reflect automation bias.

## Current Research and Recent Advances

- **Generalist biomedical VLMs:** Models trained across diverse biomedical image-text tasks show that one multimodal representation can support classification, retrieval, question answering, and generation. Their radiotherapy relevance remains a transfer hypothesis until evaluated on volumetric RT data and clinical tasks [[4]](https://doi.org/10.1038/s41591-024-03185-2). _(added: 2026-07)_
- **Clinician-VLM collaboration:** Expert evaluation of Flamingo-CXR reports showed that comparative quality varied across clinical settings and that both model and clinician reports contained consequential errors. This supports evaluating collaboration and correction workflows rather than model fluency alone [[2]](https://doi.org/10.1038/s41591-024-03302-1). _(added: 2026-07)_
- **Evaluation is lagging capability:** Recent medical VLM reviews consistently identify limited dataset diversity, weak standardized clinical metrics, privacy constraints, and insufficient external validation as major barriers [[3]](https://doi.org/10.3389/frai.2024.1430984). _(added: 2026-07)_

## Recap

Vision-language models connect visual and textual representations through contrastive alignment, cross-attention, or generative language decoding. Unlike vision-only CNNs or transformers, they can retrieve with natural-language concepts, answer questions, and generate text. Radiation oncology offers valuable multimodal use cases but also difficult volumetric, spatial, longitudinal, privacy, and safety requirements. Clinical value must be demonstrated through grounded factual evaluation and prospective human-VLM workflow studies, with constrained use and full provenance.

## References

1. Radford A, Kim JW, Hallacy C, et al. Learning transferable visual models from natural language supervision. *Proceedings of the 38th International Conference on Machine Learning*. 2021. [PMLR](https://proceedings.mlr.press/v139/radford21a.html)
2. Tanno R, Barrett DGT, Sellergren A, et al. Collaboration between clinicians and vision-language models in radiology report generation. *Nature Medicine*. 2025;31:599-608. [DOI](https://doi.org/10.1038/s41591-024-03302-1)
3. Hartsock I, Rasool G. Vision-language models for medical report generation and visual question answering: a review. *Frontiers in Artificial Intelligence*. 2024;7:1430984. [DOI](https://doi.org/10.3389/frai.2024.1430984)
4. Zhang S, Xu Y, Usuyama N, et al. A generalist vision-language foundation model for diverse biomedical tasks. *Nature Medicine*. 2024;30:3129-3141. [DOI](https://doi.org/10.1038/s41591-024-03185-2)
