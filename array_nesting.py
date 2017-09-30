#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 23:18:09 2017

@author: feigao
"""


class Solution:
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        longest = 0
        for n in range(len(nums)):
            if n in seen:
                continue
            else:
                length = 0
                while n not in seen:
                    seen.add(n)
                    n = nums[n]
                    length += 1
                if length > longest:
                    longest = length
        return longest


sol = Solution()
print(sol.arrayNesting([5, 4, 0, 3, 1, 6, 2]))
print(sol.arrayNesting(list(range(1, 20000)) + [0]))
