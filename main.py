"""Last Text at One Percent — the dying phone's final text.

The phone "fixes" its dying battery the only way it knows how: by
deleting the things draining it — the owner's 4,000 photos, the ex,
and, to save power, itself. The kicker absolves the charger, the one
thing that was never at fault. One clause of setup, payoff at the end.
The opening is just "1%." — the whole setup fits in a text fragment,
and every word after it earns its place.
"""

import os

ENTRY = (
    "1%. I fixed the battery: deleted your 4,000 photos, your ex, "
    "and, to save power, myself. Tell the charger it wasn't its fault."
)

# The gate: 1 to 200 characters, a single line, not only whitespace.
assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
assert "\n" not in ENTRY, "entry must be a single line"
assert ENTRY.strip(), "entry must not be only whitespace"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
