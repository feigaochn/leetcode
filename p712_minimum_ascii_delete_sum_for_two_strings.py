class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        dp = [[0 for _ in (s2 + " ")] for _ in (s1 + " ")]
        for i in range(len(s1)):
            for j in range(len(s2)):
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
                if s1[i] == s2[j]:
                    dp[i + 1][j + 1] = max(dp[i + 1][j + 1],
                                           ord(s1[i]) + dp[i][j])
        return sum(map(ord, s1)) + sum(map(ord, s2)) - dp[-1][-1] * 2


sol = Solution().minimumDeleteSum
print(sol("at", "a"), '?= 116')
print(sol("sea", "eat"), '?= 231')
print(sol("delete", "leet"), "?= 403")
