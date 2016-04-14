# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: longest increasing path in a matrix
#
# Given an integer matrix, find the length of the longest increasing path.
# 
# From each cell, you can either move to four directions: left, right, up or
# down. You may NOT move diagonally or move outside of the boundary (i.e.
# wrap-around is not allowed).
# 
# Example 1:
# 
# nums = [
#   [9,9,4],
#   [6,6,8],
#   [2,1,1]
# ]
# 
# Return 4
# 
# The longest increasing path is [1, 2, 6, 9].
# 
# Example 2:
# 
# nums = [
#   [3,4,5],
#   [3,2,6],
#   [2,2,1]
# ]
# 
# Return 4
# 
# The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not
# allowed.
# Credits:Special thanks to @dietpepsi for adding this problem and creating
# all test cases.
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Depth-first Search
# Topological Sort
# Memoization


class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        n_rows, n_cols = len(matrix), len(matrix[0])

        def _nbs(r, c):
            if r > 0:
                yield ((r - 1, c))
            if r < n_rows - 1:
                yield ((r + 1, c))
            if c > 0:
                yield ((r, c - 1))
            if c < n_cols - 1:
                yield ((r, c + 1))

        from collections import defaultdict
        nbs = defaultdict(list)
        distances = defaultdict(int)
        frontier = []
        for r in range(n_rows):
            for c in range(n_cols):
                v = matrix[r][c]
                small = True
                for nr, nc in _nbs(r, c):
                    nv = matrix[nr][nc]
                    if v < nv:
                        nbs[(r, c)].append((nr, nc))
                    elif v > nv:
                        small = False
                if small:
                    distances[(r, c)] = 1
                    frontier.append((r, c))

        while frontier:
            r, c = frontier.pop()
            d = distances[(r, c)]
            for nr, nc in nbs[(r, c)]:
                if d + 1 > distances[(nr, nc)]:
                    frontier.append((nr, nc))
                    distances[(nr, nc)] = d + 1

        return max(distances.values())


