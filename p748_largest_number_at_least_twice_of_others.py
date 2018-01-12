class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        elif len(nums) == 1:
            return 0
        first, second = nums[:2]
        large_idx = 0
        if first < second:
            first, second = second, first
            large_idx = 1
        for idx, other in enumerate(nums[2:], 2):
            if other > first:
                first, second = other, first
                large_idx = idx
            elif other > second:
                second = other
        if first >= 2 * second:
            return large_idx
        else:
            return -1
