#!/usr/bin/env python
# coding: utf-8


class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        from collections import defaultdict
        from itertools import combinations

        maps = defaultdict(int)
        for s in strs:
            for l in range(1, len(s) + 1):
                for t in combinations(s, l):
                    maps[''.join(t)] += 1
        ones = []
        for s, o in maps.items():
            if o == 1:
                ones.append(s)
        if ones:
            return max(map(len, ones))
        else:
            return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.findLUSlength(["aba", "cdc", "eae"]))
    print(sol.findLUSlength(["aba", "aba"]))
    print(sol.findLUSlength(["aaa", "aa"]))
    print(sol.findLUSlength(["aaa", "aaa", "aa"]))
