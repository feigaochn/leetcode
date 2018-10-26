class Solution:
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        if not A:
            return 0
        low = min(A)
        high = max(A)
        return max((high - K) - (low + K), 0)
        