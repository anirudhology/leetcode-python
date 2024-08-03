import unittest

from problems.backtracking.subsets_ii import SubsetsII


class SubsetsIITest(unittest.TestCase):
    def setUp(self):
        self.subsetsII = SubsetsII()

    def test_subsetsWithDup(self):
        nums1 = [1, 2, 2]
        expected1 = [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
        self.assertCountEqual(self.subsetsII.subsetsWithDup(nums1), expected1)

        nums2 = [4, 4, 4, 1, 4]
        expected2 = [[], [1], [1, 4], [1, 4, 4], [1, 4, 4, 4], [1, 4, 4, 4, 4], [4], [4, 4], [4, 4, 4], [4, 4, 4, 4]]
        self.assertCountEqual(self.subsetsII.subsetsWithDup(nums2), expected2)

        nums3 = []
        expected3 = []
        self.assertCountEqual(self.subsetsII.subsetsWithDup(nums3), expected3)

        nums4 = None
        expected4 = []
        # noinspection PyTypeChecker
        self.assertCountEqual(self.subsetsII.subsetsWithDup(nums4), expected4)


if __name__ == "__main__":
    unittest.main()
