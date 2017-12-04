"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's
(representing land) connected 4-directionally (horizontal or vertical.) You may
assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no
island, the maximum area is 0.)
"""


class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_area = 0
        for ir in range(len(grid)):
            for ic in range(len(grid[0])):
                if grid[ir][ic] == 1:
                    queue = []

                    grid[ir][ic] = -1
                    area = 1
                    queue.append((ir, ic))

                    while queue:
                        r, c = queue.pop()
                        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            if (0 <= r + dr < len(grid)
                                    and 0 <= c + dc < len(grid[0])
                                    and grid[r + dr][c + dc] == 1):
                                grid[r + dr][c + dc] = -1
                                area += 1
                                queue.append((r + dr, c + dc))
                    max_area = max(max_area, area)
        return max_area


def main():
    sol = Solution().maxAreaOfIsland
    print(
        sol([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0,
              0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0,
                   0], [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
                        0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
             [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0,
              0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0,
                   0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]), '?= 6')
    print(sol([[1, 1, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [0, 0, 0, 1, 1],
             [0, 0, 0, 1, 1]]), '?= 4')


if __name__ == '__main__':
    main()
