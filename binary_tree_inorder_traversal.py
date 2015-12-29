# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: binary tree inorder traversal
#
# Given a binary tree, return the inorder traversal of its nodes' values.
# 
# For example:
# Given binary tree {1,#,2,3},
# 
#    1
#     \
#      2
#     /
#    3
# 
# return [1,3,2].
# 
# Note: Recursive solution is trivial, could you do it iteratively?
# confused what "{1,#,2,3}" means? > read more on how binary tree is
# serialized on OJ.
# OJ's Binary Tree Serialization:
# 
# The serialization of a binary tree follows a level order traversal, where
# '#' signifies a path terminator where no node exists below.
# 
# Here's an example:
# 
#    1
#   / \
#  2   3
#     /
#    4
#     \
#      5
# 
# The above binary tree is serialized as "{1,2,3,#,#,4,#,#,5}".
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Tree
# Hash Table
# Stack
# 
# Show Similar Problems
# 
#  (M) Validate Binary Search Tree
#  (M) Binary Tree Preorder Traversal
#  (H) Binary Tree Postorder Traversal
#  (M) Binary Search Tree Iterator
#  (M) Kth Smallest Element in a BST
#  (H) Closest Binary Search Tree Value II
#  (M) Inorder Successor in BST


# Definition for a binary tree node.
from node.btree import TreeNode


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        lst = []
        if not root:
            return lst
        if root.left:
            lst.extend(self.inorderTraversal(root.left))
        lst.append(root.val)
        if root.right:
            lst.extend(self.inorderTraversal(root.right))
        return lst


def main():
    solver = Solution()
    tree1 = TreeNode(1)
    tree1.right = TreeNode(2)
    tree1.right.left = TreeNode(3)
    tests = [
        ((tree1,), [1, 3, 2]),
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.inorderTraversal(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
