"""Conventional Camelot Wheel mappings."""

from camelot_core.keys import MusicalKey

CAMELOT_KEYS = {
    "1A": MusicalKey("Ab", "minor"),
    "2A": MusicalKey("Eb", "minor"),
    "3A": MusicalKey("Bb", "minor"),
    "4A": MusicalKey("F", "minor"),
    "5A": MusicalKey("C", "minor"),
    "6A": MusicalKey("G", "minor"),
    "7A": MusicalKey("D", "minor"),
    "8A": MusicalKey("A", "minor"),
    "9A": MusicalKey("E", "minor"),
    "10A": MusicalKey("B", "minor"),
    "11A": MusicalKey("F#", "minor"),
    "12A": MusicalKey("C#", "minor"),
    "1B": MusicalKey("B", "major"),
    "2B": MusicalKey("F#", "major"),
    "3B": MusicalKey("Db", "major"),
    "4B": MusicalKey("Ab", "major"),
    "5B": MusicalKey("Eb", "major"),
    "6B": MusicalKey("Bb", "major"),
    "7B": MusicalKey("F", "major"),
    "8B": MusicalKey("C", "major"),
    "9B": MusicalKey("G", "major"),
    "10B": MusicalKey("D", "major"),
    "11B": MusicalKey("A", "major"),
    "12B": MusicalKey("E", "major"),
}


def camelot_to_key(code):
    """Convert a Camelot code to its musical key."""
    if code not in CAMELOT_KEYS:
        raise ValueError(f"Invalid Camelot code: {code}")
    return CAMELOT_KEYS[code]


def key_to_camelot(name, mode):
    """Convert a musical key name and mode to a Camelot code."""
    key = MusicalKey(name, mode)

    for code, musical_key in CAMELOT_KEYS.items():
        if (
            musical_key.pitch_class == key.pitch_class
            and musical_key.mode == key.mode
        ):
            return code

    raise ValueError(f"Musical key not found: {name} {mode}")
