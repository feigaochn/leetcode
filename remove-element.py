#!/bin/env python3

# author: Fei Gao
#
# Remove Element
#
# Given an array and a value, remove all instances of that value in place and
# return the new length.
# The order of elements can be changed. It doesn't matter what you leave beyond
# the new length.


class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        head = 0
        tail = len(A) - 1
        while True:
            while head < len(A) and A[head] != elem:
                head += 1
            while tail >= 0 and A[tail] == elem:
                tail -= 1
            if head >= tail:
                break
            # print(head, tail, A)
            A[head], A[tail] = A[tail], A[head]
        return head


def main():
    solver = Solution()
    tests = [
        ([1, 1, 1, 2, 2], 2),
        ([1, 1, 1, 2, 2], 3),
        ([1, 1, 1, 2, 2], 1)
    ]
    for A, elem in tests:
        print(A, elem)
        print(' ->')
        result = solver.removeElement(A, elem)
        print(result)
        print(A)
        print('~'*10)
    pass
if __name__ == '__main__':
    main()
    pass
