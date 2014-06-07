# author: Fei Gao
#
# Gray Code
#
# The gray code is a binary numeral system where two successive values differ
# in only one bit.
# Given a non-negative integer n representing the total number of bits in the
# code, print the sequence of gray code. A gray code sequence must begin with
# 0.
# For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:
# 00 - 0
# 01 - 1
# 11 - 3
# 10 - 2
# Note:
# For a given n, a gray code sequence is not uniquely defined.
# For example, [0,2,3,1] is also a valid gray code sequence according to the
# above definition.
# For now, the judge is able to judge based on one instance of gray code
# sequence. Sorry about that.


class Solution:
    # @return a list of integers
    def grayCode(self, n):
        gray = [0]
        for i in range(n):
            gray = gray[:] + [x + 2**i for x in gray[::-1]]
        return gray


def main():
    solver = Solution()
    for n in range(1, 4):
        print(n, ':\n',
              '\n'.join(['{:04b}'.format(k) for k in solver.grayCode(n)]))


if __name__ == '__main__':
    main()
    pass
