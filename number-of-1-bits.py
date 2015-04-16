class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        w = 0
        while n:
            if n % 2 == 1:
                w += 1
            n = n // 2
        return w
        