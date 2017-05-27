#!/usr/bin/env python2
# coding: utf-8

import sys


class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        if len(wall) < 1: return 0
        from collections import defaultdict

        marks = defaultdict(int)
        for row in wall:
            w = 0
            for m in row[:-1]:
                w += m
                marks[w] += 1

        height = best = len(wall)
        for gap in marks.values():
            if best > height - gap:
                best = height - gap
        return best


def main(args):
    sol = Solution()
    print(sol.leastBricks([[1, 2, 2, 1],
                           [3, 1, 2],
                           [1, 3, 2],
                           [2, 4],
                           [3, 1, 2],
                           [1, 3, 1, 1]]))
    return


if __name__ == '__main__':
    main(sys.argv[1:])
