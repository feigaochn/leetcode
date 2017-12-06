# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: binary tree postorder traversal
#
# Given a binary tree, return the postorder traversal of its nodes' values.
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
# return [3,2,1].
# 
# Note: Recursive solution is trivial, could you do it iteratively?
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Tree
# Stack
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
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        else:
            return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]


def main():
    solver = Solution()
    tests = [
        (('param',), 'result'),
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.postorderTraversal(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
