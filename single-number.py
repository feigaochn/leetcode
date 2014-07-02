# author: Fei Gao
#
# Single Number
#
# Given an array of integers, every element appears twice except for one. Find that single one.
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?


class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        assert isinstance(A, list)
        from functools import reduce
        return reduce(lambda x,y: x ^ y, A, 0)


def main():
    solver = Solution()
    tests = [[1, 1, 2], [1, 0, -1, 1, 0]]
    for test in tests:
        print(test)
        print(' ->')
        result = solver.singleNumber(test)
        print(result)
        print('~'*10)
    pass


if __name__ == '__main__':
    main()
    pass
