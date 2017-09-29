#!/usr/bin/env python
# coding: utf-8


# p655

from utils import build_binary_tree, TreeNode


class Solution:
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """

        def get_depth(node: TreeNode):
            if node is None:
                return 0
            else:
                return 1 + max(get_depth(node.left), get_depth(node.right))

        depth = get_depth(root)
        mat = [["" for _ in range(2 ** depth - 1)] for _ in range(depth)]

        def print_node(node: TreeNode, row, col: int):
            if node is None:
                return
            # print(row, col, node.val)
            mat[row - 1][col - 1] = str(node.val)
            print_node(node.left, row + 1, col - 2 ** (depth - row - 1))
            print_node(node.right, row + 1, col + 2 ** (depth - row - 1))

        print_node(root, 1, 2 ** (depth - 1))
        return mat
        # return '\n'.join(' '.join(line) for line in mat)


if __name__ == '__main__':
    sol = Solution()
    print(sol.printTree(build_binary_tree([1, 2])))
    print(sol.printTree(build_binary_tree([1, 2, 3, None, 4])))
    print(sol.printTree(build_binary_tree([1, 2, 5, 3, None, None, None, 4])))
