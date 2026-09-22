import unittest

from camelot_core.camelot import CAMELOT_KEYS
from camelot_core.compatibility import compatible_keys


class TestCompatibility(unittest.TestCase):
    def test_8a_compatibility(self):
        self.assertEqual(
            compatible_keys("8A"),
            ["7A", "8A", "9A", "8B"],
        )

    def test_wraparound_at_1(self):
        self.assertEqual(
            compatible_keys("1A"),
            ["12A", "1A", "2A", "1B"],
        )

    def test_wraparound_at_12(self):
        self.assertEqual(
            compatible_keys("12A"),
            ["11A", "12A", "1A", "12B"],
        )

    def test_invalid_code(self):
        with self.assertRaises(ValueError):
            compatible_keys("13A")

        with self.assertRaises(ValueError):
            compatible_keys("8C")

    def test_every_position_has_four_unique_compatible_keys(self):
        for code in CAMELOT_KEYS:
            with self.subTest(code=code):
                results = compatible_keys(code)

                self.assertEqual(len(results), 4)
                self.assertEqual(len(set(results)), 4)

                for result in results:
                    self.assertIn(result, CAMELOT_KEYS)

    def test_compatibility_is_symmetric(self):
        for code in CAMELOT_KEYS:
            for compatible_code in compatible_keys(code):
                with self.subTest(
                    code=code,
                    compatible_code=compatible_code,
                ):
                    self.assertIn(
                        code,
                        compatible_keys(compatible_code),
                    )


if __name__ == "__main__":
    unittest.main()
