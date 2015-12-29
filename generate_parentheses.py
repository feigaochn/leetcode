# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: generate parentheses
#
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
# 
# For example, given n = 3, a solution set is:
# 
# "((()))", "(()())", "(())()", "()(())", "()()()"
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Backtracking
# String
# 
# Show Similar Problems
# 
#  (M) Letter Combinations of a Phone Number
#  (E) Valid Parentheses


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        next = {''}
        for i in range(2*n):
            cur = next.copy()
            next = set()
            for p in cur:
                l = p.count('(')
                r = len(p) - l
                if l < n:
                    next.add(p + '(')
                if l > r:
                    next.add(p + ')')
        return list(next)


def main():
    solver = Solution()
    tests = [
        ((0,), 'result'),
        ((1,), 'result'),
        ((2,), 'result'),
        ((3,), 'result'),
        ((4,), 'result'),
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.generateParenthesis(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
