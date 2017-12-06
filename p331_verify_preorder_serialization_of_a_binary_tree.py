# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: verify preorder serialization of a binary tree
#
# One way to serialize a binary tree is to use pre-order traversal. When we
# encounter a non-null node, we record the node's value. If it is a null node,
# we record using a sentinel value such as #.
# 
#      _9_
#     /   \
#    3     2
#   / \   / \
#  4   1  #  6
# / \ / \   / \
# # # # #   # #
# 
# For example, the above binary tree can be serialized to the string
# "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.
# 
# Given a string of comma separated values, verify whether it is a correct
# preorder traversal serialization of a binary tree. Find an algorithm without
# reconstructing the tree.
# Each comma separated value in the string must be either an integer or a
# character '#' representing null pointer.
# You may assume that the input format is always valid, for example it could
# never contain two consecutive commas such as "1,,3".
# Example 1:
# "9,3,4,#,#,1,#,#,2,#,6,#,#"
# Return true
# Example 2:
# "1,#"
# Return false
# Example 3:
# "9,#,#,1"
# Return false
# Credits:Special thanks to @dietpepsi for adding this problem and creating
# all test cases.
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Stack


class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        tree = ''.join('n' if c != '#' else '#' for c in preorder.split(','))
        while tree.count('n##'):
            tree = tree.replace('n##', '#')
        return tree == '#'


def main():
    solver = Solution()
    tests = [
        (("9,3,4,#,#,1,#,#,2,#,6,#,#",), 1),
        (("1,#",), 0),
        (("1,#,#,1",), 0)
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.isValidSerialization(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
