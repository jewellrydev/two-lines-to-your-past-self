#!/usr/bin/env python3
"""Two Lines to Your Past Self entry: a warning and why the moment mattered."""
import os

LINES = (
    "When the deploy breaks at 2 a.m. and you reach for the rewrite button, stop and count the semicolons first: it is one missing semicolon, and it is always the semicolon.",
    "That night mattered because panic wrote worse code than the bug did, and every calm fix since then has started with rereading the error message instead of fearing it.",
)


def main() -> None:
    os.umask(0o022)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(LINES) + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
