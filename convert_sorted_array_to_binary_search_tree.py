# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: convert sorted array to binary search tree
#
# Given an array where elements are sorted in ascending order,
# convert it to a height balanced BST.
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Tree
# Depth-first Search
# 
# Show Similar Problems
# 
#  (M) Convert Sorted List to Binary Search Tree


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return '[{}, {}, {}]'.format(self.val, str(self.left), str(self.right))

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        n = len(nums)
        if n < 1: return None
        lo, hi = 0, n-1
        mi = (lo + hi + 1) // 2
        root = TreeNode(nums[mi])
        if mi - lo > 0:
            root.left = self.sortedArrayToBST(nums[lo:mi])
        if hi - mi > 0:
            root.right = self.sortedArrayToBST(nums[mi+1:hi+1])
        return root


def main():
    solver = Solution()
    tests = [
        ((range(1),), None),
        ((range(2),), None),
        ((range(3),), None),
        ((range(5),), None),
        ((range(15),), None),
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.sortedArrayToBST(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
