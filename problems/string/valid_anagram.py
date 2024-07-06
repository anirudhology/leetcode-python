class ValidAnagram:

    @staticmethod
    def isAnagram(s: str, t: str) -> bool:
        # Special case
        if len(s) != len(t):
            return False
        # List to store the frequencies of characters
        frequencies = [0] * 26
        # Traverse through both strings
        for i in range(len(s)):
            s_index = ord(s[i]) - ord('a')
            t_index = ord(t[i]) - ord('a')
            frequencies[s_index] += 1
            frequencies[t_index] -= 1
        # Check if any character has non-zero frequency
        for frequency in frequencies:
            if frequency != 0:
                return False
        return True
