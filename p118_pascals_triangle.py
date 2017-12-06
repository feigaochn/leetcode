# author: Fei Gao
#
# Pascals Triangle
#
# Given numRows, generate the first numRows of Pascal's triangle.
# For example, given numRows = 5,
# Return
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]


class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows < 1:
            return []
        elif numRows == 1:
            return [[1]]
        pascal = [[1]]
        for row in range(numRows - 1):
            pascal.append([1] + [pascal[-1][i] + pascal[-1][i+1] for i in range(len(pascal[-1])-1)] + [1])
        return pascal


def main():
    solver = Solution()
    tests = [5, 1, 2, 3, 10]
    for test in tests:
        print(test)
        print(' ->')
        result = solver.generate(test)
        print(result)
        print('~'*10)
    pass


if __name__ == '__main__':
    main()
    pass
