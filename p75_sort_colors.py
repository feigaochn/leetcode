class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        n0 = A.count(0)
        n1 = A.count(1)
        n2 = A.count(2)
        for i in range(n0):
            A[i] = 0
        for i in range(n0, n0+n1):
            A[i] = 1
        for i in range(n0+n1, n0+n1+n2):
            A[i] = 2