import unittest

from problems.array.longest_consecutive_sequence import LongestConsecutiveSequence


class TestLongestConsecutiveSequence(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(LongestConsecutiveSequence.longestConsecutive([]), 0)

    def test_single_element(self):
        self.assertEqual(LongestConsecutiveSequence.longestConsecutive([1]), 1)

    def test_no_consecutive_sequence(self):
        self.assertEqual(LongestConsecutiveSequence.longestConsecutive([10, 5, 100]), 1)

    def test_consecutive_sequence(self):
        self.assertEqual(LongestConsecutiveSequence.longestConsecutive([100, 4, 200, 1, 3, 2]), 4)

    def test_mixed_numbers(self):
        self.assertEqual(LongestConsecutiveSequence.longestConsecutive([100, 4, 200, 1, 3, 2, 2, 2]), 4)

    def test_duplicates(self):
        self.assertEqual(LongestConsecutiveSequence.longestConsecutive([1, 2, 0, 1]), 3)

    def test_large_range(self):
        self.assertEqual(LongestConsecutiveSequence.longestConsecutive([10, 1, 3, 5, 2, 4, 11]), 5)

    def test_null_array(self):
        # noinspection PyTypeChecker
        self.assertEqual(LongestConsecutiveSequence.longestConsecutive(None), 0)


if __name__ == '__main__':
    unittest.main()
