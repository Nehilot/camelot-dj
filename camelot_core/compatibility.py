"""Basic harmonic compatibility rules for Camelot DJ."""

from camelot_core.camelot import CAMELOT_KEYS


def compatible_keys(code):
    """Return the basic harmonically compatible Camelot codes."""
    if code not in CAMELOT_KEYS:
        raise ValueError(f"Invalid Camelot code: {code}")

    number = int(code[:-1])
    letter = code[-1]

    previous_number = 12 if number == 1 else number - 1
    next_number = 1 if number == 12 else number + 1
    other_letter = "B" if letter == "A" else "A"

    return [
        f"{previous_number}{letter}",
        code,
        f"{next_number}{letter}",
        f"{number}{other_letter}",
    ]
