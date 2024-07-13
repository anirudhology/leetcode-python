import unittest

from problems.stack.valid_parentheses import ValidParentheses


class TestValidParentheses(unittest.TestCase):
    def setUp(self):
        self.validator = ValidParentheses()

    def test_empty_string(self):
        self.assertTrue(self.validator.isValid(""))

    def test_single_left_parenthesis(self):
        self.assertFalse(self.validator.isValid("("))

    def test_single_right_parenthesis(self):
        self.assertFalse(self.validator.isValid(")"))

    def test_single_left_brace(self):
        self.assertFalse(self.validator.isValid("{"))

    def test_single_right_brace(self):
        self.assertFalse(self.validator.isValid("}"))

    def test_single_left_bracket(self):
        self.assertFalse(self.validator.isValid("["))

    def test_single_right_bracket(self):
        self.assertFalse(self.validator.isValid("]"))

    def test_valid_simple(self):
        self.assertTrue(self.validator.isValid("()"))
        self.assertTrue(self.validator.isValid("[]"))
        self.assertTrue(self.validator.isValid("{}"))

    def test_valid_nested(self):
        self.assertTrue(self.validator.isValid("({[]})"))
        self.assertTrue(self.validator.isValid("[{()}]"))
        self.assertTrue(self.validator.isValid("{[()]}"))

    def test_invalid_mixed(self):
        self.assertFalse(self.validator.isValid("(]"))
        self.assertFalse(self.validator.isValid("[)"))
        self.assertFalse(self.validator.isValid("{)"))

    def test_invalid_unmatched_left(self):
        self.assertFalse(self.validator.isValid("({["))

    def test_invalid_unmatched_right(self):
        self.assertFalse(self.validator.isValid(")}]"))

    def test_valid_complex(self):
        self.assertTrue(self.validator.isValid("{[()()]()}"))

    def test_invalid_complex(self):
        self.assertFalse(self.validator.isValid("{[()([)]}"))

    def test_valid_with_repeated_characters(self):
        self.assertTrue(self.validator.isValid("()()()"))
        self.assertTrue(self.validator.isValid("[][][]"))
        self.assertTrue(self.validator.isValid("{}{}{}"))

    def test_invalid_with_repeated_characters(self):
        self.assertFalse(self.validator.isValid("((())"))
        self.assertFalse(self.validator.isValid("{{{{}}"))
        self.assertTrue(self.validator.isValid("[[[]]]"))

    def test_null_string(self):
        # noinspection PyTypeChecker
        self.assertTrue(self.validator.isValid(None))


if __name__ == "__main__":
    unittest.main()
