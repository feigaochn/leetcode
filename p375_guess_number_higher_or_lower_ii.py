#!/usr/bin/env python
# coding: utf-8

class Solution:
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        inf = float('inf')
        dp = [[inf if s < e else 0
               for e in range(n)]
              for s in range(n)]
        # print(dp)
        for l in range(1, n):
            for s in range(n - l):
                e = s + l
                if e >= n:
                    break
                for x in range(s + 1, e):
                    dp[s][e] = min(dp[s][e],
                                   x + 1 + max(dp[s][x - 1],
                                               dp[x + 1][e]))
                dp[s][e] = min(dp[s][e],
                               s + 1 + dp[s + 1][e],
                               dp[s][e - 1] + e + 1)
        # print(dp[0])
        return dp[0][n - 1]


if __name__ == '__main__':
    sol = Solution().getMoneyAmount
    print(sol(10))
