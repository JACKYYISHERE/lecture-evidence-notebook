#!/usr/bin/env python3
import argparse
import html
import re
from pathlib import Path


def strip_vtt_markup(text: str) -> str:
    return html.unescape(re.sub(r"<[^>]+>", "", text)).strip()


def parse_vtt(vtt: str) -> list[dict]:
    lines = vtt.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    cues = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line or line == "WEBVTT" or line.isdigit():
            i += 1
            continue
        if "-->" not in line:
            i += 1
            continue
        start, rest = line.split("-->", 1)
        end = rest.split()[0]
        i += 1
        text_lines = []
        while i < len(lines) and lines[i].strip():
            text_lines.append(strip_vtt_markup(lines[i]))
            i += 1
        text = " ".join(t for t in text_lines if t).strip()
        speaker = ""
        match = re.match(r"^([^:]{1,80}):\s+(.*)$", text)
        if match:
            speaker, text = match.group(1).strip(), match.group(2).strip()
        if text:
            cues.append({"start": start.strip(), "end": end.strip(), "speaker": speaker, "text": text})
    return cues


def srt_timestamp(ts: str) -> str:
    return ts.replace(".", ",")


def write_outputs(cues: list[dict], out_dir: Path, base: str) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)

    (out_dir / f"{base}.txt").write_text(
        "\n".join(
            f"[{c['start']}] {c['speaker'] + ': ' if c['speaker'] else ''}{c['text']}" for c in cues
        ) + "\n",
        encoding="utf-8",
    )

    (out_dir / f"{base}.srt").write_text(
        "\n".join(
            f"{idx}\n{srt_timestamp(c['start'])} --> {srt_timestamp(c['end'])}\n"
            f"{c['speaker'] + ': ' if c['speaker'] else ''}{c['text']}\n"
            for idx, c in enumerate(cues, 1)
        ),
        encoding="utf-8",
    )

    md = [f"# Transcript", "", f"- Cues: {len(cues)}", ""]
    for c in cues:
        who = f" **{c['speaker']}**:" if c["speaker"] else ""
        md.append(f"- `{c['start']} - {c['end']}`{who} {c['text']}")
    (out_dir / f"{base}.md").write_text("\n".join(md) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Convert WebVTT transcript to Markdown, TXT, and SRT.")
    parser.add_argument("vtt", help="Input .vtt file.")
    parser.add_argument("--out-dir", default=None, help="Output directory. Defaults to input file directory.")
    parser.add_argument("--base", default="transcript", help="Output basename.")
    args = parser.parse_args()

    vtt_path = Path(args.vtt)
    out_dir = Path(args.out_dir) if args.out_dir else vtt_path.parent
    cues = parse_vtt(vtt_path.read_text(encoding="utf-8"))
    write_outputs(cues, out_dir, args.base)
    print(f"Converted {len(cues)} cues into {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

