# author: Fei Gao
#
# Jump Game
#
# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Determine if you are able to reach the last index.
# For example:
# A = [2,3,1,1,4], return true.
# A = [3,2,1,0,4], return false.


class Solution:
    # @param A, a list of integers
    # @return a boolean

    def canJump(self, A):
        if A is None or len(A) == 0:
            return False
        far = 0
        for i in range(len(A)):
            if i <= far:
                far = max(far, i + A[i])
        # return far
        return far >= len(A)-1


def main():
    solver = Solution()
    for test in [[2, 3, 1, 1, 4],
                 [3, 2, 1, 0, 4],
                 list(range(5, -1, -1))+[0]]:
        print(test, '\n    -> ', solver.canJump(test))
    pass


if __name__ == '__main__':
    main()
    pass
