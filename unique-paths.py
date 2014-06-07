# author: Fei Gao
#
# Unique Paths
#
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in
# the diagram below).
# The robot can only move either down or right at any point in time. The robot
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in
# the diagram below).
# How many possible unique paths are there?
# Above is a 3 x 7 grid. How many possible unique paths are there?
# Note: m and n will be at most 100.


class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        mm = m - 1
        nn = n - 1
        if mm > nn:
            mm, nn = nn, mm
        res = 1
        for i in range(mm):
            res = res * (nn + mm - i)
            res = res // (i + 1)
        return res


def main():
    solver = Solution()
    print(solver.uniquePaths(2, 3))
    pass


if __name__ == '__main__':
    main()
    pass
