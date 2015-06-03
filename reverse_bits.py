class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return int(''.join('1' if n & (1<<i) != 0 else '0' for i in range(0, 32)), 2)