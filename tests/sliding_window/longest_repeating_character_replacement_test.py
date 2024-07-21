import unittest

from problems.sliding_window.longest_repeating_character_replacement import LongestRepeatingCharacterReplacement


class LongestRepeatingCharacterReplacementTest(unittest.TestCase):

    def test_characterReplacement(self):
        self.assertEqual(LongestRepeatingCharacterReplacement.characterReplacement("AABABBA", 1), 4)
        self.assertEqual(LongestRepeatingCharacterReplacement.characterReplacement("", 2), 0)
        # noinspection PyTypeChecker
        self.assertEqual(LongestRepeatingCharacterReplacement.characterReplacement(None, 2), 0)
        self.assertEqual(LongestRepeatingCharacterReplacement.characterReplacement("A", 2), 1)
        self.assertEqual(LongestRepeatingCharacterReplacement.characterReplacement("ABCDE", 10), 5)
        self.assertEqual(LongestRepeatingCharacterReplacement.characterReplacement("AAAA", 2), 4)
        self.assertEqual(LongestRepeatingCharacterReplacement.characterReplacement("ABAB", 2), 4)
        self.assertEqual(LongestRepeatingCharacterReplacement.characterReplacement("ABCDE", 0), 1)
        self.assertEqual(LongestRepeatingCharacterReplacement.characterReplacement("AABBB", 1), 4)
        self.assertEqual(LongestRepeatingCharacterReplacement.characterReplacement("ABAA", 0), 2)


if __name__ == "__main__":
    unittest.main()
