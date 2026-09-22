"""Explanations for basic Camelot compatibility suggestions."""

from camelot_core.camelot import CAMELOT_KEYS
from camelot_core.compatibility import compatible_keys


def explain_compatibility(code):
    """Return compatible Camelot codes with a Spanish explanation."""
    if code not in CAMELOT_KEYS:
        raise ValueError(f"Invalid Camelot code: {code}")

    number = int(code[:-1])
    letter = code[-1]

    explanations = {}

    for candidate in compatible_keys(code):
        candidate_number = int(candidate[:-1])
        candidate_letter = candidate[-1]

        if candidate == code:
            reason = "Misma tonalidad."
        elif candidate_letter != letter:
            reason = (
                "Mismo número, modo mayor/menor relativo "
                "en la rueda Camelot."
            )
        else:
            reason = "Tonalidad vecina en la rueda Camelot."

        explanations[candidate] = reason

    return explanations
