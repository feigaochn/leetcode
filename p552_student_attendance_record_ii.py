#!/usr/bin/env python3
# coding: utf-8

import sys


class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        mod = 10 ** 9 + 7

        lastLL = [0] * (n + 2)
        lastPL = [0] * (n + 2)
        lastLP = [0] * (n + 2)
        lastPP = [0] * (n + 2)
        total = [1] * (n + 2)

        lastLL[2] = lastLP[2] = lastPP[2] = lastPL[2] = 1
        total[1] = 2
        total[2] = 4

        for i in range(3, n + 1):
            lastLL[i] = (lastPL[i - 1])
            lastPL[i] = (lastLP[i - 1] + lastPP[i - 1]) % mod

            lastLP[i] = (lastLL[i - 1] + lastPL[i - 1]) % mod
            lastPP[i] = (lastLP[i - 1] + lastPP[i - 1]) % mod

            total[i] = (lastPP[i] + lastPL[i] + lastLP[i] + lastLL[i]) % mod

        ret = total[n]

        # f + 'A' + (n-1-f)
        for f in range(0, n):
            ret = (ret + total[f] * total[n - 1 - f]) % mod

        return ret


def main(args):
    sol = Solution()
    print(sol.checkRecord(10 ** 5))
    print(sol.checkRecord(1))
    return


if __name__ == '__main__':
    main(sys.argv[1:])
