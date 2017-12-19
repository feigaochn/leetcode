class Solution:
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        count = 0
        dp_new = {0: 1}
        while dp_new:
            dp_old = dp_new.copy()
            dp_new = {}
            for v, c, in dp_old.items():
                for n in nums:
                    if v + n <= target:
                        dp_new[v + n] = c + dp_new.get(v + n, 0)

            count += dp_new.get(target, 0)
        return count


fn = Solution().combinationSum4

print(fn([1, 2, 3], 40))
