# Search a 2D Matrix
#
# Total Accepted: 11690 Total Submissions: 38252 My Submissions
#
# Write an efficient algorithm that searches for a value in an m x n matrix.
# This matrix has the following properties:
#
# Integers in each row are sorted from left to right.
#
# The first integer of each row is greater than the last integer of the
# previous row.
#
# For example,
#
# Consider the following matrix:
#
# [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
#
# Given target = 3, return true.

import bisect


class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean

    def searchMatrix(self, matrix, target):
        if len(matrix) is 0 or len(matrix[0]) is 0:
            return False
        r, c = len(matrix), len(matrix[0])
        ger = bisect.bisect_left([row[0] for row in matrix], target)
        if ger is r:
            ger = ger-1
        if target < matrix[ger][0]:
            ger -= 1
        if ger < 0:
            return False
        gec = bisect.bisect_left(matrix[ger], target)
        if gec is c:
            gec = gec-1
        return target == matrix[ger][gec]
        pass

if __name__ == '__main__':
    matrix = [list(range(0, 4, 2)), list(range(4, 8, 2))]
    print(matrix)
    for target in range(-1, 8):
        print(target, Solution().searchMatrix(matrix, target))

    matrix = [[-i] for i in range(0, 7, 2)]
    matrix.reverse()
    print(matrix)
    for target in range(-8, 1):
        print(target, Solution().searchMatrix(matrix, target))
