# TODO: Establish a Novice Learning Architecture

**Section:** Root (cross-cutting)
**Priority:** High
**Owner:** (unassigned)
**Opened:** 2026-07-11

## Gap

The repository is organized as a sequence of topics, but not yet as a coherent learning path. Chapters rarely state prerequisites or learning outcomes, terminology is introduced at uneven levels, and the detailed deep-learning chapter begins with the perceptron without first establishing data, labels, features, training, inference, uncertainty, or the end-to-end model-development lifecycle. A clinician, engineer, or general technical reader therefore cannot easily tell what to read first, what proficiency means, or which concepts are essential for a given role.

The existing glossary is embedded in the AI chapter and does not cover the combined AI, imaging, radiation-oncology, validation, and deployment vocabulary used across the book.

## What Is Needed

1. Define two or three explicit reader routes on `docs/index.md` (for example: clinician, technical/engineering, and complete beginner), including prerequisites and recommended chapter order.
2. Add measurable learning objectives and a short prerequisite/reading-route note to each chapter.
3. Add an early conceptual bridge explaining the common AI lifecycle: clinical question, data and labels, development split, training, validation, inference, deployment, monitoring, and retirement.
4. Create one cross-book glossary with canonical definitions, first-use expansion of abbreviations, and links from chapters; remove or redirect duplicate local definitions.
5. Add consistent end-of-chapter recaps that answer the learning objectives and identify common novice misconceptions or unsafe interpretations.
6. Define a small set of recurring example cases that later chapters can reference so readers can follow data and decisions through the complete radiotherapy pathway.

## Acceptance Criteria

- [ ] `docs/index.md` states the intended audiences, assumed knowledge, reader routes, and what a proficient reader should be able to do
- [ ] Every chapter begins with prerequisites and three to seven observable learning objectives
- [ ] The AI lifecycle is explained before detailed model architectures are introduced
- [ ] A single cross-book glossary covers AI, statistics, imaging, DICOM-RT, radiotherapy, validation, safety, and regulatory terminology
- [ ] Abbreviations are expanded on first use and conflicting definitions are reconciled
- [ ] Every recap maps back to its chapter's learning objectives and includes at least one important limitation or misconception
- [ ] A novice reviewer and one clinician or physicist reviewer can follow their stated route without encountering an undefined prerequisite term
