# Memory System

The memory system prevents long-chat context blowup. It stores reusable learning assets instead of raw conversations.

## Principle

Do not remember everything.

Remember only:

- topics,
- examples,
- screenshots,
- traps,
- open questions,
- evidence links.

## Files

```text
course_memory/
  topic_index.md
  screenshot_index.md
  example_bank.json
  quiz_traps.md
  open_questions.md
```

## `topic_index.md`

Use for topic navigation.

Store:

- topic name,
- lecture/bundle,
- recording range,
- slide reference,
- transcript reference,
- related examples,
- related topics.

## `screenshot_index.md`

Use for visual evidence.

Every screenshot should have:

- stable filename,
- recording timestamp,
- slide/page reference,
- transcript cue,
- what the instructor wrote,
- what it means,
- examples that use it.

When tutoring, always refer to the screenshot filename.

## `example_bank.json`

Use for reusable classroom examples.

Every example should have:

- `id`,
- `identity`,
- `topic`,
- `recording_time`,
- `screenshot`,
- `slide_ref`,
- `transcript_ref`,
- `rules`,
- `trap`,
- `memory`.

## `quiz_traps.md`

Use for exam risk.

Store:

- trap,
- why learners get it wrong,
- correct handling,
- evidence.

## `open_questions.md`

Use when something is not solved yet.

Store:

- unclear point,
- evidence already checked,
- next action.

## Retrieval

Use exact search before loading large files:

```bash
rg -n "keyword one|keyword two|example name" course_memory/ local_bundles/*/transcript.md
```

Then load only the matching topic/example/screenshot sections.
