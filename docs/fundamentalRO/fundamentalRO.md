# 3: Fundamentals of Radiation Oncology

Radiation oncology uses ionizing radiation to control or eradicate cancer while limiting injury to normal tissue. It is both a clinical specialty and a technical system: physicians define the therapeutic intent and target, medical physicists establish and verify the dosimetric chain, dosimetrists translate the prescription into a deliverable plan, and radiation therapists reproduce and deliver that plan. AI applications discussed elsewhere in this book operate inside this system, so their outputs must be understood in terms of dose, anatomy, biology, uncertainty, and clinical responsibility.

## Ionizing Radiation in Medicine

Ionizing radiation carries enough energy to remove electrons from atoms. In radiotherapy, the clinically useful result is energy deposition in tissue. That deposition damages cellular molecules directly and also creates reactive chemical species, particularly through interactions with water.

The principal treatment modalities are:

- **Photons:** high-energy x-rays produced by a linear accelerator or gamma rays from a radionuclide source. Photons can treat deep targets but deposit dose before and beyond the target.
- **Electrons:** charged particles with a finite useful range, commonly used for superficial lesions.
- **Protons and heavier ions:** charged particles that lose much of their energy near the end of their path. Their finite range can reduce exit dose, although range uncertainty must be managed.
- **Brachytherapy sources:** sealed radioactive sources placed in or near a target, producing a steep dose gradient governed strongly by distance.
- **Unsealed radionuclides:** radiopharmaceuticals that localize through physiological or molecular mechanisms and irradiate disease from within the body.

