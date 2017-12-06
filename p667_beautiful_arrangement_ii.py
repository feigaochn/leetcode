#!/usr/bin/env python
# coding: utf-8

# p667

class Solution:
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        lst = []
        for i in range(k + 1):
            if i % 2 == 0:
                lst.append(i // 2 + 1)
            else:
                lst.append(k + 1 - (i // 2))
        return lst + list(range(k + 2, n + 1))


if __name__ == '__main__':
    sol = Solution()
    print(sol.constructArray(10, 1))
    print(sol.constructArray(10, 2))
    print(sol.constructArray(10, 3))
    print(sol.constructArray(10, 4))
    print(sol.constructArray(10, 5))
    print(sol.constructArray(10, 9))
