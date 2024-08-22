class LongestCommonSubsequence:
    @staticmethod
    def longestCommonSubsequence(text1: str, text2: str) -> int:
        # Lengths of the strings
        m, n = len(text1), len(text2)
        # Lookup table to store longest length until index i in string
        # text1 and index j in string text2
        lookup = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        # Populate the table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # For same characters
                if text1[i - 1] == text2[j - 1]:
                    lookup[i][j] = 1 + lookup[i - 1][j - 1]
                else:
                    lookup[i][j] = max(lookup[i - 1][j], lookup[i][j - 1])
        return lookup[m][n]
