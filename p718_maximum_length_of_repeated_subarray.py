class Solution:
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        dp = [[0 for _ in B + [0]] for _ in A + [0]]
        max_dp = 0
        for i, a in enumerate(A, 1):
            for j, b in enumerate(B, 1):
                if a == b:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    max_dp = max(max_dp, dp[i][j])
                else:
                    dp[i][j] = 0
        return max_dp


fn = Solution().findLength

print(fn([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]))
