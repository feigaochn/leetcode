# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return "[{},{}]".format(self.start, self.end)

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval

    def insert(self, intervals, newInterval):
        # trivial case
        if intervals is None or len(intervals) == 0:
            return [newInterval]

        return self._gao3(intervals, newInterval)

    def _gao3(self, ins, nin):
        result = []
        ns, ne = nin.start, nin.end
        is_insert = False
        for i in ins:
            if i.end < nin.start:
                result.append(i)
            elif i.start > nin.end:
                if is_insert is False:
                    is_insert = True
                    result.append(Interval(ns, ne))
                result.append(i)
            else:
                ns = min(ns, i.start)
                ne = max(ne, i.end)
        if is_insert is False:
            result.append(Interval(ns, ne))
        return result

def test():
    print(Solution().insert([Interval(1,3), Interval(6,9)], Interval(2,5)))


if __name__ == '__main__':
    test()