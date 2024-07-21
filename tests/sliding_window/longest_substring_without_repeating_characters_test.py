import unittest

from problems.sliding_window.longest_substring_without_repeating_characters import \
    LongestSubstringWithoutRepeatingCharacters


class TestLongestSubstringWithoutRepeatingCharacters(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(LongestSubstringWithoutRepeatingCharacters.lengthOfLongestSubstring(""), 0)

    def test_none_string(self):
        # noinspection PyTypeChecker
        self.assertEqual(LongestSubstringWithoutRepeatingCharacters.lengthOfLongestSubstring(None), 0)

    def test_single_character(self):
        self.assertEqual(LongestSubstringWithoutRepeatingCharacters.lengthOfLongestSubstring("a"), 1)

    def test_all_unique_characters(self):
        self.assertEqual(LongestSubstringWithoutRepeatingCharacters.lengthOfLongestSubstring("abcde"), 5)

    def test_all_same_characters(self):
        self.assertEqual(LongestSubstringWithoutRepeatingCharacters.lengthOfLongestSubstring("aaaaa"), 1)

    def test_mixed_characters(self):
        self.assertEqual(LongestSubstringWithoutRepeatingCharacters.lengthOfLongestSubstring("abcabcbb"), 3)

    def test_string_with_spaces(self):
        self.assertEqual(LongestSubstringWithoutRepeatingCharacters.lengthOfLongestSubstring("a b c a b c b b"), 3)

    def test_string_with_numbers(self):
        self.assertEqual(LongestSubstringWithoutRepeatingCharacters.lengthOfLongestSubstring("1234567890"), 10)

    def test_complex_string(self):
        self.assertEqual(LongestSubstringWithoutRepeatingCharacters.lengthOfLongestSubstring("pwwkewabcdef"), 7)


if __name__ == '__main__':
    unittest.main()
