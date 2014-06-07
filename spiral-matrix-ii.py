# author: Fei Gao
#
# Spiral Matrix II
#
# Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
# For example,
# Given n = 3,
# You should return the following matrix:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]


class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        if n <= 0:
            return []
        grid = [[0 for i in range(n)] for _ in range(n)]
        r, c = 0, 0
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0
        for i in range(1, n**2 + 1):
            grid[r][c] = i
            dr, dc = direction[d%4]
            if r+dr < 0 or r+dr >= n or c+dc < 0 or c+dc >= n or grid[r+dr][c+dc] != 0:
                d += 1
            dr, dc = direction[d%4]
            r += dr
            c += dc
        return grid


def main():
    solver = Solution()
    for test in [3, 0, 1, 8]:
        print(test, ' -> ', solver.generateMatrix(test))
    pass


if __name__ == '__main__':
    main()
    pass
