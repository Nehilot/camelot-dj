"""Musical key definitions for Camelot DJ."""

from dataclasses import dataclass


NOTE_PITCH_CLASSES = {
    "C": 0,
    "B#": 0,
    "C#": 1,
    "Db": 1,
    "D": 2,
    "D#": 3,
    "Eb": 3,
    "E": 4,
    "Fb": 4,
    "E#": 5,
    "F": 5,
    "F#": 6,
    "Gb": 6,
    "G": 7,
    "G#": 8,
    "Ab": 8,
    "A": 9,
    "A#": 10,
    "Bb": 10,
    "B": 11,
    "Cb": 11,
}

VALID_NOTES = set(NOTE_PITCH_CLASSES)


@dataclass(frozen=True)
class MusicalKey:
    """Represent a musical key."""

    name: str
    mode: str

    def __post_init__(self):
        """Validate the musical note name and mode."""
        if self.name not in VALID_NOTES:
            raise ValueError(f"Invalid musical note: {self.name}")

        if self.mode not in ("major", "minor"):
            raise ValueError("mode must be major or minor")

    @property
    def pitch_class(self):
        """Return the note's pitch class, from 0 to 11."""
        return NOTE_PITCH_CLASSES[self.name]
