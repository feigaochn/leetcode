class Solution:
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        d8 = [(dr * rs, dc * cs) for dr in [1, 2] for dc in [1, 2]
              if dr != dc for rs in [1, -1] for cs in [1, -1]]
        prob = [[[
            0 if r < 2 or r > N + 1 or c < 2 or c > N + 1 else 1
            for c in range(N + 4)
        ] for r in range(N + 4)] for k in range(K + 1)]
        for k in range(1, K + 1):
            for x in range(2, 2 + N):
                for y in range(2, 2 + N):
                    prob[k][x][y] = sum(
                        prob[k - 1][x + dr][y + dc] for dr, dc in d8) / 8.0

        return prob[K][r + 2][c + 2]


fn = Solution().knightProbability

print(fn(3, 2, 0, 0))
print(fn(25, 100, 0, 0))
