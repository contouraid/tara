# 4: Medical Imaging in Radiation Oncology

## How to Use This Guide

This guide introduces imaging modalities used in radiation oncology and the formats used to store and exchange their data. Acquisition time, availability, image quality, and risk vary by protocol and institution, so the summary table is illustrative rather than a universal operational specification [[2]](https://doi.org/10.1155/2022/5164970).

| Modality     | Typical Uses                                                                 | Duration             | Pros                                                                 | Cons                                                                   |
|--------------|-------------------------------------------------------------------------------|----------------------|----------------------------------------------------------------------|------------------------------------------------------------------------|
| X-ray        | Fracture diagnosis; Lung infection detection; Dental evaluation              | 10–15 minutes        | Quick and accessible; Relatively low cost; Effective for detecting fractures and lung conditions | Limited soft tissue detail; Exposure to ionizing radiation             |
| Fluoroscopy  | Barium enema procedures; Cardiac catheterization; Joint injections           | 30 minutes – 2 hours | Real-time imaging; Guidance during procedures                        | Exposure to ionizing radiation; Potential for contrast dye reactions   |
| CT Scan      | Tumor detection and staging; Vascular disease evaluation; Internal injury assessment | 20–25 minutes        | High-resolution images; Fast scanning times; Excellent for bone and vascular evaluation | Higher radiation dose than X-rays; Contrast dye may be required        |
| MRI          | Brain and spinal cord imaging; Soft tissue evaluation; Multiple sclerosis diagnosis | 45 minutes – 1 hour  | Detailed soft tissue images; No ionizing radiation; Multiplanar imaging capabilities | Longer scanning times; Claustrophobic for some patients; Limited availability for certain conditions |
| Ultrasound   | Prenatal imaging and monitoring; Abdominal and pelvic evaluation; Cardiac and vascular imaging | 30 minutes – 1 hour  | Real-time imaging; No ionizing radiation; Safe for pregnant women     | Operator-dependent; Limited penetration for deep structures            |
| PET Scan     | Cancer diagnosis and staging; Brain function evaluation; Heart disease assessment | 1.5 – 2 hours        | Functional and metabolic information; Detection of small lesions; Accurate staging of cancers | High cost; Limited availability; Requires radiotracer administration   |
| Mammography  | Breast cancer screening; Detection of breast abnormalities                   | 30 minutes           | Early detection of breast cancer; High-resolution images              | Slight discomfort during the procedure                                |

---

## X-ray Imaging

X-ray imaging creates a projection from differential attenuation of ionizing electromagnetic radiation in the body [[3]](https://www.nibib.nih.gov/science-education/science-topics/medical-x-rays).

At its core, X-ray imaging works by directing a controlled beam of X-rays through the patient's body toward a detector. Dense structures like bones absorb more radiation and appear white or light gray on the resulting image, while less dense tissues like fat and air appear darker. This differential absorption creates the contrast necessary for diagnostic interpretation.

In radiation oncology, conventional X-ray imaging serves multiple critical functions. During the treatment planning phase, X-rays help localize tumors and identify anatomical landmarks. Throughout the treatment course, they verify patient positioning and treatment field alignment through portal imaging. For certain cancer types, particularly those affecting bony structures, X-rays provide valuable diagnostic information and can help monitor treatment response.

The technology has evolved significantly from traditional film-based systems to digital radiography, which offers improved image quality, lower radiation doses, and enhanced workflow efficiency. Modern X-ray systems in radiation oncology departments often feature flat-panel detectors that convert X-rays directly into digital signals, enabling immediate image review and integration with treatment planning systems.

Despite being one of the oldest imaging technologies, X-ray imaging continues to play a vital role in radiation oncology due to its accessibility, speed, and relative simplicity. When combined with newer technologies like cone-beam CT, X-ray imaging provides essential guidance for precise radiation delivery.

### Clinical Uses in Radiation Oncology

X-ray imaging serves multiple essential functions in radiation oncology practice:

- **Treatment planning support**: Provides initial anatomical information for treatment planning, particularly for bone-related targets
- **Patient positioning verification**: Ensures accurate patient setup before treatment delivery
- **Portal imaging**: Verifies radiation field placement during treatment
- **Treatment response assessment**: Monitors changes in tumor size or bone healing after radiation therapy
- **Brachytherapy guidance**: Assists in the placement of radioactive implants
- **Skeletal metastasis evaluation**: Identifies and assesses bone metastases that may require palliative radiation
- **Complication monitoring**: Detects radiation-induced changes such as radiation pneumonitis

The simplicity and accessibility of X-ray imaging make it a practical first-line imaging option for many radiation oncology applications, particularly when rapid assessment is needed or when more complex imaging modalities are unavailable.

### Strengths and Limitations

X-ray imaging offers several distinct advantages that maintain its relevance in modern radiation oncology:

| Strengths | Limitations |
|-----------|-------------|
| Widely available and accessible | Limited soft tissue contrast |
| Relatively inexpensive | Two-dimensional representation of three-dimensional structures |
| Fast acquisition time | Uses ionizing radiation |
| Excellent for visualizing bone structures | Cannot distinguish between many types of soft tissues |
| Portable options available for bedside imaging | Higher risk for children and pregnant women |
| High spatial resolution for certain applications | Multiple exposures increase lifetime radiation risk |
| Established technology with well-understood parameters | Cannot visualize physiological or functional information |

Understanding these strengths and limitations helps radiation oncologists determine when X-ray imaging is appropriate and when more advanced modalities should be employed. For example, while X-rays excel at detecting bone metastases, they are less effective for delineating soft tissue tumors where CT or MRI would be preferred.

> **Figure suggestion:** Add a diagram showing how X-rays pass through tissues of different densities to create a radiographic image, with annotations explaining the relationship between tissue density and image appearance.

---

## Computed Tomography (CT)

Computed tomography (CT) reconstructs cross-sectional attenuation maps from multiple X-ray projections. Its radiotherapy role, contrast, artifacts, and risks depend on the acquisition and reconstruction protocol [[2]](https://doi.org/10.1155/2022/5164970).

Unlike conventional X-rays that project all structures onto a single plane, CT provides true anatomical cross-sections by measuring the X-ray attenuation coefficients of tissues from multiple angles. These measurements are reconstructed into images where each pixel represents a tissue's radiodensity, quantified in Hounsfield Units (HU). This standardized scale assigns water a value of 0 HU, with air at approximately -1000 HU and dense bone reaching +1000 HU or higher.

In radiation oncology, CT serves as the primary imaging modality for treatment planning due to its excellent geometric accuracy, tissue density information, and widespread availability. The electron density information derived from CT images is essential for calculating radiation dose distributions, as it directly correlates with how radiation interacts with tissues. This makes CT indispensable for creating accurate dose calculations in treatment planning systems.

Modern CT scanners can acquire images with submillimeter resolution in seconds, enabling rapid imaging of entire anatomical regions with minimal motion artifacts. Advanced techniques like four-dimensional CT (4D-CT) capture organ motion throughout the respiratory cycle, critical for treating tumors in the chest and abdomen where respiratory movement affects target position.

The evolution of CT technology continues with dual-energy CT, which uses two different energy spectra to better characterize tissues, and cone-beam CT integrated into linear accelerators, which enables image-guided radiation therapy with daily verification of tumor position.

### Clinical Uses in Radiation Oncology

CT imaging is fundamental to radiation oncology workflow and serves multiple critical functions:

- **Treatment planning**: Provides the primary dataset for defining target volumes and organs at risk
- **Electron density mapping**: Enables accurate dose calculation algorithms
- **Tumor localization and volume determination**: Precisely defines the extent of disease
- **Image guidance during radiation therapy**: Verifies patient positioning before and during treatment
- **Response assessment**: Evaluates tumor changes during and after treatment
- **Adaptive radiotherapy**: Supports plan modifications based on anatomical changes during treatment
- **Stereotactic radiosurgery planning**: Provides high-precision targeting for focused radiation delivery
- **Virtual simulation**: Replaces conventional simulators for treatment field design

The integration of CT into radiation therapy workflows has dramatically improved treatment precision and enabled the development of highly conformal techniques like intensity-modulated radiation therapy (IMRT) and stereotactic body radiation therapy (SBRT).

### Strengths and Limitations

CT imaging offers numerous advantages that have established it as the cornerstone of radiation oncology imaging:

| Strengths | Limitations |
|-----------|-------------|
| High spatial resolution | Radiation exposure (ionizing radiation) |
| Excellent geometric accuracy | Limited soft tissue contrast compared to MRI |
| Fast acquisition time | Risk of contrast agent reactions |
| Provides electron density information for dose calculation | Not ideal for certain soft tissue evaluations |
| Widely available | Motion artifacts can affect image quality |
| Relatively affordable compared to other advanced modalities | Limited functional information |
| Provides detailed anatomical information | Dental and other metal artifacts can degrade image quality |

Despite these limitations, CT remains the primary imaging modality for radiation therapy planning due to its geometric accuracy, electron density information, and widespread availability. When enhanced soft tissue contrast is needed, CT is often supplemented with MRI or PET imaging through image registration techniques.

> **Figure suggestion:** Include a diagram of a modern CT scanner with labeled components, alongside an axial CT image showing different tissue densities with Hounsfield Unit values for key structures.

---

## Magnetic Resonance Imaging (MRI)

Magnetic resonance imaging (MRI) uses nuclear magnetic resonance rather than ionizing radiation and can provide multiple forms of soft-tissue contrast. Its appearance and geometric fidelity depend on the sequence, hardware, reconstruction, and correction methods [[2]](https://doi.org/10.1155/2022/5164970).

MRI utilizes powerful magnetic fields, radio frequency pulses, and sophisticated computer processing to generate detailed images of the body's internal structures. The fundamental principle involves aligning hydrogen protons in the body with a strong magnetic field, then disturbing this alignment with radiofrequency pulses. As protons return to their equilibrium state, they emit signals that are detected and processed into images. The varying relaxation properties of different tissues—primarily T1 (longitudinal) and T2 (transverse) relaxation times—create the remarkable contrast that distinguishes MRI from other imaging modalities.

In radiation oncology, MRI excels at visualizing tumor boundaries in soft tissues, particularly in the brain, head and neck, pelvis, and liver. The superior contrast between tumor and surrounding normal tissues enables more precise target volume delineation, potentially reducing treatment volumes and sparing healthy tissue. This is especially valuable for tumors that are poorly visualized on CT, such as prostate cancer, where MRI has become the gold standard for local staging and treatment planning.

Modern MRI techniques have expanded beyond anatomical imaging to include functional and physiological assessment. Diffusion-weighted imaging (DWI) measures the random motion of water molecules, helping identify areas of restricted diffusion characteristic of many tumors. Perfusion imaging evaluates tissue vascularity, while magnetic resonance spectroscopy (MRS) provides biochemical information about tissue metabolism. These advanced techniques offer insights into tumor biology that can inform treatment decisions and response assessment.

The integration of MRI into radiation therapy workflows continues to evolve, with MRI simulators and MRI-guided linear accelerators representing the cutting edge of technology that enables real-time imaging during treatment delivery.

### Clinical Uses in Radiation Oncology

MRI serves multiple critical functions in modern radiation oncology practice:

- **Tumor delineation**: Superior soft tissue contrast for precise target volume definition
- **Treatment planning for specific sites**: Essential for brain, head and neck, prostate, and gynecological cancers
- **Critical structure identification**: Clearly visualizes organs at risk, particularly neural structures
- **Functional imaging**: Provides information on tumor physiology through techniques like diffusion and perfusion imaging
- **Treatment response assessment**: Evaluates changes in tumor size, composition, and function during and after treatment
- **Brachytherapy guidance**: Assists in applicator placement and dose planning for prostate and gynecological brachytherapy
- **Stereotactic radiosurgery planning**: Provides detailed anatomical information for precise targeting
- **MR-guided radiotherapy**: Enables real-time imaging during treatment delivery with specialized systems

The integration of MRI with CT through image registration has become standard practice for many disease sites, combining the electron density information from CT with the superior soft tissue contrast of MRI.

### Strengths and Limitations

MRI offers several distinct advantages while also presenting certain challenges in radiation oncology applications:

| Strengths | Limitations |
|-----------|-------------|
| Excellent soft tissue contrast | Longer acquisition time compared to CT |
| No ionizing radiation | Higher cost and limited availability in some regions |
| Multiple contrast mechanisms (T1, T2, FLAIR, etc.) | Contraindicated for patients with certain metallic implants |
| Functional and physiological information | Claustrophobia issues for some patients |
| High sensitivity for detecting certain pathologies | Motion artifacts can degrade image quality |
| Multiplanar imaging capabilities | Geometric distortion can affect treatment planning accuracy |
| Advanced techniques for tissue characterization | Not suitable for patients with certain medical devices (pacemakers, etc.) |

Despite these limitations, MRI has become essential in radiation oncology, particularly for tumors in anatomical regions where soft tissue contrast is crucial for accurate target delineation. Ongoing technological developments continue to address the challenges of geometric distortion and integration into treatment planning systems.

> **Figure suggestion:** Include a comparison of CT and MRI images of the same anatomical region (e.g., brain or prostate) to demonstrate the superior soft tissue contrast of MRI, with annotations highlighting key structures visible on MRI but not on CT.

---

## Ultrasound Imaging

Ultrasound forms images from transmitted and received acoustic waves rather than ionizing radiation. Image quality is operator-, window-, anatomy-, and device-dependent [[2]](https://doi.org/10.1155/2022/5164970).

The fundamental principle of ultrasound involves transmitting sound waves with frequencies above the range of human hearing (typically 2-15 MHz) into the body using a transducer. As these waves encounter tissues with different acoustic properties, they are reflected back to the transducer at varying intensities. The transducer converts these reflected sound waves into electrical signals that are processed to generate real-time images. The time delay between transmission and reception of the sound waves determines the depth of the reflecting structures, while the intensity of the reflected signals creates contrast between different tissue types.

In radiation oncology, ultrasound serves specialized functions rather than as a primary planning modality. Its most established role is in prostate brachytherapy, where transrectal ultrasound guides the precise placement of radioactive seeds. For external beam radiation therapy of prostate cancer, transabdominal ultrasound systems can verify daily prostate position, enabling image-guided treatment delivery without additional radiation exposure. Ultrasound has also found applications in breast cancer radiotherapy for tumor bed localization after lumpectomy and in abdominal treatments for tracking organ motion.

The technology continues to evolve with 3D/4D capabilities that capture volumetric data over time, elastography that measures tissue stiffness, and contrast-enhanced techniques that improve visualization of vascular structures. These advancements expand the potential applications of ultrasound in radiation oncology, particularly for real-time monitoring during treatment delivery.

While ultrasound cannot replace CT or MRI for comprehensive treatment planning due to its limited field of view and operator dependence, its unique advantages of real-time imaging, absence of ionizing radiation, and portability make it a valuable complementary tool in specific clinical scenarios.

### Clinical Uses in Radiation Oncology

Ultrasound serves several specialized functions in radiation oncology practice:

- **Prostate brachytherapy guidance**: Real-time visualization for radioactive seed placement
- **Image-guided radiation therapy**: Daily localization of prostate and other accessible tumors
- **Breast tumor bed localization**: Identification of the lumpectomy cavity for partial breast irradiation
- **Organ motion assessment**: Real-time monitoring of abdominal organ movement during respiration
- **Gynecological brachytherapy**: Assistance in applicator placement and assessment
- **Soft tissue visualization**: Complementary information for treatment planning in accessible sites
- **Vascular assessment**: Evaluation of tumor vascularity with Doppler and contrast-enhanced techniques

The real-time nature of ultrasound imaging provides unique capabilities for certain radiation oncology applications, particularly when immediate feedback is needed during procedures.

### Strengths and Limitations

Ultrasound imaging offers several distinct advantages while also presenting certain inherent limitations:

| Strengths | Limitations |
|-----------|-------------|
| No ionizing radiation | Limited depth penetration |
| Real-time imaging capability | Operator-dependent (requires skilled technicians) |
| Highly portable | Limited field of view |
| Cost-effective compared to other modalities | Difficulty imaging through bone or air |
| Excellent for soft tissue differentiation in accessible regions | Image quality affected by patient factors (obesity, etc.) |
| No special preparation required for most examinations | Less detailed for certain applications compared to CT/MRI |
| Doppler capabilities for vascular assessment | Resolution limitations for deep structures |

Understanding these strengths and limitations helps radiation oncologists determine when ultrasound can provide valuable information and when other imaging modalities are more appropriate. The complementary nature of ultrasound makes it particularly useful in multimodality imaging approaches.

> **Figure suggestion:** Include an image showing a transabdominal ultrasound being used for prostate localization in radiation therapy, with annotations explaining how the ultrasound data is integrated with the treatment planning system.

---

## Positron Emission Tomography (PET)

Positron emission tomography (PET) estimates the spatial distribution of a positron-emitting radiotracer. What the image represents depends on the tracer, uptake interval, acquisition, reconstruction, and biological context [[4]](https://www.nibib.nih.gov/science-education/science-topics/nuclear-medicine).

PET imaging relies on the detection of positron-emitting radiopharmaceuticals (tracers) that are introduced into the patient's body, typically via intravenous injection. These tracers consist of biologically active molecules labeled with positron-emitting radionuclides such as fluorine-18, carbon-11, or oxygen-15. As these radionuclides decay, they emit positrons that travel a short distance before colliding with electrons in surrounding tissues. This collision results in annihilation, producing two 511 keV gamma rays traveling in nearly opposite directions. PET scanners detect these coincident gamma rays and use sophisticated algorithms to reconstruct three-dimensional images of the tracer distribution.

The most widely used PET tracer is 18F-fluorodeoxyglucose (FDG), a glucose analog that accumulates in metabolically active tissues, particularly malignant tumors that exhibit increased glucose metabolism. However, numerous other tracers have been developed to target specific biological processes, including 18F-fluorothymidine (FLT) for cell proliferation, 18F-fluoromisonidazole (FMISO) for hypoxia, and prostate-specific membrane antigen (PSMA) tracers for prostate cancer.

In radiation oncology, PET/CT has become an essential tool for target volume delineation in multiple cancer types, particularly lung, head and neck, lymphoma, and increasingly, prostate cancer. The metabolic information from PET complements the anatomical information from CT, allowing radiation oncologists to more accurately define tumor extent and distinguish viable tumor from atelectasis, necrosis, or fibrosis. This functional information can lead to both expansion of target volumes to include PET-positive regions not apparent on CT and reduction of volumes by excluding PET-negative regions that appear abnormal on CT.

Beyond initial staging and treatment planning, PET plays a crucial role in treatment response assessment and adaptive radiotherapy. Early metabolic changes during treatment can predict ultimate response, potentially allowing for treatment intensification in poor responders or de-escalation in good responders.

The integration of PET into radiation therapy workflows continues to evolve, with developments in respiratory-gated PET acquisition, novel tracers for specific tumor types, and the emergence of PET/MRI as a hybrid modality combining the metabolic information of PET with the superior soft tissue contrast of MRI.

### Clinical Uses in Radiation Oncology

PET imaging serves multiple critical functions in modern radiation oncology practice:

- **Tumor staging and characterization**: Identifies the extent of disease, including distant metastases
- **Target volume delineation**: Defines metabolically active tumor regions for treatment planning
- **Treatment response assessment**: Evaluates metabolic changes during and after treatment
- **Adaptive radiotherapy**: Guides plan modifications based on tumor response
- **Radiation dose escalation**: Identifies regions of high metabolic activity or hypoxia for dose painting
- **Recurrence detection**: Distinguishes between post-treatment changes and tumor recurrence
- **Prognostic information**: Provides data on tumor aggressiveness and likely treatment response
- **Treatment field verification**: Ensures coverage of all metabolically active disease

The integration of PET into radiation therapy planning has significantly impacted target definition for multiple cancer types, often changing management decisions and treatment volumes compared to conventional imaging alone.

### Strengths and Limitations

PET imaging offers several distinct advantages while also presenting certain challenges in radiation oncology applications:

| Strengths | Limitations |
|-----------|-------------|
| Visualizes metabolic/functional information | Limited spatial resolution compared to CT/MRI |
| Highly sensitive for detecting many cancer types | Radiation exposure to patient |
| Whole-body imaging capability | Relatively high cost |
| Can detect disease before anatomical changes occur | Limited availability compared to CT |
| Provides prognostic information | Requires radioactive tracer injection |
| Quantitative measurements possible | Uptake in inflammatory and normal tissues can cause false positives |
| Excellent for cancer staging and restaging | Scanning time (typically 20-30 minutes) |

Despite these limitations, PET has become an essential component of radiation oncology practice, particularly for diseases where accurate staging and target delineation significantly impact treatment outcomes. The complementary nature of functional and anatomical imaging has led to the widespread adoption of hybrid PET/CT and, increasingly, PET/MRI systems.

> **Figure suggestion:** Include a side-by-side comparison of CT, PET, and fused PET/CT images of a lung tumor case, demonstrating how the metabolic information from PET can change the apparent tumor extent compared to CT alone.

---

## Nuclear Medicine

Nuclear medicine uses radiopharmaceuticals for functional imaging or therapy. Planar scintigraphy, SPECT, PET, and radionuclide therapy have different instrumentation and intended uses [[4]](https://www.nibib.nih.gov/science-education/science-topics/nuclear-medicine).

The fundamental principle of nuclear medicine involves administering radioactive tracers (radiopharmaceuticals) that localize in specific organs or tissues based on their physiological or pathological characteristics. These tracers emit gamma rays that are detected by gamma cameras, which create two-dimensional planar images or, with Single Photon Emission Computed Tomography (SPECT), three-dimensional tomographic images. Unlike PET, which detects paired gamma rays resulting from positron annihilation, conventional nuclear medicine directly detects the gamma rays emitted by radiotracers such as technetium-99m, iodine-123, or gallium-67.

In radiation oncology, nuclear medicine studies provide functional information that complements the anatomical data from CT and MRI. Bone scintigraphy, using technetium-99m-labeled phosphonates, remains a standard technique for detecting bone metastases that may require palliative radiation. Sentinel lymph node mapping with radioactive colloids guides surgical sampling and subsequent radiation field design for breast cancer and melanoma. Radioiodine whole-body scanning plays a crucial role in thyroid cancer management, identifying residual disease or recurrence that may benefit from further radioiodine therapy or external beam radiation.

Beyond diagnostic applications, nuclear medicine includes therapeutic procedures collectively known as radionuclide therapy or molecular radiotherapy. These treatments use radionuclides that emit particles (typically beta or alpha particles) to deliver radiation directly to tumor cells. Examples include radioiodine (I-131) for thyroid cancer, radium-223 for bone metastases from prostate cancer, and lutetium-177-DOTATATE for neuroendocrine tumors. These therapies often complement external beam radiation therapy in multimodality treatment approaches.

The field continues to evolve with the development of SPECT/CT hybrid systems that combine functional and anatomical information, novel radiotracers for specific tumor types, and theranostic approaches that use similar compounds for both diagnosis and therapy.

### Clinical Uses in Radiation Oncology

Nuclear medicine serves several important functions in radiation oncology practice:

- **Bone metastasis detection**: Identifies osseous spread that may require palliative radiation
- **Lymphatic mapping**: Guides radiation field design based on drainage patterns
- **Thyroid cancer management**: Detects residual or recurrent disease requiring further treatment
- **Neuroendocrine tumor localization**: Identifies primary and metastatic sites for targeted radiotherapy
- **Cardiac and lung function assessment**: Evaluates potential impact of radiation on critical organs
- **Radionuclide therapy**: Delivers targeted radiation to specific tumor types
- **Treatment response evaluation**: Assesses changes in tracer uptake following therapy
- **Physiological imaging**: Provides functional information about organs within radiation fields

The complementary nature of nuclear medicine studies makes them valuable additions to the imaging arsenal in radiation oncology, particularly for specific disease sites and clinical scenarios.

### Strengths and Limitations

Nuclear medicine imaging offers several distinct advantages while also presenting certain inherent limitations:

| Strengths | Limitations |
|-----------|-------------|
| Provides functional and physiological information | Limited spatial resolution compared to CT/MRI |
| Whole-body imaging capability for many studies | Radiation exposure to patients and staff |
| High sensitivity for specific conditions | Longer acquisition times for some studies |
| Can detect disease before anatomical changes | Limited availability in some regions |
| Quantitative measurements possible | Requires specialized facilities and handling procedures |
| Theranostic potential (diagnosis and therapy) | Interpretation complexity requiring specialized training |
| Ability to assess specific molecular targets | Short half-life of some tracers requires on-site or nearby production |

Understanding these strengths and limitations helps radiation oncologists determine when nuclear medicine studies can provide valuable information for treatment planning and response assessment. The integration of SPECT/CT has significantly improved the utility of nuclear medicine in radiation oncology by providing anatomical context for functional findings.

> **Figure suggestion:** Include an image showing a bone scan with multiple metastatic lesions alongside the corresponding radiation treatment plan targeting the symptomatic sites, demonstrating how nuclear medicine findings guide palliative radiotherapy.

---

## Medical Imaging Storage File Types

Storage formats encode pixels together with geometry, acquisition, identifiers, and other metadata. DICOM is the clinical interoperability standard; research formats such as NIfTI and MINC have different information models and conversion can discard clinically important metadata [[1]](https://doi.org/10.1007/s10278-013-9657-9).

Medical image file formats must accommodate not only the pixel data representing the images themselves but also extensive metadata describing acquisition parameters, patient information, and in the case of radiation oncology, treatment planning details. The complexity of these requirements has led to the development of specialized formats and systems tailored to medical applications.

The Digital Imaging and Communications in Medicine (DICOM) standard has emerged as the universal format for medical imaging, providing a comprehensive framework for image storage, transmission, and associated information. DICOM files encapsulate both image data and a header containing metadata in a single file, enabling the accurate interpretation and display of images across different systems. For radiation oncology, DICOM-RT extensions specifically address the unique requirements of radiation therapy, including structure sets defining target volumes and organs at risk, treatment plans describing beam arrangements and dose prescriptions, and dose distributions resulting from treatment planning calculations.

Beyond DICOM, several other formats have specific applications in research and specialized clinical settings. The Neuroimaging Informatics Technology Initiative (NIfTI) format, an evolution of the older Analyze format, is commonly used in neuroimaging research and supports better spatial orientation information. The Medical Imaging NetCDF (MINC) format, developed at the Montreal Neurological Institute, offers flexibility for multi-dimensional data and is primarily used in research environments.

For the management and distribution of medical images, Picture Archiving and Communication Systems (PACS) serve as the backbone of clinical imaging workflows. These networked systems provide storage, retrieval, and viewing capabilities for DICOM images, enabling clinicians to access studies from anywhere within a healthcare network. In radiation oncology departments, PACS integration with treatment planning systems, record and verify systems, and linear accelerators creates a comprehensive ecosystem for image-guided radiation therapy.

The evolution toward enterprise imaging strategies has led to the development of Vendor Neutral Archives (VNAs) that store images in standard formats accessible regardless of the proprietary systems that created them. These advanced systems facilitate data migration, system upgrades, and interoperability across healthcare enterprises.

As imaging technologies continue to advance, storage requirements grow exponentially, necessitating robust archiving solutions that balance accessibility, security, and cost-effectiveness. Cloud-based storage options are increasingly being adopted, offering scalability and disaster recovery capabilities while raising considerations about data security and transfer speeds.

### Common Medical Image File Formats

Various file formats serve different needs in medical imaging, each with specific characteristics and applications:

| Format | Structure | Primary Use | Strengths | Limitations |
|--------|-----------|-------------|-----------|-------------|
| DICOM | Single file with header and image data | Clinical standard for all modalities | Comprehensive metadata, universal support | Complex structure, large file size |
| DICOM-RT | DICOM extensions for radiation therapy | Radiation oncology treatment planning | Supports specialized RT objects (structure sets, plans, dose) | Requires specialized viewers |
| Analyze | Separate header (.hdr) and image (.img) files | Legacy research format | Simple structure | Limited metadata, being phased out |
| NIfTI | Single (.nii) or dual (.hdr/.img) files | Neuroimaging research | Better spatial orientation than Analyze | Limited clinical adoption |
| MINC | NetCDF-based format | Research, especially neuroimaging | Flexible multi-dimensional support | Complex structure, limited clinical use |

DICOM remains the predominant format in clinical radiation oncology, with specialized extensions addressing the unique requirements of treatment planning and delivery.

### Storage and Management Systems

Effective management of medical images requires sophisticated systems that enable storage, retrieval, and distribution:

- **PACS (Picture Archiving and Communication System)**: Networked computers for storing, retrieving, distributing, and presenting medical images
- **VNA (Vendor Neutral Archive)**: Advanced PACS that stores images in standard formats accessible regardless of proprietary systems
- **DICOM servers**: Specialized systems for handling DICOM data transmission and storage
- **Treatment planning systems**: Specialized software for radiation therapy planning that imports and manages imaging data
- **Record and verify systems**: Ensure planned treatments match delivered treatments, including image verification
- **Oncology information systems**: Comprehensive platforms integrating imaging, planning, and treatment delivery data

These systems must address several critical requirements, including long-term archiving for cancer survivorship monitoring, rapid retrieval during treatment planning and delivery, integration with treatment machines, and compliance with healthcare data security regulations.

> **Figure suggestion:** Include a diagram showing the flow of imaging data through a radiation oncology department, from acquisition through various storage systems to treatment planning and delivery, highlighting the role of DICOM and PACS in this workflow.

---

## Radiotherapy Data and Informatics Foundations

An AI dataset is not a folder of unrelated images. It is a selection from a longitudinal clinical record in which objects refer to one another, may be revised, and may describe what was intended rather than what was delivered. Before extracting arrays, define the clinical episode, resolve the object relationships, and retain enough provenance to reconstruct every derived example. DICOM Working Group 7 maintains the radiotherapy objects and their relationships [[6]](https://www.dicomstandard.org/activity/wgs/wg-07); the DICOM Standard remains the authority for the exact information model and attributes [[5]](https://www.dicomstandard.org/).

This section covers the source data, geometry, provenance, and cohort controls. The downstream [radiomics and dosiomics workflow](../clinicalPrediction/clinicalPrediction.md) is treated canonically in the clinical-prediction chapter, including acquisition stability, segmentation sensitivity, standardized feature extraction, longitudinal biomarkers, and external validation.

### One Patient, Connected Data

The following table is a conceptual object graph for one patient. Arrows mean "references, is derived from, or is linked to," not merely "has the same filename."

| Patient-level entity | Typical source or object | Connects to | What must remain traceable |
|---|---|---|---|
| Stable longitudinal identity and treatment course | oncology information system (OIS), enterprise master patient index | all studies, prescriptions, plans, fractions, notes, and outcomes | source identifiers, pseudonym map, episode rules, and merge/split history |
| Planning and diagnostic images | DICOM CT, MR, PET, CBCT, radiographs | frame of reference; structures; registrations; acquisition protocol | Study/Series/SOP Instance UIDs, modality, timestamps, orientation, spacing, and calibration |
| Targets and organs at risk | RT Structure Set (RTSTRUCT), DICOM Segmentation (SEG), surface or newer RT geometric objects | source images; plan; dose; annotator and guideline | ROI/segment identifier, meaning, version, author, creation method, and source image |
| Prescription and intent | OIS/electronic health record (EHR), structured prescription, newer RT course objects | plan, diagnosis, treatment course | dose and fractionation, units, target, intent, approval state, and amendments |
| Planned treatment | RT Plan and newer second-generation RT radiation objects | structures, prescription, beams/control points, calculated dose | plan UID, plan version, approval status, machine/technique, and referenced objects |
| Calculated dose | RT Dose | plan, dose grid, structures, and image frame | Dose Units, Dose Type, Dose Summation Type, Dose Grid Scaling, grid geometry, and algorithm |
| Spatial relationships | Spatial Registration, Deformable Spatial Registration, rigid transforms | image series, contours, and sometimes dose accumulation | source/target frames, transform direction, algorithm, reviewer, and intended use |
| Delivery and verification | RT Treatment Record, newer RT Radiation Record, machine logs, setup images | plan, fraction/session, machine, and measured or reconstructed dose | delivered control points, timestamps, interruptions, overrides, and deviations |
| Clinical variables and outcomes | EHR/OIS tables, pathology, laboratory systems, notes, toxicity and survival registries | patient, diagnosis, treatment episode, follow-up time | definition, code system, observation time, censoring, extraction method, and adjudication |

Legacy RTSTRUCT stores contours as patient-coordinate points associated with referenced images; DICOM SEG stores labeled pixels with coded segment metadata. RT Plan represents intended treatment, RT Dose a calculated or measured dose distribution, and treatment records what a delivery system reports as performed. These objects are complementary, not interchangeable. Newer second-generation RT objects separate prescriptions, radiation sets, and radiation records more explicitly, but support across clinical systems remains uneven [[16]](https://www.dicomstandard.org/news/supplements/view/rt-radiation-records). An OIS or EHR is still needed for diagnosis, prescription context, approvals, toxicity, and outcomes that are absent or inconsistently encoded in DICOM.

File proximity and matching patient names do not establish a valid relationship. Resolve DICOM references and UIDs, confirm the clinical episode and approval state, then record any heuristic fallback. A plan may reference an earlier structure-set version; a dose may be associated with one plan sum rather than a delivered course; a copied plan may coexist with the approved plan; and a treatment record may be incomplete.

### Geometry, Coordinates, and Units

A voxel index $(i,j,k)$ is an array address. A world or patient coordinate $(x,y,z)$ is a physical location, usually expressed in millimetres. They are connected by an affine mapping built from image origin, row and column direction cosines, pixel spacing, and slice positions. DICOM's Image Position (Patient), Image Orientation (Patient), and Pixel Spacing describe slices in a patient-based coordinate system [[7]](https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.7.6.2.html). Array order chosen by a software library is not a substitute for this metadata.

A Frame of Reference UID identifies a spatial coordinate frame. Matching frames support direct geometric interpretation, but do not prove that anatomy is unchanged. Different frames require a verified registration or another explicit transform. Always record transform direction: a matrix that maps moving coordinates to fixed coordinates cannot safely be used as its inverse without inversion and validation.

Before using an image, contour, registration, or dose grid, verify:

- origin, direction cosines, handedness, patient position, field of view, spacing, and slice ordering;
- Frame of Reference UIDs and the complete chain of spatial transforms;
- physical units, including millimetres versus centimetres, Gy versus cGy, CT rescale slope/intercept, PET SUV conventions, and RT Dose Grid Scaling;
- whether coordinates denote voxel centres or boundaries and whether a crop or pad changed the origin;
- dose grid origin, orientation, offsets, dimensions, and referenced plan—not only its matrix shape.

RTSTRUCT contour points are continuous physical coordinates. Rasterization converts polygons to a label grid and therefore requires a declared target grid, inside/outside rule, treatment of holes and non-planar contours, and boundary convention. Converting the mask back to contours is not exactly reversible. Partial-volume or supersampling methods may preserve small structures better than a single centre-point test, but their output is still a derived representation.

Resampling chooses a new grid and estimates values that were not directly acquired. Linear or higher-order interpolation is commonly used for continuous intensities; nearest-neighbour or label-aware methods avoid inventing category values in masks. Dose interpolation should preserve geometry and units, but interpolation alone does not establish that dose is physically transferable between changing anatomies. Every resampled object should retain the source UID, transform, target grid, interpolation method, software version, and quality checks.

#### Worked failure: a plausible but wrong dose feature

Suppose a planning CT has 1 mm in-plane spacing and 3 mm slice spacing, while RT Dose is stored on a separate 2.5 mm grid. A script reads both pixel arrays, resizes dose to the CT matrix dimensions, and calculates mean parotid dose inside a rasterized RTSTRUCT mask. The overlay looks plausible, but the script ignored Image Position (Patient), orientation, dose-grid offsets, and Dose Grid Scaling. The dose is shifted superiorly and its stored integer values are interpreted as Gy.

The result can be numerically stable and clinically wrong. The correct workflow is to convert contour points and dose samples into their declared patient coordinates, apply any required verified registration, multiply stored dose values by Dose Grid Scaling, resample physical dose onto a declared evaluation grid, and compare landmarks, extents, isocentre, and known DVH values. A unit test with identical matrix shapes would not detect the error; a physical-coordinate phantom with an asymmetric landmark would.

### Cohort Construction and Provenance

Write the cohort definition before inspecting model performance. Name the clinical question, sites and dates, unit of analysis, index time, eligible modalities and protocols, treatment intent, inclusion/exclusion rules, follow-up requirement, and outcome definitions. Preserve a flow count from all potentially eligible patients through every exclusion, including missing or corrupt data. Excluding records after seeing their labels or predictions introduces selection bias.

Build a manifest with one row per source object or derived artifact. It should include a stable pseudonymous patient key, episode and time point, source system, DICOM UIDs or database keys, acquisition and approval times, object version, checksum, extraction query or code version, label provenance, and exclusion reason. Keep the immutable raw snapshot separate from versioned derived data.

Common curation failures and controls include:

- **Longitudinal identity:** reconcile local identifiers, merges, aliases, and transfers through an approved linkage process. Never infer identity from name alone. Preserve the mapping in a separately controlled location.
- **Duplicates and relatives:** detect duplicate SOP instances, repeated reconstructions, copied plans, propagated contours, and near-identical exports. Decide which is canonical without erasing the relationship.
- **Labels:** distinguish manual, consensus, propagated, algorithm-generated, edited, and administratively coded labels. Record annotator role, guideline, tools, source information, blinding, and adjudication. Measure inter-observer variation when no unique ground truth exists.
- **Names and ontologies:** preserve the source ROI name, map it to a controlled concept and code where possible, record laterality and target role separately, and version the mapping table. Do not merge `Parotid_L`, `Lt_Parotid`, and `parotid` by string similarity without review.
- **Missingness:** distinguish not measured, not applicable, unavailable, failed extraction, and truly negative. Report missingness by site, period, and outcome; missing fields may encode workflow or disease severity.
- **Versions:** freeze dataset releases. A corrected contour, changed outcome, new follow-up date, or revised mapping creates a new version with a change log rather than silently altering the old release.

### Split First, Then Fit Preprocessing

Assign patients—not slices, patches, structures, plans, or fractions—to exactly one development or evaluation partition. Group known duplicates and related treatment episodes before splitting. If the intended use predicts a future event, ensure that every feature was available at the prediction time and prefer a temporal test cohort. For multi-site studies, reserve sites or scanner/protocol groups when the claim is transportability, and keep the final test set inaccessible until decisions are frozen.

Leakage can occur even after patient-level splitting. The following must be learned or selected using training data only: intensity-normalization statistics, histogram templates, imputation values, feature selection, registration atlases, patch-sampling distributions, class weights, augmentation ranges informed by the data, harmonization parameters, calibration, and decision thresholds. Fit them within each cross-validation training fold, then apply the frozen transform to its validation fold. Never use test labels to select crops, reject "bad" cases, or choose a checkpoint.

Registration and preprocessing also carry clinical information. Registering every case to a template built from all patients leaks test anatomy. Cropping around a test-set ground-truth contour gives the model localization information unavailable in use. Patch extraction can put neighbouring patches or propagated versions of the same structure in different splits. Augmented copies remain members of their source patient's split. Save the complete preprocessing graph and test it on held-out cases with missing series, unexpected orientation, extreme spacing, and unsupported labels.

### De-identification, Linkage, and Governance

Privacy work is risk management, not a single "remove patient name" operation. The DICOM Basic Application Level Confidentiality Profile addresses metadata; separate options cover burned-in pixels, recognizable visual features, structured content, descriptors, dates, UIDs, and private attributes [[8]](https://dicom.nema.org/medical/dicom/current/output/html/part15.html). A release process should inventory and test all of these surfaces:

- standard and private DICOM metadata, UIDs, filenames, directory paths, device and institution identifiers;
- burned-in text, overlays, screenshots, secondary captures, and scanned documents;
- free-text reports, plan/structure descriptions, comments, prescriptions, and machine logs;
- absolute and relative dates, rare event sequences, ages, locations, and longitudinal visit patterns;
- facial anatomy in head CT, MR, PET, surface images, and reconstructions;
- join keys and quasi-identifiers across imaging, genomic, billing, registry, and outcomes tables.

Date shifting must be consistent within a patient if intervals matter, while its method and resulting analytic limitations are documented. Removing facial anatomy may impair head-and-neck tasks and must be validated. Retaining stable UIDs or dates can aid longitudinal linkage but increases re-identification risk. Free-text review and pixel inspection require dedicated controls; a metadata allow-list cannot inspect what is visually encoded.

**Legal note:** the meanings and sufficiency of anonymization, de-identification, consent, and lawful processing depend on jurisdiction, purpose, data flow, and institutional policy. This chapter is technical guidance, not legal advice. Anonymization aims to make re-identification no longer reasonably possible under the applicable standard; pseudonymization replaces direct identifiers but retains a separately controlled re-linkage route and therefore usually remains personal or protected data. Consent is one possible governance basis, not a synonym for de-identification. Obtain local privacy, ethics, information-security, data-use, retention, and cross-border-transfer review.

### Reproducible and Shareable Datasets

A reusable dataset release should include a data dictionary, cohort flow, object relationship schema, provenance manifest, ontology mapping, missingness report, de-identification statement, intended and prohibited uses, license or data-use agreement, known errors and limitations, version history, and checksums. Dataset documentation can follow the datasheet pattern of recording motivation, composition, collection, preprocessing, uses, distribution, and maintenance [[13]](https://doi.org/10.1145/3458723). A model card should separately state intended use, training and evaluation populations, metrics, subgroup and robustness results, limitations, ethical considerations, and model/preprocessing version.

FAIR means **findable, accessible, interoperable, and reusable**; it does not mean unrestricted or anonymous. Controlled-access data can be FAIR when metadata, identifiers, access procedures, standards, and reuse conditions are clear [[9]](https://doi.org/10.1038/sdata.2016.18).

Representative public or research-access RT datasets illustrate why the access terms and limitations must be read rather than inferred from the word "public":

| Dataset | Modalities and representative task | License/access | Important limitations |
|---|---|---|---|
| NSCLC-Radiomics [[10]](https://doi.org/10.7937/K9/TCIA.2015.PF0M9REI) | 422 lung-cancer CT studies with RTSTRUCT/SEG and clinical outcomes; segmentation, radiomics, and outcome modelling | TCIA download; CC BY-NC 3.0 | retrospective single-domain cohort; selected structures; some scans have missing slices; collection corrections and versions matter |
| LCTSC [[11]](https://doi.org/10.7937/K9/TCIA.2017.3R3FVZ08) | 60 thoracic CT/RTSTRUCT cases; organ-at-risk segmentation | TCIA download; CC BY 3.0 | small challenge cohort; limited structures and diversity; a structure-name error was corrected in a later version |
| Head-Neck-PET-CT [[12]](https://doi.org/10.7937/K9/TCIA.2017.8OJE5Q00) | 298 patients with PET/CT, planning CT, REG, RTSTRUCT, RTPLAN, RTDOSE, clinical variables and outcomes; multimodal radiomics and treatment-data research | images require a TCIA restricted agreement; clinical tables are CC BY 3.0 | older retrospective acquisitions across four institutions; heterogeneous GTV names; facial reconstruction risk and access conditions constrain reuse |
| OpenKBP [[14]](https://doi.org/10.1002/mp.14845) | 340 head-and-neck cases represented as CT, masks and dose for 3-D dose prediction and DVH benchmarking | public challenge dataset; verify the current host's terms before redistribution | task-specific, preprocessed representation rather than a complete DICOM clinical record; fixed challenge split and one planning context limit broader claims |

Federated or distributed learning moves computation to institutional data and aggregates model updates or statistics instead of pooling raw records. It can broaden collaboration where central sharing is impractical, but it does not remove the need for contracts, privacy/security analysis, common definitions, data-quality checks, site-level evaluation, or protection against update leakage and attacks. Non-identically distributed institutional data can produce unstable or unfair performance, and model updates may disclose information. Federated learning should therefore be documented as a governed data flow, not described as automatic anonymization [[15]](https://doi.org/10.1038/s41598-020-69250-1).

## Current Research and Recent Advances

- **Second-generation radiotherapy objects:** DICOM is separating prescriptions, radiation sets, and radiation records more explicitly than legacy RT objects. Adoption remains system-dependent, so datasets must declare which object generation and implementation they use [[16]](https://www.dicomstandard.org/news/supplements/view/rt-radiation-records). _(added: 2026-07)_
- **Distributed learning:** Federated learning supports multi-institution analysis without centralizing raw records, but heterogeneous sites, privacy leakage, security, and governance remain active constraints rather than solved properties [[15]](https://doi.org/10.1038/s41598-020-69250-1). _(added: 2026-07)_
- **Dataset documentation:** Datasheets make provenance, composition, intended use, and known limitations inspectable. For radiotherapy, this documentation must also cover linked DICOM objects, coordinate handling, plan versions, and whether dose was planned or delivered [[13]](https://doi.org/10.1145/3458723). _(added: 2026-07)_

## Recap

Medical imaging supports target delineation, planning, guidance, and response assessment, but an RT-AI example is meaningful only when its images, structures, prescription, plan, dose, registration, delivery, clinical variables, and outcomes are linked to the correct patient and time point. Physical coordinates, frames of reference, transforms, units, rasterization, and dose-grid geometry must be verified before arrays are compared. Reproducible development also requires explicit cohort rules, patient-level and temporal splits, training-only preprocessing, label and version provenance, privacy controls across metadata and content, and documentation of access conditions and limitations.

---

## References

1. Larobina M, Murino L. Medical Image File Formats. *Journal of Digital Imaging*. 2014;27(2):200-206. [DOI](https://doi.org/10.1007/s10278-013-9657-9)
2. Hussain S, Mubeen I, Ullah N, et al. Modern Diagnostic Imaging Technique Applications and Risk Factors in the Medical Field: A Review. *BioMed Research International*. 2022;2022:5164970. [DOI](https://doi.org/10.1155/2022/5164970)
3. National Institute of Biomedical Imaging and Bioengineering. X-rays. [NIBIB](https://www.nibib.nih.gov/science-education/science-topics/medical-x-rays)
4. National Institute of Biomedical Imaging and Bioengineering. Nuclear Medicine. [NIBIB](https://www.nibib.nih.gov/science-education/science-topics/nuclear-medicine)
5. Digital Imaging and Communications in Medicine. DICOM Standard. [DICOM](https://www.dicomstandard.org/)
6. DICOM Standards Committee Working Group 7. Radiotherapy. [DICOM WG-07](https://www.dicomstandard.org/activity/wgs/wg-07)
7. DICOM Standards Committee. PS3.3, Image Plane Module. [DICOM Standard](https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.7.6.2.html)
8. DICOM Standards Committee. PS3.15, Security and System Management Profiles: Attribute Confidentiality Profiles. [DICOM Standard](https://dicom.nema.org/medical/dicom/current/output/html/part15.html)
9. Wilkinson MD, Dumontier M, Aalbersberg IJ, et al. The FAIR Guiding Principles for scientific data management and stewardship. *Scientific Data*. 2016;3:160018. [DOI](https://doi.org/10.1038/sdata.2016.18)
10. Aerts HJWL, et al. Data From NSCLC-Radiomics (version 4). The Cancer Imaging Archive. 2014. [Dataset DOI](https://doi.org/10.7937/K9/TCIA.2015.PF0M9REI)
11. Yang J, et al. Data from Lung CT Segmentation Challenge. The Cancer Imaging Archive. 2017. [Dataset DOI](https://doi.org/10.7937/K9/TCIA.2017.3R3FVZ08)
12. Vallières M, et al. Data from Head-Neck-PET-CT. The Cancer Imaging Archive. 2017. [Dataset DOI](https://doi.org/10.7937/K9/TCIA.2017.8OJE5Q00)
13. Gebru T, Morgenstern J, Vecchione B, et al. Datasheets for Datasets. *Communications of the ACM*. 2021;64(12):86-92. [DOI](https://doi.org/10.1145/3458723)
14. Babier A, Zhang B, Mahmood R, et al. OpenKBP: The open-access knowledge-based planning grand challenge and dataset. *Medical Physics*. 2021;48(9):5549-5561. [DOI](https://doi.org/10.1002/mp.14845)
15. Sheller MJ, Edwards B, Reina GA, et al. Federated learning in medicine: facilitating multi-institutional collaborations without sharing patient data. *Scientific Reports*. 2020;10:12598. [DOI](https://doi.org/10.1038/s41598-020-69250-1)
16. DICOM Standards Committee. Supplement 191: Radiotherapy Radiation Record. [DICOM supplement](https://www.dicomstandard.org/news/supplements/view/rt-radiation-records)
