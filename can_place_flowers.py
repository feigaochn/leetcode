#!/usr/bin/env python
# coding: utf-8


class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if not flowerbed:
            return n == 0

        from itertools import groupby
        gps = list()
        for group in groupby(flowerbed):
            gps.append((group[0], len(list(group[1]))))

        if len(gps) == 1:
            if gps[0][0] == 0:
                flowers = (gps[0][1] + 1) // 2
            else:
                flowers = 0
        else:
            flowers = 0
            for i, (v, k) in enumerate(gps):
                if v == 0:
                    if i == 0 or i == len(gps) - 1:
                        flowers += k // 2
                    else:
                        flowers += (k - 1) // 2

        return flowers >= n


if __name__ == '__main__':
    sol = Solution()
    print(sol.canPlaceFlowers([1, 0, 0, 0, 1], 1))
    print(sol.canPlaceFlowers([1, 0, 0, 0, 1], 2))
    print(sol.canPlaceFlowers([1, 0, 0, 0, 1, 0, 0], 2))
    print(sol.canPlaceFlowers([], 1))
    print(sol.canPlaceFlowers([0], 2))