The IAEA radiation oncology physics handbook provides a comprehensive treatment of the machines, interactions, dosimetry, and safety systems behind these modalities [[1]](https://www-pub.iaea.org/MTCD/Publications/PDF/Pub1196_web.pdf).

### Absorbed Dose

Absorbed dose is energy imparted per unit mass:

$$D = \frac{dE}{dm}$$

Its SI unit is the gray (Gy), equal to one joule per kilogram. A prescribed dose is not a property of a machine setting alone. It depends on the beam energy and geometry, patient anatomy, tissue density, field modulation, and the dose-calculation model.

The aim is not simply to deliver a large dose. A plan must produce an acceptable spatial distribution: adequate target coverage, tolerable dose to organs at risk, and a deliverable arrangement that remains safe under realistic setup and motion uncertainties.

### How Photons Deposit Energy

Megavoltage photons used in external-beam radiotherapy interact mainly through Compton scattering over much of the clinically relevant energy range. The photon transfers energy to an electron, and the resulting secondary electron deposits energy along its path. This distinction explains why photon fluence, charged-particle transport, and absorbed dose are related but not interchangeable quantities.

Photon beams exhibit a build-up region below the surface because secondary electrons travel before depositing their energy. This skin-sparing effect is one reason megavoltage beams are useful for deep tumors. Beyond the depth of maximum dose, attenuation and geometric divergence reduce the dose with depth.

### Charged Particles and Range

Electrons lose energy continuously through interactions with matter and scatter substantially, limiting their use for deep, sharply bounded targets. Protons also lose energy along their path, but their stopping power rises near the end of the range, forming the Bragg peak. Multiple proton energies are combined into a spread-out Bragg peak to cover a target volume.

The sharp distal gradient of a proton field is valuable only when its position is understood. Conversion from CT numbers to stopping power, anatomical change, setup error, and motion all introduce range uncertainty. Robust planning therefore evaluates plausible uncertainty scenarios rather than assuming one perfectly known patient geometry.

## From Prescription to Delivery

### Simulation and Patient Model

The planning process begins with simulation. The patient is positioned in a reproducible treatment posture, immobilized when appropriate, and imaged over the required anatomy. Planning CT supplies geometry and electron-density information. MRI, PET, or other studies may be added to improve target or normal-tissue definition; these images must be aligned carefully with the planning image.

The resulting patient model contains:

- the external body contour;
- gross, clinical, and planning target volumes;
- organs at risk and planning risk volumes where used;
- image data used for material or density assignment;
- uncertainty assumptions, such as setup margins or motion envelopes.

The related imaging and registration concepts are developed in [Chapter 4](../medicalImaging/medicalImaging.md) and [Chapter 6](../registration/registration.md).

### Target Volumes and Margins

The **gross tumor volume (GTV)** represents visible or otherwise demonstrable disease. The **clinical target volume (CTV)** includes the GTV and/or tissue considered at risk of microscopic disease. The **planning target volume (PTV)** adds a geometrical margin intended to make the prescribed CTV dose sufficiently likely despite setup and internal-motion uncertainties.

A margin is not a correction for poor image quality or a substitute for understanding uncertainty. It encodes a specific uncertainty model. Adaptive radiotherapy may reduce some components by observing anatomy during treatment, but it also adds registration, contouring, replanning, and decision uncertainties.

### Treatment Planning

A treatment planning system calculates dose and helps optimize machine parameters. In three-dimensional conformal radiotherapy, field shapes and weights are chosen to conform the high-dose region. Intensity-modulated radiation therapy (IMRT) and volumetric-modulated arc therapy (VMAT) vary fluence using multileaf collimators, gantry motion, and dose rate. Stereotactic treatments use small margins and high dose per fraction, demanding especially accurate localization and delivery.

The planner balances target objectives against organ-at-risk constraints. Because these objectives compete, there is rarely a single mathematically unique "best" plan. Clinical judgment determines which trade-offs are acceptable. [Chapter 7](../treatmentPlanning/treatmentPlanning.md) explains how knowledge-based and learning-based methods support this process.

### Image Guidance and Delivery

At treatment, lasers and external marks provide initial positioning. Image-guided radiotherapy then compares current anatomy with a reference using planar imaging, cone-beam CT, surface imaging, ultrasound, MRI, or implanted markers. Corrections may include translations, rotations, or—in adaptive workflows—a new contour set and treatment plan.

The record-and-verify or oncology information system controls treatment parameters and documents delivery. Independent checks, machine interlocks, time-outs, and professional review form a layered safety system. Automation should strengthen these layers rather than collapse them into one opaque decision.

## Radiobiology

Radiobiology connects physical dose with biological effect. Equal physical doses can have different consequences depending on fraction size, treatment time, radiation quality, tissue type, oxygenation, and the spatial distribution of dose.

### DNA Damage and Cell Fate

Radiation can damage DNA directly or indirectly through reactive species. Double-strand breaks and complex clustered damage are especially consequential. Cells may repair the damage correctly, misrepair it, undergo apoptosis or other forms of death, enter senescence, or lose reproductive capacity. In radiotherapy, **clonogenic cell death**—loss of the ability to produce a viable colony—is a central endpoint.

Tumors and normal tissues are heterogeneous. Cell-cycle state, hypoxia, intrinsic radiosensitivity, microenvironment, immune response, and DNA-repair capacity all influence response. A dose-response model is therefore a useful abstraction, not a complete description of an individual patient's biology.

### Fractionation and the Linear-Quadratic Model

Most external-beam courses divide total dose into fractions. Fractionation permits repair and repopulation between treatments and can exploit differences between tumor and normal-tissue response. A commonly used model for surviving fraction after dose $D$ is:

$$S(D) = e^{-(\alpha D + \beta D^2)}$$

For $n$ fractions of size $d$, the biologically effective dose (BED), under the model's assumptions, is:

$$BED = nd\left(1 + \frac{d}{\alpha/\beta}\right)$$

The $\alpha/\beta$ ratio describes the modelled sensitivity to fraction size. Late-responding normal tissues often have lower ratios than many tumors and early-responding tissues. BED and equivalent-dose calculations are comparison tools; they do not remove uncertainty about recovery, overall treatment time, dose heterogeneity, or the validity of extrapolation to extreme fraction sizes.

### The Biological Rs

The classic framework for fractionated radiotherapy includes:

- **Repair** of sublethal damage between fractions;
- **Redistribution** of surviving cells through cell-cycle phases;
- **Reoxygenation** of previously hypoxic tumor regions;
- **Repopulation** during a treatment course;
- **Radiosensitivity**, acknowledging biological variation between cells and tumors.

These mechanisms help explain why changing fraction size or overall treatment time can change outcome even when total physical dose is unchanged.

### Tumor Control and Normal-Tissue Complication

Tumor control probability (TCP) and normal-tissue complication probability (NTCP) models summarize relationships among dose, volume, and outcome. They can support comparison and optimization, but they inherit limitations from their datasets and assumptions. A model trained on one technique, contouring convention, population, or follow-up pattern may not transport reliably to another.

AI outcome models face the same issue at greater dimensionality. Their validation must include calibration, external evaluation, subgroup performance, and clinical utility, as discussed in [Chapter 9](../validation/validation.md).

## A Brief Evolution of the Field

Radiation treatment began soon after the discovery of x-rays and radioactivity. Early practice used superficial x-ray tubes and radium with limited ability to quantify or shape dose. The development of megavoltage machines improved penetration and skin sparing. Cobalt units and medical linear accelerators enabled reliable high-energy external-beam treatment.

Computed tomography transformed planning from surface landmarks and two-dimensional projections to a three-dimensional patient model. Multileaf collimators, inverse planning, IMRT, and VMAT increased conformality. On-board imaging enabled smaller margins and more frequent correction. Stereotactic techniques combined accurate localization with ablative fractionation. Proton and ion therapy expanded the available physical dose distributions, while modern brachytherapy integrated three-dimensional imaging and computerized optimization.

The current field is increasingly adaptive. Daily volumetric imaging, MR-guided treatment, automated contouring, rapid optimization, and accumulated-dose estimation allow treatment to respond to anatomical change. These capabilities also increase system complexity: more transformations, models, data interfaces, and time-sensitive decisions must be commissioned and monitored.

## The Roles of AI in Radiation Oncology

AI can support nearly every transition in the radiotherapy pathway:

- image reconstruction, denoising, and synthetic imaging;
- target and organ-at-risk contouring;
- multimodal and longitudinal registration;
- dose prediction and treatment-plan optimization;
- plan, machine, and workflow quality assurance;
- outcome prediction and patient selection;
- documentation and multimodal decision support.

The clinical question is not whether a model is accurate in isolation. It is whether the complete human-machine process produces safer, more consistent, or more efficient care for the intended population. That requires local validation, defined oversight, failure handling, and post-deployment monitoring.

## Current Research and Recent Advances

- **Biology-guided personalization:** Research increasingly combines spatial dose with imaging, molecular, and longitudinal response data to move beyond population-level constraints. These models remain sensitive to endpoint definition, confounding, and dataset shift, so prospective clinical utility must be demonstrated rather than inferred from retrospective discrimination alone [[2]](https://doi.org/10.1038/s41571-020-0417-8). _(added: 2026-07)_
- **Online adaptive radiotherapy:** Integrated imaging, automated contour propagation or segmentation, rapid replanning, and on-couch review are turning adaptation into a fraction-level workflow. The opportunity is tighter personalization; the safety challenge is validating every compressed step under time pressure [[3]](https://doi.org/10.1016/j.ijrobp.2020.10.021). _(added: 2026-07)_
- **Automation as a sociotechnical system:** Contemporary radiation oncology AI guidance emphasizes data quality, representative evaluation, human factors, and lifecycle monitoring rather than benchmark performance alone [[2]](https://doi.org/10.1038/s41571-020-0417-8). _(added: 2026-07)_

## Recap

Radiation oncology combines radiation physics, patient-specific dosimetry, radiobiology, imaging, treatment delivery, and layered safety processes. Physical dose must be interpreted through its spatial distribution and biological context. Modern treatment has evolved toward highly conformal and adaptive workflows, creating valuable roles for AI while increasing the need for validation, human oversight, and quality assurance across the complete clinical system.

## References

1. Podgorsak EB, ed. *Radiation Oncology Physics: A Handbook for Teachers and Students*. International Atomic Energy Agency; 2005. [IAEA publication](https://www-pub.iaea.org/MTCD/Publications/PDF/Pub1196_web.pdf)
2. Huynh E, Hosny A, Guthier C, et al. Artificial intelligence in radiation oncology. *Nature Reviews Clinical Oncology*. 2020;17:771-781. [DOI](https://doi.org/10.1038/s41571-020-0417-8)
3. Glide-Hurst CK, Lee P, Yock AD, et al. Adaptive radiation therapy (ART) strategies and technical considerations: a state of the ART review from NRG Oncology. *International Journal of Radiation Oncology, Biology, Physics*. 2021;109(4):1054-1075. [DOI](https://doi.org/10.1016/j.ijrobp.2020.10.021)
