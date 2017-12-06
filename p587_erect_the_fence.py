#!/usr/bin/env python3
# coding: utf-8

import sys


class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

    def __repr__(self):
        return "({}, {})".format(self.x, self.y)


class Solution(object):
    def outerTrees(self, points):
        """
        :type points: List[Point]
        :rtype: List[Point]
        """

        def ccw(p1, p2, p3):
            return (p2.x - p1.x) * (p3.y - p1.y) >= (p2.y - p1.y) * (p3.x - p1.x)

        points.sort(key=(lambda p1: (p1.x, p1.y)))

        hull = []

        for pt in points:
            while len(hull) >= 2 and not ccw(hull[-2], hull[-1], pt):
                hull.pop()
            if pt not in hull:
                hull.append(pt)

        i, t = len(points) - 2, len(hull) + 1
        while i >= 0:
            pt = points[i]
            while len(hull) >= t and not ccw(hull[-2], hull[-1], pt):
                hull.pop()
            if pt not in hull:
                hull.append(pt)
            i -= 1
        return hull


def main(args):
    sol = Solution()
    print(sol.outerTrees([Point(a, b) for a, b in [[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]]]))
    print(sol.outerTrees([Point(a, b) for a, b in [[1, 2], [2, 2], [4, 2]]]))
    print(sol.outerTrees([Point(a, b) for a, b in [[2, 1], [2, 2], [2, 4]]]))
    print(sol.outerTrees([Point(a, b) for a, b in [[1, 2], [2, 1]]]))
    print(sol.outerTrees([Point(a, b) for a, b in [[1, 2]]]))
    return


if __name__ == '__main__':
    main(sys.argv[1:])
