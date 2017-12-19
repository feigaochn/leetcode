class Solution:
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        size = len(grid)
        update = {((0, 0), (0, 0)): grid[0][0]}
        while update:
            print(update)
            last = update.copy()
            update = {}
            for (p1, p2), v in last.items():
                if p1 == p2 == (size - 1, size - 1):
                    return v
                for p1d in [(1, 0), (0, 1)]:
                    p1nr = p1[0] + p1d[0]
                    p1nc = p1[1] + p1d[1]
                    p1n = (p1nr, p1nc)
                    if not (0 <= p1nr < size and 0 <= p1nc < size
                            and grid[p1nr][p1nc] != -1):
                        continue
                    for p2d in [(1, 0), (0, 1)]:
                        p2nr = p2[0] + p2d[0]
                        p2nc = p2[1] + p2d[1]
                        p2n = (p2nr, p2nc)
                        if not (0 <= p2nr < size and 0 <= p2nc < size
                                and p1nr >= p2nr and grid[p2nr][p2nc] != -1):
                            continue
                        vn = v + grid[p1nr][p1nc] + grid[p2nr][p2nc] - (
                            p1n == p2n) * grid[p1nr][p1nc]
                        update[(p1n, p2n)] = max(update.get((p1n, p2n), 0), vn)
        return 0


fn = Solution().cherryPickup

print(fn([[0, 1, -1], [1, 0, -1], [1, 1, 1]]))
print(
    fn([
        [0, 1, 1, 0, 0],
        [1, 1, 1, 1, 0],
        [-1, 1, 1, 1, -1],
        [0, 1, 1, 1, 0],
        [1, 0, -1, 0, 0],
    ]))
