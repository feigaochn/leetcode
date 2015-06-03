# author: Fei Gao
# date: Sun Jun  1 18:59:01 2014
#
# Binary Tree Level Order Traversal
#
# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
# For example:
# Given binary tree {3,9,20,#,#,15,7},
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
# confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.
# OJ's Binary Tree Serialization:
# The serialization of a binary tree follows a level order traversal, where '#' signifies a path terminator where no node exists below.
# Here's an example:
#    1
#   / \
#  2   3
#     /
#    4
#     \
#      5
# The above binary tree is serialized as "{1,2,3,#,#,4,#,#,5}".


class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
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
        return result


def main():
    solver = Solution()
    pass


if __name__ == '__main__':
    main()
    pass
