import unittest

from camelot_core.compatibility_explanations import (
    explain_compatibility,
)


class TestCompatibilityExplanations(unittest.TestCase):
    def test_explanations_for_8a(self):
        result = explain_compatibility("8A")

        self.assertEqual(
            list(result),
            ["7A", "8A", "9A", "8B"],
        )
        self.assertEqual(result["8A"], "Misma tonalidad.")
        self.assertEqual(
            result["7A"],
            "Tonalidad vecina en la rueda Camelot.",
        )
        self.assertEqual(
            result["9A"],
            "Tonalidad vecina en la rueda Camelot.",
        )
        self.assertEqual(
            result["8B"],
            "Mismo número, modo mayor/menor relativo "
            "en la rueda Camelot.",
        )

    def test_all_positions_have_explanations(self):
        for number in range(1, 13):
            for letter in ("A", "B"):
                code = f"{number}{letter}"

                with self.subTest(code=code):
                    result = explain_compatibility(code)
                    self.assertEqual(len(result), 4)
                    self.assertIn(code, result)

    def test_invalid_code(self):
        with self.assertRaises(ValueError):
            explain_compatibility("13A")


if __name__ == "__main__":
    unittest.main()
