#!/usr/bin/env python
# coding: utf-8

# p671

from utils import build_binary_tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None  # type: TreeNode
        self.right = None  # type: TreeNode


class Solution:
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        vals = []
        lower = root.val

        def search(node: TreeNode):
            if node is None:
                return
            elif node.val > lower:
                vals.append(node.val)
            elif node.val == lower:
                search(node.left)
                search(node.right)

        search(root)
        return min(vals, default=-1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.findSecondMinimumValue(TreeNode(2)))
    print(sol.findSecondMinimumValue(build_binary_tree([2, 2, 5, None, None, 5, 7])))
    print(sol.findSecondMinimumValue(
        build_binary_tree([2, 2, 2])))
