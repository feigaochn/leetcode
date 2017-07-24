#!/usr/bin/env python
# coding: utf-8

from utils.binary_tree import TreeNode, build_binary_tree


class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None and t2 is None:
            return None

        if t1 is None and t2 is not None:
            node = TreeNode(t2.val)
            node.left = self.mergeTrees(None, t2.left)
            node.right = self.mergeTrees(None, t2.right)
            return node
        elif t1 is not None and t2 is None:
            node = TreeNode(t1.val)
            node.left = self.mergeTrees(t1.left, None)
            node.right = self.mergeTrees(t1.right, None)
            return node
        elif t1 is not None and t2 is not None:
            node = TreeNode(t1.val + t2.val)
            node.left = self.mergeTrees(t1.left, t2.left)
            node.right = self.mergeTrees(t1.right, t2.right)
            return node


if __name__ == '__main__':
    sol = Solution()
    print(build_binary_tree([1, 2, 3, None, 5]))
    t1, t2 = build_binary_tree([1, 3, 2, 5]), build_binary_tree([2, 1, 3, None, 4, None, 7])
    print(t1, t2)
    t3 = sol.mergeTrees(t1, t2)
    print(t3)
