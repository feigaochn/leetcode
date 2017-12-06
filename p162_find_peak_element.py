# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: find peak element
#
# A peak element is an element that is greater than its neighbors.
# Given an input array where num[i] ≠ num[i+1], find a peak element and return
# its index.
# The array may contain multiple peaks, in that case return the index to any
# one of the peaks is fine.
# You may imagine that num[-1] = num[n] = -∞.
# For example, in array [1, 2, 3, 1], 3 is a peak element and your function
# should return the index number 2.
# click to show spoilers.
# Note:
# Your solution should be in logarithmic complexity.
# 
# Credits:Special thanks to @ts for adding this problem and creating all test
# cases.
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Array
# Binary Search


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i, n in enumerate(nums):
            if ((i == 0 or (i > 0 and n > nums[i-1]))
                and (i == len(nums)-1 or (i < len(nums) - 1 and n > nums[i+1]))):
                return i


def main():
    solver = Solution()
    tests = [
        (([1, 2, 3, 1],), 2),
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.findPeakElement(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
