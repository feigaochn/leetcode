class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        from heapq import heappush, heappop

        frontier = [(matrix[0][0], 0, 0)]
        chosen = []
        while len(chosen) < k:
            value, r, c = heappop(frontier)
            chosen.append(value)
            if r + 1 < len(matrix) and (matrix[r + 1][c], r + 1,
                                        c) not in frontier:
                heappush(frontier, (matrix[r + 1][c], r + 1, c))
            if c + 1 < len(matrix[0]) and (matrix[r][c + 1], r,
                                           c + 1) not in frontier:
                heappush(frontier, (matrix[r][c + 1], r, c + 1))
        return chosen[-1]


fn = Solution().kthSmallest

for k in range(9):
    print(fn(
        [[1, 5, 9], [10, 11, 13], [12, 13, 15]],
        k+1,
    ))
