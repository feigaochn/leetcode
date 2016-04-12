# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: populating next right pointers in each node ii
#
# Follow up for problem "Populating Next Right Pointers in Each Node".
# What if the given tree could be any binary tree? Would your previous
# solution still work?
# 
# Note:
# You may only use constant extra space.
# 
# For example,
# Given the following binary tree,
# 
#          1
#        /  \
#       2    3
#      / \    \
#     4   5    7
# 
# After calling your function, the tree should look like:
# 
#          1 -> NULL
#        /  \
#       2 -> 3 -> NULL
#      / \    \
#     4-> 5 -> 7 -> NULL
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Tree
# Depth-first Search
# 
# Show Similar Problems
# 
#  (M) Populating Next Right Pointers in Each Node


# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        # TODO
        return


def main():
    solver = Solution()
    tests = [
        (('param',), 'result'),
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.__init__(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
