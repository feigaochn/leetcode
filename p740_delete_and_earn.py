#!/usr/bin/env python
# coding: utf-8


"""
Given an array nums of integers, you can perform operations on the array.

In each operation, you pick any nums[i] and delete it to earn nums[i] points. After, you must delete every element equal to nums[i] - 1 or nums[i] + 1.

You start with 0 points. Return the maximum number of points you can earn by applying such operations.
"""


class Solution:
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        from itertools import groupby
        nums = [(v, v * len(list(gp))) for v, gp in groupby(nums)]
        dp_take = dp_notake = 0
        pre_v = -10
        for v, s in nums:
            if v > pre_v + 1:
                dp_take_new = s + max(dp_take, dp_notake)
                dp_notake_new = max(dp_take, dp_notake)
            elif v == pre_v + 1:
                dp_take_new = s + dp_notake
                dp_notake_new = max(dp_take, dp_notake)
            pre_v = v
            dp_take = dp_take_new
            dp_notake = dp_notake_new
        return max(dp_take, dp_notake)


if __name__ == '__main__':
    sol = Solution().deleteAndEarn
    print(sol([3, 4, 2]), 6)
    print(sol([2, 2, 3, 3, 3, 4]), 9)
