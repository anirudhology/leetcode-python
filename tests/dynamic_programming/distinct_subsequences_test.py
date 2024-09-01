import unittest

from problems.dynamic_programming.distinct_subsequences import DistinctSubsequences


class TestDistinctSubsequences(unittest.TestCase):

    def setUp(self):
        self.distinct_subsequences = DistinctSubsequences()

    def test_num_distinct_empty_strings(self):
        self.assertEqual(self.distinct_subsequences.numDistinct("", ""), 1)

    def test_num_distinct_empty_target(self):
        self.assertEqual(self.distinct_subsequences.numDistinct("abc", ""), 1)

    def test_num_distinct_empty_source(self):
        self.assertEqual(self.distinct_subsequences.numDistinct("", "abc"), 0)

    def test_num_distinct_same_strings(self):
        self.assertEqual(self.distinct_subsequences.numDistinct("abc", "abc"), 1)

    def test_num_distinct_general_cases(self):
        self.assertEqual(self.distinct_subsequences.numDistinct("babgbag", "bag"), 5)
        self.assertEqual(self.distinct_subsequences.numDistinct("rabbbit", "rabbit"), 3)
        self.assertEqual(self.distinct_subsequences.numDistinct("abc", "def"), 0)


if __name__ == "__main__":
    unittest.main()
