class NumberOf1Bits:
    @staticmethod
    def hammingWeight(n: int) -> int:
        set_bits = 0
        while n > 0:
            n &= (n - 1)
            set_bits += 1
        return set_bits
