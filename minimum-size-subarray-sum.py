# coding: utf-8

# author: Fei Gao
#
# Minimum Size Subarray Sum
#
# Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return 0 instead.
# For example, given the array [2,3,1,2,4,3] and s = 7,
# the subarray [4,3] has the minimal length under the problem constraint.
# click to show more practice.
# More practice:
# If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).


class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        cum = [0]
        for n in nums:
            cum.append(cum[-1] + n)
        if cum[-1] < s:
            return 0
        p1 = p2 = 0
        width = len(nums)
        while p1 <= p2 <= len(nums):
            if cum[p2] - cum[p1] >= s:
                width = min(width, p2 - p1)
                p1 += 1
            else:
                p2 += 1
        return width


def main():
    solver = Solution()
    tests = [
        (7, [2, 3, 1, 2, 4, 3])
    ]
    for test in tests:
        print(test)
        print(' ->')
        result = solver.minSubArrayLen(*test)
        print(result)
        print('~' * 10)
    pass


if __name__ == '__main__':
    main()
    pass
