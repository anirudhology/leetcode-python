from typing import List


class PlusOne:
    @staticmethod
    def plusOne(digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        output = [0] * (n + 1)
        output[0] = 1
        return output
