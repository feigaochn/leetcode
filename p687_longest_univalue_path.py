#!/usr/bin/env python
# coding: utf-8


"""
Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

Note: The length of path between two nodes is represented by the number of edges between them.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        def process(node: TreeNode) -> (int, int):
            """Return the best path, and best path including node"""
            if node is None:
                return (0, 0, None)
            lb, lp, lv = process(node.left)
            rb, rp, rv = process(node.right)
            bb = bp = 1
            if lv == node.val:
                bb += lp
                bp = max(bp, 1 + lp)
            if rv == node.val:
                bb += rp
                bp = max(bp, 1 + rp)
            bb = max([bb, lb, rb])
            return (bb, bp, node.val)

        return process(root)[0] - 1

if __name__ == '__main__':
    root = TreeNode(1)
    sol = Solution().longestUnivaluePath
    print(sol)
