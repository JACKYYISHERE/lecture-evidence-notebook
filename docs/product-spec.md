# Product Spec

## Working Name

Lecture Evidence Notebook

## One-Line Pitch

A local-first study tool that syncs recordings, transcripts, slides, and instructor annotations into evidence-linked study notes.

## Target Users

- learners with long recorded classes, workshops, talks, or tutorials,
- exam-focused learners,
- sessions where slides are incomplete without instructor explanations,
- users who care about timestamped evidence.

## Core User Stories

1. As a learner, I can create one bundle per recorded session.
2. As a learner, I can search a topic and find the matching recording timestamp.
3. As a learner, I can send a slide screenshot and recover the instructor's notes or annotations.
4. As a learner, I can save an example into memory and reuse it later.
5. As a learner, I can export cleaned evidence notes for backup or external review.

## MVP Scope

Must have:

- bundle initializer,
- VTT transcript converter,
- local HTTP Range server for video seeking,
- memory templates,
- example bank schema,
- safety-focused GitHub docs.

Should have next:

- screenshot capture helper,
- transcript snippet extractor by timestamp,
- topic-to-chapter matcher,
- cleaned evidence export folder generator.

Could have later:

- OCR for frames,
- automatic slide matching,
- vector search,
- web UI,
- browser extension,
- multi-course or multi-subject dashboard.

## Non-Goals

- Do not host private or restricted recordings.
- Do not bypass platform permissions.
- Do not replace copyright checks.
- Do not promise perfect handwriting OCR.
- Do not analyze a full multi-hour recording unless the user asks and accepts the cost.

## Evidence Standard

A good generated note should include:

- screenshot filename,
- recording timestamp,
- slide/page,
- transcript cue,
- rule,
- instructor annotation,
- exam handling,
- trap,
- memory line.

## Component Dependencies

Required:

- Python 3.10+,
- `rg` recommended for fast search,
- a browser for local video playback.

Optional:

- `ffmpeg` for direct frame extraction,
- OpenCLI or another browser automation layer,
- OCR tool for image-like PDFs/slides,
- optional external study tools for review, if useful.
