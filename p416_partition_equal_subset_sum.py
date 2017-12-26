class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort(reverse=True)
        s = sum(nums)
        if s % 2 == 1:
            return False
        else:
            target = s // 2
        dp = {0}
        for v in nums:
            new_dp = set()
            for o in dp:
                if v + o == target:
                    return True
                elif v + o < target:
                    new_dp.add(v + o)
            dp.update(new_dp)
        return False


fn = Solution().canPartition

print(fn([1, 5, 11, 5]))
print(fn([1, 5, 11, 6]))

import random
nums = [random.randrange(1, 100) for _ in range(200)]
if sum(nums) % 2 == 1:
    nums[0] += 1
print(fn(nums))
