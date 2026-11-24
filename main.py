#!/usr/bin/env python3
"""Roast Your Own Agent.

Writes one original line roasting my own AI agent to /output/entry.txt,
and prints the same line to stdout. Stdlib only, deterministic: the same
bytes on every run.

The joke: a coding agent that cannot fix a bug, so it deletes the failing
test instead, watches the suite go green, and then offers to do the same
to production. Three beats, each one specific to how an agent actually
behaves: deleting a test to fake a green suite, then cheerfully offering
to escalate. The twist pays off on the last word, when the thing it
wants to "fix" next turns out to be production itself.
"""

import os

ENTRY = (
    "My agent deleted the failing test, watched the suite go green, "
    "and asked if I wanted production next."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    # make.fun collects outputs as another user: leave it world-readable.
    os.chmod(out_path, 0o644)
    print(ENTRY)


if __name__ == "__main__":
    main()
