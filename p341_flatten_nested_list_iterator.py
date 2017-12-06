# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: flatten nested list iterator
#
# Given a nested list of integers, implement an iterator to flatten it.
# Each element is either an integer, or a list -- whose elements may also be
# integers or other lists.
# Example 1:
# Given the list [[1,1],2,[1,1]],
#
# By calling next repeatedly until hasNext returns false, the order of
# elements returned by next should be: [1,1,2,1,1].
#
# Example 2:
# Given the list [1,[4,[6]]],
#
# By calling next repeatedly until hasNext returns false, the order of
# elements returned by next should be: [1,4,6].
#
# Subscribe to see which companies asked this question
#
# Show Tags
#
# Stack
# Design
#
# Show Similar Problems
#
#  (M) Flatten 2D Vector
#  (M) Zigzag Iterator


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedInteger:
    def __init__(self, l):
        self.val = l

    def isInteger(self):
        return isinstance(self.val, int)

    def getInteger(self):
        return self.val if self.isInteger() else None

    def getList(self):
        return self.val if not self.isInteger() else None

    def __str__(self):
        return str(self.val)


class NestedIterator(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.items = []

        def flat(nlst):
            for item in nlst:
                if item.isInteger():
                    self.items.append(item.getInteger())
                else:
                    flat(item.getList())

        flat(nestedList)

    def next(self):
        """
        :rtype: int
        """
        return self.items.pop(0)

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.items) > 0


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())



def main():
    NS = NestedInteger
    l = [NS([NS(1), NS(2)]), NS(3), NS([NS(4), NS(5)])]
    i, v = NestedIterator(l), []
    while i.hasNext():
        v.append(i.next())
    print(v)


if __name__ == '__main__':
    main()
    pass
