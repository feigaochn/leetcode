# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: balanced binary tree
#
# Given a binary tree, determine if it is height-balanced.
# 
# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more
# than 1.
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
#  (E) Maximum Depth of Binary Tree


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        cache = {None: 0}

        def depth(node):
            if node not in cache:
                cache[node] = 1 + max(depth(node.left), depth(node.right))
            return cache[node]

        def check(node):
            return node is None or (-1 <= depth(node.left) - depth(node.right) <= 1
                                    and check(node.left)
                                    and check(node.right))

        return check(root)


def main():
    import utils
    root = utils.build_binary_tree([1, 2, 2, 3, None, None, 3, 4, None, None, 4])

    print(Solution().isBalanced(root))

    root = utils.build_binary_tree([1])
    print(Solution().isBalanced(root))

    print(Solution().isBalanced(None))


if __name__ == '__main__':
    main()
    pass
