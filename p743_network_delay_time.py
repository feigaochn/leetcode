class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        from collections import defaultdict
        edges = defaultdict(dict)
        for u, v, w in times:
            edges[u][v] = w
        reach = {K: 0}
        frontier = {K}
        while frontier:
            u = frontier.pop()
            cur_dist = reach[u]
            for v, d in edges[u].items():
                if v not in reach or cur_dist + d < reach[v]:
                    reach[v] = cur_dist + d
                    frontier.add(v)
        if len(reach) == N:
            return max(reach.values())
        else:
            return -1


fn = Solution().networkDelayTime

print(fn([[1, 2, 3], [1, 3, 1], [3, 2, 3]], 3, 1))
print(fn([], 2, 1))
