#!/usr/bin/env python
# coding: utf-8


class Solution:
    def judgeSquareSum(self, c):
        """Given a non-negative integer c, your task is to decide whether
        there're two integers a and b such that a**2 + b**2 = c.

        :type c: int
        :rtype: bool
        """
        from math import sqrt
        for a in range(1 + int(sqrt(c / 2))):
            b = int(sqrt(c - a * a))
            if a ** 2 + b ** 2 == c:
                return True
        return False


if __name__ == '__main__':
    sol = Solution()
    for c in range(10):
        print(c, sol.judgeSquareSum(c))
    print(sol.judgeSquareSum(10 ** 9))
