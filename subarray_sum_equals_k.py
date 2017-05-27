#!/usr/bin/env python3
# coding: utf-8

import sys


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0

        res = 0
        if k < 0:
            k = -k
            nums = [-v for v in nums]
        prefix = [(0, -1)]
        for i, v in enumerate(nums):
            prefix.append((prefix[-1][0] + v, i))
        prefix.sort()

        print(prefix)

        i, j = 0, 1
        while j < len(prefix):
            a, b = prefix[i], prefix[j]
            if a[0] + k < b[0]:
                i += 1
            elif a[0] + k > b[0]:
                j += 1
            else:
                jj = j
                while j < len(prefix) and a[0] + k == prefix[j][0]:
                    if a[1] < prefix[j][1]:
                        res += 1
                    j += 1
                i += 1
                j = jj
            while i >= j:
                j += 1
        return res


def main(args):
    sol = Solution()

    print(sol.subarraySum([1, 1, 1], 2))
    print(sol.subarraySum([-1, -1, 1], 1))
    print(sol.subarraySum([0, 0, 0], 0))
    return


if __name__ == '__main__':
    main(sys.argv[1:])
