import unittest

from problems.bfs.pacific_atlantic_water_flow import PacificAtlanticWaterFlow


class PacificAtlanticWaterFlowTest(unittest.TestCase):

    def test_pacificAtlantic_empty_grid(self):
        pacific_atlantic_water_flow = PacificAtlanticWaterFlow()
        heights = []
        result = pacific_atlantic_water_flow.pacificAtlantic(heights)
        self.assertEqual(result, [])

    def test_pacificAtlantic_single_cell_grid(self):
        pacific_atlantic_water_flow = PacificAtlanticWaterFlow()
        heights = [[1]]
        result = pacific_atlantic_water_flow.pacificAtlantic(heights)
        self.assertEqual(result, [[0, 0]])

    def test_pacificAtlantic_flat_grid(self):
        pacific_atlantic_water_flow = PacificAtlanticWaterFlow()
        heights = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
        result = pacific_atlantic_water_flow.pacificAtlantic(heights)
        self.assertEqual(len(result), 9)  # All cells should be reachable by both oceans

    def test_pacificAtlantic_mountain_grid(self):
        pacific_atlantic_water_flow = PacificAtlanticWaterFlow()
        heights = [
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4]
        ]
        result = pacific_atlantic_water_flow.pacificAtlantic(heights)
        self.assertEqual(len(result), 7)  # Specific cells should be reachable by both oceans


if __name__ == '__main__':
    unittest.main()
