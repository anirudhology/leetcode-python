import unittest

from problems.bfs.rotting_oranges import RottingOranges


class TestRottingOranges(unittest.TestCase):

    def test_orangesRotting_empty_grid(self):
        rotten_oranges = RottingOranges()
        grid = []
        self.assertEqual(rotten_oranges.orangesRotting(grid), 0)

    def test_orangesRotting_no_fresh_oranges(self):
        rotten_oranges = RottingOranges()
        grid = [
            [2, 2, 0],
            [2, 0, 2],
            [0, 2, 2]
        ]
        self.assertEqual(rotten_oranges.orangesRotting(grid), 0)

    def test_orangesRotting_all_fresh_oranges(self):
        rotten_oranges = RottingOranges()
        grid = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
        self.assertEqual(rotten_oranges.orangesRotting(grid), -1)

    def test_orangesRotting_rotten_spread(self):
        rotten_oranges = RottingOranges()
        grid = [
            [2, 1, 1],
            [1, 1, 0],
            [0, 1, 1]
        ]
        self.assertEqual(rotten_oranges.orangesRotting(grid), 4)

    def test_orangesRotting_rotten_spread_with_unreachable(self):
        rotten_oranges = RottingOranges()
        grid = [
            [2, 1, 1],
            [0, 1, 0],
            [1, 0, 1]
        ]
        self.assertEqual(rotten_oranges.orangesRotting(grid), -1)


if __name__ == '__main__':
    unittest.main()
