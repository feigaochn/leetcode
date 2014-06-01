# author: Fei Gao
#
# Minimum Path Sum
#
# Given a m x n grid filled with non-negative numbers, find a path from
# top left to bottom right which minimizes the sum of all numbers along
# its path.
# Note: You can only move either down or right at any point in time.


class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        # DP
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        n_row = len(grid)
        n_col = len(grid[0])
        dp = [[None for col in range(n_col)] for row in range(n_row)]
        for r in range(n_row):
            for c in range(n_col):
                if r == 0 and c > 0:  # first row: update from left
                    dp[r][c] = dp[r][c - 1] + grid[r][c]
                elif c == 0 and r > 0:  # first column: update from up
                    dp[r][c] = dp[r - 1][c] + grid[r][c]
                elif r > 0 and c > 0:  # update from min of left and up
                    dp[r][c] = min(dp[r - 1][c], dp[r][c - 1]) + grid[r][c]
                else:
                    dp[r][c] = grid[r][c]
        return dp[n_row - 1][n_col - 1]


def main():
    solver = Solution()
    import random

    for r in range(5):
        for c in range(5):
            grid = [[random.randrange(10) for _ in range(c)] for _ in range(r)]
            print(grid, solver.minPathSum(grid))
    pass


if __name__ == '__main__':
    main()
    pass
