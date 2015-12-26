# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: missing number
#
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
# 
# For example,
# Given nums = [0, 1, 3] return 2.
# 
# Note:
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
# 
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Array
# Math
# Bit Manipulation
# 
# Show Similar Problems
# 
#  (H) First Missing Positive
#  (M) Single Number
#  (H) Find the Duplicate Number

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)


def main():
    solver = Solution()
    tests = [
        (([0, 1, 3],), 2),
    ]
    for params, expect in tests:
        print('-'*5 + 'TEST' + '-'*5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.missingNumber(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
