# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: count of smaller numbers after self
#
# You are given an integer array nums and you have to return a new counts
# array.
# The counts array has the property where counts[i] is
# the number of smaller elements to the right of nums[i].
# 
# Example:
# 
# Given nums = [5, 2, 6, 1]
# 
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.
# 
# Return the array [2, 1, 1, 0].
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Divide and Conquer
# Binary Indexed Tree
# Segment Tree
# Binary Search Tree
# 
# Show Similar Problems
# 
#  (H) Count of Range Sum


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        import bisect
        buffer = []
        result = []
        for v in nums[::-1]:
            result.append(bisect.bisect_left(buffer, v))
            buffer.insert(result[-1], v)
        return result[::-1]


def main():
    solver = Solution()
    tests = [
        (([5, 2, 6, 1],), [2, 1, 1, 0]),
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.countSmaller(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
