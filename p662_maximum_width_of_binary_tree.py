#!/usr/bin/env python
# coding: utf-8


class Solution:
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        from collections import defaultdict, deque
        levels = defaultdict(set)
        # levels[0].add(0)
        queue = deque()
        queue.append((0, 0, root))
        while queue:
            depth, idx, node = queue.popleft()
            levels[depth].add(idx)
            if node.left:
                queue.append((depth + 1, idx * 2, node.left))
            if node.right:
                queue.append((depth + 1, idx * 2 + 1, node.right))
        return max(max(row) - min(row) + 1 for row in levels.values())


if __name__ == '__main__':
    from utils import build_binary_tree

    sol = Solution().widthOfBinaryTree
    print(sol(build_binary_tree([1, 2, 3, 4, None, None, 5])))
