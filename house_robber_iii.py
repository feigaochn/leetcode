# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: house robber iii
#
# The thief has found himself a new place for his thievery again. There is
# only one entrance to this area, called the "root." Besides the root, each
# house has one and only one parent house. After a tour, the smart thief
# realized that "all houses in this place forms a binary tree". It will
# automatically contact the police if two directly-linked houses were broken
# into on the same night.
# 
# Determine the maximum amount of money the thief can rob tonight without
# alerting the police.
# 
# Example 1:
# 
#      3
#     / \
#    2   3
#     \   \
#      3   1
# 
# Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
# 
# Example 2:
# 
#      3
#     / \
#    4   5
#   / \   \
#  1   3   1
# 
# Maximum amount of money the thief can rob = 4 + 5 = 9.
# 
# Credits:Special thanks to @dietpepsi for adding this problem and creating
# all test cases.
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Tree
# Depth-first Search
# 
# Show Similar Problems
# 
#  (E) House Robber
#  (M) House Robber II


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def best(node=root):
            return max(take(node), leave(node))

        def leave(node=root):
            if node is None:
                return 0
            else:
                return best(node.left) + best(node.right)

        def take(node=root):
            if node is None:
                return 0
            else:
                return node.val + leave(node.left) + leave(node.right)

        # TODO: TLE
        return best()


def main():
    solver = Solution()
    from utils import build_binary_tree
    null = None
    tests = [
        ((build_binary_tree([3, 2, 3, None, 3, None, 1]),), 7),
        ((build_binary_tree([2, 1, 3, None, 4]),), 7),

    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.rob(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
