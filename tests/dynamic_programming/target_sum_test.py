import unittest

from problems.dynamic_programming.target_sum import TargetSum


class TestTargetSum(unittest.TestCase):

    def test_find_target_sum_ways_simple_case(self):
        ts = TargetSum()
        self.assertEqual(ts.findTargetSumWays([1, 1, 1, 1, 1], 3), 5)

    def test_find_target_sum_ways_empty_array(self):
        ts = TargetSum()
        self.assertEqual(ts.findTargetSumWays([], 3), 0)

    def test_find_target_sum_ways_null_array(self):
        ts = TargetSum()
        self.assertEqual(ts.findTargetSumWays(None, 3), 0)

    def test_find_target_sum_ways_no_solution(self):
        ts = TargetSum()
        self.assertEqual(ts.findTargetSumWays([1, 2, 3], 7), 0)

    def test_find_target_sum_ways_single_element_target_met(self):
        ts = TargetSum()
        self.assertEqual(ts.findTargetSumWays([5], 5), 1)

    def test_find_target_sum_ways_single_element_target_not_met(self):
        ts = TargetSum()
        self.assertEqual(ts.findTargetSumWays([5], 3), 0)


if __name__ == '__main__':
    unittest.main()
