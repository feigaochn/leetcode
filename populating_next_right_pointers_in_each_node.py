# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: populating next right pointers in each node
#
# Given a binary tree
# 
#     struct TreeLinkNode {
#       TreeLinkNode *left;
#       TreeLinkNode *right;
#       TreeLinkNode *next;
#     }
# 
# Populate each next pointer to point to its next right node. If there is
# no next right node, the next pointer should be set to NULL.
# Initially, all next pointers are set to NULL.
# 
# Note:
# 
# You may only use constant extra space.
# You may assume that it is a perfect binary tree (ie, all leaves are at
# the same level, and every parent has two children).
# 
# For example,
# Given the following perfect binary tree,
# 
#          1
#        /  \
#       2    3
#      / \  / \
#     4  5  6  7
# 
# After calling your function, the tree should look like:
# 
#          1 -> NULL
#        /  \
#       2 -> 3 -> NULL
#      / \  / \
#     4->5->6->7 -> NULL
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
#  (H) Populating Next Right Pointers in Each Node II
#  (M) Binary Tree Right Side View


# Definition for binary tree with next pointer.
class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root: return root
        next_level = [root]
        while next_level:
            cur_level = next_level[::]
            next_level = []
            for idx, node in enumerate(cur_level):
                node.next = cur_level[idx + 1] if idx + 1 < len(cur_level) else None
                if node.left: next_level.append(node.left)
                if node.right: next_level.append(node.right)



def main():
    solver = Solution()
    tests = [
        (('param',), 'result'),
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.connect(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
