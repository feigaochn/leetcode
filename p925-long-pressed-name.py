class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        from itertools import groupby

        def counter(s):
            return [(l, len(list(r))) for l, r in groupby(s)]

        c1 = counter(name)
        c2 = counter(typed)
        return len(c1) == len(c2) and all(
            a == b and x <= y for (a, x), (b, y) in zip(c1, c2)
        )

sol = Solution().isLongPressedName
print(sol("alex", "aaleex"))
print(sol("saeed", "ssaaedd"))
print(sol("leelee", "lleeelee"))
print(sol("laiden", "laiden"))
