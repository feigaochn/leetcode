class Solution:
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """

        def split(s):
            return ("".join(sorted(s[::2])), "".join(sorted(s[1::2])))

        ss = [split(s) for s in A]
        return len(set(ss))
