class MyCalendarThree:
    def __init__(self):
        self.events = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: int
        """
        self.events.append((start, 1))
        self.events.append((end, -1))
        self.events.sort()

        booked = most = 0
        for _, d in self.events:
            booked += d
            most = max(most, booked)
        return most


# Your MyCalendarThree object will be instantiated and called as such:
obj = MyCalendarThree()

for (st, en) in [(10, 20), (50, 60), (10, 40), (5, 15),
    (5, 10), (25, 55)]:
    print(st, en, obj.book(st, en))
