from collections import defaultdict
from random import choice


class Solution:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.d = defaultdict(list)
        for i, v in enumerate(nums):
            self.d[v].append(i)

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        return choice(self.d[target])


# Your Solution object will be instantiated and called as such:
nums = [1, 2, 3, 3, 3]
obj = Solution(nums)
for _ in range(100):
    print(obj.pick(3))
