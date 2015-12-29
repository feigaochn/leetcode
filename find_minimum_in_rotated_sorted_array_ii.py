# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: find minimum in rotated sorted array ii
#
# Follow up for "Find Minimum in Rotated Sorted Array":
# What if duplicates are allowed?
# Would this affect the run-time complexity? How and why?
# 
# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# Find the minimum element.
# The array may contain duplicates.
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Array
# Binary Search
# 
# Show Similar Problems
# 
#  (M) Find Minimum in Rotated Sorted Array


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        hi = len(nums) - 1
        while low <= hi:
            if nums[low] == nums[hi]:
                hi -= 1
                continue
            mi = (low + hi) // 2
            # print(low, mi, hi)
            if nums[mi] <= nums[hi]:
                hi = mi
            else:
                low = mi + 1
        return nums[low]


def main():
    solver = Solution()
    tests = [
        (([2, 3, 4, 0, 1],), 0),
        (([2, 3, 4, 4, 0, 1],), 0),
        (([2, 3, 4, 0, 0, 1],), 0),
        (([2, 3, 4, 0, 1, 2],), 0),
        (([1, 0, 1, 1, 1],), 0),
        (([0],), 0)
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.findMin(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
