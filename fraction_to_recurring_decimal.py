# coding: utf-8

# author: Fei Gao
#
# Fraction To Recurring Decimal

# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
# If the fractional part is repeating, enclose the repeating part in parentheses.
# For example,
# Given numerator = 1, denominator = 2, return "0.5".
# Given numerator = 2, denominator = 1, return "2".
# Given numerator = 2, denominator = 3, return "0.(6)".
# Credits:Special thanks to @Shangrila for adding this problem and creating all test cases.
# Show Tags


class Solution:
    # @param {integer} numerator
    # @param {integer} denominator
    # @return {string}
    def fractionToDecimal(self, nu, de):
        def red(aa, bb):
            a, b = min(aa, bb), max(aa, bb)
            while a:
                a, b = b % a, a
            return aa // b, bb // b

        sign = '-' if nu * de < 0 else ''

        nu, de = red(abs(nu), abs(de))
        # print(sign, nu, de)

        integral = nu // de
        nu %= de

        s = '{}{}'.format(sign, integral)

        if nu == 0:
            return s
        else:
            s += '.'

        f = []
        nus = {nu: 0}
        while nu:
            nu *= 10
            f.append(nu // de)
            nu %= de
            if nu in nus:
                break
            else:
                nus[nu] = len(f)
        # print(nus, nus[nu])
        f = list(map(str, f))
        return s + ''.join(f[:nus[nu]]) + ('(' + ''.join(f[nus[nu]:]) + ')' if nu else '')


def main():
    solver = Solution()
    tests = [
        (1, 2),
        (0, 1),
        (0, -1),
        (-1, 5),
        (-2, -25),
        (3, -16),
        (1, 100),
        (2, 1),
        (2, 3),
        (1, 6),
        (13, 15),
        (1, 700),
    ]
    for test in tests:
        print(test)
        print(' ->')
        result = solver.fractionToDecimal(*test)
        print(result)
        print('~' * 10)
    pass


if __name__ == '__main__':
    main()
    pass
