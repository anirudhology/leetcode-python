import unittest

from problems.string.valid_palindrome import ValidPalindrome


class TestValidPalindrome(unittest.TestCase):

    def setUp(self):
        self.valid_palindrome = ValidPalindrome()

    def test_null_string(self):
        # noinspection PyTypeChecker
        self.assertTrue(self.valid_palindrome.isPalindrome(None))

    def test_empty_string(self):
        self.assertTrue(self.valid_palindrome.isPalindrome(""))

    def test_single_character_string(self):
        self.assertTrue(self.valid_palindrome.isPalindrome("a"))
        self.assertTrue(self.valid_palindrome.isPalindrome("Z"))
        self.assertTrue(self.valid_palindrome.isPalindrome("1"))

    def test_valid_palindrome(self):
        self.assertTrue(self.valid_palindrome.isPalindrome("A man, a plan, a canal: Panama"))
        self.assertTrue(self.valid_palindrome.isPalindrome("racecar"))
        self.assertTrue(self.valid_palindrome.isPalindrome("0P0"))

    def test_invalid_palindrome(self):
        self.assertFalse(self.valid_palindrome.isPalindrome("hello"))
        self.assertFalse(self.valid_palindrome.isPalindrome("race a car"))
        self.assertFalse(self.valid_palindrome.isPalindrome("abc123"))

    def test_mixed_alphanumeric(self):
        self.assertTrue(self.valid_palindrome.isPalindrome("A1b2B1a"))
        self.assertFalse(self.valid_palindrome.isPalindrome("A1b2B3a"))

    def test_special_characters(self):
        self.assertTrue(self.valid_palindrome.isPalindrome("!@#$%^&*()_+"))
        self.assertTrue(self.valid_palindrome.isPalindrome("A man, a plan, a canal, Panama!"))
        self.assertTrue(self.valid_palindrome.isPalindrome("No 'x' in Nixon"))

    def test_isAlphanumeric(self):
        self.assertTrue(self.valid_palindrome.isAlphanumeric('a'))
        self.assertTrue(self.valid_palindrome.isAlphanumeric('Z'))
        self.assertTrue(self.valid_palindrome.isAlphanumeric('1'))
        self.assertFalse(self.valid_palindrome.isAlphanumeric('!'))
        self.assertFalse(self.valid_palindrome.isAlphanumeric(' '))


if __name__ == '__main__':
    unittest.main()
