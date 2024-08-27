import unittest

from problems.matrix.happy_number import HappyNumber


class TestHappyNumber(unittest.TestCase):
    def setUp(self):
        self.happy_number = HappyNumber()

    def test_isHappy(self):
        # Test happy numbers
        self.assertTrue(self.happy_number.isHappy(1))
        self.assertTrue(self.happy_number.isHappy(7))
        self.assertTrue(self.happy_number.isHappy(19))

        # Test unhappy numbers
        self.assertFalse(self.happy_number.isHappy(2))
        self.assertFalse(self.happy_number.isHappy(4))
        self.assertFalse(self.happy_number.isHappy(20))

        # Test number with multiple digits that is not happy
        self.assertFalse(self.happy_number.isHappy(21))

if __name__ == '__main__':
    unittest.main()
