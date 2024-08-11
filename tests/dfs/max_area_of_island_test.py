import unittest

from problems.dfs.max_area_of_island import MaxAreaOfIsland


class MaxAreaOfIslandTest(unittest.TestCase):

    def setUp(self):
        self.max_area_of_island = MaxAreaOfIsland()

    def test_empty_grid(self):
        self.assertEqual(self.max_area_of_island.maxAreaOfIsland([]), 0)

    def test_null_grid(self):
        # noinspection PyTypeChecker
        self.assertEqual(self.max_area_of_island.maxAreaOfIsland(None), 0)

    def test_single_island(self):
        grid = [
            [1, 1, 0, 0],
            [1, 1, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(self.max_area_of_island.maxAreaOfIsland(grid), 4)

    def test_multiple_islands(self):
        grid = [
            [1, 0, 0, 1, 1],
            [0, 0, 1, 1, 0],
            [0, 1, 0, 0, 0],
            [1, 1, 0, 1, 1]
        ]
        self.assertEqual(self.max_area_of_island.maxAreaOfIsland(grid), 4)

    def test_no_islands(self):
        grid = [
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(self.max_area_of_island.maxAreaOfIsland(grid), 0)

    def test_mixed_grid(self):
        grid = [
            [1, 0, 1, 0],
            [0, 1, 0, 1],
            [1, 0, 1, 0]
        ]
        self.assertEqual(self.max_area_of_island.maxAreaOfIsland(grid), 1)


if __name__ == '__main__':
    unittest.main()
