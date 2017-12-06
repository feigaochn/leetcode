# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: lowest common ancestor of a binary search tree
#
# Given a binary search tree (BST), find the lowest common ancestor (LCA)
# of two given nodes in the BST.
# 
# According to the definition of LCA on Wikipedia: “The lowest common
# ancestor is defined between two nodes v and w as the lowest node in T
# that has both v and w as descendants (where we allow a node to be a
# descendant of itself).”
# 
#         _______6______
#        /              \
#     ___2__          ___8__
#    /      \        /      \
#    0      _4       7       9
#          /  \
#          3   5
# 
# For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6.
# Another example is LCA of nodes 2 and 4 is 2, since a node can be a
# descendant of itself according to the LCA definition.
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Tree
# 
# Show Similar Problems
# 
#  (M) Lowest Common Ancestor of a Binary Tree


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val <= root.val <= q.val or q.val <= root.val <= p.val:
            return root
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)


def main():
    from node.btree import TreeNode
    root = TreeNode()
    root.build_from_list([6, 2, 8, 0, 4, 7, 9, 3, 5])
    root.print_mlr()
    solver = Solution()
    tests = [
        ((root, root.left, root.right), root),
        ((root, root.left, root.left.left), root.left),
        ((root, root.left.left, root.left.right), root.left),
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect.val))

        result = solver.lowestCommonAncestor(*params)
        print('Result: ' + str(result.val))
    pass


if __name__ == '__main__':
    main()
    pass
