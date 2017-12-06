# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: longest increasing subsequence
#
# Given an unsorted array of integers, find the length of longest increasing
# subsequence.
# 
# For example,
# Given [10, 9, 2, 5, 3, 7, 101, 18],
# The longest increasing subsequence is [2, 3, 7, 101], therefore the length
# is 4. Note that there may be more than one LIS combination, it is only
# necessary for you to return the length.
# 
# Your algorithm should run in O(n2) complexity.
# 
# Follow up: Could you improve it to O(n log n) time complexity?
# Credits:Special thanks to @pbrother for adding this problem and creating all
# test cases.
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Dynamic Programming
# Binary Search


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2: return n
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


def main():
    solver = Solution()
    tests = [
        (([10, 9, 2, 5, 3, 7, 101, 18],), 4),
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.lengthOfLIS(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
