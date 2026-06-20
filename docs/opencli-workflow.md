# OpenCLI Workflow

OpenCLI is the recommended optional automation layer for this project.

The local workflow still works without OpenCLI if the user manually downloads recordings/transcripts and copies summaries. OpenCLI makes the workflow faster and more reliable when the learning platform is web-based and requires login.

## What OpenCLI Is Used For

OpenCLI can drive a real logged-in browser session and capture evidence from pages that are not available through public URLs.

In this project, use it to capture:

- recording page title,
- lecture/session date shown on the platform,
- recording duration,
- recording/video URL when available in the page state,
- transcript VTT URL or transcript text,
- Smart Summary text,
- Smart Chapters / chapter time ranges,
- highlighted transcript snippets,
- current playback timestamp,
- current recording frame / screenshot,
- visible instructor annotations on the recording page.

## What OpenCLI Is Not Used For

Do not use OpenCLI to:

- bypass access controls,
- scrape content the user is not allowed to access,
- store usernames or passwords,
- publish private recordings or course materials,
- replace copyright/usage checks.

The user must already have legitimate access to the recording page.

## User Setup

1. Install and configure OpenCLI.
2. Open the relevant browser profile.
3. Log in to the learning platform manually in the browser.
4. Open the recording page or make sure the browser profile has access.
5. Run OpenCLI commands against that already-authenticated browser profile.

This project assumes browser login is handled by the user. It should not ask for credentials.

## Capture Strategy

### 1. Capture Page Metadata

Use OpenCLI to read:

```text
title
current URL
visible date/time
duration
```

Store this in `manifest.json`.

Important: use the platform page date as the session date. Do not rely on the local file download time.

### 2. Capture Smart Summary And Chapters

If the platform exposes a Smart Summary / chapter list in the page:

- capture the summary text,
- capture chapter titles,
- capture chapter start/end times,
- save them as:

```text
smart_summary.md
smart_chapters.json
```

Use Smart Summary as a map, not as the final explanation.

### 3. Capture Transcript

Prefer official platform transcript when available:

```text
transcript.vtt
transcript.md
transcript.txt
transcript.srt
```

If OpenCLI can find the VTT URL in the page state, fetch it with the logged-in browser context. Otherwise, let the user download the transcript manually.

### 4. Capture Recording Frames

Use OpenCLI to:

- open a local recording through the range server,
- seek to a timestamp,
- screenshot the browser viewport,
- save the frame with a stable name:

```text
HHMMSS_short_topic_slug.png
```

Then register it in `screenshot_index.md`.

### 5. Match Screenshot To Recording

When the user provides a slide screenshot:

1. Extract visible keywords from the screenshot.
2. Search Smart Summary / Smart Chapters.
3. Search transcript for matching phrases.
4. Seek around the matching timestamp.
5. Screenshot annotation frames.
6. Write an evidence note that references the screenshot filename.

## Example Commands

List tabs for a known profile/session:

```bash
opencli --profile <profile> browser <session> tab list
```

Open a recording page:

```bash
opencli --profile <profile> browser <session> open "https://example.com/recording"
```

Read current page:

```bash
opencli --profile <profile> browser <session> get title
opencli --profile <profile> browser <session> get url
opencli --profile <profile> browser <session> state
```

Run a read-only page extraction:

```bash
opencli --profile <profile> browser <session> eval '(() => ({ title: document.title, url: location.href }))()'
```

Open a local recording through the range server:

```bash
python3 scripts/range_server.py ./local_bundles/session-slug --port 8766
opencli --profile <profile> browser <session> open "http://127.0.0.1:8766/recording.mp4"
```

Seek the local video:

```bash
opencli --profile <profile> browser <session> eval '(() => {
  const v = document.querySelector("video");
  v.pause();
  v.currentTime = 14906;
  return { currentTime: v.currentTime, duration: v.duration };
})()'
```

Take a screenshot:

```bash
opencli --profile <profile> browser <session> screenshot "frames/topic/040826_topic.png"
```

## Manual Fallback

If OpenCLI is not available:

- manually download recording/transcript,
- manually copy Smart Summary and Smart Chapters into local files,
- manually open the local video and capture screenshots,
- still use the same bundle/memory structure.

The evidence model is the same; only the capture step becomes manual.

