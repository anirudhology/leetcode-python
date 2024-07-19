import unittest

from problems.binary_search.koko_eating_bananas import KokoEatingBananas


class KokoEatingBananasTest(unittest.TestCase):
    def setUp(self):
        self.solution = KokoEatingBananas()

    def test_empty_piles(self):
        self.assertEqual(self.solution.minEatingSpeed([], 5), 0)

    def test_null_piles(self):
        # noinspection PyTypeChecker
        self.assertEqual(self.solution.minEatingSpeed(None, 5), 0)

    def test_zero_hours(self):
        self.assertEqual(self.solution.minEatingSpeed([3, 6, 7, 11], 0), 0)

    def test_single_pile(self):
        self.assertEqual(self.solution.minEatingSpeed([100], 1), 100)

    def test_single_pile_multiple_hours(self):
        self.assertEqual(self.solution.minEatingSpeed([100], 10), 10)

    def test_multiple_piles_exact_hours(self):
        self.assertEqual(self.solution.minEatingSpeed([3, 6, 7, 11], 8), 4)

    def test_multiple_piles_more_hours(self):
        self.assertEqual(self.solution.minEatingSpeed([30, 11, 23, 4, 20], 6), 23)

    def test_multiple_piles_less_hours(self):
        self.assertEqual(self.solution.minEatingSpeed([30, 11, 23, 4, 20], 5), 30)

    def test_large_piles(self):
        self.assertEqual(self.solution.minEatingSpeed([1000000000], 2), 500000000)

    def test_uniform_piles_exact_hours(self):
        self.assertEqual(self.solution.minEatingSpeed([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 10), 1)

    def test_uniform_piles_more_hours(self):
        self.assertEqual(self.solution.minEatingSpeed([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 20), 1)

    def test_uniform_piles_less_hours(self):
        self.assertEqual(self.solution.minEatingSpeed([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 5), 1)


if __name__ == '__main__':
    unittest.main()
