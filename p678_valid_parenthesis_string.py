class Solution:
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        from functools import lru_cache

        @lru_cache(maxsize=4096)
        def is_valid(p):
            if not p:
                return True
            elif len(p) == 1:
                return p == '*'
            elif len(p) == 2:
                return p[0] in "(*" and p[-1] in "*)"
            else:
                if any((is_valid(p[:i]) and is_valid(p[i:]))
                       for i in range(1, len(p))):
                    return True
                else:
                    return p[0] in "*(" and p[-1] in "*)" and is_valid(p[1:-1])

        return is_valid(s)


sol = Solution()

print(sol.checkValidString("()"))
print(sol.checkValidString("(*)"))
print(sol.checkValidString("(*))"))
print(sol.checkValidString("*)"))
print(sol.checkValidString("***"))
print(sol.checkValidString("((*"))
