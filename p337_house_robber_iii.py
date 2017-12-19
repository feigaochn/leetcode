from utils import build_binary_tree, TreeNode


class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        def work(node: TreeNode):
            """Return (take, not take)
            """
            if node is None:
                return 0, 0
            l1, l2 = work(node.left)
            r1, r2 = work(node.right)
            return (l2 + node.val + r2, max(l1, l2) + max(r1, r2))

        r1, r2 = work(root)

        return max(r1, r2)


fn = Solution().rob
print(fn(build_binary_tree([3, 2, 3, 3, None, 1])))
print(fn(build_binary_tree([3, 4, 5, 1, 3, 1])))
print(fn(build_binary_tree([1, 4, 5, 1, 1, 10])))
