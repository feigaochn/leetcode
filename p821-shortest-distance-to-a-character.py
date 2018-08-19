# Given a string S and a character C, return an array of integers representing
# the shortest distance from the character C in the string.

# Example 1:
# Input: S = "loveleetcode", C = 'e' Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]

# Note:
#     S string length is in [1, 10000].  C is a single character, and guaranteed
#     to be in string S.  All letters in S and C are lowercase.


class Solution:

    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        n = len(S)
        dist = [99999] * n
        d = 99999
        for i in range(n):
            if S[i] == C:
                d = 0
            dist[i] = min(dist[i], d)
            d += 1
        d = 99999
        for i in range(n):
            if S[n - 1 - i] == C:
                d = 0
            dist[n - 1 - i] = min(dist[n - 1 - i], d)
            d += 1
        return dist


sol = Solution().shortestToChar
print(sol(S="loveleetcode", C="e"))
