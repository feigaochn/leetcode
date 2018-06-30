class Solution:
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        from bisect import bisect_left as bi
        rows = defaultdict(list)
        cols = defaultdict(list)
        for r, c in mines:
            rows[r].append(c)
            cols[c].append(r)
        for n in range(N):
            rows[n].extend([-1, N])
            rows[n].sort()
            cols[n].extend([-1, N])
            cols[n].sort()
        # print(rows, cols)
        k = 0
        for r in range(N):
            for c in range(N):
                ci = bi(rows[r], c)
                ri = bi(cols[c], r)
                # print(r, c, ri, ci)
                cur_k = min(r - cols[c][ri - 1], cols[c][ri] - r,
                            c - rows[r][ci - 1], rows[r][ci] - c)
                k = max(k, cur_k)
        return k


sol = Solution().orderOfLargestPlusSign

print(sol(5, [[4, 2]]))
print(sol(2, []))
print(sol(1, [[0, 0]]))

from random import randrange, seed
seed(42)
n = 500
print(sol(n, [[randrange(n), randrange(n)] for _ in range(5000)]))
