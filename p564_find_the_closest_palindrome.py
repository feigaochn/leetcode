#!/usr/bin/env python3
# coding: utf-8

import sys


class Solution(object):
    def nearestPalindromic(self, origin):
        """
        :type origin: str
        :rtype: str
        """
        l = len(origin)
        best = []

        pal = "9" * (l - 1)
        if pal and pal != origin:
            best.append(pal)
        # direct
        old = origin[::]
        pal = old[:(len(old) + 1) // 2] + old[:len(old) // 2][::-1]
        if pal != origin:
            best.append(pal)

        for mid in [10 ** (l // 2), 10 ** ((l - 1) // 2)]:

            old = str(int(origin) + mid)
            pal = old[:(len(old) + 1) // 2] + old[:len(old) // 2][::-1]
            if pal != origin:
                best.append(pal)

            old = str(int(origin) - mid)
            pal = old[:(len(old) + 1) // 2] + old[:len(old) // 2][::-1]
            if pal != origin:
                best.append(pal)

        # print(origin, best)
        return min(best, key=lambda v: (abs(int(v) - int(origin)), int(v)))


def main(args):
    sol = Solution()
    print(sol.nearestPalindromic("123"))
    print(sol.nearestPalindromic("1234"))
    print(sol.nearestPalindromic("17001"))
    print(sol.nearestPalindromic("3"))
    print(sol.nearestPalindromic("1"))
    print(sol.nearestPalindromic("9"))
    print(sol.nearestPalindromic("10"))
    print(sol.nearestPalindromic("11"))
    print(sol.nearestPalindromic("1213"))

    for i in range(1, 20):
        print(i, sol.nearestPalindromic(str(i)))
    return


if __name__ == '__main__':
    main(sys.argv[1:])
