# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return "[{}, {}]".format(self.start, self.end)

    def __repr__(self):
        return self.__str__()


class SummaryRanges:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head2tail = dict()

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        before = after = None
        for h, t in self.head2tail.items():
            if h <= val <= t:
                return
            elif t + 1 == val:
                before = [h, t]
            elif val + 1 == h:
                after = [h, t]
        if before and after:
            self.head2tail.pop(after[0])
            self.head2tail[before[0]] = after[1]
        elif before:
            self.head2tail[before[0]] = val
        elif after:
            self.head2tail.pop(after[0])
            self.head2tail[val] = after[1]
        else:
            self.head2tail[val] = val

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        return [Interval(s, e) for s, e in sorted(self.head2tail.items())]


# Your SummaryRanges object will be instantiated and called as such:
obj = SummaryRanges()
for val in [1, 3, 7, 2, 6]:
    obj.addNum(val)
    print(obj.getIntervals())
