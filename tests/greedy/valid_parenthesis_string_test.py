import unittest

from problems.greedy.valid_parenthesis_string import ValidParenthesisString


class TestValidParenthesisString(unittest.TestCase):

    def setUp(self):
        self.valid_parenthesis_string = ValidParenthesisString()

    def test_check_valid_string(self):
        # Test null input
        self.assertTrue(self.valid_parenthesis_string.checkValidString(None))

        # Test empty string
        self.assertTrue(self.valid_parenthesis_string.checkValidString(""))

        # Test valid strings
        self.assertTrue(self.valid_parenthesis_string.checkValidString("()"))
        self.assertTrue(self.valid_parenthesis_string.checkValidString("(*)"))
        self.assertTrue(self.valid_parenthesis_string.checkValidString("(*))"))

        # Test invalid strings
        self.assertFalse(self.valid_parenthesis_string.checkValidString(")"))
        self.assertFalse(self.valid_parenthesis_string.checkValidString(")("))
        self.assertTrue(self.valid_parenthesis_string.checkValidString("((*)"))
        self.assertFalse(self.valid_parenthesis_string.checkValidString("((*))("))

    def test_edge_cases(self):
        # Test string with only one *
        self.assertTrue(self.valid_parenthesis_string.checkValidString("*"))

        # Test string with multiple *
        self.assertTrue(self.valid_parenthesis_string.checkValidString("***"))

        # Test strings with nested parentheses
        self.assertTrue(self.valid_parenthesis_string.checkValidString("(())"))
        self.assertFalse(self.valid_parenthesis_string.checkValidString("(()))"))


if __name__ == '__main__':
    unittest.main()
