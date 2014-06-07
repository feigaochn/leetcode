# author: Fei Gao
#
# First Missing Positive
#
# Given an unsorted integer array, find the first missing positive integer.
# For example,
# Given [1,2,0] return 3,
# and [3,4,-1,1] return 2.
# Your algorithm should run in O(n) time and uses constant space.


class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        if not A:
            return 1
        i = 0
        while i < len(A):
            v = A[i]
            if 0 < v <= len(A):
                if v-1 <= i:
                    A[v-1] = ''
                elif A[v-1] != '':
                    A[v-1], A[i] = '', A[v-1]
                    continue
            i += 1

        for i in range(len(A)):
            if A[i] != '':
                return i+1
        return len(A)+1


def main():
    solver = Solution()
    tests = [[3], [1, 2, 0], [3, 4, -1, 1], [], [0], [1, 2], [3, 1], [1, 1], [2, 2], [3]*3]
    for test in tests:
        print(test)
        result = solver.firstMissingPositive(test)
        print(' ->')
        print(test)
        print(result)
        print('~'*10)
    pass


if __name__ == '__main__':
    main()
    pass
