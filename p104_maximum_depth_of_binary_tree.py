# author: Fei Gao
# date: Sun Jun  1 14:19:20 2014
#
# Maximum Depth Of Binary Tree
#
# Given a binary tree, find its maximum depth.
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
#
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

    def maxDepth(self, root):

        def max_depth(root):
            """
            find maximum depth of root
            """
            # bfs
            depth = 0
            cur_depth = [root]
            while len(cur_depth) != 0:
                next_depth = []
                for node in cur_depth:
                    if node.left is not None:
                        next_depth.append(node.left)
                    if node.right is not None:
                        next_depth.append(node.right)
                depth += 1
                cur_depth = next_depth
            return depth

        return max_depth(root) if root is not None else 0


def main():
    solver = Solution()
    root = TreeNode()
    root.build_from_list([1, 2, 3, 4])
    print(solver.maxDepth(root))
    pass


if __name__ == '__main__':
    main()
    pass
