class ValidParenthesisString:
    @staticmethod
    def checkValidString(s: str) -> bool:
        # Special case
        if s is None or not len(s):
            return True
        # Count of minimum and maximum open parentheses
        min_open, max_open = 0, 0
        # Traverse through the string
        for c in s:
            # If it is a left parenthesis, it means you have one
            # more open parenthesis to worry about
            if c == '(':
                min_open += 1
                max_open += 1
            # If it is right parenthesis, it means you have one
            # less open parenthesis to worry about
            elif c == ')':
                min_open -= 1
                max_open -= 1
            # If it is *, it means there are three cases
            # 1. If we make it as ), then we have one less open parenthesis to worry about
            # 2. If we make it as (, then we have one more open parentheses
            # to worry about
            # 3. No impact at all
            elif c == '*':
                min_open -= 1
                max_open += 1

            # There are more closing parentheses, then opening ones
            if max_open < 0:
                return False
            # We can't have negative open parenthesis count
            if min_open < 0:
                min_open = 0

        return min_open == 0
