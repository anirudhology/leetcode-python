import unittest

from problems.dynamic_programming.maximum_product_subarray import MaximumProductSubarray


class TestMaximumProductSubarray(unittest.TestCase):

    def setUp(self):
        self.maximum_product_subarray = MaximumProductSubarray()

    def test_max_product(self):
        # Test case for null input
        # noinspection PyTypeChecker
        self.assertEqual(self.maximum_product_subarray.maxProduct(None), 0)

        # Test case for empty array
        self.assertEqual(self.maximum_product_subarray.maxProduct([]), 0)

        # Test case for single positive element
        self.assertEqual(self.maximum_product_subarray.maxProduct([2]), 2)

        # Test case for single negative element
        self.assertEqual(self.maximum_product_subarray.maxProduct([-2]), -2)

        # Test case for array with both positive and negative elements
        self.assertEqual(self.maximum_product_subarray.maxProduct([2, 3, -2, 4]), 6)

        # Test case for array with a zero
        self.assertEqual(self.maximum_product_subarray.maxProduct([-2, 0, -1, 6, -4]), 24)

        # Test case for all negative elements
        self.assertEqual(self.maximum_product_subarray.maxProduct([-1, -3, -4]), 12)

        # Test case for all positive elements
        self.assertEqual(self.maximum_product_subarray.maxProduct([1, 2, 3, 4, 5, 6]), 720)

        # Test case for array with a mix of positive, negative, and zero elements
        self.assertEqual(self.maximum_product_subarray.maxProduct([-2, 0, -1, -3, 10, 6]), 180)


if __name__ == '__main__':
    unittest.main()
