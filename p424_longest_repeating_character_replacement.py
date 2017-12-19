class Solution:
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        best = 0
        for c in set(s):
            h = t = d = 0
            while t < len(s):
                if s[t] != c:
                    d += 1
                    while d > k and h <= t:
                        if s[h] != c:
                            d -= 1
                        h += 1
                best = max(best, t + 1 - h)
                t += 1
            best = max(best, t - h)
        return best


fn = Solution().characterReplacement

print(fn("AAAB", 0))
print(fn("ABAAB", 0))
print(fn("ABAB", 2))
print(fn("ABBB", 2))
print(fn("ABBBA", 2))
print(fn("AABABBA", 1))
