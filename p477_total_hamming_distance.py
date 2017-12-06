#!/usr/bin/env python3
# coding: utf-8

import sys
from math import log2


class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        for b in range(31):
            zero = one = 0
            for num in nums:
                if num & (1 << b):
                    one += 1
                else:
                    zero += 1
            ret += one * zero
        return ret


def main(args):
    print(Solution().totalHammingDistance(list(range(10 ** 4))))
    # print(log2(10 ** 9), 2 ** 30)
    return


if __name__ == '__main__':
    main(sys.argv[1:])
