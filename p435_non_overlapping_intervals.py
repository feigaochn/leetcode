# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        intervals.sort(key=lambda i: (i.end, i.start))
        kicks = 0
        pre_end = intervals[0].end
        for it in intervals[1:]:
            if it.start < pre_end:
                kicks += 1
            else:
                pre_end = it.end
        return kicks


fn = Solution().eraseOverlapIntervals

print(fn([Interval(*it) for it in [[1, 2], [2, 3], [3, 4], [1, 3]]]))
print(fn([Interval(*it) for it in [[1, 2], [1, 2], [1, 2]]]))
print(fn([Interval(*it) for it in [[1, 2], [2, 3]]]))
