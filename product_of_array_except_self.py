# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: product of array except self
#
# Given an array of n integers where n > 1, nums, return an array output
# such that output[i] is equal to the product of all the elements of nums except nums[i].
# Solve it without division and in O(n).
# For example, given [1,2,3,4], return [24,12,8,6].
# 
# Follow up:
# Could you solve it with constant space complexity? (Note: The output array does not
# count as extra space for the purpose of space complexity analysis.)
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Array
# 
# Show Similar Problems
# 
#  (H) Trapping Rain Water
#  (M) Maximum Product Subarray
#  (H) Paint House II


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = [1 for n in nums]
        p = 1
        for i in range(len(nums)):
            output[i] *= p
            p *= nums[i]
        p = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= p
            p *= nums[i]
        return output


def main():
    solver = Solution()
    tests = [
        (([1, 2, 3, 4],), [24, 12, 8, 6]),
        (([1],), [1]),
        (([3, 4],), [4, 3])
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.productExceptSelf(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
