#!/usr/bin/env python
# coding: utf-8


class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict
        vps = defaultdict(int)
        for p, v in enumerate(nums):
            vps[v] += 1
        best = 0
        for v in vps:
            if v + 1 in vps:
                best = max(best, vps[v] + vps[v + 1])
        return best


if __name__ == '__main__':
    sol = Solution()
    print(sol.findLHS([1, 3, 2, 2, 5, 2, 3, 7]))
    print(sol.findLHS([1, 1, 1]))
