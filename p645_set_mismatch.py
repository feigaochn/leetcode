#!/usr/bin/env python
# coding: utf-8


class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        minus = n * (n + 1) // 2 - sum(nums)  # miss - dup
        minus2 = sum(i * i for i in range(1, n + 1)) - sum(map(lambda x: x * x, nums))  # miss^2 - dup^2
        plus = minus2 // minus
        miss = (minus + plus) // 2
        dup = (plus - minus) // 2

        return [dup, miss]


if __name__ == '__main__':
    sol = Solution()
    print(sol.findErrorNums([1, 2, 2, 4]))
    print(sol.findErrorNums([2, 2]))
