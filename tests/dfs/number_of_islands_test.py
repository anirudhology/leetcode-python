import unittest

from problems.dfs.number_of_islands import NumberOfIslands


class NumIslandsTest(unittest.TestCase):

    def setUp(self):
        self.number_of_islands = NumberOfIslands()

    def test_empty_grid(self):
        self.assertEqual(self.number_of_islands.numIslands([]), 0)

    def test_null_grid(self):
        # noinspection PyTypeChecker
        self.assertEqual(self.number_of_islands.numIslands(None), 0)

    def test_single_island(self):
        grid = [
            ['1', '1', '0', '0'],
            ['1', '1', '0', '0'],
            ['0', '0', '0', '0'],
            ['0', '0', '0', '0']
        ]
        self.assertEqual(self.number_of_islands.numIslands(grid), 1)

    def test_multiple_islands(self):
        grid = [
            ['1', '1', '0', '0', '1'],
            ['1', '0', '0', '1', '1'],
            ['0', '0', '1', '0', '0'],
            ['1', '0', '0', '1', '1']
        ]
        self.assertEqual(self.number_of_islands.numIslands(grid), 5)

    def test_no_islands(self):
        grid = [
            ['0', '0', '0', '0'],
            ['0', '0', '0', '0']
        ]
        self.assertEqual(self.number_of_islands.numIslands(grid), 0)

    def test_mixed_grid(self):
        grid = [
            ['1', '0', '1', '0'],
            ['0', '1', '0', '1'],
            ['1', '0', '1', '0']
        ]
        self.assertEqual(self.number_of_islands.numIslands(grid), 6)


if __name__ == '__main__':
    unittest.main()
