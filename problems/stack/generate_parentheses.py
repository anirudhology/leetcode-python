from typing import List


class GenerateParentheses:
    def generateParenthesis(self, n: int) -> List[str]:
        # List to store the combinations
        combinations = []
        # Special case
        if n <= 0:
            return combinations
        # Stack to store combinations
        stack = []
        self.generate(n, 0, 0, stack, combinations)
        return combinations

    def generate(self, n: int, left: int, right: int, stack: List[str], combinations: List[str]):
        # Base case
        if left == right and left == n:
            combination = "".join(stack)
            combinations.append(combination)
            return
        # Add left parenthesis, if possible
        if left < n:
            stack.append('(')
            self.generate(n, left + 1, right, stack, combinations)
            stack.pop()
        # Match right parentheses
        if right < left:
            stack.append(')')
            self.generate(n, left, right + 1, stack, combinations)
            stack.pop()
