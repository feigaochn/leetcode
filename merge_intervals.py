# author: Fei Gao
#
# Merge Intervals
#
# Given a collection of intervals, merge all overlapping intervals.
# For example,
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18].


# Definition for an interval.
class Interval:

    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval

    def merge(self, intervals):
        intervals.sort(key=(lambda x: (x.start, x.end)))
        if len(intervals) == 1:
            return intervals
        result = intervals[0:1]
        for itv in intervals[1:]:
            if itv.start <= result[-1].end:
                result[-1].end = max(result[-1].end, itv.end)
            else:
                result.append(itv)
        return result


def main():
    solver = Solution()
    itvs = []
    for itv in [[1, 3], [2, 6], [8, 10], [15, 18]]:
        itvs.append(Interval(s=itv[0], e=itv[1]))
    res = solver.merge(itvs)
    for itv in res:
        print(itv.start, itv.end)
    pass


if __name__ == '__main__':
    main()
    pass
