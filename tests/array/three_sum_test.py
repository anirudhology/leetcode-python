import unittest

from problems.array.three_sum import ThreeSum


class ThreeSumTest(unittest.TestCase):
    def test_three_sum(self):
        ts = ThreeSum()

        # Test case 1: General case with multiple triplets
        nums = [-1, 0, 1, 2, -1, -4]
        expected = [[-1, -1, 2], [-1, 0, 1]]
        result = ts.threeSum(nums)
        self.assertEqual(result, expected)

        # Test case 2: No triplets sum to zero
        nums = [1, 2, -2, -1]
        expected = []
        result = ts.threeSum(nums)
        self.assertEqual(result, expected)

        # Test case 3: Triplets with zeros
        nums = [0, 0, 0, 0]
        expected = [[0, 0, 0]]
        result = ts.threeSum(nums)
        self.assertEqual(result, expected)

        # Test case 4: Single triplet case
        nums = [-2, 0, 2]
        expected = [[-2, 0, 2]]
        result = ts.threeSum(nums)
        self.assertEqual(result, expected)

        # Test case 5: Less than three elements
        nums = [1, 2]
        expected = []
        result = ts.threeSum(nums)
        self.assertEqual(result, expected)

        # Test case 6: List with negative numbers
        nums = [-4, -2, -1]
        expected = []
        result = ts.threeSum(nums)
        self.assertEqual(result, expected)

        # Test case 7: List with duplicate numbers
        nums = [-1, -1, 2]
        expected = [[-1, -1, 2]]
        result = ts.threeSum(nums)
        self.assertEqual(result, expected)

        # Test case 8: Empty list
        nums = []
        expected = []
        result = ts.threeSum(nums)
        self.assertEqual(result, expected)

        # Test case 9: None input
        nums = None
        expected = []
        # noinspection PyTypeChecker
        result = ts.threeSum(nums)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
