#!/usr/bin/env python
# coding: utf-8


class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        if not pairs:
            return 0
        pairs.sort(key=lambda p: (p[1], p[0]))
        end = pairs[0][0] - 1
        result = []
        for st, en in pairs:
            if end < st:
                result.append((st, en))
                end = en
        # print(result)
        return len(result)


if __name__ == '__main__':
    sol = Solution()
    print(sol.findLongestChain([[1, 2], [2, 3], [3, 4]]))
    print(sol.findLongestChain([[1, 3], [2, 3], [3, 4]]))
