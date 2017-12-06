#!/usr/bin/env python
# coding: utf-8


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = max(nums)
        try:
            max2 = max(n for n in nums if n < max1)
            max3 = max(n for n in nums if n < max2)
            return max3
        except ValueError:
            return max1


if __name__ == '__main__':
    sol = Solution()
    print(sol.thirdMax([3, 2, 1]))
    print(sol.thirdMax([3, 2]))
    print(sol.thirdMax([3, 2, 2, 1]))
