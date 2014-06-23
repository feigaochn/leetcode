# author: Fei Gao
#
# Remove Duplicates From Sorted Array Ii
#
# Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?
# For example,
# Given sorted array A = [1,1,1,2,2,3],
# Your function should return length = 5, and A is now [1,1,2,2,3].


class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0
        cnt = 1
        i1 = 0
        i2 = 1
        while i2 < len(A):
            if A[i2] != A[i1]:
                i1 += 1
                A[i1] = A[i2]
                cnt = 1
            elif cnt == 1:
                i1 += 1
                A[i1] = A[i2]
                cnt = 2
            i2 += 1
        i1 += 1
        nlen = i1
        while i1 < len(A):
            A[i1] = None
            i1 += 1
        return nlen


def main():
    solver = Solution()
    tests = [[1, 1, 1, 1, 2, 2, 3]]
    for test in tests:
        print(test)
        print(' ->')
        result = solver.removeDuplicates(test)
        print(result, test[:result])
        print('~'*10)
    pass


if __name__ == '__main__':
    main()
    pass
