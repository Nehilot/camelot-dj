import unittest

from camelot_core.camelot import (
    CAMELOT_KEYS,
    camelot_to_key,
    key_to_camelot,
)


class TestCamelotConversions(unittest.TestCase):
    def test_camelot_to_key(self):
        self.assertEqual(camelot_to_key("8A").name, "A")
        self.assertEqual(camelot_to_key("8A").mode, "minor")
        self.assertEqual(camelot_to_key("8B").name, "C")
        self.assertEqual(camelot_to_key("8B").mode, "major")

    def test_key_to_camelot(self):
        self.assertEqual(key_to_camelot("A", "minor"), "8A")
        self.assertEqual(key_to_camelot("C", "major"), "8B")
        self.assertEqual(key_to_camelot("Ab", "minor"), "1A")

    def test_all_positions_round_trip(self):
        for code, key in CAMELOT_KEYS.items():
            with self.subTest(code=code):
                self.assertEqual(
                    key_to_camelot(key.name, key.mode),
                    code,
                )
                self.assertEqual(camelot_to_key(code), key)

    def test_invalid_camelot_code(self):
        with self.assertRaises(ValueError):
            camelot_to_key("13A")

        with self.assertRaises(ValueError):
            camelot_to_key("8C")

    def test_unknown_musical_key(self):
        with self.assertRaises(ValueError):
            key_to_camelot("H", "major")

    def test_invalid_mode(self):
        with self.assertRaises(ValueError):
            key_to_camelot("A", "dorian")

    def test_enharmonic_equivalents(self):
        self.assertEqual(key_to_camelot("G#", "minor"), "1A")
        self.assertEqual(key_to_camelot("D#", "minor"), "2A")
        self.assertEqual(key_to_camelot("A#", "minor"), "3A")
        self.assertEqual(key_to_camelot("C#", "major"), "3B")
        self.assertEqual(key_to_camelot("F#", "major"), "2B")


if __name__ == "__main__":
    unittest.main()
