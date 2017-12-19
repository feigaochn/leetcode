# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        import bisect
        starts = [(it.start, idx) for idx, it in enumerate(intervals)]
        starts.sort()
        ends = [(it.end, idx) for idx, it in enumerate(intervals)]
        ends.sort()
        result = []
        for it in intervals:
            idx = bisect.bisect_left(starts, (it.end, -1))
            if idx == len(intervals):
                result.append(-1)
            else:
                result.append(starts[idx][1])
        return result


fn = Solution().findRightInterval

print(fn([Interval(*it) for it in [[1, 2]]]))
print(fn([Interval(*it) for it in [[1, 2], [2, 3]]]))
print(fn([Interval(*it) for it in [[2, 3], [1, 2]]]))
print(fn([Interval(*it) for it in [[3, 4], [2, 3], [1, 2]]]))
