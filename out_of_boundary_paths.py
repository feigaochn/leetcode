#!/usr/bin/env python3
# coding: utf-8

import sys


class Solution:
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        if N == 0:
            return 0
        from collections import defaultdict
        mod = 10 ** 9 + 7
        ret = 0
        maps = [defaultdict(int), defaultdict(int)]
        for c in range(n):
            maps[1][(0, c)] += 1
            maps[1][(m - 1, c)] += 1
        for r in range(m):
            maps[1][(r, 0)] += 1
            maps[1][(r, n - 1)] += 1

        ret += maps[1].get((i, j), 0)

        for step in range(2, N + 1):
            midx = step % 2
            for r in range(m):
                for c in range(n):
                    maps[midx][(r, c)] = (maps[1 - midx].get((r - 1, c), 0) +
                                          maps[1 - midx].get((r + 1, c), 0) +
                                          maps[1 - midx].get((r, c - 1), 0) +
                                          maps[1 - midx].get((r, c + 1), 0))
                    if maps[midx][(r, c)] > mod:
                        maps[midx][(r, c)] %= mod
            ret = (ret + maps[midx].get((i, j), 0)) % mod
            # print(step, maps[midx])

        return ret


def main(args):
    sol = Solution()
    print(sol.findPaths(2, 2, 2, 0, 0))
    print(sol.findPaths(1, 3, 3, 0, 1))
    print(sol.findPaths(50, 50, 50, 0, 0))
    return


if __name__ == '__main__':
    main(sys.argv[1:])
