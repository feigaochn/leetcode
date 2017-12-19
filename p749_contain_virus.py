class Solution:
    def containVirus(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        d4 = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        walls = set()
        nrows = len(grid)
        ncols = len(grid[0])

        def valid(r, c):
            return 0 <= r < nrows and 0 <= c < ncols

        def get_regions(grid):
            """
            Return list of tuple (contaminated, neighbor, boundry length)
            """
            regions = []
            for r in range(len(grid)):
                for c in range(len(grid[r])):
                    if grid[r][c] == 1:
                        cc = set()
                        frontier = {(r, c)}
                        neighbor = set()
                        boundry = set()
                        while frontier:
                            pr, pc = pos = frontier.pop()
                            grid[pr][pc] = 2
                            cc.add(pos)
                            for dr, dc in d4:
                                nr, nc = pr + dr, pc + dc
                                if valid(nr, nc):
                                    if grid[nr][nc] == 1:
                                        frontier.add((nr, nc))
                                    elif grid[nr][nc] == 0:
                                        if (pr, pc, nr, nc) not in walls:
                                            boundry.add(((pr, pc), (nr, nc)))
                                            boundry.add(((nr, nc), (pr, pc)))
                                            neighbor.add((nr, nc))
                        regions.append((cc, neighbor, boundry))
            for r in range(nrows):
                for c in range(ncols):
                    if grid[r][c] == 2:
                        grid[r][c] = 1
            return regions

        def night(grid):
            for r in range(nrows):
                for c in range(ncols):
                    if grid[r][c] != 1:
                        continue
                    for dr, dc in d4:
                        nr, nc = r + dr, c + dc
                        if (valid(nr, nc) and grid[nr][nc] == 0
                                and ((r, c), (nr, nc)) not in walls):
                            grid[nr][nc] = 2
            for r in range(nrows):
                for c in range(ncols):
                    if grid[r][c] == 2:
                        grid[r][c] = 1

        while True:
            regions = get_regions(grid)
            if not regions:
                # no more active affected area
                break
            # the one with most threaten area
            choose = max(regions, key=lambda t: len(t[1]))
            # mark the walled cells to -1
            for r, c in choose[0]:
                grid[r][c] = -1
            walls.update(choose[2])
            night(grid)

        return len(walls) // 2


fn = Solution().containVirus
print(
    fn([
        [0, 1, 0, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ]))
print(fn([
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1],
]))
print(
    fn([
        [1, 1, 1, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 0, 0, 0],
    ]))
