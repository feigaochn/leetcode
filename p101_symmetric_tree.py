# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: symmetric tree
#
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric
# around its center).
# 
# For example, this binary tree is symmetric:
# 
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# 
# But the following is not:
# 
#     1
#    / \
#   2   2
#    \   \
#    3    3
# 
# Note:
# Bonus points if you could solve it both recursively and iteratively.
# 
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
# Depth-first Search


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from utils import TreeNode, build_binary_tree

print(build_binary_tree([1, 2, 3, None, None, 4, None, None, 5]))


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def rotate(node):
            if node is not None:
                node.left, node.right = rotate(node.right), rotate(node.left)
            return node

        def is_same(node1, node2):
            if node1 is None and node2 is None:
                return True
            elif node1 is None or node2 is None:
                return False
            else:
                return (node1.val == node2.val
                        and is_same(node1.left, node2.left)
                        and is_same(node1.right, node2.right))

        if root is None:
            return True
        left = root.left
        right = rotate(root.right)

        return is_same(left, right)


def main():
    solver = Solution()
    tests = [
        ((build_binary_tree([1,2,2]),),True ),
        ((build_binary_tree([1,2,2,None,3,None,3]),),False)
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.isSymmetric(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
