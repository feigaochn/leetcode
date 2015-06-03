# author: Fei Gao
# date: Sat May 31 13:19:23 2014
#
# Spiral matrix
#
# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
# For example,
# Given the following matrix:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# You should return [1,2,3,6,9,8,7,4,5].


class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers

    def spiralOrder(self, matrix):
        result = []
        rows = len(matrix)
        if rows == 0:
            return result
        columns = len(matrix[0])
        if columns == 0:
            return result
        steps = 0
        while rows > 0 and columns > 0:
            steps_mod = steps % 4
            # print("Before Steps: ", steps, matrix, result)
            if steps_mod == 0:  # up
                result += matrix.pop(0)
                rows -= 1
            elif steps_mod == 1:  # right
                result += [row.pop() for row in matrix]
                columns -= 1
            elif steps_mod == 2:  # down
                result += matrix.pop()[::-1]
                rows -= 1
            elif steps_mod == 3:  # left
                result += [row.pop(0) for row in matrix][::-1]
                columns -= 1
            # print("After Steps: ", steps, matrix, result)
            steps += 1
        return result
        pass

if __name__ == '__main__':
    nums = list(range(100))
    for r in range(4, 8):
        for c in range(4, 8):
            matrix = [nums[c*j:c*(j+1)] for j in range(r)]
            print('-'*20)
            for row in matrix:
                print(row)
            print("Solution: ", Solution().spiralOrder(matrix))
    pass
