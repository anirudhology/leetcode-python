import unittest

from problems.dynamic_programming.palindromic_substrings import PalindromicSubstrings


class PalindromicSubstringsTest(unittest.TestCase):

    def setUp(self):
        self.palindromic_substrings = PalindromicSubstrings()

    def test_count_substrings(self):
        # Test case for null string
        # noinspection PyTypeChecker
        self.assertEqual(self.palindromic_substrings.countSubstrings(None), 0)

        # Test case for empty string
        self.assertEqual(self.palindromic_substrings.countSubstrings(""), 0)

        # Test case for single character string
        self.assertEqual(self.palindromic_substrings.countSubstrings("a"), 1)

        # Test case for string with all same characters
        self.assertEqual(self.palindromic_substrings.countSubstrings("aaaa"), 10)

        # Test case for string with mixed characters
        self.assertEqual(self.palindromic_substrings.countSubstrings("abc"), 3)

        # Test case for string with palindromic substrings
        self.assertEqual(self.palindromic_substrings.countSubstrings("aaa"), 6)


if __name__ == '__main__':
    unittest.main()
