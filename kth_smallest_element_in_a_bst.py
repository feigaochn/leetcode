# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: kth smallest element in a bst
#
# Given a binary search tree, write a function kthSmallest to find the kth
# smallest element in it.
# Note:
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
# Follow up:
# What if the BST is modified (insert/delete operations) often and you need to
# find the kth smallest frequently? How would you optimize the kthSmallest
# routine?
# 
# Try to utilize the property of a BST.
# What if you could modify the BST node's structure?
# The optimal runtime complexity is O(height of BST).
# 
# Credits:Special thanks to @ts for adding this problem and creating all test
# cases.
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Tree
# Binary Search
# 
# Show Similar Problems
# 
#  (M) Binary Tree Inorder Traversal


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def kthSmallest(self, root, k):
        """ 1 <= k <= size(BST)
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if root is None:
            return None

        def flatten(node: TreeNode):
            if node is None:
                return []
            else:
                return flatten(node.left) + [node.val] + flatten(node.right)

        return sorted(flatten(root))[k - 1]

import node.btree


def main():
    solver = Solution()
    t = node.btree.TreeNode().build_from_list([1,2,3])
    tests = [
        ((t,2), 2),
        ((node.btree.TreeNode().build_from_list([]), 0), None)
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.kthSmallest(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
