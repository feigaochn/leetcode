#!/usr/bin/env python
# coding: utf-8

"""
A magical string S consists of only '1' and '2' and obeys the following rules:

The string S is magical because concatenating the number of contiguous occurrences of characters '1' and '2' generates the string S itself.

The first few elements of string S is the following: S = "1221121221221121122……"

If we group the consecutive '1's and '2's in S, it will be:

1 22 11 2 1 22 1 22 11 2 11 22 ......

and the occurrences of '1's or '2's in each group are:

1 2	2 1 1 2 1 2 2 1 2 2 ......

You can see that the occurrence sequence above is the S itself.

Given an integer N as input, return the number of '1's in the first N number in the magical string S.

Note: N will not exceed 100,000.
"""


class Solution:
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        magic = [1, 2, 2]
        p = 2
        s = 1
        while len(magic) < n:
            for _ in range(magic[p]):
                magic.append(s)
            s = 3 - s
            p += 1
        # print(magic)
        return magic[:n].count(1)


if __name__ == '__main__':
    sol = Solution().magicalString
    print(sol(6), '?= 3')
    print(sol(19), '?= 9')
    print(sol(10**5), '?= ??')
