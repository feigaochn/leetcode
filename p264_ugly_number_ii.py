#!/usr/bin/env python
# coding: utf-8

class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        p2 = p3 = p5 = 0
        ugly = [1]
        for _ in range(n - 1):
            next = min(ugly[p2] * 2,
                       ugly[p3] * 3,
                       ugly[p5] * 5)
            ugly.append(next)
            if next == ugly[p2] * 2:
                p2 += 1
            if next == ugly[p3] * 3:
                p3 += 1
            if next == ugly[p5] * 5:
                p5 += 1
        return ugly[-1]


if __name__ == '__main__':
    sol = Solution().nthUglyNumber
    print(sol(1))
    print(sol(10))
    print(sol(1000))
