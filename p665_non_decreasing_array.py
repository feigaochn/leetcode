#!/usr/bin/env python
# coding: utf-8

# p665


class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        jumps = []
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                jumps.append(i)
        if len(jumps) == 0:
            return True
        elif len(jumps) >= 2:
            return False
        else:
            j = jumps[0]
            if j == 0 or j == len(nums) - 2:
                return True
            else:
                return nums[j] <= nums[j + 2] or nums[j - 1] <= nums[j + 1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.checkPossibility([4, 2, 3]))
    print(sol.checkPossibility([-1, 4, 2, 3]))
    print(sol.checkPossibility([4, 2, 1]))
    print(sol.checkPossibility([1, 2, 3, 1]))
    print(sol.checkPossibility([2, 3, 3, 2, 4]))
