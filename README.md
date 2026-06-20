# Lecture Evidence Notebook

Local-first tooling for turning recorded classes, workshops, talks, and tutorials into evidence-linked study notes.

The goal is not to summarize a lecture blindly. The goal is to keep every useful note traceable to:

- the official slide/PDF page,
- the transcript timestamp,
- the recording frame / instructor annotation screenshot,
- and a reusable example or exam trap.

## Why This Exists

Many learning sessions have the important material split across different places:

- slides show the formal rule,
- the instructor explains the logic orally,
- the recording shows handwritten annotations, arrows, circles, and examples,
- the platform summary gives a topic map.

Most AI note tools handle only one or two of these. This project keeps them together in a local bundle.

## Repo vs Local Data

This repository contains reusable tooling and templates:

- scripts,
- schemas,
- templates,
- workflow docs,
- empty/sample memory files.

Each user brings their own local learning materials:

- recordings,
- platform transcripts,
- slide PDFs,
- screenshots,
- Smart Summary / chapter exports,
- course memory.

Those files live in local bundle folders such as `local_bundles/`. A different user or AI agent should clone the repo, then create their own local bundles with their own materials.

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
  recording.mp4              # local user material
  recording_audio.m4a         # local user material
  transcript.vtt              # local user material
  transcript.md               # generated local transcript
  slides.pdf                  # local user material
  smart_summary.md            # optional local platform export
  smart_chapters.json         # optional local platform export
  frames/                     # local screenshots
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

Clone the repo:

```bash
git clone https://github.com/JACKYYISHERE/lecture-evidence-notebook.git
cd lecture-evidence-notebook
```

For another AI agent, start here:

```text
Read README.md first.
Then read docs/workflow.md and docs/opencli-workflow.md.
Use scripts/init_bundle.py to create a local bundle.
Put the user's own recordings, transcripts, slides, and screenshots into that local bundle.
```

Create a local bundle:

```bash
python3 scripts/init_bundle.py \
  --course "Example Course" \
  --lecture "2026-06-17-session-01" \
  --out ./local_bundles
```

Convert a WebVTT transcript:

```bash
python3 scripts/vtt_to_markdown.py \
  ./local_bundles/2026-06-17-session-01/transcript.vtt \
  --out-dir ./local_bundles/2026-06-17-session-01
```

Serve a bundle so Chrome can seek long MP4 recordings:

```bash
python3 scripts/range_server.py \
  ./local_bundles/2026-06-17-session-01 \
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
I have a screenshot of a formula slide. Find the classroom note.
```

Expected process:

```text
formula keywords
→ smart chapter: relevant topic range
→ transcript around the matching explanation
→ screenshot frame around the annotated moment
→ note explains the slide rule, instructor annotation, worked example, and common trap
```

## Tooling Philosophy

- Local-first: private materials stay on your machine.
- Evidence-first: every explanation should point to a screenshot filename and timestamp.
- Search-first: use `rg` and structured memory before loading long transcripts.
- Small-memory: do not store whole chats; store reusable learning assets.
- Human-in-the-loop: do not OCR or analyze the whole recording unless needed.

## Docs

- [Agent quick start](docs/agent-quick-start.md)
- [Product spec](docs/product-spec.md)
- [Component requirements](docs/components.md)
- [Workflow](docs/workflow.md)
- [Memory system](docs/memory-system.md)
- [OpenCLI workflow](docs/opencli-workflow.md)
- [GitHub publishing notes](docs/github-notes.md)
