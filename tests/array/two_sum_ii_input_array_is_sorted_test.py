import unittest

from problems.array.two_sum_ii_input_array_is_sorted import TwoSumIIInputArrayIsSorted


class TwoSumIIInputArrayIsSortedTest(unittest.TestCase):

    def test_two_sum(self):
        two_sum_ii_input_array_is_sorted = TwoSumIIInputArrayIsSorted()

        self.assertEqual(two_sum_ii_input_array_is_sorted.twoSum([2, 7, 11, 15], 9), [1, 2])
        self.assertEqual(two_sum_ii_input_array_is_sorted.twoSum([2, 3, 4], 6), [1, 3])
        self.assertEqual(two_sum_ii_input_array_is_sorted.twoSum([-1, 0], -1), [1, 2])
        self.assertEqual(two_sum_ii_input_array_is_sorted.twoSum([1, 2, 3, 4, 4], 7), [3, 5])
        self.assertEqual(two_sum_ii_input_array_is_sorted.twoSum([1, 2, 3, 4, 6], 10), [4, 5])

    def test_edge_cases(self):
        solution = TwoSumIIInputArrayIsSorted()

        self.assertIsNone(solution.twoSum([], 9))
        # noinspection PyTypeChecker
        self.assertIsNone(solution.twoSum(None, 9))
        self.assertIsNone(solution.twoSum([1], 1))
        self.assertEqual(solution.twoSum([1, 2], 3), [1, 2])


if __name__ == "__main__":
    unittest.main()
