# coding: utf-8

# author: Fei Gao
#
# Range Sum Query 2d Immutable

# Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
# The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.
# Example:
# Given matrix = [
#   [3, 0, 1, 4, 2],
#   [5, 6, 3, 2, 1],
#   [1, 2, 0, 1, 5],
#   [4, 1, 0, 1, 7],
#   [1, 0, 3, 0, 5]
# ]
# sumRegion(2, 1, 4, 3) -> 8
# sumRegion(1, 1, 2, 2) -> 11
# sumRegion(1, 2, 2, 4) -> 12
# Note:
# You may assume that the matrix does not change.
# There are many calls to sumRegion function.
# You may assume that row1 &le; row2 and col1 &le; col2.
# Subscribe to see which companies asked this question


class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            self._sums = None
        else:
            num_rows, num_cols = len(matrix), len(matrix[0])
            self._sums = [[0 for c in range(num_cols + 1)] for r in range(num_rows + 1)]
            for r in range(num_rows):
                for c in range(num_cols):
                    self._sums[r + 1][c + 1] = matrix[r][c] + self._sums[r][c + 1] + \
                                               self._sums[r + 1][c] - self._sums[r][c]

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if self._sums:
            return (self._sums[row2 + 1][col2 + 1] + self._sums[row1][col1]
                    - self._sums[row1][col2 + 1] - self._sums[row2 + 1][col1])
        else:
            return 0


# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)


def main():
    solver = NumMatrix([
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ])
    # sumRegion(2, 1, 4, 3) -> 8
    # sumRegion(1, 1, 2, 2) -> 11
    # sumRegion(1, 2, 2, 4) -> 12
    tests = [
        (2, 1, 4, 3),  # 8
        (1, 1, 2, 2),  # 11
        (1, 2, 2, 4),  # 12
    ]
    for test in tests:
        print(test)
        print(' ->')
        result = solver.sumRegion(*test)
        print(result)
        print('~' * 10)
    pass


if __name__ == '__main__':
    main()
    pass
