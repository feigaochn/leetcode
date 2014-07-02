# author: Fei Gao
#
# Single Number II
#
# Given an array of integers, every element appears three
# times except for one. Find that single one.
# Note:
# Your algorithm should have a linear runtime complexity.
# Could you implement it without using extra memory?


class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        assert isinstance(A, list)
        neg = 0
        bits = [0 for _ in range(64)]
        for val in A:
            if val < 0:
                neg += 1
                val = -val
            idx = 0
            while val != 0:
                if val % 2 == 1:
                    bits[idx] += 1
                val //= 2
                idx += 1
        if neg % 3 == 0:
            neg = 1
        else:
            neg = -1
        number = sum([(1 if val % 3 != 0 else 0) * 2**idx for idx, val in enumerate(bits)])
        return number*neg


def main():
    solver = Solution()
    tests = [[1]*3+[2],
             [-1]*6+[-7]*2]
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
