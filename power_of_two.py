# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: power of two
#
# Given an integer, write a function to determine if it is a power of two.
# 
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Math
# Bit Manipulation
# 
# Show Similar Problems
# 
#  (E) Number of 1 Bits


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n != 0 and (n & (-n)) == n


def main():
    solver = Solution()
    tests = [
        (('param',), 'result'),
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.isPowerOfTwo(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
