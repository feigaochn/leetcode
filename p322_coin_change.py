# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: coin change
#
# You are given coins of different denominations and a total amount of money
# amount. Write a function to compute the fewest number of coins that you need
# to make up that amount. If that amount of money cannot be made up by any
# combination of the coins, return -1.
# 
# Example 1:
# coins = [1, 2, 5], amount = 11
# return 3 (11 = 5 + 5 + 1)
# 
# Example 2:
# coins = [2], amount = 3
# return -1.
# 
# Note:
# You may assume that you have an infinite number of each kind of coin.
# 
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Dynamic Programming

from typing import List


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort()
        dp = [amount + 1 for _ in range(amount + 1)]
        dp[0] = 0
        for v in range(1, amount + 1):
            for c in coins:
                if c > v: break
                dp[v] = min(dp[v], dp[v-c] + 1)
        return -1 if dp[amount] == amount + 1 else dp[-1]


def main():
    solver = Solution()
    tests = [
        (([1, 2, 5], 11), 3),
        (([2], 3), -1),
        (([186, 419, 83, 408], 6249), None),
        (([384, 324, 196, 481], 285), None),
        (([406, 435, 260, 178, 55], 2924), None),
        (([99, 100], 99 * 99), 99),
        (([88, 227, 216, 96, 209, 172, 259], 6928), None),
        (([1], 0), 0),
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.coinChange(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
