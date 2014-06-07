# author: Fei Gao
#
# Subsets Ii
#
# Given a collection of integers that might contain duplicates, S, return all possible subsets.
# Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# For example,
# If S = [1,2,2], a solution is:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]

import itertools


class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        all_subsets = list()
        for i in range(len(S) + 1):
            for sub in itertools.combinations(S, i):
                all_subsets.append(sorted(list(sub)))
        mylist = sorted(all_subsets)
        last = mylist[-1]
        for i in range(len(mylist) - 2, -1, -1):
            if last == mylist[i]:
                del mylist[i]
            else:
                last = mylist[i]
        return mylist


def main():
    solver = Solution()

    tests = [list(range(3)), list(range(4, 0, -1)), [1, 1, 2]]

    for test in tests:
        result = solver.subsetsWithDup(test)
        print(test)
        print(' ->')
        print(result)
        print()
    pass


if __name__ == '__main__':
    main()
    pass
