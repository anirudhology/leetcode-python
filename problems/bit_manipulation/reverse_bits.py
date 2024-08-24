class ReverseBits:
    @staticmethod
    def reverseBits(n: int) -> int:
        output = 0
        for i in range(32):
            output <<= 1
            output += (n & 1)
            n >>= 1
        return output
