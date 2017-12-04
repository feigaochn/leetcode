#!/usr/bin/env python
# coding: utf-8

"""
Implement a MyCalendar class to store your events. A new event can be added if
adding the event will not cause a double booking.

Your class will have the method, book(int start, int end). Formally, this
represents a booking on the half open interval [start, end), the range of real
numbers x such that start <= x < end.

A double booking happens when two events have some non-empty intersection (ie.,
there is some time that is common to both events.)

For each call to the method MyCalendar.book, return true if the event can be
added to the calendar successfully without causing a double booking. Otherwise,
return false and do not add the event to the calendar.

Your class will be called like this: MyCalendar cal = new MyCalendar();
MyCalendar.book(start, end)
"""


class MyCalendar:
    def __init__(self):
        self.events = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for (s, e) in self.events:
            if not (start >= e or end <= s):
                return False
        else:
            self.events.append((start, end))
            return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

if __name__ == '__main__':
    obj = MyCalendar()
    print(obj.book(10, 20))
    print(obj.book(15, 25))
    print(obj.book(20, 30))
