# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: find median from data stream
#
# Median is the middle value in an ordered integer list. If the size of the
# list is even, there is no middle value. So the median is the mean of the two
# middle value.
# Examples:
# [2,3,4] , the median is 3
# [2,3], the median is (2 + 3) / 2 = 2.5
# 
# Design a data structure that supports the following two operations:
# 
# void addNum(int num) - Add a integer number from the data stream to the data
# structure.
# double findMedian() - Return the median of all elements so far.
# 
# For example:
# 
# add(1)
# add(2)
# findMedian() -> 1.5
# add(3)
# findMedian() -> 2
# 
# Credits:Special thanks to @Louis1992 for adding this problem and creating
# all test cases.
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Heap
# Design


class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._data = []
        self._len = 0

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        import bisect
        self._data.insert(bisect.bisect(self._data, num), num)
        self._len += 1

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if self._len % 2 == 1:
            return self._data[self._len // 2]
        else:
            return (self._data[self._len // 2 - 1] + self._data[self._len // 2]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()


def main():
    mf = MedianFinder()
    mf.addNum(1)
    print(mf.findMedian())
    pass


if __name__ == '__main__':
    main()
    pass
