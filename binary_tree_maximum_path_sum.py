# author: Fei Gao
# date: Sun Jun  1 12:41:21 2014
#
# Binary Tree Maximum Path Sum
#
# Given a binary tree, find the maximum path sum.
# The path may start and end at any node in the tree.
# For example:
# Given the below binary tree,
#        1
#       / \
#      2   3
# Return 6.


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from node import TreeNode


class Solution:
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        if root is None:
            return 0
        # isinstance(root, TreeNode)

        def gao(node):
            if node.left is not None and node.right is not None:
                l_max_sum, l_max_path = gao(node.left)
                r_max_sum, r_max_path = gao(node.right)
                max_path = max(l_max_path, r_max_path, 0) + node.val
                max_sum = max(l_max_sum, r_max_sum,
                              max(l_max_path, r_max_path, 0) + node.val,
                              l_max_path + node.val + r_max_path)
            elif node.left is not None and node.right is None:
                l_max_sum, l_max_path = gao(node.left)
                max_sum = max(l_max_sum, max(l_max_path, 0) + node.val)
                max_path = max(l_max_path, 0) + node.val
            elif node.left is None and node.right is not None:
                r_max_sum, r_max_path = gao(node.right)
                max_sum = max(r_max_sum, max(r_max_path, 0) + node.val)
                max_path = max(r_max_path, 0) + node.val
            else:
                max_sum, max_path = node.val, node.val

            return max_sum, max_path

        result, _ = gao(root)

        return result
        pass


def main():
    solver = Solution()
    root = TreeNode().build_from_list([1, 2, 3])
    print(solver.maxPathSum(root))
    pass


if __name__ == '__main__':
    main()
    pass
