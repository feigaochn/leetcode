#!/usr/bin/env python
# coding: utf-8

# p540


class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 3:
            return nums[0] ^ nums[1] ^ nums[2]
        pivot = len(nums) // 2
        pivot -= (pivot % 2)
        if nums[pivot] == nums[pivot + 1]:
            return self.singleNonDuplicate(nums[pivot + 2:])
        else:
            return self.singleNonDuplicate(nums[:pivot + 1])


if __name__ == '__main__':
    sol = Solution()
    print(sol.singleNonDuplicate([1]))
    print(sol.singleNonDuplicate([1, 1, 2]))
    print(sol.singleNonDuplicate([1, 2, 2]))
    print(sol.singleNonDuplicate([1, 2, 2, 3, 3]))
    print(sol.singleNonDuplicate([1, 1, 2, 3, 3]))
    print(sol.singleNonDuplicate([1, 1, 2, 2, 3]))
    print(sol.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))
    print(sol.singleNonDuplicate([1, 1, 2, 2, 3, 4, 4, 8, 8]))
    print(sol.singleNonDuplicate([1, 2, 2, 3, 3, 4, 4, 8, 8]))
