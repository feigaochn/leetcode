# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: intersection of two arrays
#
# Given two arrays, write a function to compute their intersection.
# 
# Example:
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].
# 
# Note:
# 
# Each element in the result must be unique.
# The result can be in any order.
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Binary Search
# Hash Table
# Two Pointers
# Sort


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1).intersection(set(nums2)))


def main():
    solver = Solution()
    tests = [
        (([1, 2, 2, 1], [2, 2]), [2]),
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.intersection(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
