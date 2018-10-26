class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        from functools import reduce
        from math import gcd
        from collections import Counter

        counts = list(Counter(deck).values())
        return reduce(gcd, counts) >= 2
