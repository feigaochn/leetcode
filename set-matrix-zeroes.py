#!/bin/env python3

# author: Fei Gao
#
# Set Matrix Zeroes
#
# Given a m x n matrix, if an element is 0, set its entire row and column to 0.
# Do it in place.
# click to show follow up.
# Follow up:
# Did you use extra space?
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?


class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.

    def setZeroes(self, matrix):
        num_row = len(matrix)
        num_col = len(matrix[0])
        for row in range(num_row):
            for col in range(num_col):
                if matrix[row][col] == 0:
                    # same row, before
                    for i in range(col):
                        matrix[row][i] = 0
                    # same row, after
                    for i in range(col+1, num_col):
                        if matrix[row][i] != 0:
                            matrix[row][i] = None
                    # same col, before
                    for i in range(row):
                        matrix[i][col] = 0
                    # same col, after
                    for i in range(row+1, num_row):
                        if matrix[i][col] != 0:
                            matrix[i][col] = None
                elif matrix[row][col] == None:
                    matrix[row][col] = 0
        return matrix


def main():
    solver = Solution()
    tests = [[[1,0],[1,1]]]
    for test in tests:
        print(test)
        print(' ->')
        result = solver.setZeroes(test)
        print(result)
        print('~'*10)
    pass
if __name__ == '__main__':
    main()
    pass
