# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: add digits
#
# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit. 
# 
# For example:
# 
# Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.
# 
# Follow up:
# Could you do it without any loop/recursion in O(1) runtime?
# 
# A naive implementation of the above process is trivial. Could you come up with other methods? 
# What are all the possible results?
# How do they occur, periodically or randomly?
# You may find this Wikipedia article useful.
# 
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
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

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num > 9:
            num = sum(map(int, list(str(num))))
        return num


def main():
    solver = Solution()
    tests = [
        ((38,), 2),
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.addDigits(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