def main():
    solver = Solution()
    tests = [
        (([
              [9, 9, 4],
              [6, 6, 8],
              [2, 1, 1]
          ],), '4'),
        (([
              [3, 4, 5],
              [3, 2, 6],
              [2, 2, 1]
          ],), '4'),
        (([
              [6, 11, 8, 10, 5, 16, 15, 19, 15, 11, 18, 1, 14, 14, 1, 3, 12, 16, 13, 19, 13, 14, 18, 10, 7, 4, 3, 17, 2,
               19, 2, 18, 14, 14, 19, 8, 8, 10],
              [13, 6, 7, 15, 14, 12, 1, 12, 9, 7, 13, 16, 18, 7, 15, 11, 1, 16, 18, 5, 19, 2, 10, 1, 6, 15, 11, 18, 19,
               10,
               10, 12, 15, 5, 7, 5, 15, 0],
              [19, 4, 18, 13, 13, 18, 2, 13, 1, 8, 9, 17, 13, 13, 14, 10, 0, 17, 4, 19, 8, 0, 16, 8, 6, 0, 11, 1, 17, 2,
               14, 1, 2, 16, 18, 17, 8, 0],
              [12, 1, 12, 1, 11, 1, 3, 10, 1, 14, 11, 13, 3, 11, 12, 3, 8, 11, 9, 14, 2, 5, 4, 16, 18, 16, 15, 17, 10,
               6,
               4, 16, 12, 4, 12, 17, 9, 19],
              [8, 19, 19, 8, 8, 9, 17, 19, 9, 18, 2, 14, 3, 13, 5, 15, 8, 1, 4, 12, 1, 1, 18, 18, 18, 8, 15, 0, 8, 0,
               16,
               9, 4, 4, 17, 6, 3, 6],
              [16, 11, 2, 11, 19, 18, 7, 2, 10, 5, 17, 15, 14, 17, 2, 12, 18, 19, 3, 15, 17, 11, 9, 19, 4, 1, 19, 9, 10,
               12, 11, 4, 14, 6, 3, 0, 1, 18],
              [14, 16, 14, 8, 0, 8, 7, 19, 6, 2, 14, 14, 2, 12, 16, 9, 19, 14, 17, 16, 14, 2, 2, 4, 17, 14, 1, 13, 1, 7,
               4,
               14, 16, 12, 5, 4, 3, 14],
              [8, 11, 15, 5, 17, 18, 11, 9, 18, 16, 6, 4, 3, 9, 7, 3, 2, 8, 17, 9, 2, 8, 18, 11, 3, 2, 16, 14, 6, 5, 8,
               15,
               11, 4, 19, 12, 13, 1],
              [10, 13, 3, 18, 17, 10, 10, 14, 0, 8, 6, 11, 6, 12, 13, 3, 16, 15, 2, 14, 7, 12, 3, 10, 14, 5, 0, 14, 14,
               5,
               1, 5, 11, 19, 18, 19, 12, 15],
              [13, 17, 8, 14, 0, 18, 5, 3, 10, 10, 10, 5, 13, 7, 16, 5, 19, 16, 17, 6, 2, 2, 18, 12, 12, 11, 3, 17, 19,
               13,
               5, 11, 6, 15, 19, 11, 2, 3],
              [6, 4, 17, 0, 16, 4, 9, 4, 0, 19, 1, 15, 9, 5, 1, 11, 1, 10, 15, 19, 8, 6, 7, 6, 14, 16, 7, 16, 9, 0, 16,
               8,
               12, 12, 14, 6, 2, 0],
              [6, 14, 7, 2, 15, 3, 14, 17, 10, 9, 3, 7, 15, 8, 16, 10, 1, 13, 3, 19, 10, 4, 15, 17, 9, 4, 0, 14, 9, 12,
               8,
               1, 15, 19, 1, 19, 3, 7],
              [13, 0, 0, 12, 5, 14, 18, 19, 10, 5, 6, 10, 14, 3, 5, 10, 19, 2, 13, 8, 2, 11, 5, 2, 11, 19, 16, 1, 13,
               10,
               2, 13, 4, 13, 19, 1, 15, 3],
              [13, 17, 10, 7, 5, 2, 1, 6, 9, 19, 11, 12, 1, 19, 17, 2, 16, 12, 17, 14, 18, 0, 4, 6, 0, 7, 17, 0, 0, 7,
               5,
               19, 0, 19, 16, 16, 14, 12],
              [16, 8, 2, 15, 18, 13, 0, 1, 2, 12, 8, 1, 12, 13, 4, 2, 13, 12, 1, 13, 11, 16, 18, 2, 14, 6, 7, 8, 16, 8,
               18,
               16, 16, 18, 4, 18, 12, 14],
              [14, 14, 0, 4, 2, 2, 7, 14, 2, 1, 13, 3, 9, 9, 14, 15, 10, 2, 15, 3, 14, 11, 15, 19, 0, 18, 5, 3, 3, 11,
               5,
               4, 12, 3, 5, 16, 7, 11],
              [14, 4, 17, 8, 4, 7, 12, 13, 7, 8, 11, 8, 4, 3, 8, 11, 4, 1, 1, 11, 7, 8, 19, 0, 5, 1, 14, 15, 19, 4, 1,
               15,
               5, 12, 1, 19, 13, 10],
              [6, 7, 12, 19, 14, 19, 0, 9, 3, 9, 14, 14, 16, 18, 5, 17, 12, 15, 1, 15, 14, 2, 18, 9, 9, 8, 9, 4, 8, 7,
               1,
               9, 14, 9, 2, 8, 14, 0],
              [0, 6, 9, 17, 19, 18, 13, 15, 0, 5, 13, 9, 15, 12, 6, 8, 19, 11, 7, 16, 16, 17, 12, 11, 16, 15, 2, 3, 18,
               3,
               7, 17, 7, 1, 4, 6, 7, 17],
              [5, 11, 0, 4, 16, 9, 9, 10, 10, 18, 6, 17, 15, 12, 0, 19, 5, 3, 2, 1, 0, 15, 11, 0, 2, 12, 18, 15, 14, 5,
               0,
               7, 7, 13, 4, 7, 7, 17],
              [10, 15, 5, 15, 19, 7, 17, 8, 8, 6, 10, 16, 18, 10, 18, 3, 1, 15, 2, 8, 17, 7, 0, 11, 7, 16, 0, 5, 5, 10,
               15,
               7, 10, 1, 15, 0, 13, 2],
              [0, 15, 16, 10, 15, 17, 16, 0, 14, 8, 16, 12, 11, 2, 16, 18, 19, 5, 13, 4, 7, 3, 2, 0, 13, 8, 14, 6, 5,
               11,
               17, 2, 18, 14, 12, 3, 13, 6],
              [10, 3, 5, 14, 5, 15, 14, 4, 18, 7, 17, 10, 1, 4, 8, 8, 17, 10, 3, 12, 16, 16, 10, 10, 6, 6, 17, 17, 1,
               14,
               7, 3, 6, 12, 19, 5, 18, 13],
              [7, 0, 0, 3, 3, 13, 7, 18, 4, 7, 7, 11, 6, 18, 6, 6, 11, 12, 5, 3, 3, 8, 17, 13, 6, 5, 4, 10, 0, 4, 1, 0,
               9,
               14, 1, 10, 0, 9],
              [11, 11, 10, 4, 7, 15, 14, 19, 10, 7, 19, 14, 2, 8, 10, 11, 6, 17, 12, 18, 6, 10, 8, 16, 9, 5, 8, 12, 14,
               19,
               10, 15, 9, 4, 19, 12, 11, 4],
              [11, 4, 2, 13, 14, 10, 13, 14, 11, 17, 7, 3, 8, 13, 18, 16, 3, 13, 10, 4, 0, 4, 15, 6, 4, 3, 5, 19, 2, 2,
               0,
               19, 8, 6, 1, 7, 13, 14],
              [9, 16, 6, 12, 12, 13, 8, 15, 16, 15, 9, 3, 12, 5, 14, 13, 0, 8, 17, 8, 0, 1, 11, 2, 13, 15, 11, 4, 4, 1,
               3,
               2, 10, 19, 3, 6, 13, 13],
              [4, 6, 2, 0, 10, 6, 11, 17, 2, 0, 16, 1, 3, 16, 17, 19, 19, 4, 3, 6, 7, 1, 17, 18, 13, 8, 18, 14, 18, 19,
               18,
               1, 8, 1, 14, 14, 9, 9],
              [8, 6, 11, 0, 15, 8, 0, 17, 19, 15, 10, 13, 14, 4, 15, 8, 1, 4, 10, 2, 15, 6, 19, 17, 11, 2, 5, 16, 8, 17,
               16, 5, 5, 17, 1, 1, 7, 2],
              [2, 0, 0, 3, 6, 0, 2, 10, 9, 14, 5, 18, 18, 3, 2, 11, 2, 6, 9, 1, 15, 12, 13, 14, 17, 6, 0, 19, 0, 3, 6,
               14,
               7, 13, 0, 17, 17, 5],
              [6, 15, 7, 19, 8, 12, 14, 8, 6, 8, 3, 7, 15, 13, 5, 4, 1, 13, 13, 16, 4, 10, 13, 14, 13, 17, 8, 3, 5, 7,
               7,
               8, 3, 8, 10, 14, 2, 2],
              [9, 3, 4, 13, 13, 8, 13, 13, 11, 4, 16, 13, 4, 10, 17, 4, 16, 3, 3, 2, 9, 7, 12, 0, 11, 6, 4, 5, 6, 1, 3,
               8,
               16, 18, 16, 19, 6, 5],
              [15, 7, 5, 4, 9, 15, 18, 10, 19, 3, 12, 9, 5, 2, 18, 1, 2, 11, 1, 10, 14, 17, 7, 10, 19, 2, 6, 1, 9, 18,
               16,
               13, 1, 1, 12, 5, 17, 10],
              [15, 10, 2, 17, 1, 13, 15, 0, 15, 17, 6, 2, 6, 1, 5, 8, 1, 14, 3, 8, 7, 18, 0, 17, 16, 10, 19, 1, 0, 18,
               0,
               15, 7, 14, 19, 16, 8, 10],
              [16, 9, 3, 11, 12, 11, 13, 1, 16, 0, 16, 16, 1, 6, 4, 15, 9, 8, 10, 18, 2, 18, 16, 15, 5, 18, 10, 8, 1,
               10,
               4, 19, 17, 12, 16, 6, 0, 8],
              [14, 16, 16, 10, 12, 6, 3, 8, 8, 11, 19, 12, 15, 9, 9, 11, 0, 1, 13, 6, 4, 10, 0, 13, 1, 15, 10, 2, 5, 15,
               18, 8, 14, 9, 1, 4, 8, 14],
              [4, 10, 16, 3, 19, 13, 1, 17, 7, 6, 0, 3, 3, 11, 12, 9, 8, 15, 0, 19, 10, 18, 1, 6, 7, 15, 9, 9, 6, 18, 2,
               5,
               4, 12, 7, 1, 1, 2],
              [4, 12, 10, 14, 18, 17, 0, 6, 8, 1, 13, 3, 8, 1, 6, 5, 5, 15, 9, 5, 13, 11, 16, 19, 4, 3, 19, 11, 14, 15,
               16,
               8, 2, 16, 10, 15, 3, 3],
              [4, 6, 6, 10, 19, 5, 2, 0, 14, 11, 10, 14, 14, 13, 13, 15, 3, 4, 8, 16, 2, 13, 11, 4, 13, 14, 18, 18, 13,
               1,
               17, 10, 15, 4, 16, 4, 15, 8],
              [1, 9, 1, 11, 18, 6, 13, 1, 18, 5, 10, 0, 4, 7, 15, 7, 1, 13, 16, 13, 8, 13, 4, 8, 3, 17, 4, 8, 8, 18, 19,
               2,
               5, 14, 12, 1, 10, 8],
              [2, 8, 18, 10, 10, 16, 1, 5, 0, 5, 1, 1, 8, 0, 11, 16, 16, 15, 14, 0, 16, 9, 19, 17, 13, 6, 11, 9, 18, 15,
               6,
               8, 13, 2, 13, 16, 11, 15],
              [11, 10, 8, 0, 14, 0, 18, 12, 17, 14, 12, 16, 9, 7, 6, 4, 9, 1, 16, 16, 7, 17, 13, 2, 18, 2, 14, 15, 1, 2,
               0,
               10, 2, 14, 19, 14, 1, 10],
              [5, 9, 16, 16, 4, 18, 4, 7, 7, 8, 6, 5, 4, 16, 3, 15, 6, 4, 18, 17, 6, 3, 4, 1, 10, 5, 14, 8, 13, 12, 16,
               12,
               11, 10, 5, 18, 12, 17],
              [0, 11, 11, 10, 10, 15, 9, 9, 1, 10, 12, 9, 1, 18, 0, 14, 10, 7, 9, 19, 15, 6, 11, 3, 6, 17, 13, 7, 8, 3,
               0,
               13, 13, 16, 13, 9, 0, 1],
              [0, 17, 13, 6, 1, 8, 1, 9, 7, 8, 2, 19, 12, 0, 9, 2, 7, 13, 16, 17, 18, 13, 17, 9, 16, 7, 5, 4, 2, 5, 6,
               16,
               15, 3, 18, 15, 18, 14],
              [16, 10, 1, 5, 8, 9, 16, 5, 19, 16, 19, 12, 5, 12, 8, 4, 12, 14, 17, 13, 14, 1, 10, 0, 3, 4, 16, 15, 0, 6,
               11, 2, 0, 17, 18, 13, 5, 10],
              [4, 14, 11, 14, 5, 6, 18, 15, 0, 15, 13, 11, 6, 8, 8, 15, 5, 4, 18, 16, 18, 5, 12, 10, 15, 1, 19, 13, 4,
               5,
               5, 0, 2, 6, 15, 19, 3, 1],
              [6, 9, 6, 14, 12, 8, 7, 16, 18, 8, 2, 1, 1, 14, 17, 5, 5, 3, 19, 6, 18, 7, 8, 3, 2, 6, 7, 1, 17, 14, 13,
               19,
               13, 19, 9, 18, 9, 0],
              [4, 5, 12, 14, 9, 0, 18, 8, 5, 3, 4, 5, 18, 10, 5, 11, 19, 16, 2, 13, 10, 16, 3, 12, 17, 6, 0, 7, 6, 11,
               3,
               16, 17, 11, 15, 8, 0, 4],
              [6, 3, 10, 8, 8, 17, 13, 13, 16, 1, 8, 4, 5, 15, 9, 15, 10, 4, 4, 9, 6, 19, 12, 16, 8, 1, 2, 7, 10, 2, 9,
               18,
               17, 14, 9, 14, 17, 6],
              [16, 6, 19, 4, 11, 3, 17, 15, 5, 17, 18, 0, 7, 19, 8, 6, 16, 2, 14, 0, 16, 11, 14, 1, 16, 1, 11, 19, 9,
               10,
               0, 16, 7, 17, 2, 10, 8, 14],
              [1, 17, 18, 3, 11, 14, 9, 18, 1, 17, 2, 12, 14, 4, 13, 4, 14, 0, 15, 18, 4, 12, 9, 0, 12, 4, 1, 11, 1, 13,
               19, 15, 14, 13, 11, 0, 5, 15],
              [1, 9, 13, 10, 1, 3, 1, 4, 3, 15, 6, 15, 8, 5, 8, 18, 11, 16, 6, 9, 15, 0, 0, 13, 16, 7, 10, 16, 16, 5, 4,
               19, 10, 15, 9, 11, 15, 10],
              [17, 7, 13, 2, 19, 18, 7, 13, 19, 13, 15, 11, 13, 15, 12, 11, 10, 8, 0, 11, 17, 17, 19, 5, 11, 6, 5, 6,
               16,
               12, 5, 14, 11, 14, 7, 10, 12, 10],
              [2, 19, 16, 8, 3, 11, 13, 14, 5, 12, 13, 4, 18, 17, 14, 17, 6, 13, 4, 11, 11, 9, 18, 11, 10, 10, 15, 12,
               13,
               8, 13, 14, 11, 10, 5, 0, 16, 17],
              [7, 15, 2, 0, 19, 7, 13, 15, 1, 6, 10, 13, 9, 4, 5, 16, 16, 18, 4, 7, 17, 7, 0, 6, 15, 14, 14, 6, 8, 18,
               15,
               6, 6, 1, 2, 7, 5, 14],
              [19, 11, 7, 14, 6, 8, 8, 7, 9, 7, 18, 4, 11, 17, 8, 1, 10, 14, 10, 3, 9, 9, 19, 0, 19, 4, 7, 16, 18, 8,
               16,
               0, 8, 11, 15, 17, 19, 18],
              [7, 12, 13, 6, 3, 18, 5, 2, 18, 15, 5, 14, 5, 0, 17, 8, 16, 10, 0, 0, 13, 1, 18, 12, 2, 8, 6, 5, 17, 5, 5,
               8,
               15, 17, 12, 9, 11, 10],
              [12, 1, 10, 1, 8, 16, 0, 13, 17, 5, 16, 18, 6, 3, 0, 19, 1, 2, 16, 9, 18, 7, 10, 8, 4, 13, 8, 16, 18, 12,
               15,
               14, 13, 16, 11, 3, 11, 11],
              [3, 6, 3, 16, 15, 14, 5, 15, 17, 14, 8, 15, 6, 12, 13, 12, 10, 5, 7, 14, 14, 19, 12, 15, 6, 18, 15, 19, 2,
               8,
               14, 18, 7, 8, 12, 17, 9, 19],
              [5, 14, 3, 6, 3, 6, 12, 13, 2, 11, 11, 12, 18, 19, 17, 11, 4, 18, 16, 0, 11, 8, 16, 6, 14, 15, 12, 18, 4,
               10,
               6, 17, 19, 6, 3, 16, 13, 0],
              [5, 0, 5, 10, 7, 14, 3, 15, 5, 7, 16, 13, 2, 18, 13, 0, 11, 7, 5, 9, 13, 12, 10, 6, 14, 7, 5, 5, 16, 19,
               11,
               0, 3, 12, 14, 8, 2, 6],
              [4, 19, 14, 14, 2, 16, 11, 19, 8, 13, 4, 8, 13, 3, 14, 19, 15, 11, 16, 15, 9, 14, 2, 11, 5, 7, 8, 14, 13,
               4,
               7, 12, 1, 18, 4, 7, 0, 3],
              [0, 0, 9, 3, 15, 4, 5, 19, 4, 14, 6, 5, 2, 7, 14, 12, 6, 13, 6, 5, 6, 18, 11, 0, 2, 13, 0, 9, 6, 11, 1,
               10,
               4, 3, 12, 9, 4, 9],
              [1, 16, 18, 13, 12, 17, 14, 12, 4, 1, 15, 12, 3, 5, 11, 8, 2, 7, 16, 3, 7, 11, 2, 2, 10, 13, 19, 6, 0, 8,
               3,
               1, 13, 10, 4, 8, 17, 2],
              [18, 13, 0, 4, 10, 12, 12, 11, 9, 19, 16, 5, 4, 0, 18, 17, 2, 19, 13, 1, 2, 0, 10, 11, 15, 17, 9, 13, 11,
               4,
               1, 6, 16, 0, 4, 16, 10, 17],
              [16, 8, 10, 1, 12, 14, 19, 4, 19, 18, 3, 16, 4, 4, 17, 18, 5, 3, 6, 4, 6, 1, 10, 8, 11, 2, 9, 11, 18, 3,
               16,
               16, 4, 8, 11, 8, 18, 18],
              [12, 1, 0, 7, 13, 7, 9, 19, 2, 19, 19, 15, 15, 8, 6, 9, 6, 16, 8, 12, 10, 15, 9, 0, 7, 8, 8, 18, 8, 1, 2,
               13,
               7, 1, 17, 15, 12, 5],
              [6, 10, 11, 3, 10, 0, 9, 19, 15, 15, 10, 1, 7, 8, 17, 16, 13, 11, 7, 5, 15, 14, 9, 3, 16, 18, 1, 11, 12,
               15,
               8, 6, 2, 14, 4, 10, 10, 5],
              [5, 18, 4, 14, 10, 6, 9, 9, 15, 14, 6, 8, 5, 19, 14, 2, 1, 16, 9, 7, 5, 0, 15, 14, 9, 1, 5, 9, 12, 13, 4,
               3,
               8, 5, 1, 6, 7, 3],
              [14, 16, 7, 8, 16, 3, 8, 7, 8, 15, 2, 14, 4, 12, 0, 11, 10, 17, 19, 11, 0, 9, 19, 3, 8, 18, 12, 8, 10, 19,
               9,
               4, 10, 0, 19, 7, 15, 8],
              [4, 4, 3, 8, 11, 14, 8, 15, 1, 16, 2, 0, 18, 9, 1, 0, 14, 0, 2, 9, 18, 18, 0, 5, 2, 10, 0, 18, 2, 15, 8,
               7,
               10, 15, 4, 2, 19, 12],
              [15, 13, 12, 15, 3, 6, 17, 4, 2, 16, 16, 16, 5, 12, 14, 12, 9, 13, 16, 16, 12, 9, 19, 12, 6, 16, 10, 6,
               18,
               16, 16, 3, 5, 6, 18, 16, 1, 7],
              [2, 7, 18, 15, 6, 16, 10, 16, 4, 18, 11, 5, 11, 10, 4, 10, 12, 14, 1, 19, 18, 7, 7, 7, 4, 9, 4, 10, 6, 0,
               3,
               0, 3, 12, 1, 19, 10, 7],
              [4, 9, 7, 16, 17, 2, 14, 16, 14, 12, 11, 8, 17, 0, 16, 17, 0, 14, 4, 4, 13, 9, 17, 10, 18, 1, 6, 1, 3, 14,
               3,
               18, 17, 18, 9, 5, 3, 0],
              [1, 15, 2, 0, 13, 7, 6, 11, 4, 17, 9, 15, 0, 9, 9, 15, 6, 11, 18, 9, 13, 12, 8, 2, 19, 19, 6, 12, 1, 7, 5,
               7,
               9, 14, 2, 1, 11, 3],
              [4, 8, 1, 1, 17, 6, 12, 11, 15, 9, 5, 13, 18, 1, 1, 13, 1, 9, 2, 4, 18, 2, 6, 16, 12, 16, 9, 5, 8, 0, 3,
               0,
               12, 19, 3, 16, 0, 16],
              [4, 16, 3, 5, 11, 10, 3, 4, 2, 18, 0, 9, 12, 0, 19, 1, 10, 17, 10, 1, 6, 9, 1, 13, 2, 5, 4, 8, 19, 15, 0,
               12,
               8, 2, 13, 12, 3, 6],
              [16, 15, 8, 1, 15, 5, 18, 16, 14, 0, 15, 9, 5, 7, 19, 13, 0, 11, 0, 11, 6, 19, 4, 15, 19, 19, 0, 18, 1,
               19,
               2, 19, 10, 17, 19, 15, 17, 8],
              [12, 2, 18, 16, 18, 6, 4, 11, 4, 13, 14, 10, 17, 6, 13, 1, 15, 17, 18, 13, 4, 16, 3, 12, 11, 7, 17, 7, 11,
               4,
               18, 4, 8, 4, 0, 0, 15, 14],
              [11, 7, 10, 18, 18, 15, 16, 6, 1, 16, 3, 8, 0, 5, 3, 16, 4, 0, 6, 9, 9, 4, 11, 8, 6, 16, 17, 18, 4, 17, 6,
               6,
               18, 8, 16, 10, 18, 10],
              [7, 11, 19, 5, 8, 9, 2, 8, 7, 17, 6, 4, 16, 6, 13, 17, 9, 6, 9, 16, 16, 14, 10, 2, 15, 18, 17, 19, 2, 11,
               8,
               2, 0, 12, 13, 8, 3, 11],
              [12, 1, 10, 12, 15, 6, 5, 12, 1, 17, 0, 4, 8, 8, 15, 2, 17, 16, 18, 5, 16, 6, 5, 5, 8, 15, 17, 2, 17, 10,
               3,
               18, 10, 4, 5, 13, 2, 4],
              [19, 9, 11, 13, 15, 12, 2, 16, 18, 9, 9, 18, 7, 4, 0, 11, 5, 2, 8, 19, 4, 17, 1, 1, 9, 14, 15, 2, 17, 4,
               0,
               4, 8, 8, 1, 5, 19, 2],
              [10, 15, 0, 12, 8, 5, 5, 0, 8, 16, 5, 12, 10, 19, 18, 1, 15, 7, 8, 7, 7, 15, 8, 16, 7, 16, 16, 18, 8, 7,
               12,
               16, 14, 3, 5, 17, 8, 13],
              [14, 14, 12, 3, 5, 10, 6, 6, 12, 1, 18, 6, 16, 6, 4, 14, 3, 11, 8, 10, 6, 2, 3, 14, 19, 0, 18, 11, 5, 2,
               1,
               13, 16, 13, 16, 11, 17, 5],
              [9, 9, 8, 18, 11, 8, 14, 10, 8, 16, 6, 19, 16, 0, 2, 0, 11, 16, 6, 3, 4, 11, 17, 11, 13, 9, 17, 16, 4, 15,
               14, 7, 7, 7, 11, 4, 0, 7],
              [5, 8, 15, 13, 4, 5, 2, 5, 5, 0, 12, 10, 13, 13, 17, 15, 13, 14, 10, 14, 19, 14, 8, 1, 16, 6, 0, 1, 9, 11,
               2,
               1, 10, 15, 15, 19, 11, 8],
              [6, 8, 2, 11, 17, 3, 14, 18, 18, 11, 12, 9, 1, 8, 19, 4, 9, 16, 14, 2, 11, 18, 9, 15, 10, 12, 0, 2, 18, 5,
               18, 6, 16, 19, 5, 0, 15, 11],
              [4, 10, 6, 0, 2, 11, 13, 14, 17, 14, 1, 3, 16, 13, 1, 0, 9, 3, 3, 6, 4, 16, 16, 5, 8, 13, 16, 5, 7, 11, 6,
               11, 19, 4, 13, 0, 8, 17]],), 'unknown'),
        (([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [19, 18, 17, 16, 15, 14, 13, 12, 11, 10],
           [20, 21, 22, 23, 24, 25, 26, 27, 28, 29], [39, 38, 37, 36, 35, 34, 33, 32, 31, 30],
           [40, 41, 42, 43, 44, 45, 46, 47, 48, 49], [59, 58, 57, 56, 55, 54, 53, 52, 51, 50],
           [60, 61, 62, 63, 64, 65, 66, 67, 68, 69], [79, 78, 77, 76, 75, 74, 73, 72, 71, 70],
           [80, 81, 82, 83, 84, 85, 86, 87, 88, 89], [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],
           [100, 101, 102, 103, 104, 105, 106, 107, 108, 109], [119, 118, 117, 116, 115, 114, 113, 112, 111, 110],
           [120, 121, 122, 123, 124, 125, 126, 127, 128, 129], [139, 138, 137, 136, 135, 134, 133, 132, 131, 130],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],), 'unknown'),
        (([
              [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
               29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54,
               55,
               56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81,
               82,
               83, 84, 85, 86, 87, 88, 89, 90, 91, 92],
              [185, 184, 183, 182, 181, 180, 179, 178, 177, 176, 175, 174, 173, 172, 171, 170, 169, 168, 167, 166, 165,
               164, 163, 162, 161, 160, 159, 158, 157, 156, 155, 154, 153, 152, 151, 150, 149, 148, 147, 146, 145, 144,
               143, 142, 141, 140, 139, 138, 137, 136, 135, 134, 133, 132, 131, 130, 129, 128, 127, 126, 125, 124, 123,
               122, 121, 120, 119, 118, 117, 116, 115, 114, 113, 112, 111, 110, 109, 108, 107, 106, 105, 104, 103, 102,
               101, 100, 99, 98, 97, 96, 95, 94, 93],
              [186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206,
               207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227,
               228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248,
               249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269,
               270, 271, 272, 273, 274, 275, 276, 277, 278],
              [371, 370, 369, 368, 367, 366, 365, 364, 363, 362, 361, 360, 359, 358, 357, 356, 355, 354, 353, 352, 351,
               350, 349, 348, 347, 346, 345, 344, 343, 342, 341, 340, 339, 338, 337, 336, 335, 334, 333, 332, 331, 330,
               329, 328, 327, 326, 325, 324, 323, 322, 321, 320, 319, 318, 317, 316, 315, 314, 313, 312, 311, 310, 309,
               308, 307, 306, 305, 304, 303, 302, 301, 300, 299, 298, 297, 296, 295, 294, 293, 292, 291, 290, 289, 288,
               287, 286, 285, 284, 283, 282, 281, 280, 279],
              [372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392,
               393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413,
               414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434,
               435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455,
               456, 457, 458, 459, 460, 461, 462, 463, 464],
              [557, 556, 555, 554, 553, 552, 551, 550, 549, 548, 547, 546, 545, 544, 543, 542, 541, 540, 539, 538, 537,
               536, 535, 534, 533, 532, 531, 530, 529, 528, 527, 526, 525, 524, 523, 522, 521, 520, 519, 518, 517, 516,
               515, 514, 513, 512, 511, 510, 509, 508, 507, 506, 505, 504, 503, 502, 501, 500, 499, 498, 497, 496, 495,
               494, 493, 492, 491, 490, 489, 488, 487, 486, 485, 484, 483, 482, 481, 480, 479, 478, 477, 476, 475, 474,
               473, 472, 471, 470, 469, 468, 467, 466, 465],
              [558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578,
               579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599,
               600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620,
               621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641,
               642, 643, 644, 645, 646, 647, 648, 649, 650],
              [743, 742, 741, 740, 739, 738, 737, 736, 735, 734, 733, 732, 731, 730, 729, 728, 727, 726, 725, 724, 723,
               722, 721, 720, 719, 718, 717, 716, 715, 714, 713, 712, 711, 710, 709, 708, 707, 706, 705, 704, 703, 702,
               701, 700, 699, 698, 697, 696, 695, 694, 693, 692, 691, 690, 689, 688, 687, 686, 685, 684, 683, 682, 681,
               680, 679, 678, 677, 676, 675, 674, 673, 672, 671, 670, 669, 668, 667, 666, 665, 664, 663, 662, 661, 660,
               659, 658, 657, 656, 655, 654, 653, 652, 651],
              [744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764,
               765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785,
               786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806,
               807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827,
               828, 829, 830, 831, 832, 833, 834, 835, 836],
              [929, 928, 927, 926, 925, 924, 923, 922, 921, 920, 919, 918, 917, 916, 915, 914, 913, 912, 911, 910, 909,
               908, 907, 906, 905, 904, 903, 902, 901, 900, 899, 898, 897, 896, 895, 894, 893, 892, 891, 890, 889, 888,
               887, 886, 885, 884, 883, 882, 881, 880, 879, 878, 877, 876, 875, 874, 873, 872, 871, 870, 869, 868, 867,
               866, 865, 864, 863, 862, 861, 860, 859, 858, 857, 856, 855, 854, 853, 852, 851, 850, 849, 848, 847, 846,
               845, 844, 843, 842, 841, 840, 839, 838, 837],
              [930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 946, 947, 948, 949, 950,
               951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971,
               972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992,
               993, 994, 995, 996, 997, 998, 999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010,
               1011,
               1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1022],
              [1115, 1114, 1113, 1112, 1111, 1110, 1109, 1108, 1107, 1106, 1105, 1104, 1103, 1102, 1101, 1100, 1099,
               1098,
               1097, 1096, 1095, 1094, 1093, 1092, 1091, 1090, 1089, 1088, 1087, 1086, 1085, 1084, 1083, 1082, 1081,
               1080,
               1079, 1078, 1077, 1076, 1075, 1074, 1073, 1072, 1071, 1070, 1069, 1068, 1067, 1066, 1065, 1064, 1063,
               1062,
               1061, 1060, 1059, 1058, 1057, 1056, 1055, 1054, 1053, 1052, 1051, 1050, 1049, 1048, 1047, 1046, 1045,
               1044,
               1043, 1042, 1041, 1040, 1039, 1038, 1037, 1036, 1035, 1034, 1033, 1032, 1031, 1030, 1029, 1028, 1027,
               1026,
               1025, 1024, 1023],
              [1116, 1117, 1118, 1119, 1120, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128, 1129, 1130, 1131, 1132,
               1133,
               1134, 1135, 1136, 1137, 1138, 1139, 1140, 1141, 1142, 1143, 1144, 1145, 1146, 1147, 1148, 1149, 1150,
               1151,
               1152, 1153, 1154, 1155, 1156, 1157, 1158, 1159, 1160, 1161, 1162, 1163, 1164, 1165, 1166, 1167, 1168,
               1169,
               1170, 1171, 1172, 1173, 1174, 1175, 1176, 1177, 1178, 1179, 1180, 1181, 1182, 1183, 1184, 1185, 1186,
               1187,
               1188, 1189, 1190, 1191, 1192, 1193, 1194, 1195, 1196, 1197, 1198, 1199, 1200, 1201, 1202, 1203, 1204,
               1205,
               1206, 1207, 1208],
              [1301, 1300, 1299, 1298, 1297, 1296, 1295, 1294, 1293, 1292, 1291, 1290, 1289, 1288, 1287, 1286, 1285,
               1284,
               1283, 1282, 1281, 1280, 1279, 1278, 1277, 1276, 1275, 1274, 1273, 1272, 1271, 1270, 1269, 1268, 1267,
               1266,
               1265, 1264, 1263, 1262, 1261, 1260, 1259, 1258, 1257, 1256, 1255, 1254, 1253, 1252, 1251, 1250, 1249,
               1248,
               1247, 1246, 1245, 1244, 1243, 1242, 1241, 1240, 1239, 1238, 1237, 1236, 1235, 1234, 1233, 1232, 1231,
               1230,
               1229, 1228, 1227, 1226, 1225, 1224, 1223, 1222, 1221, 1220, 1219, 1218, 1217, 1216, 1215, 1214, 1213,
               1212,
               1211, 1210, 1209],
              [1302, 1303, 1304, 1305, 1306, 1307, 1308, 1309, 1310, 1311, 1312, 1313, 1314, 1315, 1316, 1317, 1318,
               1319,
               1320, 1321, 1322, 1323, 1324, 1325, 1326, 1327, 1328, 1329, 1330, 1331, 1332, 1333, 1334, 1335, 1336,
               1337,
               1338, 1339, 1340, 1341, 1342, 1343, 1344, 1345, 1346, 1347, 1348, 1349, 1350, 1351, 1352, 1353, 1354,
               1355,
               1356, 1357, 1358, 1359, 1360, 1361, 1362, 1363, 1364, 1365, 1366, 1367, 1368, 1369, 1370, 1371, 1372,
               1373,
               1374, 1375, 1376, 1377, 1378, 1379, 1380, 1381, 1382, 1383, 1384, 1385, 1386, 1387, 1388, 1389, 1390,
               1391,
               1392, 1393, 1394],
              [1487, 1486, 1485, 1484, 1483, 1482, 1481, 1480, 1479, 1478, 1477, 1476, 1475, 1474, 1473, 1472, 1471,
               1470,
               1469, 1468, 1467, 1466, 1465, 1464, 1463, 1462, 1461, 1460, 1459, 1458, 1457, 1456, 1455, 1454, 1453,
               1452,
               1451, 1450, 1449, 1448, 1447, 1446, 1445, 1444, 1443, 1442, 1441, 1440, 1439, 1438, 1437, 1436, 1435,
               1434,
               1433, 1432, 1431, 1430, 1429, 1428, 1427, 1426, 1425, 1424, 1423, 1422, 1421, 1420, 1419, 1418, 1417,
               1416,
               1415, 1414, 1413, 1412, 1411, 1410, 1409, 1408, 1407, 1406, 1405, 1404, 1403, 1402, 1401, 1400, 1399,
               1398,
               1397, 1396, 1395],
              [1488, 1489, 1490, 1491, 1492, 1493, 1494, 1495, 1496, 1497, 1498, 1499, 1500, 1501, 1502, 1503, 1504,
               1505,
               1506, 1507, 1508, 1509, 1510, 1511, 1512, 1513, 1514, 1515, 1516, 1517, 1518, 1519, 1520, 1521, 1522,
               1523,
               1524, 1525, 1526, 1527, 1528, 1529, 1530, 1531, 1532, 1533, 1534, 1535, 1536, 1537, 1538, 1539, 1540,
               1541,
               1542, 1543, 1544, 1545, 1546, 1547, 1548, 1549, 1550, 1551, 1552, 1553, 1554, 1555, 1556, 1557, 1558,
               1559,
               1560, 1561, 1562, 1563, 1564, 1565, 1566, 1567, 1568, 1569, 1570, 1571, 1572, 1573, 1574, 1575, 1576,
               1577,
               1578, 1579, 1580],
              [1673, 1672, 1671, 1670, 1669, 1668, 1667, 1666, 1665, 1664, 1663, 1662, 1661, 1660, 1659, 1658, 1657,
               1656,
               1655, 1654, 1653, 1652, 1651, 1650, 1649, 1648, 1647, 1646, 1645, 1644, 1643, 1642, 1641, 1640, 1639,
               1638,
               1637, 1636, 1635, 1634, 1633, 1632, 1631, 1630, 1629, 1628, 1627, 1626, 1625, 1624, 1623, 1622, 1621,
               1620,
               1619, 1618, 1617, 1616, 1615, 1614, 1613, 1612, 1611, 1610, 1609, 1608, 1607, 1606, 1605, 1604, 1603,
               1602,
               1601, 1600, 1599, 1598, 1597, 1596, 1595, 1594, 1593, 1592, 1591, 1590, 1589, 1588, 1587, 1586, 1585,
               1584,
               1583, 1582, 1581],
              [1674, 1675, 1676, 1677, 1678, 1679, 1680, 1681, 1682, 1683, 1684, 1685, 1686, 1687, 1688, 1689, 1690,
               1691,
               1692, 1693, 1694, 1695, 1696, 1697, 1698, 1699, 1700, 1701, 1702, 1703, 1704, 1705, 1706, 1707, 1708,
               1709,
               1710, 1711, 1712, 1713, 1714, 1715, 1716, 1717, 1718, 1719, 1720, 1721, 1722, 1723, 1724, 1725, 1726,
               1727,
               1728, 1729, 1730, 1731, 1732, 1733, 1734, 1735, 1736, 1737, 1738, 1739, 1740, 1741, 1742, 1743, 1744,
               1745,
               1746, 1747, 1748, 1749, 1750, 1751, 1752, 1753, 1754, 1755, 1756, 1757, 1758, 1759, 1760, 1761, 1762,
               1763,
               1764, 1765, 1766],
              [1859, 1858, 1857, 1856, 1855, 1854, 1853, 1852, 1851, 1850, 1849, 1848, 1847, 1846, 1845, 1844, 1843,
               1842,
               1841, 1840, 1839, 1838, 1837, 1836, 1835, 1834, 1833, 1832, 1831, 1830, 1829, 1828, 1827, 1826, 1825,
               1824,
               1823, 1822, 1821, 1820, 1819, 1818, 1817, 1816, 1815, 1814, 1813, 1812, 1811, 1810, 1809, 1808, 1807,
               1806,
               1805, 1804, 1803, 1802, 1801, 1800, 1799, 1798, 1797, 1796, 1795, 1794, 1793, 1792, 1791, 1790, 1789,
               1788,
               1787, 1786, 1785, 1784, 1783, 1782, 1781, 1780, 1779, 1778, 1777, 1776, 1775, 1774, 1773, 1772, 1771,
               1770,
               1769, 1768, 1767],
              [1860, 1861, 1862, 1863, 1864, 1865, 1866, 1867, 1868, 1869, 1870, 1871, 1872, 1873, 1874, 1875, 1876,
               1877,
               1878, 1879, 1880, 1881, 1882, 1883, 1884, 1885, 1886, 1887, 1888, 1889, 1890, 1891, 1892, 1893, 1894,
               1895,
               1896, 1897, 1898, 1899, 1900, 1901, 1902, 1903, 1904, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912,
               1913,
               1914, 1915, 1916, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1926, 1927, 1928, 1929, 1930,
               1931,
               1932, 1933, 1934, 1935, 1936, 1937, 1938, 1939, 1940, 1941, 1942, 1943, 1944, 1945, 1946, 1947, 1948,
               1949,
               1950, 1951, 1952],
              [2045, 2044, 2043, 2042, 2041, 2040, 2039, 2038, 2037, 2036, 2035, 2034, 2033, 2032, 2031, 2030, 2029,
               2028,
               2027, 2026, 2025, 2024, 2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011,
               2010,
               2009, 2008, 2007, 2006, 2005, 2004, 2003, 2002, 2001, 2000, 1999, 1998, 1997, 1996, 1995, 1994, 1993,
               1992,
               1991, 1990, 1989, 1988, 1987, 1986, 1985, 1984, 1983, 1982, 1981, 1980, 1979, 1978, 1977, 1976, 1975,
               1974,
               1973, 1972, 1971, 1970, 1969, 1968, 1967, 1966, 1965, 1964, 1963, 1962, 1961, 1960, 1959, 1958, 1957,
               1956,
               1955, 1954, 1953],
              [2046, 2047, 2048, 2049, 2050, 2051, 2052, 2053, 2054, 2055, 2056, 2057, 2058, 2059, 2060, 2061, 2062,
               2063,
               2064, 2065, 2066, 2067, 2068, 2069, 2070, 2071, 2072, 2073, 2074, 2075, 2076, 2077, 2078, 2079, 2080,
               2081,
               2082, 2083, 2084, 2085, 2086, 2087, 2088, 2089, 2090, 2091, 2092, 2093, 2094, 2095, 2096, 2097, 2098,
               2099,
               2100, 2101, 2102, 2103, 2104, 2105, 2106, 2107, 2108, 2109, 2110, 2111, 2112, 2113, 2114, 2115, 2116,
               2117,
               2118, 2119, 2120, 2121, 2122, 2123, 2124, 2125, 2126, 2127, 2128, 2129, 2130, 2131, 2132, 2133, 2134,
               2135,
               2136, 2137, 2138],
              [2231, 2230, 2229, 2228, 2227, 2226, 2225, 2224, 2223, 2222, 2221, 2220, 2219, 2218, 2217, 2216, 2215,
               2214,
               2213, 2212, 2211, 2210, 2209, 2208, 2207, 2206, 2205, 2204, 2203, 2202, 2201, 2200, 2199, 2198, 2197,
               2196,
               2195, 2194, 2193, 2192, 2191, 2190, 2189, 2188, 2187, 2186, 2185, 2184, 2183, 2182, 2181, 2180, 2179,
               2178,
               2177, 2176, 2175, 2174, 2173, 2172, 2171, 2170, 2169, 2168, 2167, 2166, 2165, 2164, 2163, 2162, 2161,
               2160,
               2159, 2158, 2157, 2156, 2155, 2154, 2153, 2152, 2151, 2150, 2149, 2148, 2147, 2146, 2145, 2144, 2143,
               2142,
               2141, 2140, 2139],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
               0,
               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
               0,
               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],), 'un')
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.longestIncreasingPath(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass