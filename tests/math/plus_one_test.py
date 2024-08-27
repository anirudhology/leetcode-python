import unittest

from problems.math.plus_one import PlusOne


class TestPlusOne(unittest.TestCase):

    def setUp(self):
        self.plus_one = PlusOne()

    def test_plus_one_no_carry_over(self):
        self.assertEqual(self.plus_one.plusOne([1, 2, 3]), [1, 2, 4])

    def test_plus_one_with_carry_over_in_middle(self):
        self.assertEqual(self.plus_one.plusOne([1, 2, 9]), [1, 3, 0])

    def test_plus_one_with_all_nines(self):
        self.assertEqual(self.plus_one.plusOne([9, 9, 9]), [1, 0, 0, 0])

    def test_plus_one_empty_array(self):
        self.assertEqual(self.plus_one.plusOne([]), [1])


if __name__ == '__main__':
    unittest.main()
