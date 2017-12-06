# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: self crossing
#
#     You are given an array x of n positive numbers. You start at point (0,0)
# and moves x[0] metres to the north, then x[1] metres to the west,
#     x[2] metres to the south,
#     x[3] metres to the east and so on. In other words, after each move your
# direction changes
#     counter-clockwise.
# 
#     Write a one-pass algorithm with O(1) extra space to determine, if your
# path crosses itself, or not.
# 
# Example 1:
# 
# Given x = [2, 1, 1, 2],
# ┌───┐
# │   │
# └───┼──>
#     │
# 
# Return true (self crossing)
# 
# Example 2:
# 
# Given x = [1, 2, 3, 4],
# ┌──────┐
# │      │
# │
# │
# └────────────>
# 
# Return false (not self crossing)
# 
# Example 3:
# 
# Given x = [1, 1, 1, 1],
# ┌───┐
# │   │
# └───┼>
# 
# Return true (self crossing)
# 
# Credits:Special thanks to @dietpepsi for adding this problem and creating
# all test cases.
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Math

class Solution(object):
    def isSelfCrossing(self, x):
        """
        :type x: list[int]
        :rtype: bool
        """

        def between(v1, v2, v3):
            return v2 <= v1 <= v3 or v3 <= v1 <= v2

        from collections import deque
        pts = deque([0, 0, 0], maxlen=10)
        sign = [1, -1, -1, 1]
        for i, d in enumerate(x):
            pts.appendleft(d * sign[i % 4] + pts[1])
            if len(pts) > 5 and between(pts[4], pts[0], pts[2]) and between(pts[1], pts[3], pts[5]):
                return True
            if len(pts) > 7 and between(pts[6], pts[0], pts[2]) and between(pts[1], pts[7], pts[5]):
                return True
        # print(pts)
        return False


def main():
    solver = Solution()
    tests = [
        (([2],), False),
        (([2, 1, 1, 2],), True),
        (([1, 2, 3, 4],), False),
        (([1, 1, 1, 1],), True),
        (([1, 1, 2, 1, 1],), True),
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.isSelfCrossing(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
