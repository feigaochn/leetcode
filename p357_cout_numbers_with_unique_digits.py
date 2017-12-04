#!/usr/bin/env python
# coding: utf-8


"""
Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:
Given n = 2, return 91. (The answer should be the total numbers in the range of 0 ≤ x < 100, excluding [11,22,33,44,55,66,77,88,99])
"""


class Solution:
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        from math import factorial

        def perm(n, k):
            if n >= k:
                return factorial(n) // factorial(n - k)
            else:
                return 0

        nums = [1] + [9 * perm(9, k) for k in range(n + 1)]
        return sum(nums[:n + 1])


if __name__ == '__main__':
    sol = Solution().countNumbersWithUniqueDigits
    print(sol(0))
    print(sol(1))
    print(sol(2))
    print(sol(3))
    print(sol(31))
