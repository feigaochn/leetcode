# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: find minimum in rotated sorted array
#
# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# Find the minimum element.
# You may assume no duplicate exists in the array.
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
#  (H) Search in Rotated Sorted Array
#  (H) Find Minimum in Rotated Sorted Array II


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        hi = len(nums) - 1
        while True:
            if nums[low] <= nums[hi]:
                return nums[low]
            mi = (low + hi)//2
            if nums[mi] >= nums[low]:
                low = mi + 1
            else:
                hi = mi



def main():
    solver = Solution()
    tests = [
        (([1,2,0],), 0),
        (([1,0],), 0),
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
