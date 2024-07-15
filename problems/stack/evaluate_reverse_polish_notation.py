from collections import deque
from typing import List


class EvaluateReversePolishNotation:
    @staticmethod
    def evalRPN(tokens: List[str]) -> int:
        # Stack to store the operands
        operands = deque()
        # Process the tokens
        for token in tokens:
            if token == "+":
                x, y = operands.pop(), operands.pop()
                operands.append(x + y)
            elif token == "-":
                x, y = operands.pop(), operands.pop()
                operands.append(y - x)
            elif token == "*":
                x, y = operands.pop(), operands.pop()
                operands.append(x * y)
            elif token == "/":
                x, y = operands.pop(), operands.pop()
                # Use int() for truncation towards zero
                operands.append(int(y / x))
            else:
                operands.append(int(token))
        return operands.pop()
