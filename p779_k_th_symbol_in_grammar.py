class Solution:
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """

        def solve(n, k):
            if n == 0:
                return 0
            else:
                l = solve(n - 1, k // 2)
                return (l + k) % 2

        return solve(N - 1, K - 1)


sol = Solution().kthGrammar

print(sol(1, 1))
print(sol(2, 1))
print(sol(2, 2))
print(sol(4, 5))
print(sol(30, 2**(30 - 1) - 102))
