# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: rectangle area
#
# Find the total area covered by two rectilinear rectangles in a 2D plane.
# Each rectangle is defined by its bottom left corner and top right corner as
# shown in the figure.
# 
# Assume that the total area is never beyond the maximum possible value of
# int.
# 
# Credits:Special thanks to @mithmatt for adding this problem, creating the
# above image and all test cases.
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Math


class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        assert A <= C and B <= D
        assert E <= G and F <= H
        x1, y1 = max(A, E), max(B, F)
        x2, y2 = min(C, G), min(D, H)
        area = (C - A) * (D - B) + (G - E) * (H - F)
        if x2 >= x1 and y2 >= y1:
            return area - (x2 - x1) * (y2 - y1)
        else:
            return area


def main():
    solver = Solution()
    tests = [
        (('param',), 'result'),
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.computeArea(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
