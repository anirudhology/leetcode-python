class HappyNumber:
    @staticmethod
    def isHappy(n: int) -> bool:
        # Special case
        if n == 1 or n == 7:
            return True

        def calculate_square_of_digits(num):
            square = 0
            while num > 0:
                remainder = num % 10
                square += remainder ** 2
                num //= 10
            return square

        while n > 9:
            n = calculate_square_of_digits(n)
            if n == 1 or n == 7:
                return True

        return False
