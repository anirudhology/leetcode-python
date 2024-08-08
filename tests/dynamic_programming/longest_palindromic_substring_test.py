import unittest

from problems.dynamic_programming.longest_palindromic_substring import LongestPalindromicSubstring


class LongestPalindromicSubstringTest(unittest.TestCase):

    def setUp(self):
        self.longest_palindromic_substring = LongestPalindromicSubstring()

    def test_longest_palindrome(self):
        # Test case for null string
        # noinspection PyTypeChecker
        self.assertEqual(self.longest_palindromic_substring.longestPalindrome(None), None)

        # Test case for empty string
        self.assertEqual(self.longest_palindromic_substring.longestPalindrome(""), "")

        # Test case for single character string
        self.assertEqual(self.longest_palindromic_substring.longestPalindrome("a"), "a")

        # Test case for string with all same characters
        self.assertEqual(self.longest_palindromic_substring.longestPalindrome("aaaa"), "aaaa")

        # Test case for string with a palindromic substring in the middle
        self.assertEqual(self.longest_palindromic_substring.longestPalindrome("babad"), "aba")

        # Test case for string with a palindromic substring at the end
        self.assertEqual(self.longest_palindromic_substring.longestPalindrome("cbbd"), "bb")

        # Test case for string with no palindromic substring longer than one character
        self.assertEqual(self.longest_palindromic_substring.longestPalindrome("abc"), "c")

        # Test case for string with the entire string as a palindrome
        self.assertEqual(self.longest_palindromic_substring.longestPalindrome("racecar"), "racecar")


if __name__ == '__main__':
    unittest.main()
