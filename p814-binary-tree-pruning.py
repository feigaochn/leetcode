# We are given the head node root of a binary tree, where additionally every
# node's value is either a 0 or a 1.

# Return the same tree where every subtree (of the given tree) not containing a
# 1 has been removed.

# (Recall that the subtree of a node X is X, plus every node that is a
# descendant of X.)

# Definition for a binary tree node.
class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root

        l = self.pruneTree(root.left)
        r = self.pruneTree(root.right)
        root.left = l
        root.right = r

        if root.left is None and root.right is None and root.val == 0:
            return None
        else:
            return root
