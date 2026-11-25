#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry (make.fun).

Writes a single original one-line office joke to ``entry.txt`` inside the
output directory (``/output`` in the grader sandbox, overridable with the
``OUTPUT_DIR`` environment variable for local runs).

Pure Python standard library only. Deterministic: the same joke every run.
"""

import os

JOKE = (
    "I asked HR for a raise and they gave me a standing desk, "
    "so now I stand here underpaid."
)


def main() -> None:
    text = JOKE.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
