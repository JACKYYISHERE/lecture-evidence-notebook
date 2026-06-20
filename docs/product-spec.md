# Product Spec

## Working Name

Lecture Evidence Notebook

## One-Line Pitch

A local-first study tool that syncs lecture recordings, transcripts, slides, and professor annotations into evidence-linked study notes.

## Target Users

- students with long recorded lectures,
- exam-focused learners,
- courses where slides are incomplete without professor explanations,
- users who care about timestamped evidence.

## Core User Stories

1. As a student, I can create one bundle per lecture.
2. As a student, I can search a topic and find the matching recording timestamp.
3. As a student, I can send a slide screenshot and recover the professor's classroom notes.
4. As a student, I can save a classroom example into memory and reuse it later.
5. As a student, I can export cleaned evidence notes for backup or external review.

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
- multi-course dashboard.

## Non-Goals

- Do not host private recordings.
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
- professor annotation,
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
