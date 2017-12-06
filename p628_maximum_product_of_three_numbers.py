#!/usr/bin/env python
# coding: utf-8


class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        neg0, pos = [], []
        for num in nums:
            if num <= 0:
                neg0.append(num)
            elif num > 0:
                pos.append(num)
        neg0.sort(key=abs)
        pos.sort(key=abs)

        best = nums[0] * nums[1] * nums[2]
        if len(pos) >= 3:
            best = max(best, pos[-1] * pos[-2] * pos[-3])
        if len(pos) >= 1 and len(neg0) >= 2:
            best = max(best, pos[-1] * neg0[-1] * neg0[-2])

        if len(neg0) >= 3:
            best = max(best, neg0[0] * neg0[1] * neg0[2])
        if len(pos) >= 2 and len(neg0) >= 1:
            best = max(best, pos[-1] * pos[-2] * neg0[0])
        return best


if __name__ == '__main__':
    sol = Solution()
    print(sol.maximumProduct([1, 2, 3, 4]))
    print(sol.maximumProduct([1, 2, -3, -4]))
