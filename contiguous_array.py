#!/usr/bin/env python
# coding: utf-8


class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict
        sums = defaultdict(list)
        sums[0].append(-1)
        s = 0
        for i, v in enumerate(nums):
            if v == 1:
                s += 1
            else:
                s -= 1
            sums[s].append(i)
        best = 0
        for lst in sums.values():
            best = max(best, max(lst) - min(lst))
        return best


if __name__ == '__main__':
    sol = Solution()
    print(sol.findMaxLength([0, ]))
