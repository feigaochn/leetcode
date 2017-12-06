#!/usr/bin/env python
# coding: utf-8

from utils.binary_tree import build_binary_tree

null = None


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.cur_count = 0
        self.cur_value = None
        self.value = 0
        self.max_count = 0
        self.modes = []

        def dfs(node):
            if node is None:
                return
            dfs(node.left)

            if node.val != self.cur_value:
                self.cur_value = node.val
                self.cur_count = 0
            self.cur_count += 1
            if self.cur_count > self.max_count:
                self.max_count = self.cur_count
                self.modes = [self.cur_value]
            elif self.cur_count == self.max_count:
                self.modes.append(self.cur_value)

            dfs(node.right)

        dfs(root)
        return self.modes


if __name__ == '__main__':
    sol = Solution()
    print(sol.findMode(build_binary_tree([1, None, 2, 2, 3, None, None, 3])))
    print(sol.findMode(build_binary_tree([2, 1, null, null, 2])))
    print(sol.findMode(build_binary_tree([6, 2, 8, 0, 4, 7, 9, null, null, 2, 6])))
