#!/usr/bin/env python
# coding: utf-8


class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        import re
        lhs, rhs = equation.split('=', 1)

        def combine(expr):
            tokens = re.findall(r'([+-]{0,1})(\d*)(x{0,1})', expr)
            coef, cons = 0, 0
            for s, v, x in tokens:
                if s + v + x:
                    if x:
                        coef += int(v or '1') * (-1 if s == '-' else 1)
                    else:
                        cons += int(v or '1') * (-1 if s == '-' else 1)
            # print(expr, tokens, coef, cons)
            return coef, cons

        lcoef, lcons = combine(lhs)
        rcoef, rcons = combine(rhs)
        coef = lcoef - rcoef
        cons = rcons - lcons

        if coef == 0:
            if cons == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            return "x={}".format(cons // coef)


if __name__ == '__main__':
    sol = Solution()
    print(sol.solveEquation("x+5-3+x=6+x-2"))
    print(sol.solveEquation("x=x"))
    print(sol.solveEquation("2x=x"))
    print(sol.solveEquation("x=x+2"))
    print(sol.solveEquation("2x+3x-6x+1-1=x+2"))
