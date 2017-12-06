# author: Fei Gao
#
# Max Points On A Line
#
# Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

import collections


# Definition for a point
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

    def __repr__(self):
        return repr((self.x, self.y))


class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        zero = lambda x, y: abs(x - y) < 1e-6

        # counting duplicate points
        points_count = collections.defaultdict(int)
        for p in points:
            for pp in points_count:
                if zero(p.x, pp.x) and zero(p.y, pp.y):
                    points_count[pp] += 1
                    break
            else:
                points_count[p] += 1
        # print(points_count)
        pts = points_count.keys()
        if len(pts) < 2:
            return len(points)

        # calc lines: y = k * x + d
        # ratio[(k, d)] = set of indices of points on this line
        # (None, z) is the vertical line x = z
        ratio = collections.defaultdict(set)
        for i1 in range(len(pts)):
            p1 = pts[i1]
            for i2 in range(i1):
                p2 = pts[i2]
                if zero(p1.x, p2.x):
                    # vertical
                    k, d = None, p1.x
                else:
                    k = (p1.y - p2.y) / float(p1.x - p2.x)
                    d = p1.y - k * p1.x
                ratio[(k, d)].add(i1)
                ratio[(k, d)].add(i2)
        # print([pts[i] for i in max(ratio.values(), key=len)])
        return max(sum(points_count[pts[i]] for i in ratio[(k, d)]) for k, d in ratio)


def main():
    solver = Solution()
    tests = [[Point(0, 0), Point(1, 1), Point(3, 3), Point(1, 1), Point(0, 1)],
             [Point(0, 0)],
             [Point(0, 0), Point(0, 0)],
             [Point(a, b) for a, b in
              sorted([(40, -23), (9, 138), (429, 115), (50, -17), (-3, 80), (-10, 33), (5, -21), (-3, 80), (-6, -65),
               (-18, 26), (-6, -65), (5, 72), (0, 77), (-9, 86), (10, -2), (-8, 85), (21, 130), (18, -6), (-18, 26),
               (-1, -15), (10, -2), (8, 69), (-4, 63), (0, 3), (-4, 40), (-7, 84), (-8, 7), (30, 154), (16, -5),
               (6, 90), (18, -6), (5, 77), (-4, 77), (7, -13), (-1, -45), (16, -5), (-9, 86), (-16, 11), (-7, 84),
               (1, 76), (3, 77), (10, 67), (1, -37), (-10, -81), (4, -11), (-20, 13), (-10, 77), (6, -17), (-27, 2),
               (-10, -81), (10, -1), (-9, 1), (-8, 43), (2, 2), (2, -21), (3, 82), (8, -1), (10, -1), (-9, 1),
               (-12, 42), (16, -5), (-5, -61), (20, -7), (9, -35), (10, 6), (12, 106), (5, -21), (-5, 82), (6, 71),
               (-15, 34), (-10, 87), (-14, -12), (12, 106), (-5, 82), (-46, -45), (-4, 63), (16, -5), (4, 1), (-3, -53),
               (0, -17), (9, 98), (-18, 26), (-9, 86), (2, 77), (-2, -49), (1, 76), (-3, -38), (-8, 7), (-17, -37),
               (5, 72), (10, -37), (-4, -57), (-3, -53), (3, 74), (-3, -11), (-8, 7), (1, 88), (-12, 42), (1, -37),
               (2, 77), (-6, 77), (5, 72), (-4, -57), (-18, -33), (-12, 42), (-9, 86), (2, 77), (-8, 77), (-3, 77),
               (9, -42), (16, 41), (-29, -37), (0, -41), (-21, 18), (-27, -34), (0, 77), (3, 74), (-7, -69), (-21, 18),
               (27, 146), (-20, 13), (21, 130), (-6, -65), (14, -4), (0, 3), (9, -5), (6, -29), (-2, 73), (-1, -15),
               (1, 76), (-4, 77), (6, -29)])]
    ]
    for test in tests:
        print(test)
        print(' ->')
        result = solver.maxPoints(test)
        print(result)
        print('~' * 10)
    pass


if __name__ == '__main__':
    main()
    pass
