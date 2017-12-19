class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = [0, 0]
        cost.append(0)
        for c in cost:
            nc1 = dp[-1] + c
            nc2 = dp[-2] + c
            dp.append(min(nc1, nc2))
        return dp[-1]


fn = Solution().minCostClimbingStairs

print(fn([10, 15, 20]))
print(fn([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
