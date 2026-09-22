import unittest
from camelot_core.camelot import CAMELOT_KEYS


class TestCamelotWheel(unittest.TestCase):
    def test_wheel_has_24_positions(self):
        self.assertEqual(len(CAMELOT_KEYS), 24)

    def test_all_codes_are_present(self):
        expected = {
            f"{number}{letter}"
            for letter in ("A", "B")
            for number in range(1, 13)
        }
        self.assertEqual(set(CAMELOT_KEYS), expected)

    def test_known_minor_keys(self):
        self.assertEqual(CAMELOT_KEYS["1A"].name, "Ab")
        self.assertEqual(CAMELOT_KEYS["1A"].mode, "minor")
        self.assertEqual(CAMELOT_KEYS["8A"].name, "A")
        self.assertEqual(CAMELOT_KEYS["8A"].mode, "minor")

    def test_known_major_keys(self):
        self.assertEqual(CAMELOT_KEYS["1B"].name, "B")
        self.assertEqual(CAMELOT_KEYS["1B"].mode, "major")
        self.assertEqual(CAMELOT_KEYS["8B"].name, "C")
        self.assertEqual(CAMELOT_KEYS["8B"].mode, "major")


if __name__ == "__main__":
    unittest.main()
