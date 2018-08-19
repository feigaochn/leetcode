# We have a two dimensional matrix A where each value is 0 or 1.

# A move consists of choosing any row or column, and toggling each value in
# that row or column: changing all 0s to 1s, and all 1s to 0s.

# After making any number of moves, every row of this matrix is interpreted as
# a binary number, and the score of the matrix is the sum of these numbers.

# Return the highest possible score.

# Example 1:
# Input: [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
# Output: 39
# Explanation: Toggled to
# [[1,1,1,1],[1,0,0,1],[1,1,1,1]].
# 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39

# Note:
#     1 <= A.length <= 20 1 <= A[0].length <= 20 A[i][j] is 0 or 1.


class Solution:

    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        for row in A:
            if row[0] == 0:
                for i, v in enumerate(row):
                    row[i] = 1 - v
        A = [col for col in zip(*[row[::-1] for row in A])]
        result = 0
        for i, col in enumerate(A):
            zeros = col.count(0)
            ones = col.count(1)
            result += (2 ** i) * max(zeros, ones)
        return result


sol = Solution().matrixScore
print(sol([[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]), 39)
print(sol([[1, 0], [1, 1]]), 5)
