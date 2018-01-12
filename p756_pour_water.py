class Solution:
    def pourWater(self, heights, V, K):
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """
        N = len(heights)
        for _ in range(V):
            filled = K
            for i in range(K - 1, -1, -1):
                if heights[i] > heights[i + 1]:
                    break
                elif heights[i] < heights[filled]:
                    filled = i
            if filled != K:
                heights[filled] += 1
                continue
            for i in range(K + 1, N):
                if heights[i] > heights[i - 1]:
                    break
                elif heights[i] < heights[filled]:
                    filled = i
            if filled != K:
                heights[filled] += 1
                continue
            heights[K] += 1
        return heights


sol = Solution().pourWater

print(sol([2, 1, 1, 2, 1, 2, 2], V=4, K=3))
print(sol([1, 2, 3, 4], V=2, K=2))
print(sol([3, 1, 3], 5, 1))
print(
    sol([1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1], 2, 5),
    [1, 2, 3, 4, 3, 3, 2, 2, 3, 4, 3, 2, 1])
print(
    sol([1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1], 10, 2),
    [4, 4, 4, 4, 3, 3, 3, 3, 3, 4, 3, 2, 1])

import random

heights = [random.randrange(0, 100) for _ in range(100)]
V = 2000
K = random.randrange(len(heights))
print(sol(heights, V, K))
