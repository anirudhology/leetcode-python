import unittest

from problems.dynamic_programming.longest_common_subsequence import LongestCommonSubsequence


class TestLongestCommonSubsequence(unittest.TestCase):

    def test_lcs_simple_case(self):
        lcs = LongestCommonSubsequence()
        self.assertEqual(lcs.longestCommonSubsequence("abcde", "ace"), 3)

    def test_lcs_no_common_subsequence(self):
        lcs = LongestCommonSubsequence()
        self.assertEqual(lcs.longestCommonSubsequence("abc", "def"), 0)

    def test_lcs_empty_strings(self):
        lcs = LongestCommonSubsequence()
        self.assertEqual(lcs.longestCommonSubsequence("", ""), 0)

    def test_lcs_one_empty_string(self):
        lcs = LongestCommonSubsequence()
        self.assertEqual(lcs.longestCommonSubsequence("abcde", ""), 0)

    def test_lcs_full_match(self):
        lcs = LongestCommonSubsequence()
        self.assertEqual(lcs.longestCommonSubsequence("abcde", "abcde"), 5)

    def test_lcs_reversed_strings(self):
        lcs = LongestCommonSubsequence()
        self.assertEqual(lcs.longestCommonSubsequence("abcde", "edcba"), 1)


if __name__ == '__main__':
    unittest.main()
