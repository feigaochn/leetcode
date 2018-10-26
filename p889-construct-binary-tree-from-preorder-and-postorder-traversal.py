"""
Return any binary tree that matches the given preorder and postorder traversals.

Values in the traversals pre and post are distinct positive integers.

Example 1:

Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]

Note:

1 <= pre.length == post.length <= 30
pre[] and post[] are both permutations of 1, 2, ..., pre.length.
It is guaranteed an answer exists. If there exists multiple answers, you can
return any of them.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from utils import TreeNode, build_binary_tree


class Solution:
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """

        def magic(pre, post):
            if not pre:
                return None
            elif len(pre) == 1:
                return TreeNode(pre[0])
            else:
                pv = pre[0]
                ll = post.index(pre[1]) + 1
                l = magic(pre[1 : 1 + ll], post[:ll])
                r = magic(pre[ll + 1 :], post[ll:-1])
                p = TreeNode(pv)
                p.left = l
                p.right = r
                return p

        return magic(pre, post)


sol = Solution().constructFromPrePost

print(sol(pre=[1, 2, 4, 5, 3, 6, 7], post=[4, 5, 2, 6, 7, 3, 1]))
