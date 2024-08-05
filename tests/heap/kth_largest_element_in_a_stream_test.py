import unittest

from problems.heap.kth_largest_element_in_a_stream import KthLargest


class KthLargestTest(unittest.TestCase):
    def test_kth_largest(self):
        nums = [4, 5, 8, 2]
        kth_largest = KthLargest(3, nums)

        self.assertEqual(kth_largest.add(3), 4)  # returns 4
        self.assertEqual(kth_largest.add(5), 5)  # returns 5
        self.assertEqual(kth_largest.add(10), 5)  # returns 5
        self.assertEqual(kth_largest.add(9), 8)  # returns 8
        self.assertEqual(kth_largest.add(4), 8)  # returns 8


if __name__ == '__main__':
    unittest.main()
