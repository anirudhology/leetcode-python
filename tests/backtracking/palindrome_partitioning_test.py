import unittest

from problems.backtracking.palindrome_partitioning import PalindromePartitioning


class PalindromePartitioningTes(unittest.TestCase):

    def setUp(self):
        self.palindrome_partitioning = PalindromePartitioning()

    def test_partition(self):
        self.assertEqual(self.palindrome_partitioning.partition("aab"), [["a", "a", "b"], ["aa", "b"]])
        self.assertEqual(self.palindrome_partitioning.partition("a"), [["a"]])
        self.assertEqual(self.palindrome_partitioning.partition(""), [])
        self.assertEqual(self.palindrome_partitioning.partition("aba"), [["a", "b", "a"], ["aba"]])


if __name__ == '__main__':
    unittest.main()
