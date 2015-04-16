#!/bin/env python3

# author: Fei Gao
#
# Merge Sorted Array
#
# Given two sorted integer arrays A and B, merge B into A as one sorted array.
# Note:
# You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B. The number of elements initialized in A and B are m and n respectively.
# Show Tags


class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing(void)
    def merge(self, A, m, B, n):
        while m > 0 and n > 0:
            if A[m-1] > B[n-1]:
                A[m+n-1] = A[m-1]
                m -= 1
            else:
                A[m+n-1] = B[n-1]
                n -= 1
        while n > 0:
            A[n-1] = B[n-1]
            n -= 1


def main():
    solver = Solution()
    tests = [[[0], [1]]]
    for test in tests:
        print(test)
        print(' ->')
        result = solver.merge(test[0], 0, test[1], 1)
        print(test[0])
        print('~'*10)
    pass
if __name__ == '__main__':
    main()
    pass
