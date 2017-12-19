class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        total = sum(nums)
        diff = total - S
        if diff < 0 or diff % 2 == 1:
            return 0

        from collections import defaultdict

        counter = {0: 1}
        for num in nums:
            counter_update = defaultdict(int)
            counter_update.update(counter)
            for v, c in counter.items():
                counter_update[v + num] += c
            counter = counter_update
        return counter[diff//2]


fn = Solution().findTargetSumWays
print(fn([1, 0], 1))
print(
    fn([
        34, 16, 5, 38, 20, 20, 8, 43, 3, 46, 24, 12, 28, 19, 22, 28, 9, 46, 25,
        36
    ], 0))
print(fn([7, 9, 3, 8, 0, 2, 4, 8, 3, 9], 0))
print(fn([1, 1, 1, 1, 1], 3))
print(fn([1 for _ in range(20)], 0))
