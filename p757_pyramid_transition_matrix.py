#!/usr/bin/env python
# coding: utf-8

class Solution:
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        from collections import defaultdict
        from itertools import product

        trans = defaultdict(list)
        for triple in allowed:
            trans[triple[:2]].append(triple[-1])

        def dfs(row):
            if len(row) == 1:
                return True
            cand = []
            for i in range(len(row) - 1):
                tail = trans[row[i:i + 2]]
                if not tail:
                    return False
                cand.append(tail)
            for comb in product(*cand):
                if dfs(''.join(comb)):
                    return True
            return False

        return dfs(bottom)


if __name__ == '__main__':
    sol = Solution().pyramidTransition
    print(sol(bottom="XYZ", allowed=["XYD", "YZE", "DEA", "FFF"]))
    print(sol(bottom="XXYX", allowed=["XXX", "XXY", "XYX", "XYY", "YXZ"]))
