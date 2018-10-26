class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) <= 2:
            return True
        return all(a <= b for a, b in zip(A, A[1:])) or all(
            a >= b for a, b in zip(A, A[1:])
        )
