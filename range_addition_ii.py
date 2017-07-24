#!/usr/bin/env python
# coding: utf-8


class Solution:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        w, h = m, n
        for x, y in ops:
            w = min(x, w)
            h = min(y, h)

        return w * h


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxCount(3, 3, [[2, 2], [3, 3]]))
