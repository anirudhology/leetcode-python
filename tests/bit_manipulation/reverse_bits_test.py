import unittest

from problems.bit_manipulation.reverse_bits import ReverseBits


class TestReverseBits(unittest.TestCase):

    def test_reverse_bits_with_zero(self):
        reverse_bits = ReverseBits()
        self.assertEqual(reverse_bits.reverseBits(0), 0, "Reversing bits of 0 should return 0.")

    def test_reverse_bits_with_one(self):
        reverse_bits = ReverseBits()
        self.assertEqual(reverse_bits.reverseBits(1), 0b10000000000000000000000000000000,
                         "Reversing bits of 1 should return 2147483648.")

    def test_reverse_bits_with_max_integer(self):
        reverse_bits = ReverseBits()
        self.assertEqual(reverse_bits.reverseBits(0xFFFFFFFF), 0xFFFFFFFF,
                         "Reversing bits of 0xFFFFFFFF should return 0xFFFFFFFF.")

    def test_reverse_bits_with_min_integer(self):
        reverse_bits = ReverseBits()
        self.assertEqual(reverse_bits.reverseBits(0x80000000), 1, "Reversing bits of 0x80000000 should return 1.")

    def test_reverse_bits_with_negative_one(self):
        reverse_bits = ReverseBits()
        self.assertEqual(reverse_bits.reverseBits(-1), 0xFFFFFFFF, "Reversing bits of -1 should return 0xFFFFFFFF.")

    def test_reverse_bits_with_specific_number(self):
        reverse_bits = ReverseBits()
        self.assertEqual(reverse_bits.reverseBits(43261596), 964176192,
                         "Reversing bits of 43261596 should return 964176192.")


if __name__ == '__main__':
    unittest.main()
