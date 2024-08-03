import unittest

from problems.backtracking.combination_sum import CombinationSum


class CombinationSumTest(unittest.TestCase):
    def setUp(self):
        self.combination_sum = CombinationSum()

    def test_combination_sum(self):
        candidates1 = [2, 3, 6, 7]
        target1 = 7
        expected1 = [[2, 2, 3], [7]]
        self.assertCountEqual(self.combination_sum.combinationSum(candidates1, target1), expected1)

        candidates2 = [2, 3, 5]
        target2 = 8
        expected2 = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
        self.assertCountEqual(self.combination_sum.combinationSum(candidates2, target2), expected2)

        candidates3 = [2]
        target3 = 1
        expected3 = []
        self.assertCountEqual(self.combination_sum.combinationSum(candidates3, target3), expected3)

        candidates4 = []
        target4 = 7
        expected4 = []
        self.assertCountEqual(self.combination_sum.combinationSum(candidates4, target4), expected4)


if __name__ == "__main__":
    unittest.main()
