# Minimum Depth of Binary Tree
#
# Total Accepted: 13698 Total Submissions: 47167 My Submissions
#
# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the
# root node down to the nearest leaf node.Minimum Depth of Binary Tree Total
# Accepted: 13698 Total Submissions: 47167 My Submissions Given a binary tree,
# find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the
# root node down to the nearest leaf node.

from node import TreeNode


class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        return self.min_depth(root) if root is not None else 0

    # copy from node.py
    def min_depth(self, root):
        """
        find minimum depth of self
        """
        # bfs
        depth = 1
        found_leaf = False
        cur_depth = [root]
        next_depth = []
        while True:
            next_depth = []
            for node in cur_depth:
                is_leaf = True
                if node.left is not None:
                    next_depth.append(node.left)
                    is_leaf = False
                if node.right is not None:
                    next_depth.append(node.right)
                    is_leaf = False
                if is_leaf is True:
                    found_leaf = True
                    break
            if found_leaf is True:
                break
            else:
                depth += 1
                cur_depth = next_depth
        return depth


if __name__ == '__main__':
    root = TreeNode()
    root.build_from_list(list(range(10)))
    print(Solution().minDepth(root))
