import unittest

from problems.dynamic_programming.regular_expression_matching import RegularExpressionMatching


class TestRegularExpressionMatching(unittest.TestCase):

    def setUp(self):
        self.regular_expression_matching = RegularExpressionMatching()

    def test_is_match(self):
        self.assertTrue(self.regular_expression_matching.isMatch("aa", "a*"))
        self.assertTrue(self.regular_expression_matching.isMatch("ab", ".*"))
        self.assertFalse(self.regular_expression_matching.isMatch("mississippi", "mis*is*p*."))
        self.assertTrue(self.regular_expression_matching.isMatch("aab", "c*a*b"))
        self.assertFalse(self.regular_expression_matching.isMatch("ab", "a"))
        self.assertTrue(self.regular_expression_matching.isMatch("", ".*"))
        self.assertTrue(self.regular_expression_matching.isMatch("", "a*"))
        self.assertFalse(self.regular_expression_matching.isMatch("abcd", "d*"))
        self.assertTrue(self.regular_expression_matching.isMatch("aaa", "a*a"))
        self.assertFalse(self.regular_expression_matching.isMatch("aaa", "ab*a"))


if __name__ == "__main__":
    unittest.main()
