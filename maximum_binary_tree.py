#!/usr/bin/env python
# coding: utf-8

# p654

from utils import build_binary_tree, TreeNode


class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        mi, mv = max(enumerate(nums), key=lambda t: t[1])
        node = TreeNode(mv)
        node.left = self.constructMaximumBinaryTree(nums[:mi])
        node.right = self.constructMaximumBinaryTree(nums[mi + 1:])
        return node


if __name__ == '__main__':
    sol = Solution()
    print(sol.constructMaximumBinaryTree([3, 2, 1, 6, 0, 5]))
