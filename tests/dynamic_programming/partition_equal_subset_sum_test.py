import unittest

from problems.dynamic_programming.partition_equal_subset_sum import PartitionEqualSubsetSum


class TestPartitionEqualSubsetSum(unittest.TestCase):

    def setUp(self):
        self.partition_equal_subset_sum = PartitionEqualSubsetSum()

    def test_can_partition(self):
        self.assertTrue(self.partition_equal_subset_sum.canPartition([1, 5, 11, 5]))
        self.assertFalse(self.partition_equal_subset_sum.canPartition([1, 2, 3, 5]))
        self.assertFalse(self.partition_equal_subset_sum.canPartition([1, 2, 5]))
        self.assertTrue(self.partition_equal_subset_sum.canPartition([1, 2, 3, 4]))
        self.assertTrue(
            self.partition_equal_subset_sum.canPartition([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
        self.assertFalse(self.partition_equal_subset_sum.canPartition([]))
        # noinspection PyTypeChecker
        self.assertFalse(self.partition_equal_subset_sum.canPartition(None))
        self.assertFalse(self.partition_equal_subset_sum.canPartition([3]))


if __name__ == '__main__':
    unittest.main()
