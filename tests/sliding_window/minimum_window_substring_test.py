import unittest

from problems.sliding_window.minimum_window_substring import MinimumWindowSubstring


class MinimumWindowSubstringTest(unittest.TestCase):

    def setUp(self):
        self.solution = MinimumWindowSubstring()

    def test_basic_functionality(self):
        self.assertEqual(self.solution.minWindow("ADOBECODEBANC", "ABC"), "BANC")

    def test_t_longer_than_s(self):
        self.assertEqual(self.solution.minWindow("A", "AA"), "")

    def test_t_and_s_are_same(self):
        self.assertEqual(self.solution.minWindow("A", "A"), "A")

    def test_t_is_substring_of_s(self):
        self.assertEqual(self.solution.minWindow("BANC", "ABC"), "BANC")

    def test_no_possible_window(self):
        self.assertEqual(self.solution.minWindow("HELLOWORLD", "XYZ"), "")

    def test_s_is_empty(self):
        self.assertEqual(self.solution.minWindow("", "HELLO"), "")

    def test_both_s_and_t_are_empty(self):
        self.assertEqual(self.solution.minWindow("", ""), "")

    def test_repeated_characters_in_t(self):
        self.assertEqual(self.solution.minWindow("AAABBB", "AA"), "AA")

    def test_repeated_characters_in_s(self):
        self.assertEqual(self.solution.minWindow("AABCAD", "AABC"), "AABC")

    def test_s_and_t_have_no_common_characters(self):
        self.assertEqual(self.solution.minWindow("ABC", "DEF"), "")

    def test_t_contains_all_unique_characters(self):
        self.assertEqual(self.solution.minWindow("ADOBECODEBANC", "ABCDE"), "ADOBEC")


if __name__ == '__main__':
    unittest.main()
