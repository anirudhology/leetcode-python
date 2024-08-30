import unittest

from problems.greedy.partition_labels import PartitionLabels


class TestPartitionLabels(unittest.TestCase):

    def setUp(self):
        self.partition_labels = PartitionLabels()

    def test_partition_labels(self):
        # Test null input
        self.assertEqual(self.partition_labels.partitionLabels(None), [])

        # Test empty string
        self.assertEqual(self.partition_labels.partitionLabels(""), [])

        # Test string with all unique characters
        self.assertEqual(self.partition_labels.partitionLabels("abcd"), [1, 1, 1, 1])

        # Test string with all same characters
        self.assertEqual(self.partition_labels.partitionLabels("aaaa"), [4])

        # Test string with multiple partitions
        self.assertEqual(self.partition_labels.partitionLabels("ababcbacadefegdehijhklij"), [9, 7, 8])

        # Test string with overlapping partitions
        self.assertEqual(self.partition_labels.partitionLabels("eababcbaca"), [1, 9])

    def test_edge_cases(self):
        # Test single character string
        self.assertEqual(self.partition_labels.partitionLabels("a"), [1])

        # Test string with repeating characters
        self.assertEqual(self.partition_labels.partitionLabels("abacaba"), [7])


if __name__ == '__main__':
    unittest.main()
