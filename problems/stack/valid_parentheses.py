from collections import deque


class ValidParentheses:
    @staticmethod
    def isValid(s: str) -> bool:
        # Special case
        if s is None or len(s) == 0:
            return True
        # Stack to store the left parentheses
        stack = deque()
        # Process the string
        for c in s:
            # Add left parentheses to stack
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            # Match right parentheses accordingly
            elif c == ')' and len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            elif c == '}' and len(stack) > 0 and stack[-1] == '{':
                stack.pop()
            elif c == ']' and len(stack) > 0 and stack[-1] == '[':
                stack.pop()
            # For any other invalid character
            else:
                return False
        return not stack
