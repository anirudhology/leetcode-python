class DecodeWays:
    @staticmethod
    def numDecodings(s: str) -> int:
        # Special case
        if s is None or len(s) == 0:
            return 0
        # Length of the string
        n = len(s)
        # Previous and current pointers
        previous, current = 1, 0
        # Process the string from right to left
        for i in range(n - 1, -1, -1):
            temp = 0 if s[i] == '0' else previous
            if i < n - 1 and (s[i] == '1' or s[i] == '2' and s[i + 1] <= '6'):
                temp += current
            current = previous
            previous = temp
        return previous
