# DONE: Establish a Novice Learning Architecture

**Section:** Root (cross-cutting)
**Priority:** High
**Owner:** Codex
**Opened:** 2026-07-11
**Completed:** 2026-07-12

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

- [x] `docs/index.md` states the intended audiences, assumed knowledge, reader routes, and what a proficient reader should be able to do
- [x] Every chapter begins with prerequisites and three to seven observable learning objectives
- [x] The AI lifecycle is explained before detailed model architectures are introduced
- [x] A single cross-book glossary covers AI, statistics, imaging, DICOM-RT, radiotherapy, validation, safety, and regulatory terminology
- [x] Abbreviations are expanded on first use and conflicting definitions are reconciled
- [x] Every recap maps back to its chapter's learning objectives and includes at least one important limitation or misconception
- [x] A novice reviewer and one clinician or physicist reviewer can follow their stated route without encountering an undefined prerequisite term

## What Was Done

1. Expanded `docs/index.md` with explicit clinician, physicist/engineer, and complete-beginner audiences; assumed knowledge; three recommended routes; six proficiency outcomes; and a minimum-safe selective route.
2. Defined three recurring cases—a head-and-neck curative course, lung stereotactic treatment, and pelvic adaptive workflow—and connected them to chapter route notes so the same data, decisions, risks, and responsibilities recur across the pathway.
3. Added a `Before you begin` section to all 12 numbered chapters and the language-model and vision-language companion pages. Each states prerequisites, five observable learning objectives, a role-aware reading route, and relevant recurring cases.
4. Added the common clinical AI lifecycle to Chapter 1 before model architectures: intended use, data and labels, development split, training, validation, inference, deployment, monitoring/change, and retirement. The section distinguishes data, labels, features, training, development-set validation, broader clinical validation, and inference.
5. Created `docs/resources/glossary.md` as the single canonical glossary for AI/model development, statistics/evidence, imaging/DICOM-RT, radiotherapy, validation, safety, deployment, and regulation. Added first-use and conflicting-term conventions, linked it from every chapter, and removed the duplicate local glossary from Chapter 2.
6. Rewrote every chapter and companion-page recap to answer its numbered objectives explicitly and end with an important limitation or novice misconception.
7. Expanded first-use abbreviations in the new learning architecture and reconciled ambiguous uses including development-set versus clinical validation, ART101 versus adaptive radiotherapy, ground truth versus reference standard, and quality assurance versus quality control.

## Verification

- Mechanically confirmed that all 12 numbered chapters have exactly one learning guide, objective block, recap, misconception warning, and canonical glossary link; each has five objectives, within the required range of three to seven.
- Confirmed the two Chapter 2 companion pages use the same structure and that `docs/resources/glossary.md` is the only glossary heading in the source tree.
- Performed structured route walkthroughs for (a) a complete beginner and (b) a clinician/physicist using the minimum-safe selective route. Each chapter now states the knowledge needed before entry and routes missing concepts to Chapter 1, Chapter 3, Chapter 4, or the canonical glossary before application-specific material.
- Confirmed each application/lifecycle chapter references at least one recurring case or the shared case set.
- Ran `git diff --check` successfully.
- Ran a strict Sphinx HTML build with warnings treated as errors: `make -C docs html SPHINXOPTS='-W --keep-going' BUILDDIR=_build/strict` (using the repository virtual environment). The build succeeded with no warnings.
