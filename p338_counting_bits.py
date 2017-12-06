# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: counting bits
#
# Given a non negative integer number num. For every numbers i in the range 0
# ≤ i ≤ num calculate the number of 1's in their binary representation and
# return them as an array.
# 
# Example:
# For num = 5 you should return [0,1,1,2,1,2].
# 
# Follow up:
# 
# It is very easy to come up with a solution with run time
# O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a
# single pass?
# Space complexity should be O(n).
# Can you do it like a boss? Do it without using any builtin function like
# __builtin_popcount  in c++ or in any other language.
# 
# You should make use of what you have produced already.
# Divide the numbers in ranges like [2-3], [4-7], [8-15] and so on. And try to
# generate new range from previous.
# Or does the odd/even status of the number help you in calculating the number
# of 1s?
# 
# Credits:Special thanks to @ syedee  for adding this problem and creating all
# test cases.
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Dynamic Programming
# Bit Manipulation
# 
# Show Similar Problems
# 
#  (E) Number of 1 Bits


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        results = [0]
        while len(results) <= num:
            results = results + [x + 1 for x in results]
        return results[:num + 1]


def main():
    solver = Solution()
    tests = [
        ((5,), 'result'),
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.countBits(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
