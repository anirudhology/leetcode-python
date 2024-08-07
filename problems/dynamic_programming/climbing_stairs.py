class ClimbingStairs:
    @staticmethod
    def climbStairs(n: int) -> int:
        # Special cases
        if n <= 2:
            return n
        # Ways to climb previous two stairs
        a, b = 1, 2
        c = a + b
        # For remaining stairs
        for i in range(3, n + 1):
            c = a + b
            a = b
            b = c
        return c
