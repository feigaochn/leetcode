class Solution:
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        from collections import Counter
        c = Counter(S)
        counters = c.most_common()
        if counters[0][1] > (len(S) + 1) // 2:
            return ""
        s = "".join(c * v for c, v in counters)
        r = list(s)
        r[::2] = s[:(len(s) + 1) // 2]
        r[1::2] = s[(len(s) + 1) // 2:]
        return "".join(r)


sol = Solution().reorganizeString

print(sol("aab"))
print(sol("aaab"))
print(sol("vvvlo"))
