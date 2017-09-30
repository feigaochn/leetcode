#!/usr/bin/python3

# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        for e in employees:
            if e.id == id:
                return e.importance + sum(self.getImportance(employees, sub) for sub in e.subordinates)

sol = Solution().getImportance

assert sol([Employee(*data) for data in [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]]], 1) == 11
