import unittest

from problems.dynamic_programming.unique_paths import UniquePaths


class TestUniquePaths(unittest.TestCase):

    def test_unique_paths_3x7(self):
        unique_paths = UniquePaths()
        self.assertEqual(unique_paths.uniquePaths(3, 7), 28)

    def test_unique_paths_1x1(self):
        unique_paths = UniquePaths()
        self.assertEqual(unique_paths.uniquePaths(1, 1), 1)

    def test_unique_paths_2x2(self):
        unique_paths = UniquePaths()
        self.assertEqual(unique_paths.uniquePaths(2, 2), 2)

    def test_unique_paths_3x3(self):
        unique_paths = UniquePaths()
        self.assertEqual(unique_paths.uniquePaths(3, 3), 6)

    def test_unique_paths_7x3(self):
        unique_paths = UniquePaths()
        self.assertEqual(unique_paths.uniquePaths(7, 3), 28)


if __name__ == '__main__':
    unittest.main()
