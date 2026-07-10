# 6: AI in Image Registration and Fusion

Image registration estimates a spatial relationship between images. In radiation oncology, that relationship may connect different modalities acquired for planning, daily images acquired for positioning, or images collected across a treatment course. Registration makes image fusion possible, but the transformation—not the blended display—is the clinically consequential output.

A registration result is always used for a purpose: transferring a contour, comparing anatomy, accumulating dose, positioning a patient, or guiding a decision. Its suitability must therefore be judged for that specific task and anatomical region. A visually convincing overlay is not, by itself, proof that the transformation is accurate where it matters [[1]](https://doi.org/10.1002/mp.12256).

The shared prerequisites for DICOM object linkage, frames of reference, world and voxel coordinates, resampling provenance, cohort construction, and patient-level splitting are defined in [Radiotherapy Data and Informatics Foundations](../medicalImaging/medicalImaging.md). This chapter focuses on estimating and validating spatial transformations.

## The Registration Problem

Let $F(x)$ be the fixed image and $M(x)$ the moving image. Registration estimates a transformation $T$ such that the transformed moving image $M(T(x))$ aligns with $F(x)$. A typical optimization problem is:

$$T^* = \arg\min_T \left[\mathcal{D}(F, M \circ T) + \lambda\mathcal{R}(T)\right]$$

Here, $\mathcal{D}$ measures image dissimilarity, $\mathcal{R}$ regularizes implausible transformations, and $\lambda$ balances image matching against transformation smoothness or physical plausibility.

Every registration has a defined direction. If $T$ maps fixed-image coordinates into moving-image coordinates for resampling, it may not be directly interchangeable with a transformation described as moving-to-fixed. Software conventions differ, so direction, coordinate frame, voxel spacing, orientation, and interpolation must be checked explicitly.

### Fixed and Moving Images

The **fixed image** defines the output coordinate system. The **moving image** is resampled into that system. Selection is task dependent. For example, an MRI may be moved to planning CT for target delineation, while a planning CT may be moved to a daily CBCT to propagate prior contours.

Resampling creates new voxel values. Linear or spline interpolation may be suitable for intensity images, while label maps generally require nearest-neighbor or specialized label interpolation to avoid inventing fractional class identifiers. Dose interpolation requires particular care because the physical meaning of accumulated dose also depends on how anatomy and mass are mapped.

## Transformation Models

### Rigid Registration

A three-dimensional rigid transformation has six degrees of freedom: three translations and three rotations. It preserves distances and angles. Rigid registration is appropriate when anatomy can reasonably be treated as one solid object, as in many cranial applications or initial patient positioning.

Rigid registration cannot represent organ deformation, filling changes, weight loss, respiration, or relative motion between structures. A global rigid fit may also hide local mismatch: excellent alignment of the bony pelvis does not guarantee alignment of the prostate, bladder, and rectum.

### Affine Registration

An affine transformation adds scale and shear. It can compensate for global differences in size or acquisition geometry but does not model localized deformation. In clinical use, non-rigid scaling of anatomy should have a clear rationale; otherwise it may create a plausible-looking but anatomically misleading match.

### Deformable Image Registration

Deformable image registration (DIR) estimates a spatially varying displacement or velocity field. Common conventional representations include B-splines, optical-flow-like fields, demons algorithms, and diffeomorphic transformations.

A useful deformation should satisfy more than image similarity. Depending on the use case, desirable properties include:

- smoothness within deformable tissue;
- preservation of topology;
- invertibility or inverse consistency;
- low rates of folding, often assessed through the Jacobian determinant;
- appropriate behavior at sliding interfaces;
- plausible handling of appearance, disappearance, resection, and filling changes.

No regularizer makes every anatomical change correspond one-to-one. Tumor regression, atelectasis resolution, bowel gas, and surgical change can violate the assumptions of a continuous mapping.

## Monomodal and Multimodal Similarity

### Monomodal Registration

Images from the same modality often have related intensity patterns. Sum of squared differences assumes corresponding intensities should be similar. Normalized cross-correlation is more tolerant of linear intensity changes and is frequently used for CT-to-CT or MR sequence registration after appropriate preprocessing.

Even within one modality, acquisition changes can break these assumptions. Planning CT and CBCT differ in scatter, artifacts, field of view, and intensity reliability. Contrast phase, reconstruction kernel, metal artifacts, and motion can also dominate a similarity metric.

### Multimodal Registration

CT, MRI, and PET depict different tissue properties, so corresponding anatomy need not have similar intensity. Mutual information and normalized mutual information measure statistical dependence rather than direct equality and are widely used for multimodal registration.

Learned modality-invariant features and image-synthesis methods offer alternatives. A network may learn representations in which corresponding CT and MR anatomy are close, or synthesize one modality before registration. These approaches can improve optimization but introduce dependence on the training distribution and may create or suppress image features. Synthesized images should not be mistaken for observations.

## Conventional Registration Workflow

A robust conventional workflow usually includes:

1. verifying patient identity, image orientation, spacing, and frame of reference;
2. selecting the anatomically relevant region of interest;
3. preprocessing, such as bias correction, masking, or artifact management;
4. obtaining an initial alignment;
5. optimizing from coarse to fine resolution;
6. resampling the required images, labels, or other objects;
7. evaluating the result for the intended clinical task;
8. recording the software, settings, direction, reviewer, and approval state.

Initialization matters. Similarity objectives can contain local optima, and a method may converge to the wrong anatomical match when images have limited overlap or repeated structures.

## Learning-Based Registration

### Direct Transformation Prediction

Learning-based methods can train a neural network to predict transformation parameters or a dense deformation field from an image pair. VoxelMorph established a widely used formulation in which a convolutional network estimates the field and is trained with image similarity plus deformation regularization, optionally using auxiliary segmentations [[2]](https://doi.org/10.1109/TMI.2019.2897538). Once trained, inference can be substantially faster than pairwise iterative optimization.

Fast inference is especially attractive for online adaptive radiotherapy. It does not guarantee safe generalization: unusual anatomy, implants, truncated images, protocol changes, or disease outside the training distribution can produce confident but incorrect transformations.

### Supervised, Weakly Supervised, and Unsupervised Training

- **Supervised methods** use known transformations or reference deformation fields. Real clinical ground truth is rarely available, so simulated fields may not represent clinical deformation.
- **Weakly supervised methods** use corresponding landmarks or segmentations. They optimize clinically meaningful alignment but inherit annotation variability.
- **Unsupervised methods** optimize intensity or feature similarity without ground-truth transformations. They are easier to scale but may learn shortcuts that improve the loss without producing anatomically correct correspondence.

Hybrid losses commonly combine image similarity, contour overlap, landmark error, smoothness, inverse consistency, and penalties on non-positive Jacobians. The chosen loss defines what the model is rewarded for; validation must measure clinically relevant properties that are not fully represented in that loss.

### Probabilistic and Uncertainty-Aware Methods

Probabilistic registration represents a distribution over plausible transformations rather than a single field. Uncertainty maps may identify ambiguous regions, but they require calibration. Low predicted uncertainty is not evidence of correctness under distribution shift. Operational use should combine model uncertainty with deterministic checks and expert review.

### Transformer and Sequence Models

Attention-based models can capture long-range spatial relationships, while cascaded networks refine coarse fields progressively. For longitudinal radiotherapy, sequence models can use multiple treatment images rather than registering every fraction independently. Seq2Morph, for example, incorporated temporal information from weekly CBCTs and reported faster inference than an iterative comparator in a 50-patient study [[3]](https://pubmed.ncbi.nlm.nih.gov/36303270/).

## Clinical Applications

### MR-CT Registration for Target Delineation

Planning CT provides geometry and density information, while MRI often offers superior soft-tissue contrast. Rigid MR-CT registration is common for brain and other relatively rigid anatomy. In pelvis, head and neck, or abdomen, differences in positioning, distortion, and organ filling can create local mismatch.

The reviewer should check the target and adjacent organs—not only prominent bony landmarks. MRI geometric distortion, slice thickness, acquisition orientation, and time between studies must be considered. Deformable registration may improve local alignment but can also distort disease boundaries that are visible on only one modality.

### PET-CT and Functional Image Fusion

PET may inform target definition or biological interpretation. Registration must account for the lower spatial resolution of PET, respiratory mismatch, uptake time, and the fact that functional boundaries are not equivalent to anatomical boundaries. Thresholded uptake should not be treated as a geometric ground truth.

### 4D-CT and Motion Management

Four-dimensional CT sorts image data into respiratory phases. Registration between phases supports motion estimation, contour propagation, ventilation imaging research, and dose accumulation. Lung registration is difficult near sliding pleural surfaces, low-contrast regions, and anatomy affected by artifacts or disease.

Learning-based 4D-CT methods have used recursive cascades and full-resolution residual networks, demonstrating active progress on public and institutional datasets [[4]](https://pubmed.ncbi.nlm.nih.gov/38023695/). Clinical use still requires patient-specific plausibility checks because respiratory irregularity and 4D-CT sorting artifacts can corrupt the assumed correspondence.

### Adaptive Radiotherapy

DIR can propagate contours from planning CT to daily CBCT or MRI, initialize recontouring, and map dose between fractions. The propagated contour is a draft, not a new observation. Dose accumulation adds further assumptions about deformation, tissue correspondence, interpolation, and changing mass. The uncertainty of the accumulated quantity may be larger than the apparent smoothness of its display.

## Validation and Quality Assurance

AAPM Task Group 132 recommends evaluating registration and fusion software and communicating uncertainty in radiotherapy applications [[1]](https://doi.org/10.1002/mp.12256). Commissioning should include representative anatomical sites, modalities, transformation magnitudes, artifacts, and intended downstream uses.

### Evaluation Methods

No single metric is sufficient. Useful measures include:

- **Target registration error (TRE):** distance between corresponding landmarks after registration;
- **Dice similarity coefficient:** overlap of corresponding structures;
- **Surface distance and Hausdorff distance:** boundary agreement;
- **Jacobian determinant:** local expansion, contraction, and folding;
- **inverse-consistency error:** disagreement between forward and reverse transformations;
- **visual assessment:** structured review in relevant planes and regions;
- **task-based impact:** changes in contours, dose, or clinical decisions.

Dice can remain high for a large organ despite a clinically important focal error. Landmark error samples only annotated locations. Smooth Jacobians can accompany wrong correspondence. The validation set should therefore combine complementary measures and clinically meaningful failure cases.

### Patient-Specific Review

Before a transformation drives care, the user should inspect alignment at the relevant anatomy, review known failure regions, and confirm that the transformation is appropriate for the intended use. A registration accepted for image viewing may be unsuitable for contour propagation, and one accepted for contour propagation may be unsuitable for dose accumulation.

## Current Research and Recent Advances

- **Longitudinal learning:** Sequence-aware registration models are beginning to use the ordered anatomy of a radiotherapy course, rather than treating every image pair independently. Seq2Morph demonstrated this approach for planning CT and weekly CBCT registration, while emphasizing the need for broader validation [[3]](https://pubmed.ncbi.nlm.nih.gov/36303270/). _(added: 2026-07)_
- **Coarse-to-fine learned deformation:** Cascaded and transformer-based architectures seek larger capture ranges and finer local correspondence. Recent 4D-CT work reports gains over selected iterative and learning-based baselines, but most evidence remains dataset-specific [[4]](https://pubmed.ncbi.nlm.nih.gov/38023695/). _(added: 2026-07)_
- **Clinical emphasis on uncertainty and task validity:** The central research problem is shifting from producing a visually smooth warp to showing that a transformation is plausible, generalizes across sites, and is safe for a defined downstream task. TG-132's task-specific QA principles remain directly relevant to learned methods [[1]](https://doi.org/10.1002/mp.12256). _(added: 2026-07)_

## Recap

Image registration estimates spatial correspondence; fusion merely displays information using that estimate. Rigid, affine, and deformable models serve different anatomical assumptions, while monomodal and multimodal problems require different similarity strategies. Learning-based registration can greatly reduce inference time and learn useful features, but it does not remove ambiguity, artifacts, or the need for commissioning and patient-specific review. Validation must be task-specific and use complementary geometric, physical, and clinical measures.

## References

1. Brock KK, Mutic S, McNutt TR, Li H, Kessler ML. Use of image registration and fusion algorithms and techniques in radiotherapy: Report of AAPM Task Group No. 132. *Medical Physics*. 2017;44(7):e43-e76. [DOI](https://doi.org/10.1002/mp.12256)
2. Balakrishnan G, Zhao A, Sabuncu MR, Guttag J, Dalca AV. VoxelMorph: A learning framework for deformable medical image registration. *IEEE Transactions on Medical Imaging*. 2019;38(8):1788-1800. [DOI](https://doi.org/10.1109/TMI.2019.2897538)
3. Li X, et al. Seq2Morph: A deep learning deformable image registration algorithm for longitudinal imaging studies and adaptive radiotherapy. *Medical Physics*. 2023;50(1):274-287. [PubMed](https://pubmed.ncbi.nlm.nih.gov/36303270/)
4. Fu Y, et al. 4D-CT deformable image registration using unsupervised recursive cascaded full-resolution residual networks. *Medical Physics*. 2024;51(2):1037-1051. [PubMed](https://pubmed.ncbi.nlm.nih.gov/38023695/)
