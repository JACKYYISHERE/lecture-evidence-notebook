#!/usr/bin/env python3
import argparse
import os
import re
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path


class RangeRequestHandler(SimpleHTTPRequestHandler):
    def send_head(self):
        path = Path(self.translate_path(self.path))
        if not path.is_file():
            return super().send_head()

        size = path.stat().st_size
        range_header = self.headers.get("Range")
        if not range_header:
            self.send_response(200)
            self.send_header("Content-type", self.guess_type(str(path)))
            self.send_header("Content-Length", str(size))
            self.send_header("Accept-Ranges", "bytes")
            self.end_headers()
            return path.open("rb")

        match = re.match(r"bytes=(\d*)-(\d*)", range_header)
        if not match:
            self.send_error(416, "Invalid Range")
            return None

        start_s, end_s = match.groups()
        start = int(start_s) if start_s else 0
        end = int(end_s) if end_s else size - 1
        end = min(end, size - 1)
        if start > end or start >= size:
            self.send_error(416, "Requested Range Not Satisfiable")
            return None

        self.send_response(206)
        self.send_header("Content-type", self.guess_type(str(path)))
        self.send_header("Content-Range", f"bytes {start}-{end}/{size}")
        self.send_header("Content-Length", str(end - start + 1))
        self.send_header("Accept-Ranges", "bytes")
        self.end_headers()

        f = path.open("rb")
        f.seek(start)
        self.range = (start, end)
        return f

    def copyfile(self, source, outputfile):
        if hasattr(self, "range"):
            start, end = self.range
            remaining = end - start + 1
            while remaining > 0:
                chunk = source.read(min(1024 * 1024, remaining))
                if not chunk:
                    break
                outputfile.write(chunk)
                remaining -= len(chunk)
        else:
            super().copyfile(source, outputfile)


def main() -> int:
    parser = argparse.ArgumentParser(description="Serve a directory with HTTP Range support for local video seeking.")
    parser.add_argument("directory", help="Bundle directory to serve.")
    parser.add_argument("--host", default="127.0.0.1", help="Bind host. Defaults to localhost.")
    parser.add_argument("--port", type=int, default=8766, help="Port.")
    args = parser.parse_args()

    os.chdir(Path(args.directory).resolve())
    print(f"Serving {Path.cwd()} at http://{args.host}:{args.port}/")
    HTTPServer((args.host, args.port), RangeRequestHandler).serve_forever()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

