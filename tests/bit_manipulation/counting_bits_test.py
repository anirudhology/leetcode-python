import unittest

from problems.bit_manipulation.counting_bits import CountingBits


class TestCountingBits(unittest.TestCase):

    def test_count_bits_with_zero(self):
        counting_bits = CountingBits()
        self.assertEqual(counting_bits.countBits(0), [0], "Count bits of 0 should return [0].")

    def test_count_bits_with_one(self):
        counting_bits = CountingBits()
        self.assertEqual(counting_bits.countBits(1), [0, 1], "Count bits of 1 should return [0, 1].")

    def test_count_bits_with_two(self):
        counting_bits = CountingBits()
        self.assertEqual(counting_bits.countBits(2), [0, 1, 1], "Count bits of 2 should return [0, 1, 1].")

    def test_count_bits_with_five(self):
        counting_bits = CountingBits()
        self.assertEqual(counting_bits.countBits(5), [0, 1, 1, 2, 1, 2],
                         "Count bits of 5 should return [0, 1, 1, 2, 1, 2].")

    def test_count_bits_with_ten(self):
        counting_bits = CountingBits()
        self.assertEqual(counting_bits.countBits(10), [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2],
                         "Count bits of 10 should return [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2].")


if __name__ == '__main__':
    unittest.main()
