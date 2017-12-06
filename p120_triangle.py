#!/bin/env python3

# author: Fei Gao
#
# Triangle
#
# Given a triangle, find the minimum path sum from top to bottom. Each step you
# may move to adjacent numbers on the row below.
# For example, given the following triangle
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
# Note:
# Bonus point if you are able to do this using only O(n) extra space, where n
# is the total number of rows in the triangle.


class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer

    def minimumTotal(self, triangle):
        size = len(triangle)
        dp = [[0] * size, [0] * size]
        dp[0][0] = triangle[0][0]
        for row in range(1, size):
            for col in range(row+1):
                dp[row % 2][col] = \
                    min(dp[1 - row % 2][max(0, col-1): min(col+1, row)]) \
                    + triangle[row][col]
            # print(row, dp[row%2])
        return min(dp[1 - size % 2])


def main():
    solver = Solution()
    tests = [[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]],
             [[11]],
             [[-1], [-2, -3]]]
    for test in tests:
        print(test)
        print(' ->')
        result = solver.minimumTotal(test)
        print(result)
        print('~'*10)


if __name__ == '__main__':
    main()
