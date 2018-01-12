#!/usr/bin/env python
# coding: utf-8
import itertools


class Solution:
    def findMinMoves(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """
        total = sum(machines)
        if total % len(machines) != 0:
            return -1
        average = total // len(machines)
        load = [v - average for v in machines]
        acc_load = list(itertools.accumulate(load))
        # print(machines, average, load, acc_load)
        return max(max(load), max(map(abs, acc_load)))


if __name__ == '__main__':
    sol = Solution().findMinMoves
    print(sol([1, 0, 5]))
    print(sol([9, 1, 8, 8, 9]))
