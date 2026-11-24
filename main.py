"""Entrypoint for the houseplant out-of-office make.fun entry.

Writes the one-line out-of-office message to /output/entry.txt.

The fern is out until spring and is not checking anything.
"""

from pathlib import Path

PARTS = [
    "Out of office until spring. I am a fern: ",
    "I have ignored 3 emails, 2 meetings, ",
    "and one full watering this week.",
]


def entry_text() -> str:
    # The parts join into a single one-line message (one fern, three ignored emails).
    return "".join(PARTS).strip()


def main() -> None:
    text = entry_text()
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
