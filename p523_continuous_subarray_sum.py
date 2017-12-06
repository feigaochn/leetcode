#!/usr/bin/env python
# coding: utf-8


class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k < 0:
            k = -k
        if k == 0:
            k = sum(nums) + 1
        from collections import defaultdict
        mods = defaultdict(list)  # type: Map[int, List[int]]
        mods[0].append(-1)
        s = 0
        for i, v in enumerate(nums):
            s += v
            mods[s % k].append(i)

        # print(mods)
        for vals in mods.values():
            if len(vals) >= 2 and vals[-1] - vals[0] > 1:
                return True
        return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.checkSubarraySum([23, 2, 6, 4, 7], 6))
    print(sol.checkSubarraySum([23, 2, 6, 4, 7], 0))
