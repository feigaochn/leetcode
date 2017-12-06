# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: reverse string
#
# Write a function that takes a string as input and returns the string
# reversed.
# 
# Example:
# Given s = "hello", return "olleh".
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Two Pointers
# String
# 
# Show Similar Problems
# 
#  (E) Reverse Vowels of a String


class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]


def main():
    solver = Solution()
    tests = [
        (('param',), 'result'),
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.reverseString(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
