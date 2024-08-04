import unittest

from problems.backtracking.combination_sum_ii import CombinationSumII


class CombinationSumIITest(unittest.TestCase):
    def test_combination_sum2(self):
        solution = CombinationSumII()

        # Test case 1
        candidates1 = [10, 1, 2, 7, 6, 1, 5]
        target1 = 8
        expected1 = [
            [1, 1, 6],
            [1, 2, 5],
            [1, 7],
            [2, 6]
        ]
        self.assertEqual(solution.combinationSum2(candidates1, target1), expected1)

        # Test case 2
        candidates2 = [2, 5, 2, 1, 2]
        target2 = 5
        expected2 = [
            [1, 2, 2],
            [5]
        ]
        self.assertEqual(solution.combinationSum2(candidates2, target2), expected2)

        # Test case 3: Edge case, empty array
        candidates3 = []
        target3 = 3
        expected3 = []
        self.assertEqual(solution.combinationSum2(candidates3, target3), expected3)

        # Test case 4: Edge case, target is zero
        candidates4 = [1, 2, 3]
        target4 = 0
        expected4 = [[]]
        self.assertEqual(solution.combinationSum2(candidates4, target4), expected4)

        # Test case 5: Edge case, candidates are null
        candidates5 = None
        target5 = 7
        expected5 = []
        # noinspection PyTypeChecker
        self.assertEqual(solution.combinationSum2(candidates5, target5), expected5)


if __name__ == '__main__':
    unittest.main()
