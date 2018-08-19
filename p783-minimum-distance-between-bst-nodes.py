"""
Given a Binary Search Tree (BST) with the root node root, return the minimum
difference between the values of any two different nodes in the tree.

Example :

Input: root = [4,2,6,1,3,null,null]
Output: 1
Explanation:
Note that root is a TreeNode object, not an array.

The given tree [4,2,6,1,3,null,null] is represented by the following diagram:

          4
        /   \
      2      6
     / \    
    1   3  

while the minimum difference in this tree is 1, it occurs between node 1 and
node 2, also between node 3 and node 2.

Note:
    The size of the BST will be between 2 and 100.
    The BST is always valid, each node's value is an integer, and each node's
    value is different.
"""

# Definition for a binary tree node.


# class TreeNode:

#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        from math import inf

        def go(node):
            diff = inf
            val = node.val
            if node.left:
                (l1, l2), ld = go(node.left)
                lower = l1
                diff = min(diff, ld, val - l2)
            else:
                lower = node.val
            if node.right:
                (r1, r2), rd = go(node.right)
                upper = r2
                diff = min(diff, rd, r1 - val)
            else:
                upper = val
            return (lower, upper), diff

        (l, u), d = go(root)
        return d


sol = Solution().minDiffInBST

from utils.binary_tree import build_binary_tree, null

root = build_binary_tree([4, 2, 6, 1, 3, null, null])
print(sol(root))

root = build_binary_tree([27, null, 34, null, 58, 50, null, 44, null, null, null])
print(sol(root))
