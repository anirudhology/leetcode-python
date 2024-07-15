import unittest

from problems.stack.evaluate_reverse_polish_notation import EvaluateReversePolishNotation


class TestEvaluateReversePolishNotation(unittest.TestCase):
    def test_basic_operations(self):
        # Test with basic addition
        self.assertEqual(EvaluateReversePolishNotation.evalRPN(["2", "1", "+", "3", "*"]), 9)
        # Test with basic subtraction
        self.assertEqual(EvaluateReversePolishNotation.evalRPN(["4", "13", "5", "/", "+"]), 6)
        # Test with basic multiplication
        self.assertEqual(EvaluateReversePolishNotation.evalRPN(["2", "3", "*", "4", "+"]), 10)
        # Test with basic division
        self.assertEqual(EvaluateReversePolishNotation.evalRPN(["10", "6", "/", "9", "+"]), 10)

    def test_single_operation(self):
        # Single operation addition
        self.assertEqual(EvaluateReversePolishNotation.evalRPN(["2", "3", "+"]), 5)
        # Single operation subtraction
        self.assertEqual(EvaluateReversePolishNotation.evalRPN(["5", "3", "-"]), 2)
        # Single operation multiplication
        self.assertEqual(EvaluateReversePolishNotation.evalRPN(["3", "4", "*"]), 12)
        # Single operation division
        self.assertEqual(EvaluateReversePolishNotation.evalRPN(["8", "4", "/"]), 2)

    def test_negative_numbers(self):
        # Test with negative numbers
        self.assertEqual(EvaluateReversePolishNotation.evalRPN(["-2", "-1", "+"]), -3)
        self.assertEqual(EvaluateReversePolishNotation.evalRPN(["-4", "-2", "/"]), 2)
        self.assertEqual(EvaluateReversePolishNotation.evalRPN(["-2", "3", "*"]), -6)


if __name__ == "__main__":
    unittest.main()
