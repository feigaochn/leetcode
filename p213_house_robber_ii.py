# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: house robber ii
#
# Note: This is an extension of House Robber.
# After robbing those houses on that street, the thief has found himself a new
# place for his thievery so that he will not get too much attention. This
# time, all houses at this place are arranged in a circle. That means the
# first house is the neighbor of the last one. Meanwhile, the security system
# for these houses remain the same as for those in the previous street.
# Given a list of non-negative integers representing the amount of money of
# each house, determine the maximum amount of money you can rob tonight
# without alerting the police.
# Credits:Special thanks to @Freezen for adding this problem and creating all
# test cases.
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Dynamic Programming
# 
# Show Similar Problems
# 
#  (E) House Robber
#  (M) Paint House
#  (E) Paint Fence
#  (M) House Robber III


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) < 3:
            return max(nums)
        n = len(nums)

        def best(ns):
            take, leave = ns[0], 0
            for v in ns[1:]:
                take, leave = max(take, leave + v), max(take, leave)
            return max(take, leave)

        return max(best(nums[1:]), best(nums[:-1]))


def main():
    solver = Solution()
    tests = [
        (([1],), 1),
        (([1, 3],), 3),
        (([1, 2, 3],), 3),
        (([1, 2, 3, 4],), 6),
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.rob(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
