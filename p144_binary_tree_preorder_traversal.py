# author: Fei Gao
#
# Binary Tree Preorder Traversal
#
# Given a binary tree, return the preorder traversal of its nodes' values.
# For example:
# Given binary tree {1,#,2,3},
#    1
#     \
#      2
#     /
#    3
# return [1,2,3].
# Note: Recursive solution is trivial, could you do it iteratively?

from node import TreeNode


class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        preorder = []
        if root is None:
            return preorder
        queue = [root]
        while len(queue) != 0:
            node = queue.pop(0)
            preorder.append(node.val)
            if node.right is not None:
                queue.insert(0, node.right)
            if node.left is not None:
                queue.insert(0, node.left)
        return preorder


def main():
    solver = Solution()
    for test in [[1, None, 2, None, None, 3]]:
        root = TreeNode()
        root.build_from_list(test)
        print(solver.preorderTraversal(root))
    pass


if __name__ == '__main__':
    main()
    pass
