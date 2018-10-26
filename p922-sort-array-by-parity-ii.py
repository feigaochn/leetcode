class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odds = [n for n in A if n % 2 == 1]
        evens = [n for n in A if n % 2 == 0]
        A[::2] = evens
        A[1::2] = odds
        return A
        