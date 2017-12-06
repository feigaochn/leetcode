# author: Fei Gao
#
# Permutations
#
# Given a collection of numbers, return all possible permutations.
# For example,
# [1,2,3] have the following permutations:
# [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].

import itertools


class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        return [list(x) for x in itertools.permutations(num)]
        pass


def main():
    solver = Solution()
    print(solver.permute(list(range(2))[::-1]))
    pass


if __name__ == '__main__':
    main()
    pass
