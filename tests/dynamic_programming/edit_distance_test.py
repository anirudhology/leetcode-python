import unittest

from problems.dynamic_programming.edit_distance import EditDistance


class TestEditDistance(unittest.TestCase):

    def setUp(self):
        self.edit_distance = EditDistance()

    def test_min_distance_empty_strings(self):
        self.assertEqual(self.edit_distance.minDistance("", ""), 0)

    def test_min_distance_one_empty_string(self):
        self.assertEqual(self.edit_distance.minDistance("hello", ""), 5)
        self.assertEqual(self.edit_distance.minDistance("", "java"), 4)

    def test_min_distance_same_strings(self):
        self.assertEqual(self.edit_distance.minDistance("same", "same"), 0)

    def test_min_distance_different_strings(self):
        self.assertEqual(self.edit_distance.minDistance("horse", "ros"), 3)
        self.assertEqual(self.edit_distance.minDistance("intention", "execution"), 5)
        self.assertEqual(self.edit_distance.minDistance("flaw", "lawn"), 2)


if __name__ == "__main__":
    unittest.main()
