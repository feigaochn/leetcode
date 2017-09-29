#!/usr/bin/env python
# coding: utf-8


class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        points = []  # type: [int]
        for op in ops:
            if op == "C":
                points.pop()
            elif op == "D":
                points.append(points[-1] * 2)
            elif op == "+":
                points.append(points[-1] + points[-2])
            else:
                try:
                    points.append(int(op))
                except TypeError:
                    pass
        return sum(points)


if __name__ == '__main__':
    sol = Solution()
    print(sol.calPoints(["5", "2", "C", "D", "+"]))
    print(sol.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))
