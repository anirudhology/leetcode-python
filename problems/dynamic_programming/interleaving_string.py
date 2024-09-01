class InterleavingString:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Lengths of the strings
        m, n = len(s1), len(s2)
        # Special case
        if m + n != len(s3):
            return False
        # Lookup table to store if s3[0...k] can be formed by s1[0...i] and
        # s2[0...j]
        lookup = [[False] * (n + 1) for _ in range(m + 1)]
        # For empty strings
        lookup[0][0] = True
        # If s2 is empty
        for i in range(1, m + 1):
            lookup[i][0] = lookup[i - 1][0] and s1[i - 1] == s3[i - 1]
        # If s1 is empty
        for j in range(1, n + 1):
            lookup[0][j] = lookup[0][j - 1] and s2[j - 1] == s3[j - 1]
        # Populate the remaining table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                lookup[i][j] = (lookup[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (
                            lookup[i][j - 1] and s2[j - 1] == s3[i + j - 1])

        return lookup[m][n]
