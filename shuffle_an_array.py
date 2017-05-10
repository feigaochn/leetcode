#!/usr/bin/env python3
# coding: utf-8

"""A simple python3 script template.
"""

import random
import sys


class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.orig = nums[:]
        self.nums = nums[:]
        self.seed = 1
        random.seed(self.seed)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.nums = self.orig[:]
        return self.nums[:]

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        random.shuffle(self.nums)
        return self.nums[:]


def main(args):
    # Your Solution object will be instantiated and called as such:
    nums = [1, 2, 3]
    obj = Solution(nums)
    param_1 = obj.reset()
    param_2 = obj.shuffle()
    print(param_1, param_2)

    param_1 = obj.reset()
    param_2 = obj.shuffle()
    param_2 = obj.shuffle()
    param_2 = obj.shuffle()
    param_2 = obj.shuffle()
    param_2 = obj.shuffle()
    print(param_1, param_2)
    return


if __name__ == '__main__':
    main(sys.argv[1:])
