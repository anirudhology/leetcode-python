import unittest

from problems.backtracking.permutations import Permutations


class TestPermutations(unittest.TestCase):
    def setUp(self):
        self.permutations = Permutations()

    def test_permute(self):
        nums1 = [1, 2, 3]
        expected1 = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        self.assertCountEqual(self.permutations.permute(nums1), expected1)

        nums2 = [0, 1]
        expected2 = [[0, 1], [1, 0]]
        self.assertCountEqual(self.permutations.permute(nums2), expected2)

        nums3 = [1]
        expected3 = [[1]]
        self.assertCountEqual(self.permutations.permute(nums3), expected3)

        nums4 = []
        expected4 = []
        self.assertCountEqual(self.permutations.permute(nums4), expected4)

        expected5 = []
        # noinspection PyTypeChecker
        self.assertCountEqual(self.permutations.permute(None), expected5)


if __name__ == "__main__":
    unittest.main()
