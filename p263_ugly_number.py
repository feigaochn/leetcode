# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: ugly number
#
# Write a program to check whether a given number is an ugly number.
# 
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
# For example, 6, 8 are ugly while 14 is not ugly since it includes another
# prime factor 7.
# 
# Note that 1 is typically treated as an ugly number.
# 
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Math
# 
# Show Similar Problems
# 
#  (E) Happy Number
#  (E) Count Primes
#  (M) Ugly Number II


class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False
        if num == 1:
            return True
        ps = [2, 3, 5]
        for p in ps:
            while num % p == 0: num //= p
        return num == 1


def main():
    solver = Solution()
    tests = [
        ((1,), True),
        ((2,), True),
        ((14,), False),
        ((-1,), False),
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.isUgly(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
