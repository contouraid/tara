# TODO: Literature Currency — Medical Imaging Chapter

**Section:** `medicalImaging/`
**Priority:** Medium
**Owner:** (unassigned)
**Opened:** 2026-07-10

## Gap

`medicalImaging/medicalImaging.md` has a real `## References` section (7 entries), but every entry is a general medical-imaging or DICOM reference (file formats, X-ray/nuclear-medicine background, the DICOM standard itself) — none are specific to AI applications in radiation oncology imaging, and none are from the last two years. There is no "Current Research and Recent Advances" section. The chapter's per-modality subsections (CT, MRI, ultrasound, PET, nuclear medicine) each describe clinical use in RT but don't reference AI-driven advances within each modality (e.g., synthetic-CT generation, low-dose CT denoising, MR-only planning workflows).

## What Is Needed

1. Add a `## Current Research and Recent Advances` section per the Chapter Content Standard in `GUIDE.md`, ideally with sub-entries organized by modality to match the chapter's existing structure.
2. Run the searches below (last 18 months, verified per the Sourcing Rules):
   - "synthetic CT generation deep learning MRI-only radiotherapy"
   - "CBCT to CT translation deep learning adaptive radiotherapy"
   - "diffusion model medical image synthesis radiotherapy"
   - "low dose CT denoising deep learning radiation oncology"
3. Add verified, cited entries covering AI-driven imaging advances per modality, particularly synthetic-CT / MR-only planning and CBCT enhancement, which are active, clinically-relevant sub-fields not currently mentioned at all despite the chapter covering CT and MRI in detail.

## Acceptance Criteria

- [ ] Chapter has a "Current Research and Recent Advances" section with at least 3 verified, dated citations
- [ ] At least one entry addresses synthetic-CT/MR-only planning and at least one addresses CBCT enhancement
- [ ] `## References` includes at least one AI-in-RT-imaging-specific source (not just general imaging/DICOM references)
- [ ] `todo/review-log.md` has an entry recording the searches run and sources found/rejected for this chapter
