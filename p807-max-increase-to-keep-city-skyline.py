class Solution:

    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        side_view = [max(row) for row in grid]
        top_view = [max(col) for col in zip(*grid)]
        increase = 0
        for r, row in enumerate(grid):
            for c, h in enumerate(row):
                increase += min(side_view[r], top_view[c]) - h
        return increase


sol = Solution().maxIncreaseKeepingSkyline
grid = [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]

print(sol(grid))
