import unittest

from problems.array.top_k_frequent_elements import TopKFrequentElements


class TopKFrequentElementsTest(unittest.TestCase):

    def setUp(self):
        self.top_k_frequent_elements = TopKFrequentElements()

    def test_single_element(self):
        self.assertEqual(self.top_k_frequent_elements.topKFrequent([1], 1), [1])

    def test_multiple_elements(self):
        self.assertEqual(self.top_k_frequent_elements.topKFrequent([1, 1, 1, 2, 2, 3], 2), [1, 2])

    def test_negative_elements(self):
        self.assertEqual(self.top_k_frequent_elements.topKFrequent([-1, -1, -1, 1, 1, 2, 2, 2], 2), [-1, 2])

    def test_empty_list(self):
        self.assertEqual(self.top_k_frequent_elements.topKFrequent([], 1), [])

    def test_none_list(self):
        # noinspection PyTypeChecker
        self.assertEqual(self.top_k_frequent_elements.topKFrequent(None, 1), [])

    def test_k_less_than_zero(self):
        self.assertEqual(self.top_k_frequent_elements.topKFrequent([2, 3, 4], -1), [])

    def test_k_zero(self):
        self.assertEqual(self.top_k_frequent_elements.topKFrequent([1, 1, 2, 2, 3, 3], 0), [])


if __name__ == '__main__':
    unittest.main()
