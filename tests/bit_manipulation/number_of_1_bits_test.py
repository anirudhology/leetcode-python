import unittest

from problems.bit_manipulation.number_of_1_bits import NumberOf1Bits


class TestNumberOf1Bits(unittest.TestCase):

    def test_hamming_weight_zero(self):
        number_of_1_bits = NumberOf1Bits()
        self.assertEqual(number_of_1_bits.hammingWeight(0), 0, "Hamming weight of 0 should be 0.")

    def test_hamming_weight_one(self):
        number_of_1_bits = NumberOf1Bits()
        self.assertEqual(number_of_1_bits.hammingWeight(1), 1, "Hamming weight of 1 should be 1.")

    def test_hamming_weight_large_number(self):
        number_of_1_bits = NumberOf1Bits()
        self.assertEqual(number_of_1_bits.hammingWeight(11), 3, "Hamming weight of 11 (binary 1011) should be 3.")

    def test_hamming_weight_power_of_two(self):
        number_of_1_bits = NumberOf1Bits()
        self.assertEqual(number_of_1_bits.hammingWeight(16), 1, "Hamming weight of 16 (binary 10000) should be 1.")

    def test_hamming_weight_all_bits_set(self):
        number_of_1_bits = NumberOf1Bits()
        self.assertEqual(number_of_1_bits.hammingWeight(0xFFFFFFFF), 32, "Hamming weight of 0xFFFFFFFF should be 32.")

    def test_hamming_weight_mixed_bits(self):
        number_of_1_bits = NumberOf1Bits()
        self.assertEqual(number_of_1_bits.hammingWeight(29), 4, "Hamming weight of 29 (binary 11101) should be 4.")


if __name__ == '__main__':
    unittest.main()
