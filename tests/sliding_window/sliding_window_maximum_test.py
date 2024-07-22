import unittest

from problems.sliding_window.sliding_window_maximum import SlidingWindowMaximum


class SlidingWindowMaximumTest(unittest.TestCase):

    def setUp(self):
        self.solution = SlidingWindowMaximum()

    def test_maxSlidingWindow(self):
        self.assertEqual(self.solution.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3), [3, 3, 5, 5, 6, 7])
        self.assertEqual(self.solution.maxSlidingWindow([1, 3, 1, 2, 0, 5], 3), [3, 3, 2, 5])
        self.assertEqual(self.solution.maxSlidingWindow([1, 2, 3, 4, 5], 2), [2, 3, 4, 5])
        self.assertEqual(self.solution.maxSlidingWindow([9, 8, 7, 6, 5], 2), [9, 8, 7, 6])
        self.assertEqual(self.solution.maxSlidingWindow([2, 2, 2, 2], 1), [2, 2, 2, 2])
        self.assertEqual(self.solution.maxSlidingWindow([1], 1), [1])
        self.assertEqual(self.solution.maxSlidingWindow([], 0), [])
        self.assertEqual(self.solution.maxSlidingWindow([], -1), [])
        self.assertEqual(self.solution.maxSlidingWindow([1, 2, 3], 4), [])
        self.assertEqual(self.solution.maxSlidingWindow([1, -1], 1), [1, -1])
        self.assertEqual(self.solution.maxSlidingWindow([4, 3, 11, 2, 6, 5], 3), [11, 11, 11, 6])

    def test_special_cases(self):
        self.assertEqual(self.solution.maxSlidingWindow([], 3), [])
        self.assertEqual(self.solution.maxSlidingWindow([1, 2, 3], 3), [3])


if __name__ == '__main__':
    unittest.main()
