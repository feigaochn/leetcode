# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: find the duplicate number
#
# Given an array nums containing n + 1 integers where each integer is
# between 1 and n (inclusive), prove that at least one duplicate number
# must exist. Assume that there is only one duplicate number, find the
# duplicate one.
# 
# Note:
# 
# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n2).
# There is only one duplicate number in the array, but it could be repeated
# more than once.
# 
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Array
# Two Pointers
# Binary Search
# 
# Show Similar Problems
# 
#  (H) First Missing Positive
#  (M) Single Number
#  (M) Linked List Cycle II
#  (M) Missing Number


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) - 1
        lo, hi = 1, n
        while lo < hi:
            guess = (lo + hi) // 2
            if sum(1 for v in nums if lo <= v <= guess) > guess - lo + 1:
                hi = guess
            else:
                lo = guess + 1
        return lo


def main():
    solver = Solution()
    tests = [
        (([1, 1],), 1),
        (([2, 2, 1],), 2),
        (([1, 2, 3, 4, 5, 3],), 3),
        (([1, 3, 3, 3, 5, 3],), 3),
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.findDuplicate(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
