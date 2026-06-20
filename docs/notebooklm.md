# NotebookLM Integration

NotebookLM is useful as a document Q&A and study guide layer. It is not a replacement for local recording/frame extraction.

## Recommended Split

Local tool:

- downloads and stores files,
- extracts transcript,
- finds timestamps,
- screenshots recording annotations,
- builds evidence notes,
- maintains course memory.

NotebookLM:

- reads cleaned notes,
- answers across topics,
- creates study guides,
- creates quizzes,
- compares rules and examples.

## Export Set

Upload these when allowed:

- `topic_index.md`
- `example_bank.json`
- `screenshot_index.md`
- `quiz_traps.md`
- `annotation_notes.md`
- selected transcript snippets
- slides/PDF only if you have permission

## Why Not Upload Raw Video First

Raw video is large, private, and not always searchable. The useful information is usually a small number of evidence-linked moments.

Better:

```text
recording.mp4 -> local screenshots + timestamp index -> NotebookLM documents
```

