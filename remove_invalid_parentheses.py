# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: remove invalid parentheses
#
# Remove the minimum number of invalid parentheses in order to make the input
# string valid. Return all possible results.
# Note: The input string may contain letters other than the parentheses ( and
# ).
# 
# Examples:
# 
# "()())()" -> ["()()()", "(())()"]
# "(a)())()" -> ["(a)()()", "(a())()"]
# ")(" -> [""]
# 
# Credits:Special thanks to @hpplayer for adding this problem and creating all
# test cases.
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Depth-first Search
# Breadth-first Search
# 
# Show Similar Problems
# 
#  (E) Valid Parentheses


class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        results = []
        lps, rps = [], []
        for i, c in enumerate(s):
            if c == '(':
                lps.append(i)
            elif c == ')':
                rps.append(i)
        lp, rp = len(lps), len(rps)
        if lp <= rp:
            dl, dr = 0, rp - lp
        else:
            dl, dr = lp - rp, 0

        def is_valid(s):
            lp, rp = 0, 0
            for c in s:
                if c == '(':
                    lp += 1
                elif c == ')':
                    rp += 1
                if lp < rp:
                    return False
            return lp == rp

        from itertools import combinations
        while True:
            for dlps in combinations(lps, dl):
                for drps in combinations(rps, dr):
                    r = ''.join(c for i, c in enumerate(s) if i not in dlps + drps)
                    if is_valid(r):
                        results.append(r)
            if results:
                break
            else:
                dl, dr = dl + 1, dr + 1
        return list(set(results))


def main():
    solver = Solution()
    tests = [
        (("()())()",), ["()()()", "(())()"]),
        (("(a)())()",),["(a)()()", "(a())()"]),
    ((")(",), [""])
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.removeInvalidParentheses(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
