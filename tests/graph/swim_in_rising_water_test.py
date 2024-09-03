import unittest

from problems.graph.swim_in_rising_water import SwimInRisingWater


class TestSwimInRisingWater(unittest.TestCase):
    def test_swim_in_water(self):
        swim_in_rising_water = SwimInRisingWater()

        # Test case 1
        grid1 = [[0, 2], [1, 3]]
        expected1 = 3
        self.assertEqual(swim_in_rising_water.swimInWater(grid1), expected1)

        # Test case 2
        grid2 = [
            [0, 1, 2, 3, 4],
            [24, 23, 22, 21, 5],
            [12, 13, 14, 15, 16],
            [11, 17, 18, 19, 20],
            [10, 9, 8, 7, 6]
        ]
        expected2 = 16
        self.assertEqual(swim_in_rising_water.swimInWater(grid2), expected2)

        # Edge case: single cell
        grid3 = [[0]]
        expected3 = 0
        self.assertEqual(swim_in_rising_water.swimInWater(grid3), expected3)

        # Edge case: larger grid
        grid4 = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8]
        ]
        expected4 = 8
        self.assertEqual(swim_in_rising_water.swimInWater(grid4), expected4)


if __name__ == "__main__":
    unittest.main()
