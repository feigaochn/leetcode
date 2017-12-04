#!/usr/bin/env python
# coding: utf-8


"""
Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.
"""


class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = "{:b}".format(n)
        from itertools import groupby
        return all(len(list(gp[1])) == 1 for gp in groupby(s))


if __name__ == '__main__':
    sol = Solution().hasAlternatingBits
    print(sol(5), '?= True')
    print(sol(7), '?= False')
    print(sol(11), '?= False')
    print(sol(10), '?= True')
