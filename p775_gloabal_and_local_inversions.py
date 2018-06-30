class Solution:
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        import logging
        logging.basicConfig(level=logging.DEBUG)

        tails = [A[-1]]
        for x in A[-2::-1]:
            tails.append(min(x, tails[-1]))
        tails = tails[::-1]
        logging.debug(tails)
        for i in range(len(A) - 2):
            if A[i] > tails[i + 2]:
                return False
        return True


sol = Solution().isIdealPermutation
print(sol([1, 0, 2]))
print(sol([1, 2, 0]))
