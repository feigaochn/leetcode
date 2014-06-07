# author: Fei Gao
#
# Plus One
#
# Given a non-negative number represented as an array of digits, plus one to
# the number.
# The digits are stored such that the most significant digit is at the head of
# the list.


class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        return [int(i) for i in list(str(1 + int(''.join(str(d) for d in
                                                         digits))))]


def main():
    pass


if __name__ == '__main__':
    main()
    pass
