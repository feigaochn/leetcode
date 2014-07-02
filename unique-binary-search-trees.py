# author: Fei Gao
#
# Unique Binary Search Trees
#
# Given n, how many structurally unique BST's (binary search trees) that store values 1...n?
# For example,
# Given n = 3, there are a total of 5 unique BST's.
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3


class Solution:
    # @return an integer
    def numTrees(self, n):
        solutions = [1, 1, 2]
        for i in range(3, n+1):
            solutions.append(sum([solutions[i] * solutions[-1-i] for i in range(len(solutions))]))
        return solutions[n]


def main():
    solver = Solution()
    tests = list(range(5))
    for test in tests:
        print(test)
        print(' ->')
        result = solver.numTrees(test)
        print(result)
        print('~'*10)
    pass


if __name__ == '__main__':
    main()
    pass
