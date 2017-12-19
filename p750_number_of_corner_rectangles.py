class Solution:
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = []
        for row in grid:
            rows.append(set([i for i, v in enumerate(row) if v == 1]))
        recs = 0
        for i in range(len(rows)):
            for j in range(i + 1, len(rows)):
                inter = len(rows[i] & rows[j])
                recs += (inter - 1) * inter // 2
        return recs


fn = Solution().countCornerRectangles

print(
    fn([
        [1, 0, 0, 1, 0],
        [0, 0, 1, 0, 1],
        [0, 0, 0, 1, 0],
        [1, 0, 1, 0, 1],
    ]))
print(fn([[1, 1, 1], [1, 1, 1], [1, 1, 1]]))
print(fn([[1, 1, 1, 1]]))
