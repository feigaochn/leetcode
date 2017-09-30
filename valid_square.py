#!/usr/bin/env python
# coding: utf-8


class Solution:
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        pts = [p1, p2, p3, p4]

        dists = []
        for i in range(len(pts)):
            for j in range(i + 1, len(pts)):
                dists.append((pts[i][0] - pts[j][0]) ** 2
                             + (pts[i][1] - pts[j][1]) ** 2)
        dists.sort()
        if (dists[0] == dists[3] and dists[-2] == dists[-1]
            and dists[0] != dists[-1]
            and dists[0] * 2 == dists[-1]):
            return True
        else:
            return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.validSquare(p1=[0, 0], p2=[1, 1], p3=[1, 0], p4=[0, 1]))
    print(sol.validSquare(p1=[0, 0], p2=[1, 3], p3=[-1, 2], p4=[2, 1]))
