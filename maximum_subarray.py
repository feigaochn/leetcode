# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: maximum subarray
#
# Find the contiguous subarray within an array (containing at least one
# number) which has the largest sum.
# 
# For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
# the contiguous subarray [4,−1,2,1] has the largest sum = 6.
# 
# click to show more practice.
# More practice:
# If you have figured out the O(n) solution, try coding another solution
# using the divide and conquer approach, which is more subtle.
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Divide and Conquer
# Array
# Dynamic Programming
# 
# Show Similar Problems
# 
#  (M) Best Time to Buy and Sell Stock
#  (M) Maximum Product Subarray


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sums = nums[::]
        m, mi = sums[0], 0
        for i in range(1, len(nums)):
            sums[i] = max(sums[i - 1] + nums[i], nums[i])
            if sums[i] > m:
                m = sums[i]
                mi = i
        return m


def main():
    solver = Solution()
    tests = [
        (([-2, 1, -3, 4, -1, 2, 1, -5, 4],), 6),
        (([-1, -2, -3],), -1),
        (([1, -1, 1, -1],), 1),
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.maxSubArray(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
