# Lecture Evidence Notebook

Local-first tooling for turning lecture recordings into evidence-linked study notes.

The goal is not to summarize a lecture blindly. The goal is to keep every useful note traceable to:

- the official slide/PDF page,
- the transcript timestamp,
- the recording frame / professor annotation screenshot,
- and a reusable example or exam trap.

## Why This Exists

Many lectures have the important material split across different places:

- slides show the formal rule,
- the professor explains the logic orally,
- the recording shows handwritten annotations, arrows, circles, and examples,
- the platform summary gives a topic map.

Most AI note tools handle only one or two of these. This project keeps them together in a local bundle.

## What Goes On GitHub

Commit this repository:

- scripts,
- schemas,
- templates,
- workflow docs,
- empty/sample memory files.

Do **not** commit private or copyrighted course assets:

- recordings,
- Zoom transcripts,
- slide PDFs,
- screenshots containing course materials,
- student/course identifiers,
- paid course content.

The `.gitignore` is set up to keep real lecture bundles and media out of Git.

## Core Workflow

1. Create a lecture bundle.
2. Add local files: `recording.mp4`, `transcript.vtt`, `slides.pdf`, optional `smart_summary.md`.
3. Convert VTT into readable transcript formats.
4. Use smart summary and transcript search to locate topic time ranges.
5. Open the recording locally with HTTP Range support and capture screenshots around the relevant timestamp.
6. Write an evidence-linked classroom note.
7. Register reusable examples in course memory.

## Directory Model

```text
lecture_bundle/
  manifest.json
  recording.mp4              # ignored by Git
  recording_audio.m4a         # ignored by Git
  transcript.vtt              # ignored by Git by default
  transcript.md               # ignored by Git by default
  slides.pdf                  # ignored by Git
  smart_summary.md            # optional, ignored if private
  smart_chapters.json         # optional, ignored if private
  frames/                     # screenshots, ignored by Git
  notes/
    annotation_notes.md
    screenshot_index.md

course_memory/
  topic_index.md
  screenshot_index.md
  example_bank.json
  quiz_traps.md
  open_questions.md
```

## Quick Start

Create a local bundle:

```bash
python3 scripts/init_bundle.py \
  --course "HK Tax" \
  --lecture "2026-06-17-profit-tax-pa" \
  --out ./local_bundles
```

Convert a Zoom VTT transcript:

```bash
python3 scripts/vtt_to_markdown.py \
  ./local_bundles/2026-06-17-profit-tax-pa/transcript.vtt \
  --out-dir ./local_bundles/2026-06-17-profit-tax-pa
```

Serve a bundle so Chrome can seek long MP4 recordings:

```bash
python3 scripts/range_server.py \
  ./local_bundles/2026-06-17-profit-tax-pa \
  --port 8766
```

Open:

```text
http://127.0.0.1:8766/recording.mp4
```

## Evidence Note Format

```text
Example identity:
Recording:
Screenshot/frame:
Slide/page:
Transcript cue:

Slide rule:

Professor annotation:

Exam answer:

Trap:

Memory:
```

## Example Use Case

Question:

```text
I have a screenshot of the Interest Income slide. Find the classroom note.
```

Expected process:

```text
Interest Income
→ smart chapter: Interest Income Exemption Process
→ transcript around 04:08:20 - 04:33:24
→ screenshot frame around 04:29:50
→ note explains #1 receiver, #2 HK source, #3 exemption, security + interest expense restriction
```

## Tooling Philosophy

- Local-first: private materials stay on your machine.
- Evidence-first: every explanation should point to a screenshot filename and timestamp.
- Search-first: use `rg` and structured memory before loading long transcripts.
- Small-memory: do not store whole chats; store reusable learning assets.
- Human-in-the-loop: do not OCR or analyze the whole recording unless needed.

## Docs

- [Product spec](docs/product-spec.md)
- [Component requirements](docs/components.md)
- [Workflow](docs/workflow.md)
- [Memory system](docs/memory-system.md)
- [GitHub publishing notes](docs/github-notes.md)
