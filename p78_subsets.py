# author: Fei Gao
#
# Subsets
#
# Given a set of distinct integers, S, return all possible subsets.
# Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# For example,
# If S = [1,2,3], a solution is:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

import itertools


class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        all_subsets = []
        for i in range(len(S) + 1):
            all_subsets.extend([sorted(list(sub)) for sub in itertools.combinations(S, i)])
        return all_subsets


def main():
    solver = Solution()
    tests = [list(range(3)), list(range(4,0,-1)), [1,1,2]]
    for test in tests:
        result = solver.subsets(test)
        print(test, ' ->\n', result)
    pass


if __name__ == '__main__':
    main()
    pass
