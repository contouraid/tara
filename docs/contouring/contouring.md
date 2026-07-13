# 5: AI for Image Contouring

## Before you begin

**Prerequisites:** Read Chapters 1–4 or know the artificial intelligence (AI) lifecycle, U-Net concept, target and organ-at-risk roles, Digital Imaging and Communications in Medicine (DICOM) geometry, label provenance, and patient-level splitting. Use the [cross-book glossary](../resources/glossary.md).

**Learning objectives:** After this chapter, you should be able to:

1. distinguish binary, multiclass, semantic, and instance segmentation;
2. explain why U-Net, three-dimensional, attention, and foundation approaches may suit different contouring tasks;
3. choose loss and evaluation measures that expose overlap, boundary, small-structure, and clinical errors;
4. design an evaluation that accounts for observer variation, external data, expert editing, and downstream effects; and
5. specify review, quality-assurance, escalation, and monitoring controls for an autocontouring workflow.

**Reading route:** This is the first application chapter. Clinicians may focus on task definitions, evaluation, and integration; technical readers should include architectures and losses. Follow {ref}`Case A <recurring-cases>` for multimodal head-and-neck autocontouring and Case C for propagated contours in an adaptive workflow.

Target and organ-at-risk (OAR) delineation is a consequential, often time-consuming step in radiotherapy planning. Manual contours vary between observers, especially where boundaries depend on interpretation rather than a clearly visible interface [[1]](https://doi.org/10.1016/j.radonc.2016.09.019). Automated segmentation can reduce editing time for some structures and settings, but geometric agreement alone does not demonstrate clinical acceptability.

Before constructing a contouring dataset, use the canonical [radiotherapy data and informatics foundations](../medicalImaging/medicalImaging.md): it covers DICOM RT Structure Set (RTSTRUCT) and Segmentation (SEG) object provenance, physical geometry, contour rasterization, naming harmonization, patient-level splitting, and leakage-safe preprocessing.

## Contouring Fundamentals

Contouring in radiation oncology is fundamentally a segmentation task—assigning a label (e.g., tumor, specific OAR, background) to each voxel in a three-dimensional medical image, typically computed tomography (CT) or magnetic resonance imaging (MRI). Understanding the different types of segmentation is essential for applying deep learning effectively.

### Binary vs. Multi-class Segmentation

Binary segmentation involves distinguishing between two classes: the object of interest (foreground) and everything else (background). For example, segmenting a single OAR like the heart involves classifying each voxel as either "heart" or "not heart."

Multi-class segmentation extends this to multiple distinct classes simultaneously. In radiation oncology, this is common when contouring multiple OARs and potentially the target volume within the same image. The model must assign each voxel to one of several predefined classes (e.g., heart, lung, spinal cord, tumor, background).

Deep learning models for segmentation typically output a probability map for each class. For binary segmentation, a single output channel with sigmoid activation provides the probability of belonging to the foreground class. For multi-class segmentation, multiple output channels with softmax activation provide probabilities for each class, ensuring they sum to one for each voxel.

### Semantic vs. Instance Segmentation

Semantic segmentation assigns a class label to each voxel but does not distinguish between different instances of the same class. For example, if multiple lymph nodes are present, semantic segmentation would label all of them as "lymph node" without differentiating individual nodes.

Instance segmentation goes a step further by identifying and delineating each individual object instance. In the lymph node example, instance segmentation would provide a separate contour for each distinct node.

While most contouring tasks in radiation oncology currently rely on semantic segmentation (delineating specific organs or tumor volumes), instance segmentation could be relevant for tasks like identifying individual metastatic lesions or tracking multiple objects over time.

## Segmentation Architectures

Several deep learning architectures have proven particularly effective for medical image segmentation, building upon the foundational concepts of CNNs and attention mechanisms discussed in Module 4.

### U-Net and Variants

- U-Net
- Residual U-Net
- Attention U-Net
- U-Net++

The U-Net architecture was designed for biomedical image segmentation. Its encoder-decoder structure and same-scale skip connections combine contextual features with spatial localization [[2]](https://doi.org/10.1007/978-3-319-24574-4_28).

Key features of U-Net include:

Symmetric encoder-decoder paths: The encoder progressively reduces spatial resolution and increases feature channels, while the decoder symmetrically increases resolution and decreases channels.

Skip connections: Concatenating feature maps from the encoder to corresponding layers in the decoder allows the network to reuse high-resolution features, crucial for accurate boundary delineation.

Overlap-tile strategy (optional): For large images, U-Net can process overlapping patches and seamlessly combine the predictions.

Numerous variants have built upon the U-Net foundation:

Residual U-Net incorporates residual connections within the convolutional blocks, potentially improving gradient flow and enabling deeper networks.

Attention U-Net integrates attention gates into the skip connections, allowing the model to selectively focus on relevant features being passed from the encoder to the decoder.

U-Net++ uses nested and dense skip connections to further bridge the semantic gap between encoder and decoder features, potentially improving performance on complex segmentation tasks.

These U-Net based architectures form the backbone of many automated contouring systems used or investigated in radiation oncology clinics.

### V-Net for 3D Segmentation

While 2-D U-Nets process images slice by slice, CT and MRI are volumetric. V-Net extends encoder-decoder segmentation to 3-D and introduced a Dice-based objective in its original prostate-MRI evaluation [[3]](https://doi.org/10.1109/3DV.2016.79).

V-Net replaces 2D convolutions, pooling, and up-sampling operations with their 3D counterparts. It often incorporates residual connections within its convolutional blocks. By processing the entire 3D volume (or large 3D patches), V-Net can better capture the complex shapes and relationships of anatomical structures in three dimensions, potentially leading to more accurate and consistent segmentations compared to slice-by-slice 2D approaches.

The main challenge with 3D architectures like V-Net is the significantly increased computational cost and memory requirements due to the cubic growth in data size. This often necessitates processing smaller 3D patches or using techniques like downsampling to manage resource constraints.

### Attention-based Segmentation

Attention mechanisms, particularly self-attention as used in transformers, can enhance segmentation models by allowing them to capture long-range dependencies and focus on relevant image regions.

Several architectures incorporate attention:

Attention U-Net (mentioned earlier) uses attention gates in skip connections.

Transformer-based segmentation models like UNETR and Swin UNETR replace or augment parts of the U-Net architecture (typically the encoder) with transformer blocks. These models can capture global context more effectively than pure CNN approaches, which can be beneficial for segmenting large or complex structures.

Non-local networks incorporate self-attention modules within convolutional architectures to capture long-range spatial dependencies.

Attention mechanisms can help models better understand the global context of an image, differentiate between similar-looking tissues based on surrounding structures, and improve segmentation accuracy, particularly for challenging cases with ambiguous boundaries or anatomical variations.

## Loss Functions for Segmentation

The choice of loss function significantly impacts how a segmentation model learns and the quality of the resulting contours. Standard classification losses like cross-entropy can be suboptimal for segmentation, especially with imbalanced data.

- Dice Loss
- Focal Loss
- Boundary-aware Losses
- Combined Losses

### Dice Loss

Dice loss, derived from the Dice Similarity Coefficient (DSC), directly optimizes for overlap between the predicted and ground truth segmentations. It is defined as:

L_Dice = 1 - DSC = 1 - (2 * ∑(p_i * g_i) + ε) / (∑p_i + ∑g_i + ε)

Where p_i is the predicted probability for voxel i, g_i is the ground truth label (0 or 1), and ε is a small constant for numerical stability.

Dice loss is particularly effective for imbalanced segmentation tasks because it focuses on the agreement between foreground predictions and ground truth, regardless of the number of background voxels. It has become a standard loss function for medical image segmentation.

Variations like Generalized Dice Loss handle multi-class segmentation by weighting the contribution of each class based on its volume, preventing larger structures from dominating the loss.

### Focal Loss

Focal loss was proposed for dense object detection to down-weight well-classified examples; its use in segmentation is an adaptation whose value depends on the task and tuning [[4]](https://doi.org/10.1109/ICCV.2017.324):

L_Focal = -α(1-p_t)^γ * log(p_t)

Where p_t is the probability of the correct class, α balances class importance, and γ is the focusing parameter. Higher values of γ increase the focus on hard examples.

Focal loss can be effective in segmentation tasks with extreme class imbalance, helping the model learn to correctly classify rare foreground structures.

### Boundary-aware Losses

Accurate boundary delineation is often critical in radiation oncology. Boundary-aware losses explicitly penalize errors near the segmentation boundaries:

Boundary Loss computes the discrepancy between the predicted boundary and the ground truth boundary, often using distance transforms.

Weighted Cross-Entropy or Dice Loss can assign higher weights to voxels near the boundary, forcing the model to pay more attention to these critical regions.

Shape-aware losses incorporate prior knowledge about the expected shape of the structure being segmented, penalizing predictions that deviate significantly from plausible shapes.

### Combined Losses

In practice, combining multiple loss functions often yields the best results. Common combinations include:

Dice + Cross-Entropy: Balances overlap-based optimization with pixel-wise classification accuracy.

Dice + Focal Loss: Combines overlap optimization with focused learning on hard examples.

Adding boundary loss terms to Dice or cross-entropy losses to specifically improve boundary accuracy.

The optimal loss function or combination depends on the specific segmentation task, dataset characteristics, and clinical priorities for contouring accuracy.

## Evaluation Metrics for Contouring

Evaluating the performance of automated contouring models requires metrics that capture clinically relevant aspects of segmentation quality, going beyond simple overlap measures.

### Geometric Metrics

Dice Similarity Coefficient (DSC) and Intersection over Union (IoU) measure overlap but do not localize errors or encode their clinical consequence. Metric selection should follow the task's geometry and failure modes rather than convention alone [[5]](https://doi.org/10.1038/s41592-023-02151-z).

Hausdorff Distance (HD) measures the maximum distance between the surfaces of the predicted and ground truth contours, quantifying the largest boundary discrepancy. The 95th percentile HD (HD95) is often preferred as it is less sensitive to outliers.

Average Symmetric Surface Distance (ASSD) calculates the average distance between the surfaces, providing a measure of overall boundary agreement.

Volume Difference measures the percentage difference between the predicted and ground truth volumes, indicating whether the model tends to under- or overestimate the structure size.

### Clinical Acceptability Measures

While geometric metrics provide quantitative measures, clinical acceptability often involves more nuanced assessment:

Contour smoothness and regularity: Automated contours should ideally be smooth and anatomically plausible, without jagged edges or unrealistic shapes.

Boundary adherence: The contour should accurately follow the visible boundary of the structure in the image.

Inclusion of critical regions / Exclusion of nearby structures: The contour must reliably include the entire target or OAR while avoiding encroachment on adjacent critical structures.

Rating scales or qualitative assessments by expert clinicians are often used alongside geometric metrics to evaluate the clinical usability of automated contours. Studies may measure the percentage of automatically generated contours that require no edits, minor edits, or major edits by a clinician.

### Inter-observer Variability

Inter-observer agreement can contextualize model-reference agreement, but matching an average human overlap score is not sufficient to declare a contour clinically acceptable. The reference may contain systematic errors, and small geometric deviations can matter near critical interfaces [[1]](https://doi.org/10.1016/j.radonc.2016.09.019) [[5]](https://doi.org/10.1038/s41592-023-02151-z).

Metrics like DSC, HD, and ASSD can be calculated between contours drawn by different clinicians on the same images to establish a baseline for human variability. The automated model's performance is then compared to this baseline.

Evaluating against multiple expert delineations (e.g., using the STAPLE algorithm to estimate a consensus ground truth) provides a more robust assessment than comparing against a single expert contour.

## Current Research and Recent Advances

Research in deep learning for auto-contouring continues to advance rapidly, addressing remaining challenges and expanding capabilities.

### Organ-at-Risk (OAR) Contouring

Automated contouring of OARs is one of the most mature applications of deep learning in radiation oncology. Models have demonstrated high accuracy for many common OARs across different anatomical sites (head and neck, thorax, abdomen, pelvis).

Current research focuses on:

Improving robustness across different imaging protocols, scanners, and patient populations.

Handling challenging OARs with low contrast or ambiguous boundaries.

Developing models that can segment a comprehensive set of OARs simultaneously.

Integrating uncertainty estimation to flag contours that may require manual review.

Validating performance in large-scale, multi-institutional studies.

### Tumor Volume Delineation

Segmenting the gross tumor volume (GTV) and clinical target volume (CTV) is often more challenging than OAR contouring due to the variability in tumor appearance, infiltration patterns, and reliance on multi-modal imaging (e.g., PET-CT, MRI).

Research efforts include:

Developing multi-modal segmentation models that effectively fuse information from different imaging sources.

Incorporating prior knowledge about tumor growth patterns or anatomical constraints.

Addressing the significant inter-observer variability in tumor delineation.

Predicting microscopic tumor extension for CTV definition.

Using deep learning to identify tumor subregions with different biological characteristics (e.g., hypoxia, proliferation) based on imaging features (radiomics).

### Adaptive Contouring

During a course of radiation therapy, patient anatomy can change due to tumor shrinkage, weight loss, or organ motion. Adaptive radiotherapy requires re-contouring on images acquired during treatment (e.g., cone-beam CT).

Deep learning models are being developed for:

Deformable image registration to propagate initial contours to subsequent images.

Direct segmentation on daily or weekly images, potentially adapting to changes over time.

Predicting future anatomical changes to enable proactive plan adaptation.

Challenges include the lower image quality of cone-beam CT compared to planning CT and the need for rapid processing to enable online adaptation.

### Quality Assurance and Clinical Integration

A critical area of research involves developing methods for quality assurance (QA) of automated contours and facilitating safe clinical integration:

Developing AI-based QA tools that can automatically flag potentially erroneous contours for human review.

Quantifying the impact of auto-contouring on downstream treatment planning and predicted outcomes.

Designing optimal workflows that combine automated contouring with efficient human review and editing.

Establishing best practices for commissioning, validating, and monitoring auto-contouring systems in clinical practice.

Clinical integration should be evaluated as a human-AI workflow: editing time, consequential misses, downstream dosimetry, inter-user variation, and failures under distribution shift matter in addition to average overlap [[6]](https://doi.org/10.1016/j.phro.2020.10.001).

## Evidence Synthesis

The cited evidence agrees that geometric overlap alone is inadequate: boundary errors, editing patterns, anatomy, imaging quality, and the downstream use all change the clinical meaning of a score. Results are heterogeneous across structure sets, modalities, prompts, institutions, and reference contours, so performance for a common organ cannot be transferred to a tumor target or a new site without validation. MedSAM supplies an unusually large, diverse research resource, but its public benchmark performance remains proof of concept for radiotherapy until the exact target/OAR task and workflow are evaluated [[7]](https://doi.org/10.1038/s41467-024-44824-z).

| Task | Population / site | Data scale | Validation design | Comparator | Endpoint | Principal limitation | Maturity |
|---|---|---|---|---|---|---|---|
| Promptable medical-image segmentation [[7]](https://doi.org/10.1038/s41467-024-44824-z) | Multiple modalities and anatomical sites; not a dedicated RT cohort | 1,570,263 image-mask pairs across 10 modalities | Multi-dataset retrospective benchmark | Specialist segmentation methods and prompt settings | Segmentation geometry | Broad benchmark does not establish target/OAR acceptability, dosimetric safety, or RT workflow benefit | **Proof of concept** |
| Deep-learning OAR contour review [[6]](https://doi.org/10.1016/j.phro.2020.10.001) | Head-and-neck OARs at one clinical center | Single-center clinical cohort | Retrospective analysis of contours edited in routine practice | AI contour before versus after expert adjustment | Edit magnitude and location | No concurrent manual-only workflow comparator, patient endpoint, or external site | **Human-factors/workflow evaluation** |

Current citations support technical performance and a single-center editing analysis, but not general external validity, patient benefit, or a causal reduction in workload. No named-product regulatory claim is made here, and the cited set does not quantify representative routine adoption. Open research assets improve reproducibility, yet expert labels and clinical acceptance rules remain site-dependent. The main unanswered questions are which errors alter planning decisions or dose, how reliably prospective QA catches consequential failures, whether time savings persist without automation bias, and whether benefits transport across institutions and model updates. The cited evidence includes variable and occasionally large edits in difficult cases rather than a comparative harmful or null patient-outcome study; the next currency review should search explicitly for negative external and prospective workflow results.

- **Foundation-model adaptation:** Promptable segmentation models are being adapted to medical images, but performance varies by anatomy, modality, prompt, and adaptation strategy. Radiotherapy use remains benchmark evidence unless target/OAR evaluation and clinical review are reported [[7]](https://doi.org/10.1038/s41467-024-44824-z). _(added: 2026-07)_
- **Evaluation beyond a single overlap score:** Current validation guidance recommends selecting complementary metrics from the task's domain interest, error type, and properties rather than applying a fixed metric set [[5]](https://doi.org/10.1038/s41592-023-02151-z). _(added: 2026-07)_
- **Workflow endpoints:** Clinical studies increasingly measure correction burden and acceptability as well as geometry. These findings remain dependent on site, structure set, baseline workflow, and model version [[6]](https://doi.org/10.1016/j.phro.2020.10.001). _(added: 2026-07)_

## Recap

- **Objective 1:** Binary and multiclass segmentation differ in label count; semantic segmentation labels categories, whereas instance segmentation separates individual objects.
- **Objective 2:** U-Net preserves multiscale spatial detail, three-dimensional models use volumetric context, attention can connect distant regions, and foundation approaches may transfer broad representations—but suitability remains task-specific.
- **Objective 3:** Losses determine training incentives; overlap, surface, tail, small-structure, edit, and downstream dose measures expose different failures.
- **Objective 4:** Credible evaluation represents sites and devices, documents observer-derived labels, freezes the pipeline, measures expert correction and clinical consequence, and tests externally.
- **Objective 5:** Clinical use needs input checks, accountable expert review, escalation or fallback for failures, version control, and monitoring of edits and downstream effects.

**Important limitation and misconception:** A high Dice score does not prove that a contour is clinically acceptable; a small boundary error near a critical structure may matter more than a larger harmless disagreement elsewhere.

## References

1. Vinod SK, Jameson MG, Min M, Holloway LC. Uncertainties in volume delineation in radiation oncology: a systematic review and recommendations for future studies. *Radiotherapy and Oncology*. 2016. [DOI](https://doi.org/10.1016/j.radonc.2016.09.019)
2. Ronneberger O, Fischer P, Brox T. U-Net: convolutional networks for biomedical image segmentation. *MICCAI*. 2015. [DOI](https://doi.org/10.1007/978-3-319-24574-4_28)
3. Milletari F, Navab N, Ahmadi SA. V-Net: fully convolutional neural networks for volumetric medical image segmentation. *3DV*. 2016. [DOI](https://doi.org/10.1109/3DV.2016.79)
4. Lin TY, Goyal P, Girshick R, He K, Dollár P. Focal loss for dense object detection. *ICCV*. 2017. [DOI](https://doi.org/10.1109/ICCV.2017.324)
5. Maier-Hein L, Reinke A, Godau P, et al. Metrics reloaded: recommendations for image analysis validation. *Nature Methods*. 2024. [DOI](https://doi.org/10.1038/s41592-023-02151-z)
6. Brouwer CL, Boukerroui D, Oliveira J, et al. Assessment of manual adjustment performed in clinical practice following deep learning contouring for head and neck organs at risk in radiotherapy. *Physics and Imaging in Radiation Oncology*. 2020;16:54-60. [DOI](https://doi.org/10.1016/j.phro.2020.10.001)
7. Ma J, He Y, Li F, Han L, You C, Wang B. Segment anything in medical images. *Nature Communications*. 2024. [DOI](https://doi.org/10.1038/s41467-024-44824-z)
