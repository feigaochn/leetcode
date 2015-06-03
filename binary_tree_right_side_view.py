# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def rightSideView(self, root):
        right = list()
        if not root:
            return right
        currentLevel = [root]
        while currentLevel:
            nextLevel = list()
            right.append(currentLevel[-1].val)
            for node in currentLevel:
                if node.left: nextLevel.append(node.left)
                if node.right: nextLevel.append(node.right)
            currentLevel = nextLevel
        return right
        