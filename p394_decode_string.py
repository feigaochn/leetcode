class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        def work(s: str):
            if not s:
                return ""
            elif s[0].isdigit():
                lb = s.index('[')
                rb = lb
                deep = 1
                while deep:
                    rb += 1
                    if s[rb] == ']':
                        deep -= 1
                    elif s[rb] == '[':
                        deep += 1
                return work(s[lb + 1:rb]) * int(s[:lb]) + work(s[rb + 1:])
            else:
                return s[0] + work(s[1:])

        return work(s)


fn = Solution().decodeString

print(fn("3[a]2[bc]"))
print(fn("3[a2[c]]"))
print(fn("2[abc]3[cd]ef"))
print(fn("2[abc]13[cd]ef"))
