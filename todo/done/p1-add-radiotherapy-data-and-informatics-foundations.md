# DONE: Add Radiotherapy Data and Informatics Foundations

**Section:** `medicalImaging/` and `workflow/`
**Priority:** High
**Owner:** Codex
**Opened:** 2026-07-11
**Completed:** 2026-07-11

## Original Gap

The book discusses image formats and briefly names structured DICOM-RT objects, but it does not teach the data model needed to build or assess radiotherapy AI. Readers are not shown how images, structure sets, plans, dose, treatment records, registrations, prescriptions, notes, outcomes, and longitudinal identifiers relate. Coordinate systems, resampling, units, ontology harmonization, cohort construction, provenance, de-identification, and data leakage are all potential sources of silent and clinically serious error.

This is a prerequisite for nearly every technical chapter and for competent interpretation of published research. A model architecture cannot compensate for a mislabeled structure, an inconsistent frame of reference, patient-level leakage, or a dose grid interpreted in the wrong geometry.

## What Is Needed

1. Add a radiotherapy data-model section covering DICOM images and the major RT objects (RT Structure Set/Segmentation, RT Plan, RT Dose, registrations, treatment records, and relevant newer objects), plus oncology information systems and non-DICOM clinical data.
2. Explain frames of reference, orientation, spacing, voxel and world coordinates, units, contour rasterization, dose-grid alignment, and the consequences of resampling and interpolation.
3. Cover practical data curation: cohort definitions, inclusion/exclusion flow, patient-level splitting, longitudinal linkage, duplicated studies, missingness, label provenance, inter-observer variation, ontology/name harmonization, and versioning.
4. Explain preprocessing without data leakage, including normalization, augmentation, registration, patch extraction, and transformations fitted only on development data.
5. Cover de-identification of metadata, burned-in pixels, free text, dates, facial anatomy, and linked records; distinguish anonymization, pseudonymization, consent, and data governance.
6. Introduce reproducible dataset documentation, data dictionaries, model/data cards, FAIR principles, public RT datasets, federated/distributed learning, and dataset-access limitations.
7. Link this material from every application chapter rather than repeating it.

## Acceptance Criteria

- [x] A diagram or table shows how imaging, contours, plans, dose, registrations, delivery records, clinical variables, and outcomes connect for one patient
- [x] The chapter explains frames of reference, coordinate transforms, units, grid alignment, resampling, and contour conversion with at least one worked failure example
- [x] Cohort construction and patient-level/temporal splitting guidance explicitly prevents common leakage modes
- [x] Label provenance, missing data, naming harmonization, versioning, and longitudinal identity are covered
- [x] De-identification covers metadata, pixels, free text, dates, and linked data, with jurisdiction-dependent legal statements clearly labeled
- [x] At least three representative public radiotherapy datasets are described with modality, task, license/access, and known limitations
- [x] Application chapters link to this canonical treatment instead of duplicating data-handling guidance

## What Was Done

1. Added a canonical `Radiotherapy Data and Informatics Foundations` section to `docs/medicalImaging/medicalImaging.md`.
2. Documented the connected patient-level data model spanning longitudinal identity, images, structures/segmentations, prescriptions, plans, dose, registrations, delivery records, clinical variables, and outcomes, including legacy and newer RT objects.
3. Added physical-coordinate and unit guidance, contour rasterization and resampling controls, and a worked dose-grid failure example.
4. Added cohort manifests, inclusion/exclusion flows, duplicate and version controls, label provenance, missingness, ontology mapping, patient-level and temporal splitting, and training-only preprocessing guidance.
5. Added a clearly labeled jurisdiction-dependent privacy note and technical controls for metadata, pixels, free text, dates, facial anatomy, and linked records.
6. Added dataset documentation, FAIR and federated-learning guidance, plus a comparison of NSCLC-Radiomics, LCTSC, Head-Neck-PET-CT, and OpenKBP.
7. Linked the canonical section from contouring, registration, treatment planning, QA, validation, and workflow chapters.

## Verification

- Verified DICOM object, coordinate, and confidentiality claims against the DICOM Standard and Working Group 7 materials.
- Verified dataset modalities, access/license terms, versions, and stated limitations against TCIA collection pages and the peer-reviewed OpenKBP dataset paper.
- Confirmed all seven acceptance criteria are represented in the chapter and all six downstream application chapters link to the canonical treatment.
- Ran `git diff --check` and a clean strict Sphinx documentation build.
