class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        if matrix is None:
            return None

        # all rows have same length
        assert(len(set([len(row) for row in matrix])) == 1)

        if len(matrix) == len(matrix[0]):
            # inplace rotate if square shape
            n = len(matrix)
            # 1. flip over diagonal
            for i in range(n):
                for j in range(i+1, n):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            # 2. flip each row
            for i in range(n):
                matrix[i].reverse()
            return matrix
        else:
            # return new object
            rows = len(matrix)
            cols = len(matrix[0])
            result = [[None for i in range(rows)] for j in range(cols)]
            for i in range(rows):
                for j in range(cols):
                    result[j][rows-1-i] = matrix[i][j]
            return result


def test():
    mat1 = [list(range(10)), list(range(10,20))]
    print(mat1)
    print(Solution().rotate(mat1))
    mat2 = [list(range(4*i,4*i+4)) for i in range(4)]
    print(mat2)
    print(Solution().rotate(mat2))

if __name__ == '__main__':
    test()