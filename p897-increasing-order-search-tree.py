
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root
        node = TreeNode(root.val)
        
        if root.right:
            rt = self.increasingBST(root.right)
            node.right = rt
        
        if root.left:
            head = self.increasingBST(root.left)
            tail = head
            while tail.right:
                tail = tail.right
            tail.right = node
            tail = node
        else:
            head = node
        return head
