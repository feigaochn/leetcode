# author: Fei Gao
# date: Sun Jun  1 19:01:18 2014
#
# Path Sum
#
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.


class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean

    def hasPathSum(self, root, sum):
        def gao(node, sum):
            if node.left is None and node.right is None:
                return sum == node.val
            if node.left is not None \
                    and gao(node.left, sum - node.val) is True:
                return True
            if node.right is not None \
                    and gao(node.right, sum - node.val) is True:
                return True
            return False
        return False if root is None else gao(root, sum)


def main():
    pass


if __name__ == '__main__':
    main()
    pass
