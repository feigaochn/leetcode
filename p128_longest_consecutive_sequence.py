# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: longest consecutive sequence
#
# Given an unsorted array of integers, find the length of the longest
# consecutive elements sequence.
# 
# For example,
# Given [100, 4, 200, 1, 3, 2],
# The longest consecutive elements sequence is [1, 2, 3, 4]. Return its
# length: 4.
# 
# Your algorithm should run in O(n) complexity.
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Array
# Union Find
# 
# Show Similar Problems
# 
#  (M) Binary Tree Longest Consecutive Sequence


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bounds = {}
        best = 0
        for n in nums:
            if n in bounds:
                continue
            lo = bounds.get(n-1, (n, n))[0]
            hi = bounds.get(n+1, (n, n))[1]
            bounds[lo] = bounds[hi] = bounds[n] = (lo, hi)
            best = max(best, hi - lo + 1)
            # print(n, bounds)
        return best


def main():
    solver = Solution()
    tests = [
        (([100, 4, 200, 1, 3, 2],), '4'),
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.longestConsecutive(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
