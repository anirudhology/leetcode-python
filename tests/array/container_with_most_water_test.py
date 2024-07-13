import unittest

from problems.array.container_with_most_water import ContainerWithMostWater


class ContainerWithMostWaterTest(unittest.TestCase):

    def setUp(self):
        self.solution = ContainerWithMostWater()

    def test_max_area_null_array(self):
        # noinspection PyTypeChecker
        self.assertEqual(self.solution.maxArea(None), 0)

    def test_max_area_empty_array(self):
        self.assertEqual(self.solution.maxArea([]), 0)

    def test_max_area_single_element(self):
        self.assertEqual(self.solution.maxArea([1]), 0)

    def test_max_area_two_elements(self):
        self.assertEqual(self.solution.maxArea([1, 1]), 1)

    def test_max_area_typical_case(self):
        self.assertEqual(self.solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)

    def test_max_area_decreasing_heights(self):
        self.assertEqual(self.solution.maxArea([9, 8, 7, 6, 5, 4, 3, 2, 1]), 20)

    def test_max_area_increasing_heights(self):
        self.assertEqual(self.solution.maxArea([1, 2, 3, 4, 5, 6, 7, 8, 9]), 20)

    def test_max_area_same_heights(self):
        self.assertEqual(self.solution.maxArea([4, 4, 4, 4, 4]), 16)

    def test_max_area_single_high_element(self):
        self.assertEqual(self.solution.maxArea([1, 2, 4, 3]), 4)


if __name__ == '__main__':
    unittest.main()
