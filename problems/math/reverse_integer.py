class ReverseInteger:
    @staticmethod
    def reverse(x: int) -> int:
        max_value = 2 ** 31 - 1
        x_reverse = 0
        num = abs(x)
        while num != 0:
            remainder = num % 10
            # Check for overflow
            if x_reverse > (max_value // 10) or (x_reverse == (max_value // 10) and remainder > max_value % 10):
                return 0
            x_reverse = 10 * x_reverse + remainder
            num //= 10
        return -x_reverse if x < 0 else x_reverse
