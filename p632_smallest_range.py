class Solution:
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        from heapq import heappop, heappush
        minheap = []
        maxv = -10**8
        for i, xs in enumerate(nums):
            v = xs[0]
            maxv = max(maxv, v)
            heappush(minheap, (v, i, 0))

        best_range = [minheap[0][0], maxv]
        while True:
            v, ri, ci = heappop(minheap)
            if maxv - v < best_range[1] - best_range[0]:
                best_range = [v, maxv]

            ci += 1
            if ci == len(nums[ri]):
                break
            v, ri, ci = nums[ri][ci], ri, ci
            maxv = max(maxv, v)
            heappush(minheap, (v, ri, ci))

        return best_range


fn = Solution().smallestRange
print(fn([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]))
