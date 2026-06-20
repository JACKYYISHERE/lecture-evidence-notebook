# Agent Quick Start

This document is for another AI agent or coding assistant that is asked to use this repository.

## Clone

```bash
git clone https://github.com/JACKYYISHERE/lecture-evidence-notebook.git
cd lecture-evidence-notebook
```

## Read First

Read these files in order:

1. `README.md`
2. `docs/workflow.md`
3. `docs/opencli-workflow.md`
4. `docs/memory-system.md`

## Core Rule

This repo stores tooling and templates. Each user supplies their own local learning materials.

When another agent uses this repo, it should create a local bundle for that user's materials:

```text
local_bundles/<session>/
```

The user's recordings, transcripts, slides, screenshots, and memory files belong there. They are local working data, not part of the reusable repo.

## Create A Local Bundle

```bash
python3 scripts/init_bundle.py \
  --course "Example Course" \
  --lecture "session-01" \
  --out ./local_bundles
```

Then put private files in the local bundle:

```text
local_bundles/session-01/
  recording.mp4
  transcript.vtt
  slides.pdf
  smart_summary.md
  smart_chapters.json
```

These are the user's own local files.

## Convert Transcript

```bash
python3 scripts/vtt_to_markdown.py \
  ./local_bundles/session-01/transcript.vtt \
  --out-dir ./local_bundles/session-01
```

## Serve Local Recording

Use this when the browser must seek a long local MP4:

```bash
python3 scripts/range_server.py ./local_bundles/session-01 --port 8766
```

Open:

```text
http://127.0.0.1:8766/recording.mp4
```

## OpenCLI Use

If OpenCLI is available, use it for browser automation:

- capture page title/date/duration,
- capture Smart Summary and Smart Chapters,
- capture transcript VTT URL or transcript text,
- seek recording timestamps,
- screenshot instructor annotations.

The user must log in manually in the browser first. Do not ask for credentials.

## Evidence Note Standard

When answering a learning question, include:

- example identity,
- recording timestamp,
- screenshot filename,
- slide/page reference,
- transcript cue,
- formal rule,
- instructor annotation,
- exam/use-case trap,
- memory line.

## Memory Update

After extracting a useful example, update:

- `course_memory/topic_index.md`
- `course_memory/screenshot_index.md`
- `course_memory/example_bank.json`
- `course_memory/quiz_traps.md`

Store memory in the user's local course workspace. The public repo only provides the structure and scripts.
