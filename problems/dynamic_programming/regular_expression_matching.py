class RegularExpressionMatching:
    @staticmethod
    def isMatch(s: str, p: str) -> bool:
        # Lengths of strings
        m, n = len(s), len(p)
        # Lookup table to store if s[0...i] matches with p[0...j]
        lookup = [[False] * (n + 1) for _ in range(m + 1)]
        # Empty string matches with empty pattern
        lookup[0][0] = True
        # For empty string and star pattern
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                lookup[0][j] = lookup[0][j - 2]
        # Populate the remaining table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # If characters are same or we have period in pattern
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    lookup[i][j] = lookup[i - 1][j - 1]
                elif j > 1 and p[j - 1] == '*':
                    lookup[i][j] = lookup[i][j - 2]
                    if p[j - 2] == '.' or s[i - 1] == p[j - 2]:
                        lookup[i][j] = lookup[i][j] | lookup[i - 1][j]
        return lookup[m][n]
