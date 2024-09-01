class DistinctSubsequences:
    @staticmethod
    def numDistinct(s: str, t: str) -> int:
        # Lengths of both strings
        m, n = len(s), len(t)
        # Lookup table to store count of distinct subsequences
        lookup = [[0 for j in range(n + 1)] for i in range(m + 1)]
        # If t is empty, it can be subsequence of every string but only once
        for i in range(m + 1):
            lookup[i][0] = 1
        # If both strings are empty
        lookup[0][0] = 1
        # Populate the remaining table
        for j in range(1, n + 1):
            for i in range(1, m + 1):
                lookup[i][j] = lookup[i - 1][j]
                # If characters are same
                if s[i - 1] == t[j - 1]:
                    lookup[i][j] += lookup[i - 1][j - 1]
        return lookup[m][n]