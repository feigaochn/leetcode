#!/usr/bin/env python
# coding: utf-8

from utils.binary_tree import TreeNode, build_binary_tree


class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if t is None:
            return ''
        s = str(t.val)
        left = self.tree2str(t.left)
        right = self.tree2str(t.right)
        if left and right:
            return '{}({})({})'.format(s, left, right)
        if not left and right:
            return '{}({})({})'.format(s, left, right)
        if left and not right:
            return '{}({})'.format(s, left)
        return s


if __name__ == '__main__':
    sol = Solution()
    print(sol.tree2str(build_binary_tree([])))
    print(sol.tree2str(build_binary_tree([1])))
    print(sol.tree2str(build_binary_tree([1, 2, 3, 4])))
    print(sol.tree2str(build_binary_tree([1, 2, 3, None, 4])))
