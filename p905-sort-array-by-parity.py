class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return [n for n in A if n % 2 == 0] + [n for n in A if n % 2 == 1]
