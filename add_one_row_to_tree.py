#!/usr/bin/env python
# coding: utf-8

from utils.binary_tree import build_binary_tree, TreeNode


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            node = TreeNode(v)
            node.left = root
            return node

        def do(node, depth):
            if not node: return
            if depth == 2:
                nl = TreeNode(v)
                nl.left = node.left
                node.left = nl
                nr = TreeNode(v)
                nr.right = node.right
                node.right = nr
                return
            else:
                do(node.left, depth - 1)
                do(node.right, depth - 1)

        do(root, d)

        return root


if __name__ == '__main__':
    sol = Solution()
    t = build_binary_tree([4, 2, 6, 3, 1, 5])
    print(sol.addOneRow(t, 1, 2))
