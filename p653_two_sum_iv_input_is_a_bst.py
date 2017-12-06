#!/usr/bin/env python
# coding: utf-8

# p653

from utils import build_binary_tree, TreeNode


class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """

        def find(node: TreeNode, target: int) -> bool:
            if node is None:
                return False
            elif node.val == target:
                return True
            elif node.val < target:
                return find(node.right, target)
            elif node.val > target:
                return find(node.left, target)

        def go(node: TreeNode):
            return (node is not None
                    and ((node.val * 2 != k
                          and find(root, k - node.val))
                         or go(node.left)
                         or go(node.right)))

        return go(root)


if __name__ == '__main__':
    sol = Solution()
    tree = build_binary_tree([5, 3, 6, 2, 4, None, 8])
    print(sol.findTarget(tree, 10))
    print(sol.findTarget(tree, 12))
    print(sol.findTarget(tree, 16))
    print(sol.findTarget(tree, 28))
