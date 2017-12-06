#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        import re
        import fractions

        tokens = re.findall(r'[+-]{0,1}\d+/\d+', expression)
        result = sum(map(fractions.Fraction, tokens))  # type: fractions.Fraction
        return "{}/{}".format(result.numerator, result.denominator)


sol = Solution()
print(sol.fractionAddition("-1/2+1/2"))
print(sol.fractionAddition("-1/2+1/2+1/3"))
print(sol.fractionAddition("1/3-1/2"))
print(sol.fractionAddition("5/3+1/3"))
