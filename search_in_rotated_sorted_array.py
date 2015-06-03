# author: Fei Gao
#
# Search In Rotated Sorted Array
#
# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# You are given a target value to search. If found in the array return its
# index, otherwise return -1.
# You may assume no duplicate exists in the array.

import bisect


class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        if A is None or len(A) == 0:
            return -1
        min_index = self.find_min(A)
        if min_index == 0:
            return self.index(A, target)
        if A[0] <= target:
            index = self.index(A[:min_index], target)
            return index
        else:
            index = self.index(A[min_index:], target)
            if index != -1:
                index += min_index
            return index

    def index(self, a, x):
        'Locate the leftmost value exactly equal to x'
        i = bisect.bisect_left(a, x)
        if i != len(a) and a[i] == x:
            return i
        # raise ValueError
        return -1

    def find_min(self, A):
        """
        # @param A, a rotated sorted list without duplicate elements
        # @return the index of minimum element
        """
        if A[0] <= A[-1]:
            return 0
        lo = 0
        hi = len(A) - 1
        while lo < hi:
            mi = (lo + hi) // 2
            if A[mi] > A[hi]:
                lo = mi + 1
            else:
                hi = mi

        return lo


def main():
    solver = Solution()
    lst = list(range(5))
    for i in range(5):
        rlst = lst[i:] + lst[:i]
        print(rlst, " -> ", solver.find_min(rlst))
        t = 5
        print(t, solver.search(rlst, t))
    pass


if __name__ == '__main__':
    main()
    pass
