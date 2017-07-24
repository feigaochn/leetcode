#!/usr/bin/env python
# coding: utf-8


class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        from collections import defaultdict
        level_nodes = defaultdict(list)

        def dfs(node, lv):
            if not node:
                return
            else:
                level_nodes[lv].append(node.val)
                dfs(node.left, lv + 1)
                dfs(node.right, lv + 1)

        dfs(root, 0)

        averages = []
        for lv, values in level_nodes.items():
            averages.append((lv, sum(values) / len(values)))
        return [av for _, av in sorted(averages)]


if __name__ == '__main__':
    sol = Solution()
    print(sol)
