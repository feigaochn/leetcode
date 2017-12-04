#!/usr/bin/env python
# coding: utf-8


"""
Initially on a notepad only one character 'A' is present. You can perform two
operations on this notepad for each step:

1. Copy All: You can copy all the characters present on the notepad (partial
    copy is not allowed).
2. Paste: You can paste the characters which are copied last time.

Given a number n. You have to get exactly n 'A' on the notepad by performing
the minimum number of steps permitted. Output the minimum number of steps to
get n 'A'.
"""


class Solution:
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        INF = 10 ** 5
        dp = [{1: m} for m in range(n + 1)]
        # dp[m][k] the min steps to print m 'A' with k 'A' in clipboard
        dp[1][0] = 0
        for m in range(1, n):
            dp[m][m] = INF
            for k, s in dp[m].items():
                # paste
                if m + k <= n:
                    dp[m + k][k] = min(s + 1, dp[m + k].get(k, INF))
                # copy-all
                dp[m][m] = min(s + 1, dp[m].get(m, INF))

        return min(dp[n].values())


if __name__ == '__main__':
    sol = Solution().minSteps
    print(sol(1))
    print(sol(3))
    print(sol(4))
    print(sol(8))
    print(sol(1000))
    print(sol(997))
