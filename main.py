#!/usr/bin/env python3
"""One Star, Five Stars for the Food — make.fun entry.

Writes one sentence (<=200 chars) to /output/entry.txt: an alien tourist's
one-star review of Earth that still slips in a real compliment about the food.
The text is fixed and deterministic: two runs produce byte-identical output.
"""

import os

ENTRY = (
    "One star: you stare at glowing rectangles while your food gets cold, "
    "but Mbak Sari's nasi goreng earned five stars \u2014 I missed my third "
    "ship home on purpose."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.count(".") == 1, "entry must be a single sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
