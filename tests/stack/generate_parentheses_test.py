import unittest

from problems.stack.generate_parentheses import GenerateParentheses


class GenerateParenthesesTest(unittest.TestCase):

    def setUp(self):
        self.generate_parentheses = GenerateParentheses()

    def test_generateParenthesis_zero(self):
        self.assertEqual(self.generate_parentheses.generateParenthesis(0), [])

    def test_generateParenthesis_negative(self):
        self.assertEqual(self.generate_parentheses.generateParenthesis(-1), [])

    def test_generateParenthesis_one(self):
        self.assertEqual(self.generate_parentheses.generateParenthesis(1), ["()"])

    def test_generateParenthesis_two(self):
        self.assertEqual(set(self.generate_parentheses.generateParenthesis(2)), {"(())", "()()"})

    def test_generateParenthesis_three(self):
        self.assertEqual(set(self.generate_parentheses.generateParenthesis(3)), {"((()))", "(()())", "(())()", "()(())",
                                                                                 "()()()"})

    def test_generateParenthesis_four(self):
        self.assertEqual(set(self.generate_parentheses.generateParenthesis(4)),
                         {"(((())))", "((()()))", "((())())", "((()))()", "(()(()))", "(()()())", "(()())()",
                          "(())(())", "(())()()", "()((()))", "()(()())", "()(())()", "()()(())", "()()()()"})


if __name__ == "__main__":
    unittest.main()
