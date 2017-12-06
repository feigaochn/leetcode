# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: patching array
#
# Given a sorted positive integer array nums and an integer n, add/patch
# elements to the array such that any number in range [1, n] inclusive can be
# formed by the sum of some elements in the array. Return the minimum number
# of patches required.
# 
# Example 1:
# nums = [1, 3], n = 6
# Return 1.
# Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3,
# 4.
# Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3],
# [2,3], [1,2,3].
# Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
# So we only need 1 patch.
# Example 2:
# nums = [1, 5, 10], n = 20
# Return 2.
# The two patches can be [2, 4].
# Example 3:
# nums = [1, 2, 2], n = 5
# Return 0.
# Credits:Special thanks to @dietpepsi for adding this problem and creating
# all test cases.
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Greedy


class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: list[int]
        :type n: int
        :rtype: int
        """
        len1 = len(nums)
        idx = 0
        s = 0
        while True:
            if s >= n:
                break
            if idx >= len(nums) or s + 1 < nums[idx]:
                nums.insert(idx, s + 1)
            s += nums[idx]
            idx += 1
        # print(nums)
        return len(nums) - len1


def main():
    solver = Solution()
    tests = [
        (([1, 3], 6), 1),
        (([], 7), 3),
        (([1, 5, 10], 20), 2),
        (([1, 2, 2], 5), 0),
        (([1, 2, 31, 33], 2147483647), '?'),
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.minPatches(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
