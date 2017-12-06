# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: invert binary tree
#
# Invert a binary tree.
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# 
# to
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
# Trivia:
# This problem was inspired by this original tweet by Max Howell:
# Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so fuck off.
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Tree

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return root
        root.left, root.right = root.right, root.left
        if root.left: self.invertTree(root.left)
        if root.right: self.invertTree(root.right)
        return root


def main():
    solver = Solution()
    tests = [
        (('param',), 'result'),
    ]
    for params, expect in tests:
        print('-'*5 + 'TEST' + '-'*5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.__init__(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
