# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: binary search tree iterator
#
# Implement an iterator over a binary search tree (BST). Your iterator will be
# initialized with the root node of a BST.
# Calling next() will return the next smallest number in the BST.
# Note: next() and hasNext() should run in average O(1) time and uses O(h)
# memory, where h is the height of the tree.
# Credits:Special thanks to @ts for adding this problem and creating all test
# cases.
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Tree
# Stack
# Design
# 
# Show Similar Problems
# 
#  (M) Binary Tree Inorder Traversal
#  (M) Flatten 2D Vector
#  (M) Zigzag Iterator
#  (M) Peeking Iterator
#  (M) Inorder Successor in BST


# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return 'Node({})'.format(self.val)

    def __repr__(self):
        return self.__str__()


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.head = TreeNode(None)
        self.head.left = root

        self.nodes = [self.head]
        while self.nodes[-1].left is not None:
            self.nodes.append(self.nodes[-1].left)

        print(self.nodes)

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.nodes[-1] != self.head

    def next(self):
        """
        :rtype: int
        """
        val = self.nodes[-1].val

        if self.nodes[-1].right is not None:
            self.nodes.append(self.nodes[-1].right)
            while self.nodes[-1].left is not None:
                self.nodes.append(self.nodes[-1].left)
        else:
            while self.nodes[-1] == self.nodes[-2].right:
                self.nodes.pop()
            self.nodes.pop()
        return val


# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())

def main():
    # Your BSTIterator will be called like this:
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(2)

    i, v = BSTIterator(root), []
    while i.hasNext():
        print('has next')
        v.append(i.next())
    print(v)


if __name__ == '__main__':
    main()
    pass
