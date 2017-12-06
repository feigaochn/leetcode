#!/usr/bin/env python
# coding: utf-8

# p669

from utils import build_binary_tree, TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """

        def go(node: TreeNode) -> TreeNode:
            if node is None:
                return None
            if node.val < L:
                return go(node.right)
            elif node.val > R:
                return go(node.left)
            else:
                node.left = go(node.left)
                node.right = go(node.right)
            return node

        return go(root)


if __name__ == '__main__':
    sol = Solution()
    print(sol.trimBST(build_binary_tree([1, 0, 2]), 1, 2))
    print(sol.trimBST(build_binary_tree([1, 0, 2]), 3, 3))
    print(sol.trimBST(build_binary_tree([3, 0, 4, None, 2, None, None, 1]), 1, 3))
