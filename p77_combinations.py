# author: Fei Gao
#
# Combinations
#
# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
# For example,
# If n = 4 and k = 2, a solution is:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]

import itertools


class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        return [list(p) for p in itertools.combinations(range(1, n + 1), k)]


def main():
    solver = Solution()
    print(solver.combine(4, 2))
    pass


if __name__ == '__main__':
    main()
    pass
