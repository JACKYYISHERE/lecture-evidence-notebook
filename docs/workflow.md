# Workflow

## A. New Lecture

1. Download or place lecture files locally.
2. Create bundle:

```bash
python3 scripts/init_bundle.py --course "Course or Project Name" --lecture "session-slug" --out ./local_bundles
```

3. Copy private files into the bundle:

```text
recording.mp4
transcript.vtt
slides.pdf
smart_summary.md
smart_chapters.json
```

If the recording page is web-based and requires login, OpenCLI can capture page metadata, Smart Summary, Smart Chapters, transcript URLs, and screenshots from the user's already-authenticated browser session. See `docs/opencli-workflow.md`.

4. Convert transcript:

```bash
python3 scripts/vtt_to_markdown.py ./local_bundles/session-slug/transcript.vtt --out-dir ./local_bundles/session-slug
```

5. Update `manifest.json` with source URL, date, duration, and slide reference.

## B. User Provides A Screenshot

1. Extract visible keywords:

```text
slide title, section number, entity names, unusual phrases, handwritten labels
```

2. Search:

```bash
rg -n "keyword" local_bundles/<lecture>/{smart_summary.md,smart_chapters.json,transcript.md}
```

3. Find time range:

```text
smart chapter range -> transcript cue -> nearby recording frames
```

4. Capture screenshots around the likely time.

5. Explain with evidence:

```text
Refer to screenshot: 042950_two_deposits_security_vs_free.png
Recording: 04:29:50
Transcript: 04:29:50 - 04:30:01
Slide/page: slides.pdf page X
```

## C. Add To Memory

Add a reusable example:

```json
{
  "id": "example-id",
  "course": "Course or project name",
  "topic": "Topic",
  "identity": "Short human-readable example identity",
  "recording_time": "HH:MM:SS",
  "screenshot": "frames/topic/HHMMSS_slug.png",
  "slide_ref": "slides.pdf page X",
  "transcript_ref": "transcript.md cue/timestamp",
  "rules": ["Rule 1", "Rule 2"],
  "trap": "Exam trap",
  "memory": "One-line memory hook"
}
```

Update:

- `topic_index.md`,
- `screenshot_index.md`,
- `quiz_traps.md`.

## D. Export Clean Evidence Notes

Export only cleaned documents:

```text
topic_index.md
screenshot_index.md
example_bank.json
quiz_traps.md
annotation_notes.md
selected transcript snippets
slides.pdf if sharing rights allow
```

Avoid uploading:

- full private or restricted recordings,
- paid or restricted PDFs without permission,
- raw transcripts if they contain private participant names or sensitive discussion.
