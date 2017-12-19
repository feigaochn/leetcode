class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.result = []

        def work(cans, t, partials):
            # print(cans, t, partials, self.result)
            if t == 0:
                self.result.extend(partials)
                return
            elif len(cans) == 0:
                return
            elif cans[0] <= t:
                for r in range(0, t // cans[0] + 1):
                    if cans[0] * r <= t:
                        work(cans[1:], t - cans[0] * r,
                             [p + [cans[0]] * r for p in partials])

        work(sorted(candidates), target, [[]])
        return self.result


fn = Solution().combinationSum

print(fn([2, 3, 6, 7], 7))

print(fn([8, 7, 4, 3], 11))
