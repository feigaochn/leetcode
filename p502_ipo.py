#!/usr/bin/env python
# coding: utf-8

class Solution:
    def findMaximizedCapital(self, k, W, Profits, Capital):
        """
        :type k: int
        :type W: int
        :type Profits: List[int]
        :type Capital: List[int]
        :rtype: int
        """
        import heapq
        projects = sorted(zip(Capital, Profits))
        heap = []
        pos = 0
        for _ in range(k):
            while pos < len(projects) and projects[pos][0] <= W:
                heapq.heappush(heap, -projects[pos][1])
                pos += 1
            if heap:
                W += abs(heapq.heappop(heap))
        return W


if __name__ == '__main__':
    sol = Solution().findMaximizedCapital
    print(sol(k=2, W=0, Profits=[1, 2, 3], Capital=[0, 1, 1]))
