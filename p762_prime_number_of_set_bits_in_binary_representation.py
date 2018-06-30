class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        return sum(
            (bin(x).count('1') in {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31})
            for x in range(L, R + 1))


sol = Solution().countPrimeSetBits
print(sol(1, 10**4))
# print(sol(1, 10**6))
print(sol(6, 10))
print(sol(10, 15))
print(sol(289051, 294301))
