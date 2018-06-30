class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        return sum(s in J for s in S)


sol = Solution().numJewelsInStones
print(sol("aA", "aAAbbb"))
print(sol("z", "ZZ"))
print(sol("", "ab"))
print(sol("ab", ""))
