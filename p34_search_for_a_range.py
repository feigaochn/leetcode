# author: Fei Gao
# date: Sat May 31 17:07:04 2014
#
# Search For A Range
#
# Given a sorted array of integers, find the starting and ending position of a given target value.
# Your algorithm's runtime complexity must be in the order of O(log n).
# If the target is not found in the array, return [-1, -1].
# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4].

import bisect


class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        if A is None or len(A) == 0:
            return [-1, -1]
        if target < A[0] or target > A[-1]:
            return [-1, -1]
        s = bisect.bisect_left(A, target)
        if A[s] != target:
            return [-1, -1]
        e = bisect.bisect_right(A, target) - 1
        if A[e] != target:
            return [-1, -1]
        return [s, e]
        pass


def main():
    solver = Solution()
    lst = sorted(list(range(2, 10, 2)) * 3)
    print(lst)
    for i in range(0, 10):
        [s, e] = solver.searchRange(lst, i)
        print(i, s, e, end=' ')
        if s != -1 and e != -1:
            print(lst[s], lst[e], end=' ')
        print()

    print(solver.searchRange([1, 5], 4))
    pass


if __name__ == '__main__':
    main()
    pass
