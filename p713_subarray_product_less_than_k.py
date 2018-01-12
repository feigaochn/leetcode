#!/usr/bin/env python
# coding: utf-8

class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0
        prod = nums[0]
        head, tail = 0, 0
        count = 0
        while tail < len(nums):
            if head > tail:
                if head >= len(nums):
                    break
                tail = head
                prod = nums[tail]
            elif prod < k:
                # print(head, tail, prod)
                count += (tail - head + 1)
                tail += 1
                if tail == len(nums):
                    break
                prod *= nums[tail]
            else:
                prod //= nums[head]
                head += 1
        return count


if __name__ == '__main__':
    sol = Solution().numSubarrayProductLessThanK
    print(sol([10, 5, 2, 6], 100))
    print(sol([10, 5, 2, 6], 1))
    print(sol([10, 5, 2, 6], 0))
