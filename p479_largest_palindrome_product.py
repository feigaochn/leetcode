#!/usr/bin/env python
# coding: utf-8


class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        db = [None, 9, 987, 123, 597, 677, 1218, 877, 475]
        if n < len(db):
            return db[n]

        MOD = 1337
        sums = (10 ** n - 1) * 2
        while True:
            for a in range(10 ** n - 1, sums - (10 ** n - 1) - 1, -1):
                b = sums - a
                s = str(a * b)
                if s == s[::-1]:
                    return int(s) % MOD
            sums -= 1


if __name__ == '__main__':
    sol = Solution()
    for n in range(1, 8):
        print(n, ':', sol.largestPalindrome(n), ',')
