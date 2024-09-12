import unittest

from problems.array.merge_sorted_array import MergeSortedArray


class TestMergeSortedArray(unittest.TestCase):

    def setUp(self):
        self.merge_sorted_array = MergeSortedArray()

    def test_both_non_empty(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        nums2 = [2, 5, 6]
        m = 3
        n = 3
        self.assertEqual(self.merge_sorted_array.merge(nums1, m, nums2, n), [1, 2, 2, 3, 5, 6])

    def test_empty_nums2(self):
        nums1 = [1, 2, 3]
        nums2 = []
        m = 3
        n = 0
        self.assertEqual(self.merge_sorted_array.merge(nums1, m, nums2, n), [1, 2, 3])

    def test_empty_nums1(self):
        nums1 = [0, 0, 0]
        nums2 = [1, 2, 3]
        m = 0
        n = 3
        self.assertEqual(self.merge_sorted_array.merge(nums1, m, nums2, n), [1, 2, 3])

    def test_empty_both(self):
        nums1 = []
        nums2 = []
        m = 0
        n = 0
        self.assertEqual(self.merge_sorted_array.merge(nums1, m, nums2, n), [])

    def test_single_element_nums1(self):
        nums1 = [1]
        nums2 = []
        m = 1
        n = 0
        self.assertEqual(self.merge_sorted_array.merge(nums1, m, nums2, n), [1])

    def test_single_element_nums2(self):
        nums1 = [0]
        nums2 = [1]
        m = 0
        n = 1
        self.assertEqual(self.merge_sorted_array.merge(nums1, m, nums2, n), [1])


if __name__ == '__main__':
    unittest.main()
