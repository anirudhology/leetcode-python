import unittest

from problems.heap.find_median_from_data_stream import MedianFinder


class TestMedianFinder(unittest.TestCase):

    def test_add_num_and_find_median(self):
        finder = MedianFinder()

        finder.addNum(1)
        self.assertEqual(finder.findMedian(), 1.0)

        finder.addNum(2)
        self.assertEqual(finder.findMedian(), 1.5)

        finder.addNum(3)
        self.assertEqual(finder.findMedian(), 2.0)

        finder.addNum(4)
        self.assertEqual(finder.findMedian(), 2.5)

        finder.addNum(5)
        self.assertEqual(finder.findMedian(), 3.0)

    def test_single_element(self):
        finder = MedianFinder()

        finder.addNum(10)
        self.assertEqual(finder.findMedian(), 10.0)


if __name__ == "__main__":
    unittest.main()
