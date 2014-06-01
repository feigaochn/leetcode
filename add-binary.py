# author: Fei Gao
#
# Add Binary
#
# Given two binary strings, return their sum (also a binary string).
# For example,
# a = "11"
# b = "1"
# Return "100".


class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        ai = int(a, base=2)
        bi = int(b, base=2)
        return '{:b}'.format(ai + bi)


def main():
    solver = Solution()
    print(solver.addBinary('101', '1'))
    pass


if __name__ == '__main__':
    main()
    pass
