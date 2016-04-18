# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: power of four
#
# Given an integer (signed 32 bits), write a function to check whether it is a
# power of 4.
#
# Example:
# Given num = 16, return true.
# Given num = 5, return false.
#
# Follow up: Could you solve it without loops/recursion?
#
# Credits:Special thanks to @yukuairoy  for adding this problem and creating
# all test cases.
#
# Subscribe to see which companies asked this question
#
# Show Tags
#
# Bit Manipulation
#
# Show Similar Problems
#
#  (E) Power of Two
#  (E) Power of Three


class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        s = '{:b}'.format(num)
        return s.count('1') == 1 and s.count('0') % 2 == 0 and s.count('-') == 0


def main():
    solver = Solution()
    tests = [
        ((4,), True),
        ((8,), False),
        ((1,), True),
        ((16,), True),
        ((5,), False),
        ((-4,), False),
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.isPowerOfFour(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
