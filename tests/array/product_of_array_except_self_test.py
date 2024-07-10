import unittest

from problems.array.product_of_array_except_self import ProductOfArrayExceptSelf


class ProductOfArrayExceptSelfTest(unittest.TestCase):

    def test_null_array(self):
        # noinspection PyTypeChecker
        self.assertIsNone(ProductOfArrayExceptSelf.productExceptSelf(None))

    def test_single_element_array(self):
        self.assertEqual(ProductOfArrayExceptSelf.productExceptSelf([1]), [1])

    def test_two_elements_array(self):
        self.assertEqual(ProductOfArrayExceptSelf.productExceptSelf([1, 2]), [2, 1])

    def test_multiple_elements_array(self):
        self.assertEqual(ProductOfArrayExceptSelf.productExceptSelf([1, 2, 3, 4]), [24, 12, 8, 6])

    def test_array_with_zeros(self):
        self.assertEqual(ProductOfArrayExceptSelf.productExceptSelf([1, 2, 0, 4]), [0, 0, 8, 0])

    def test_array_with_multiple_zeros(self):
        self.assertEqual(ProductOfArrayExceptSelf.productExceptSelf([0, 0, 2, 4]), [0, 0, 0, 0])

    def test_array_with_negative_numbers(self):
        self.assertEqual(ProductOfArrayExceptSelf.productExceptSelf([-1, 2, -3, 4]), [-24, 12, -8, 6])


if __name__ == "__main__":
    unittest.main()
