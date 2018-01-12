#!/usr/bin/env python
# coding: utf-8


class Solution:
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        if m > n:
            m, n = n, m

        def count_leq(x):
            """Count of elements less than or equal to x"""
            return sum(min(x // d, n) for d in range(1, m + 1))

        low = 1
        high = m * n
        while low < high:
            mid = (low + high) // 2
            if count_leq(mid) < k:
                low = mid + 1
            else:
                high = mid
        return low


if __name__ == '__main__':
    sol = Solution().findKthNumber
    print(sol(3, 3, 8))
