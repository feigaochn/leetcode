#!/usr/bin/env python
# coding: utf-8


class MyCalendarTwo:

    def __init__(self):
        self.events = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        events = self.events[::]
        events.append((start, 1))
        events.append((end, -1))
        events.sort()
        count = 0
        for (ts, value) in events:
            count += value
            if count >= 3:
                return False
        self.events = events
        return True


if __name__ == '__main__':
    obj = MyCalendarTwo()
    print(obj.book(10, 20))
    print(obj.book(50, 60))
    print(obj.book(10, 40))
    print(obj.book(5, 15))
    print(obj.book(5, 10))
    print(obj.book(25, 55))
