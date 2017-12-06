#!/usr/bin/env python3
# coding: utf-8

# 643

class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        total = sum(nums[:k])
        best = total
        for p in range(k, len(nums)):
            total = total - nums[p - k] + nums[p]
            if total > best:
                best = total
        return best * 1.0 / k


import sys


def main(args):
    sol = Solution()
    print(sol.findMaxAverage([1, 12, -5, -6, 50, 3], k=4))


if __name__ == '__main__':
    main(sys.argv[1:])
