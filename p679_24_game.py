class Solution:
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        import itertools
        import fractions

        try:
            self.cache[0]
        except Exception as e:
            self.cache = dict()

        def possible(nums):
            if nums in self.cache:
                return self.cache[nums]
            ans = set()
            if len(nums) == 1:
                ans.add(nums[0])
            else:
                for sep in range(1, len(nums)):
                    head, tail = nums[:sep], nums[sep:]
                    for first in possible(head):
                        for second in possible(tail):
                            ans.add(first * second)
                            ans.add(first + second)
                            ans.add(first - second)
                            if second != 0:
                                ans.add(first / second)
            self.cache[nums] = ans
            return ans

        target = fractions.Fraction(24)
        for nums in itertools.permutations(map(fractions.Fraction, nums)):
            ans = possible(nums)
            if target in ans:
                return True
        else:
            return False


fn = Solution().judgePoint24
print(fn([4, 1, 8, 7]))
print(fn([1, 2, 2, 1]))
print(fn([3, 3, 8, 8]))
print(fn([7, 7, 8, 9]))
