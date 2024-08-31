class EditDistance:
    @staticmethod
    def minDistance(word1: str, word2: str) -> int:
        # Lengths of the strings
        m, n = len(word1), len(word2)
        # Lookup table to store minimum operations required
        lookup = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        # Base initialization
        for i in range(m + 1):
            lookup[i][0] = i
        for j in range(n + 1):
            lookup[0][j] = j
        # Populate the remaining table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # If current characters are same, we don't have to
                # do anything
                cost = 0 if word1[i - 1] == word2[j - 1] else 1
                lookup[i][j] = min(cost + lookup[i - 1][j - 1], 1 + lookup[i - 1][j], 1 + lookup[i][j - 1])

        return lookup[m][n]
