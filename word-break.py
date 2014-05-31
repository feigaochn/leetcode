class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean

    def wordBreak(self, s, dict):
        mem1 = {0: True}
        mem2 = mem1.copy()
        while True:
            for st in mem1:
                for w in dict:
                    if s[st:st+len(w)] == w:
                        mem2[st+len(w)] = True
            if mem2 != mem1:
                mem1 = mem2.copy()
            else:
                break
        return (len(s) in mem2)


s = "leetcode"
dict = ["leet", "code"]
solver = Solution()
print(solver.wordBreak(s, dict))

s = "leetcod"
dict = ["leet", "code"]
solver = Solution()
print(solver.wordBreak(s, dict))

s, dict = "bccdbacdbdacddabbaaaadababadad", [
    "cbc", "bcda", "adb", "ddca", "bad", "bbb", "dad", "dac", "ba", "aa", "bd",
    "abab", "bb", "dbda", "cb", "caccc", "d", "dd", "aadb", "cc", "b", "bcc",
    "bcd", "cd", "cbca", "bbd", "ddd", "dabb", "ab", "acd", "a", "bbcc",
    "cdcbd", "cada", "dbca", "ac", "abacd", "cba", "cdb", "dbac", "aada",
    "cdcda", "cdc", "dbc", "dbcb", "bdb", "ddbdd", "cadaa", "ddbc", "babb"]
solver = Solution()
print(solver.wordBreak(s, dict))
