# Component Requirements

## 1. Lecture Bundle Manager

Purpose: create and maintain one local folder per recorded session.

Required:

- create standard folder structure,
- store `manifest.json`,
- record course/project name, session name, date, source URL, duration, and file paths,
- never assume Finder download time is the session date.

Inputs:

- recording file,
- transcript file,
- slides PDF,
- smart summary/chapter files if available.

Outputs:

- normalized bundle folder,
- manifest,
- derived transcript formats.

## 2. Transcript Processor

Purpose: convert platform transcript files into readable/searchable forms.

Required:

- parse WebVTT,
- preserve timestamps,
- output Markdown, plain text, and optionally SRT,
- tolerate noisy auto-transcription,
- keep speaker labels when present.

Nice to have:

- search snippets around timestamp,
- merge repeated cues,
- split by smart chapter.

## 3. Smart Chapter / Summary Mapper

Purpose: use platform summary as a topic map, not as final truth.

Required:

- read `smart_summary.md` and `smart_chapters.json`,
- map topic title to time range,
- let transcript and slides verify the result.

Important:

- Smart Summary may be transcript-only and may not understand handwritten annotations.
- Use it to locate, not to prove.

## 4. Slide / PDF Reference Layer

Purpose: anchor the formal rule/template.

Required:

- store slide PDF path in manifest,
- allow page references,
- support image-like PDFs via screenshots/OCR if text extraction fails.

Principle:

- slides/PDF define the formal material,
- transcript explains the material,
- recording frames capture instructor additions.

## 5. Recording Frame Extractor

Purpose: recover instructor annotations and screen context.

Required:

- jump to timestamp in local recording,
- capture screenshot frames,
- save with stable filename:
  `HHMMSS_short_topic_slug.png`,
- record screenshot in `screenshot_index.md`.

Options:

- use `ffmpeg` if available,
- otherwise serve local MP4 with HTTP Range support and screenshot the browser.

## 6. Course Memory System

Purpose: prevent long-chat context blowup.

Required files:

- `topic_index.md`,
- `screenshot_index.md`,
- `example_bank.json`,
- `quiz_traps.md`,
- `open_questions.md`.

Principle:

- Do not save whole conversations.
- Save reusable study assets with evidence links.

## 7. Tutor / Note Generator

Purpose: generate exam-oriented explanations from evidence.

Required output:

- example identity,
- screenshot filename,
- recording timestamp,
- slide/page reference,
- transcript cue,
- rule,
- instructor annotation,
- exam answer,
- trap,
- memory line.

## 8. Evidence Exporter

Purpose: export cleaned evidence notes for backup, sharing, or use in any external study tool.

Required:

- export Markdown files without private media,
- include screenshot filenames and timestamp references,
- include example bank and topic index.

Important:

- Export is optional. The local bundle and course memory are the source of truth.
- Do not export private recordings, restricted PDFs, or screenshots unless rights allow it.

## 9. Browser Automation Layer

Purpose: automate capture from logged-in recording pages.

Recommended implementation:

- OpenCLI, or another browser automation tool with an authenticated browser profile.

Required captures when available:

- page title,
- source URL,
- platform session date,
- recording duration,
- Smart Summary,
- Smart Chapters / chapter time ranges,
- transcript VTT URL or transcript text,
- current playback timestamp,
- current visible frame/screenshot,
- visible instructor annotations.

Important:

- The user must log in manually.
- Do not ask for or store credentials.
- Browser automation is optional; manual download/copy fallback must remain supported.
- See `docs/opencli-workflow.md`.
