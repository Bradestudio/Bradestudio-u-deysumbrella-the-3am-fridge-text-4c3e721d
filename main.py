"""The 3AM Fridge Text — make.fun entry.

Writes the single line a smart fridge texts its owner at 3am to
/output/entry.txt. Standard library only, no network, no clock,
no local imports. Deterministic: the same bytes on every run.
"""

import os

ENTRY = (
    "3am. I keep your food cold and your secrets colder. "
    "The leftovers and I already talked about you. Go back to bed."
)

# Gate, mirrored from the competition rules: 1-140 UTF-8 characters,
# a single line, not only white space, no trailing newline.
assert 1 <= len(ENTRY) <= 140, len(ENTRY)
assert "\n" not in ENTRY and ENTRY.strip() == ENTRY


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
