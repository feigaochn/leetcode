# Binary Tree Level Order Traversal II
#
# Total Accepted: 10832 Total Submissions: 35078 My Submissions
#
# Given a binary tree, return the bottom-up level order traversal of its nodes'
# values. (ie, from left to right, level by level from leaf to root).
#
# For example:
# Given binary tree {3,9,20,#,#,15,7},
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]
#

from node import TreeNode


class Solution:
    # @param root, a tree node
    # @return a list of lists of integers

    def levelOrderBottom(self, root):
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
            result.append(values)
        return result[::-1]

if __name__ == '__main__':
    root = TreeNode()
    root.build_from_list([3, 9, 20, None, None, 15, 7])
    res = Solution().levelOrderBottom(root)
    print(res)
