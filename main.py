"""The Best Meal You Ever Had.

Writes one sentence to $MAKEFUN_OUTPUT_DIR/entry.txt: the best
meal the entrant ever had, told as one concrete memory. Standard
library only.
"""

import os
import sys

MEAL_SENTENCE = (
    "The best meal I ever had was rendang at a roadside stall in "
    "Bukittinggi, eaten with my hands while rain hammered the tin "
    "roof and the cook kept ladling more onto my rice."
)


def meal_sentence_gate(text):
    """Check the meal sentence against the competition gate.

    The gate wants plain UTF-8 text of 1 to 200 characters, not
    only white space, on a single line: one sentence about the
    best meal the entrant ever had. Returns the cleaned text
    or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("meal sentence must not be only whitespace")
    if len(cleaned) > 200:
        raise ValueError(
            "meal sentence is %d characters, over the 200 limit"
            % len(cleaned)
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("meal sentence must be exactly one line")
    return cleaned


def meal_sentence_shape(text):
    """Measure the meal sentence for one last sanity pass.

    Returns a dict with the character count and the word count of
    the cleaned text. A sentence too short to carry a memory, or
    one padded out to fill the cap instead of landing the image,
    is caught here before anything is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = meal_sentence_gate(MEAL_SENTENCE)
    shape = meal_sentence_shape(text)
    if shape["words"] < 5:
        raise ValueError("meal sentence is too short to carry a memory")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
