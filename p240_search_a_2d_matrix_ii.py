# coding: utf-8

# author: Fei Gao
#
# Search A 2d Matrix Ii

# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
# For example,
# Consider the following matrix:
# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# Given target = 5, return true.
# Given target = 20, return false.
# Subscribe to see which companies asked this question


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        def search(row1, row2, col1, col2):
            """Search target in sub matrix[row1:row2][col1:col2]"""
            # zero elements
            if row1 >= row2 or col1 >= col2:
                return False
            if matrix[row1][col1] == target:
                return True
            # target less than up-left corner
            if target < matrix[row1][col1]:
                return False
            # target greater than low-right corner
            if target > matrix[row2 - 1][col2 - 1]:
                return False
            row3 = (row1 + row2 + 1) // 2
            col3 = (col1 + col2 + 1) // 2
            # print(row1, row3, row2, col1, col3, col2)
            result = (search(row1, row3, col1, col3)
                      or search(row1, row3, col3, col2)
                      or search(row3, row2, col1, col3)
                      or search(row3, row2, col3, col2))
            # print(row1, row2, col1, col2, result)
            return result

        return search(0, len(matrix), 0, len(matrix[0]))


def main():
    solver = Solution()
    tests = [
        ([
             [1, 4, 7, 11, 15],
             [2, 5, 8, 12, 19],
             [3, 6, 9, 16, 22],
             [10, 13, 14, 17, 24],
             [18, 21, 23, 26, 30]
         ], 5),
        ([
             [1, 4, 7, 11, 15],
             [2, 5, 8, 12, 19],
             [3, 6, 9, 16, 22],
             [10, 13, 14, 17, 24],
             [18, 21, 23, 26, 30]
         ], 20)
    ]
    for test in tests:
        print(test)
        print(' ->')
        result = solver.searchMatrix(*test)
        print(result)
        print('~' * 10)
    pass


if __name__ == '__main__':
    main()
    pass
