#!/usr/bin/env python3
import argparse
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path


def safe_slug(value: str) -> str:
    keep = []
    for ch in value.lower().strip():
        if ch.isalnum():
            keep.append(ch)
        elif ch in " -_.":
            keep.append("-")
    slug = "".join(keep).strip("-")
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug or "lecture"


def copy_template(src: Path, dst: Path) -> None:
    if src.exists() and not dst.exists():
        shutil.copyfile(src, dst)


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a local lecture evidence bundle.")
    parser.add_argument("--course", required=True, help="Course name.")
    parser.add_argument("--lecture", required=True, help="Lecture name or slug.")
    parser.add_argument("--out", default="local_bundles", help="Output parent directory.")
    parser.add_argument("--source-url", default="", help="Optional source recording URL.")
    parser.add_argument("--lecture-date", default="", help="Optional lecture date.")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    bundle = Path(args.out) / safe_slug(args.lecture)
    bundle.mkdir(parents=True, exist_ok=True)
    (bundle / "frames").mkdir(exist_ok=True)
    (bundle / "notes").mkdir(exist_ok=True)

    manifest = {
        "course": args.course,
        "lecture": args.lecture,
        "lecture_date": args.lecture_date,
        "source_url": args.source_url,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "duration": "",
        "notes": "Keep private media and course materials local. Do not commit this bundle unless rights allow it.",
        "files": {
            "recording": "recording.mp4",
            "audio": "recording_audio.m4a",
            "transcript_vtt": "transcript.vtt",
            "transcript_md": "transcript.md",
            "slides": "slides.pdf",
            "smart_summary": "smart_summary.md",
            "smart_chapters": "smart_chapters.json"
        }
    }

    manifest_path = bundle / "manifest.json"
    if not manifest_path.exists():
        manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    copy_template(root / "templates" / "lecture_bundle" / "annotation_notes.md", bundle / "notes" / "annotation_notes.md")
    if not (bundle / "notes" / "screenshot_index.md").exists():
        (bundle / "notes" / "screenshot_index.md").write_text("# Screenshot Index\n\n", encoding="utf-8")

    print(bundle)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

