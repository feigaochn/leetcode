class Solution:
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        area = 0
        rows = len(grid)
        cols = len(grid[0])
        for r in range(rows):
            for c in range(cols):
                v = grid[r][c]
                if v > 0:
                    area += 2
                if r > 0:
                    area += max(0, v - grid[r-1][c])
                else:
                    area += v
                if r + 1 < rows:
                    area += max(0, v - grid[r+1][c])
                else:
                    area += v
                if c - 1 >= 0:
                    area += max(0, v - grid[r][c-1])
                else:
                    area += v
                if c + 1 < cols:
                    area += max(0, v - grid[r][c+1])
                else:
                    area += v
        return area