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

        def first_child(node):
            return (None if node is None else
                    node.left if node.left is not None else
                    node.right if node.right is not None else
                    first_child(node.next) if node.next is not None else
                    None)

        def work(node):
            if node is None:
                pass
            elif node.left is not None and node.right is not None:
                node.left.next = node.right
                node.right.next = first_child(node.next)
                return [node.left, node.right]
            elif node.left is not None and node.right is None:
                node.left.next = first_child(node.next)
                return [node.left]
            elif node.left is None and node.right is not None:
                node.right.next = first_child(node.next)
                return [node.right]
            else:
                return []

        queue = [root]
        while queue:
            top = queue.pop(0)
            queue.extend(work(top))


def main():
    solver = Solution()
    from utils import build_binary_tree
    tree = build_binary_tree([1,2,3,4,5,None, 7])
    print(tree)
    solver.connect(tree)
    print(tree)
    pass


if __name__ == '__main__':
    main()
    pass
