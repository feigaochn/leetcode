# You have a list of points in the plane. Return the area of the largest
# triangle that can be formed by any 3 of the points.

# Example:
# Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
# Output: 2
# Explanation: The five points are show in the figure below. The red triangle
# is the largest.

# Notes:
#     3 <= points.length <= 50.
#     No points will be duplicated.
#      -50 <= points[i][j] <= 50.
#     Answers within 10^-6 of the true value will be accepted as correct.


class Solution:

    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        from math import sqrt

        def dist(p1, p2):
            return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

        def area(d1, d2, d3):
            h = (d1 + d2 + d3) / 2.0
            return sqrt(abs(h * (h - d1) * (h - d2) * (h - d3)))

        max_area = 0
        n = len(points)
        for i in range(n):
            p1 = points[i]
            for j in range(i + 1, n):
                p2 = points[j]
                for k in range(j + 1, n):
                    p3 = points[k]
                    d1 = dist(p1, p2)
                    d2 = dist(p2, p3)
                    d3 = dist(p3, p1)
                    a = area(d1, d2, d3)
                    if a > max_area:
                        max_area = a

        return max_area


sol = Solution().largestTriangleArea
print(sol([[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]), 2)
