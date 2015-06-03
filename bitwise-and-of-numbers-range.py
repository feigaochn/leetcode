# coding: utf-8

# author: Fei Gao
#
# Bitwise And Of Numbers Range
#
# Given a range [m, n] where 0
# For example, given the range [5, 7], you should return 4.
# Credits:Special thanks to @amrsaqr for adding this problem and creating all test cases.
# Show Tags


class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def rangeBitwiseAnd(self, m, n):
        if m == n:
            return m
        bits = []
        while n != 0:
            if n - m + 1 >= 2:
                bits.append(0)
            else:
                bits.append(1 & m)
            n //= 2
            m //= 2
        return sum((2 ** i) * x for i, x in enumerate(bits))


def main():
    solver = Solution()
    tests = [(5, 7),
             (7, 8),
             (4, 5)]
    for test in tests:
        print(test)
        print(' ->')
        result = solver.rangeBitwiseAnd(*test)
        print(result)
        print('~' * 10)
    pass


if __name__ == '__main__':
    main()
    pass
