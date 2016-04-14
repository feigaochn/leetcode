# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: binary tree paths
#
# Given a binary tree, return all root-to-leaf paths.
# 
# For example, given the following binary tree:
# 
#    1
#  /   \
# 2     3
#  \
#   5
# 
# All root-to-leaf paths are:
# ["1->2->5", "1->3"]
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
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
#  (M) Path Sum II


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from utils import *


class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        results = []
        def gao(node, pre):
            if node is not None:
                leaf = True
                if node.left:
                    gao(node.left, pre + [node.val])
                    leaf = False
                if node.right:
                    gao(node.right, pre + [node.val])
                    leaf = False
                if leaf:
                    results.append(pre + [node.val])
        gao(root, [])
        # print(results)
        return ['->'.join(map(str, path)) for path in results]


def main():
    solver = Solution()
    tests = [
        ((build_binary_tree([1, 2, 3, None, 5]),), ['1->2->5', '1->3']),
        ((build_binary_tree([]),), []),
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.binaryTreePaths(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
