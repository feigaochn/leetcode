# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: trapping rain water
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it is able to trap after raining.
# 
# For example,
# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
# 
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
# In this case, 6 units of rain water (blue section) are being trapped. Thanks
# Marcos for contributing this image!
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Array
# Stack
# Two Pointers
# 
# Show Similar Problems
# 
#  (M) Container With Most Water
#  (M) Product of Array Except Self


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left = height[::]
        right = height[::]
        for i in range(1, n):
            left[i] = max(left[i - 1], height[i - 1])
            right[n - i - 1] = max(right[n - i], height[n - i])
        return sum(max(0, min(left[i], right[i]) - height[i]) for i in range(n))


def main():
    solver = Solution()
    tests = [
        (([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],), 6),
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.trap(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
