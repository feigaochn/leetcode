class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        import bisect

        t_dic = [[] for _ in range(26)]
        for i, c in enumerate(t):
            t_dic[ord(c) - ord('a')].append(i)
        last = -1
        for c in s:
            c = ord(c) - ord('a')
            last = bisect.bisect_right(t_dic[c], last)
            if last == len(t_dic[c]):
                return False
            else:
                last = t_dic[c][last]
            # print(c, last)
        else:
            return True


fn = Solution().isSubsequence

print(fn("abc", "ahbgdc"))
print(fn("axc", "ahbgdcx"))
