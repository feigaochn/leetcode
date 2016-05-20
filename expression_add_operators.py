# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: expression add operators
#
# Given a string that contains only digits 0-9 and a target value, return all
# possibilities to add binary operators (not unary) +, -, or * between the
# digits so they evaluate to the target value.
# 
# Examples:
# "123", 6 -> ["1+2+3", "1*2*3"]
# "232", 8 -> ["2*3+2", "2+3*2"]
# "105", 5 -> ["1*0+5","10-5"]
# "00", 0 -> ["0+0", "0-0", "0*0"]
# "3456237490", 9191 -> []
# 
# Credits:Special thanks to @davidtan1890 for adding this problem and creating
# all test cases.
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Divide and Conquer
# 
# Show Similar Problems
# 
#  (M) Evaluate Reverse Polish Notation
#  (H) Basic Calculator
#  (M) Basic Calculator II
#  (M) Different Ways to Add Parentheses


class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        #TODO: TLE
        from itertools import product
        results = []
        for ops in product(['', '+', '-', '*'], repeat=len(num) - 1):
            s = ''
            zero = False
            for i, op in enumerate(ops):
                if op == '' and num[i] == '0':
                    zero = True
                    break
                s += num[i] + op
            if zero:
                continue
            s += num[-1]
            if eval(s) == target:
                results.append(s)
        return results


def main():
    solver = Solution()
    tests = [
        (('123', 6), []),
        (('232', 8), []),
        (('105', 5), []),
        (('00', 0), []),
        (('3456237490', 9191), []),
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.addOperators(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
