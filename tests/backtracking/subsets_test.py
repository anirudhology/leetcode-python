import unittest

from problems.backtracking.subsets import Subsets


class SubsetsTest(unittest.TestCase):
    def setUp(self):
        self.subsets = Subsets()

    def test_subsets(self):
        nums1 = [1, 2, 3]
        expected1 = [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
        self.assertCountEqual(self.subsets.subsets(nums1), expected1)

        nums2 = [0]
        expected2 = [[], [0]]
        self.assertCountEqual(self.subsets.subsets(nums2), expected2)

        nums3 = []
        expected3 = []
        self.assertCountEqual(self.subsets.subsets(nums3), expected3)


if __name__ == "__main__":
    unittest.main()
