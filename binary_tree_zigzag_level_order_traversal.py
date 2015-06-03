# Binary Tree Zigzag Level Order Traversal
#
# Total Accepted: 9332 Total Submissions: 35534 My Submissions
#
# Given a binary tree, return the zigzag level order traversal of its nodes'
# values. (ie, from left to right, then right to left for the next level and
# alternate between).
#
# For example:
#
# Given binary tree {3,9,20,#,#,15,7},
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# return its zigzag level order traversal as:
#
# [
#       [3],
#       [20,9],
#       [15,7]
# ]

from node import TreeNode


class Solution:
    # @param root, a tree node
    # @return a list of lists of integers

    def zigzagLevelOrder(self, root):
        if root is None:
            return []
        result = []
        cur_level = [root]
        next_level = []
        while len(cur_level) > 0:
            values = []
            for node in cur_level:
                values.append(node.val)
                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)
            cur_level = next_level
            next_level = []
            result.append(values if len(result) % 2 == 0 else values[::-1])
        return result


if __name__ == '__main__':
    root = TreeNode()
    root.build_from_list([3, 9, 20, None, None, 15, 7])
    res = Solution().zigzagLevelOrder(root)
    print(res)
