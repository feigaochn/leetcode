# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: sum root to leaf numbers
#
# Given a binary tree containing digits from 0-9 only, each root-to-leaf path
# could represent a number.
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
# Find the total sum of all root-to-leaf numbers.
# For example,
# 
#     1
#    / \
#   2   3
# 
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# 
# Return the sum = 12 + 13 = 25.
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
#  (E) Path Sum
#  (H) Binary Tree Maximum Path Sum


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nums = []
        def t(node, pre):
            if node is None:
                pass
            elif node.left is None and node.right is None:
                # leaf
                nums.append(pre * 10 + node.val)
            else:
                if node.left is not None:
                    t(node.left, pre * 10 + node.val)
                if node.right is not None:
                    t(node.right, pre * 10 + node.val)
        t(root, 0)
        # print(nums)
        return sum(nums)


def main():
    solver = Solution()
    from utils import build_binary_tree
    tests = [
        ((build_binary_tree([1,2,3]),), 25),
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.sumNumbers(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
