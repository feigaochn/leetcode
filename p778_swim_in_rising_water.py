class Solution:
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        from math import inf
        height = len(grid)
        width = len(grid[0])

        elev = [[inf for c in r] for r in grid]
        elev[0][0] = grid[0][0]
        from collections import deque
        queue = deque()
        queue.append((0, 0))
        while queue:
            cr, cc = queue.popleft()
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < height and 0 <= nc < width:
                    ne = max(grid[nr][nc], elev[cr][cc])
                    if ne < elev[nr][nc]:
                        elev[nr][nc] = ne
                        queue.append((nr, nc))
        return elev[-1][-1]


sol = Solution().swimInWater

print(sol([[0, 2], [1, 3]]))
print(
    sol([
        [0, 1, 2, 3, 4],
        [24, 23, 22, 21, 5],
        [12, 13, 14, 15, 16],
        [11, 17, 18, 19, 20],
        [10, 9, 8, 7, 6],
    ]))
