class Solution:
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        import heapq
        from collections import defaultdict
        stone_set = set(stones)
        heap = [(stones[0], 0)]
        mark = defaultdict(set)
        mark[0].add(0)
        while heap:
            s, k = heapq.heappop(heap)
            if s == stones[-1]:
                return True
            if k >= 2 and s + k - 1 in stone_set and (
                    k - 1) not in mark[s + k - 1]:
                heapq.heappush(heap, (s + k - 1, k - 1))
                mark[s + k - 1].add(k - 1)
            if k >= 1 and s + k in stone_set and k not in mark[s + k]:
                heapq.heappush(heap, (s + k, k))
                mark[s + k].add(k)
            if k >= 0 and s + k + 1 in stone_set and (k + 1) not in mark[s + k + 1]:
                heapq.heappush(heap, (s + k + 1, k + 1))
                mark[s + k + 1].add(k + 1)
        else:
            return False


fn = Solution().canCross

print(fn([0, 1, 3, 5, 6, 8, 12, 17]))
print(fn([0, 2]))
print(fn([0, 1, 2, 3, 4, 8, 9, 11]))
print(fn(list(range(1100))))
