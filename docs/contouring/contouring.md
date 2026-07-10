# 5: AI for Image Contouring

Accurate delineation of target volumes and organs at risk (OARs) is a critical and often time-consuming step in radiation therapy planning. Manual contouring is subject to inter-observer variability and can be a significant bottleneck in the clinical workflow. Deep learning, particularly convolutional neural networks (CNNs), has shown remarkable success in automating this process, offering the potential for increased efficiency, consistency, and accuracy.

Before constructing a contouring dataset, use the canonical [radiotherapy data and informatics foundations](../medicalImaging/medicalImaging.md): it covers RTSTRUCT/SEG provenance, physical geometry, contour rasterization, naming harmonization, patient-level splitting, and leakage-safe preprocessing.

## Contouring Fundamentals

Contouring in radiation oncology is fundamentally a segmentation task—assigning a label (e.g., tumor, specific OAR, background) to each voxel in a 3D medical image (typically CT or MRI). Understanding the different types of segmentation is essential for applying deep learning effectively.

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

The U-Net architecture, specifically designed for biomedical image segmentation, remains the cornerstone of many contouring applications. Its encoder-decoder structure with skip connections effectively combines multi-scale feature extraction with precise spatial localization.

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

While 2D U-Nets process images slice by slice, medical imaging data in radiation oncology is inherently 3D (CT, MRI volumes). V-Net extends the U-Net concept to fully 3D convolutions, allowing the network to directly leverage spatial context across slices.

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

Focal loss, originally proposed for object detection, modifies the standard cross-entropy loss to down-weight the contribution of easy-to-classify examples (often the abundant background voxels) and focus training on harder examples (often foreground voxels or boundary regions):

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

Dice Similarity Coefficient (DSC) and Intersection over Union (IoU) remain standard metrics for assessing overall overlap.

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

It is crucial to compare the performance of automated contouring models against the inherent variability observed between human experts. A model that achieves performance comparable to inter-observer agreement is often considered clinically acceptable.

Metrics like DSC, HD, and ASSD can be calculated between contours drawn by different clinicians on the same images to establish a baseline for human variability. The automated model's performance is then compared to this baseline.

Evaluating against multiple expert delineations (e.g., using the STAPLE algorithm to estimate a consensus ground truth) provides a more robust assessment than comparing against a single expert contour.

## Current Research in Auto-contouring

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

As deep learning models for auto-contouring continue to improve in accuracy and robustness, their integration into clinical workflows holds the potential to significantly enhance the efficiency and consistency of radiation therapy planning.

## Summary and References

This article provides an overview of the application of deep learning, particularly convolutional neural networks and attention-based models, for automating the contouring process in radiation therapy planning. It explains the fundamentals of medical image segmentation, discusses key architectures like U-Net, V-Net, and transformer-based models, and reviews various loss functions and evaluation metrics relevant to clinical practice. The article also highlights current research directions, including organ-at-risk and tumor volume segmentation, adaptive contouring, and quality assurance, emphasizing the challenges and advancements in integrating AI-driven auto-contouring into clinical workflows to improve efficiency, consistency, and accuracy in radiation oncology.

- [U-Net Paper](https://arxiv.org/abs/1505.04597)
- [V-Net Paper](https://arxiv.org/abs/1606.04797)
- ...
