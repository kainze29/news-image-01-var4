"""news-image-01 var4: deliver the breaking-news timeline image.

The picture (news.png, next to this script) tells Friday 13 November
2026 the way a TV newsroom would: a red BREAKING banner, then the
day's six biggest stories in the order they unfolded, each with a
time-of-day stamp and a short headline bar. This script only moves
that fixed picture into place at /output/entry.png, after checking
it really is the 1024x1024 PNG it claims to be, and confirming the
copy came out the same size. No network, no drawing at run time, so
every run produces the same file.
"""

import hashlib
import os
import shutil
import struct

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "news.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
TARGET = os.path.join(OUT_DIR, "entry.png")

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def check_png(path):
    """Read the header and confirm a whole 1024x1024 PNG."""
    with open(path, "rb") as fh:
        head = fh.read(33)
    if head[:8] != PNG_MAGIC:
        raise SystemExit("news.png is not a PNG file")
    if head[12:16] != b"IHDR":
        raise SystemExit("news.png has no IHDR chunk where one belongs")
    width, height = struct.unpack(">II", head[16:24])
    if (width, height) != (1024, 1024):
        raise SystemExit(f"news.png is {width}x{height}, expected 1024x1024")


def file_hash(path):
    """SHA-256 of a whole file, read in chunks."""
    digest = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    check_png(SOURCE)
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, TARGET)
    if os.path.getsize(TARGET) != os.path.getsize(SOURCE):
        raise SystemExit("entry.png came out a different size than news.png")
    if file_hash(TARGET) != file_hash(SOURCE):
        raise SystemExit("entry.png bytes differ from news.png")
    print(f"wrote {TARGET} ({os.path.getsize(TARGET)} bytes)")


if __name__ == "__main__":
    main()
