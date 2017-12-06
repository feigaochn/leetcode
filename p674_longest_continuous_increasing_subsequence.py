#!/usr/bin/env python
# coding: utf-8

# p674


class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length <= 1:
            return length
        inc = 1
        ret = 1
        last = nums[0]
        for num in nums[1:]:
            if num > last:
                inc += 1
                ret = max(ret, inc)
            else:
                inc = 1
            last = num
        return ret


if __name__ == '__main__':
    sol = Solution()
    print(sol.findLengthOfLCIS([1, 3, 5, 4, 7]))
    print(sol.findLengthOfLCIS([2, 2]))
