class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        from collections import defaultdict
        diag = defaultdict(set)
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                diag[r - c].add(val)
        return all(len(vals) == 1 for vals in diag.values())


sol = Solution().isToeplitzMatrix
print(sol([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]))
print(sol([[1, 2], [2, 2]]))
print(sol([[1]]))
