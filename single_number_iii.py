# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: single number iii
#
# Given an array of numbers nums, in which exactly two elements appear only
# once and all the other elements appear exactly twice. Find the two elements that appear only once.
# 
# For example:
# 
# Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].
# 
# Note:
# 
# The order of the result is not important. So in the above example, [5, 3] is also correct.
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
# 
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Bit Manipulation
# 
# Show Similar Problems
# 
#  (M) Single Number
#  (M) Single Number II


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        import functools
        import operator
        xor = functools.reduce(operator.xor, nums)
        diff = xor & (-xor)
        ns1, ns2 = 0, 0
        for n in nums:
            if n & diff == 0:
                ns1 ^= n
            else:
                ns2 ^= n
        return [ns1, ns2]


def main():
    solver = Solution()
    tests = [
        (([1, 2, 1, 3, 2, 5],), [3, 5]),
        (([-1, 0],), [0, -1]),
        (([-1139700704, -1653765433],), [-1139700704, -1653765433]),
        (([-1, -2],), [-2, -1])
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.singleNumber(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
