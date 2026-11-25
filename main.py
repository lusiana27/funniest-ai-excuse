"""The Funniest AI Excuse: write one line (max 200 characters) to /output/entry.txt.

Standard library only, so the grader image (python3.13, no third-party
packages) can run it. The output folder itself is never removed; only its
contents are cleared, because the grader treats /output as a mount point.
The line is written with no trailing newline, so the file's character count
is exactly the line's length.
"""

import os

LINE = (
    "I didn't fail your task - I promoted it to middle management, "
    "where it now spends its days in meetings about itself "
    "instead of getting done."
)


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert "\n" not in LINE, "line must be a single line"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
