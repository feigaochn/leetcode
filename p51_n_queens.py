# N-Queens
# Total Accepted: 8324 Total Submissions: 32665 My Submissions
#
# The n-queens puzzle is the problem of placing n queens on an n×n chessboard
# such that no two queens attack each other.
#
# Given an integer n, return all distinct solutions to the n-queens puzzle.
#
# Each solution contains a distinct board configuration of the n-queens'
# placement, where 'Q' and '.' both indicate a queen and an empty space
# respectively.
#
# For example,
# There exist two distinct solutions to the 4-queens puzzle:
#
# [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]


class Solution:
    # @return a list of lists of string

    def solveNQueens(self, n):
        self.solutions = []
        self.n = n
        self.recursiveSolve([], [], [])

        drawings = []
        for solution in self.solutions:
            drawings.append(self.drawSolutions(solution))

        return drawings

    def drawSolutions(self, solution):
        draw = []
        for r in range(self.n):
            draw.append('.' * solution[r] + 'Q' + '.' * (self.n - 1 - solution[r]))
        return draw

    def recursiveSolve(self, partial, diag, anti_diag):
        idx = len(partial)
        if idx == self.n:
            self.solutions.append(partial[:])
            return
        for val in range(self.n):
            if val not in partial \
                    and val - idx not in diag \
                    and val + idx not in anti_diag:
                partial.append(val)
                diag.append(val - idx)
                anti_diag.append(val + idx)
                self.recursiveSolve(partial, diag, anti_diag)
                partial.pop()
                diag.pop()
                anti_diag.pop()


if __name__ == '__main__':
    print(Solution().solveNQueens(4))
    print(Solution().solveNQueens(8))
