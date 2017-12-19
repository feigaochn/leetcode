class Solution:
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        from collections import defaultdict
        dp = [dict(), dict()]
        chr2pos = defaultdict(list)
        for i, c in enumerate(ring):
            chr2pos[c].append(i)

        dp[1] = {0: 0}
        for idx, char in enumerate(key):
            dp[idx % 2] = dict()
            for p in chr2pos[char]:
                dp[idx % 2][p] = min(dp[(idx + 1) % 2][j] + min(
                    abs(j - p), len(ring) - abs(j - p))
                                     for j in dp[(idx + 1) % 2])
            # print(idx, char, dp[idx % 2])
        return min(dp[(1 + len(key)) % 2].values()) + len(key)


fn = Solution().findRotateSteps

print(fn("godding", "gd"))
