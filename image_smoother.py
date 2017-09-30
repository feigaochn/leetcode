#!/usr/bin/env python
# coding: utf-8

# p661

class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        if not M or not M[0]:
            return M
        rows = len(M)
        cols = len(M[0])

        def go(r, c):
            val, count = 0, 0
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if 0 <= r + dr < rows and 0 <= c + dc < cols:
                        val += M[r + dr][c + dc]
                        count += 1
            return val, count

        S = [[0 for _ in range(cols)] for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                val, count = go(i, j)
                S[i][j] = val // count
        return S


if __name__ == '__main__':
    sol = Solution()
    print(sol.imageSmoother([[1, 1, 1],
                             [1, 0, 1],
                             [1, 1, 1]]))
