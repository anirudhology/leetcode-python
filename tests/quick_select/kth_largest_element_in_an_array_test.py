import unittest

from problems.quick_select.kth_largest_element_in_an_array import KthLargestElementInAnArray


class TestKthLargestElementInAnArray(unittest.TestCase):

    def test_find_kth_largest(self):
        kth_largest_element_in_an_array = KthLargestElementInAnArray()

        self.assertEqual(kth_largest_element_in_an_array.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4)
        self.assertEqual(kth_largest_element_in_an_array.findKthLargest([1], 1), 1)
        self.assertEqual(kth_largest_element_in_an_array.findKthLargest([1, 2], 1), 2)
        self.assertEqual(kth_largest_element_in_an_array.findKthLargest([-1, -1], 2), -1)


if __name__ == '__main__':
    unittest.main()
