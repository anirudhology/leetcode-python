import unittest

from problems.array.trapping_rain_water import TrappingRainWater


class TestTrappingRainWater(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(TrappingRainWater.trap([]), 0)

    def test_single_element(self):
        self.assertEqual(TrappingRainWater.trap([1]), 0)

    def test_two_elements(self):
        self.assertEqual(TrappingRainWater.trap([1, 2]), 0)

    def test_no_trapping(self):
        self.assertEqual(TrappingRainWater.trap([1, 2, 3, 4, 5]), 0)

    def test_typical_case(self):
        self.assertEqual(TrappingRainWater.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)

    def test_all_same_height(self):
        self.assertEqual(TrappingRainWater.trap([3, 3, 3, 3]), 0)

    def test_decreasing_heights(self):
        self.assertEqual(TrappingRainWater.trap([5, 4, 3, 2, 1]), 0)

    def test_increasing_heights(self):
        self.assertEqual(TrappingRainWater.trap([1, 2, 3, 4, 5]), 0)

    def test_v_shape(self):
        self.assertEqual(TrappingRainWater.trap([2, 0, 2]), 2)

    def test_complex_case(self):
        self.assertEqual(TrappingRainWater.trap([4, 2, 0, 3, 2, 5]), 9)


if __name__ == "__main__":
    unittest.main()
