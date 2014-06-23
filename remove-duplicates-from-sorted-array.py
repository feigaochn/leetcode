# author: Fei Gao
#
# Remove Duplicates From Sorted Array
#
# Given a sorted array, remove the duplicates in place such that each element
# appear only once and return the new length.
# Do not allocate extra space for another array, you must do this in place
# with constant memory.
# For example,
# Given input array A = [1,1,2],
# Your function should return length = 2, and A is now [1,2].


class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0
        i1 = 0
        i2 = 1
        while i2 < len(A):
            if A[i2] != A[i1]:
                i1 += 1
                A[i1] = A[i2]
            i2 += 1
        i1 += 1
        nlen = i1
        while i1 < len(A):
            A[i1] = None
            i1 += 1
        return nlen


def main():
    solver = Solution()
    tests = [[1, 1, 2], [1, 1], [], [1, 1, 2, 2, 3, 3]]
    for test in tests:
        print(test)
        print(' ->')
        result = solver.removeDuplicates(test)
        print(result, test)
        print('~'*10)
    pass


if __name__ == '__main__':
    main()
    pass
