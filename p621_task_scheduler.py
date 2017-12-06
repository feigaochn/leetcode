#!/usr/bin/env python
# coding: utf-8


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        data = dict()
        for t in tasks:
            data[t] = [1, 0]
        for t in tasks:
            data[t][1] += 1

        def find_min():
            ret = list(data.keys())[0]
            for j in data:
                if data[j][0] < data[ret][0] or (data[j][0] == data[ret][0]
                                                 and data[j][1] > data[ret][1]):
                    ret = j
            return ret

        last_ts = 0
        seq = []
        for i in tasks:
            t = find_min()
            # print(i, t, data)
            last_ts = data[t][0]
            data[t][1] -= 1
            data[t][0] += (n + 1)
            if data[t][1] == 0:
                data.pop(t)
            for j in data:
                if j != t and data[j][0] <= last_ts:
                    data[j][0] += 1
        # print(seq)
        return last_ts


if __name__ == '__main__':
    sol = Solution()
    from string import ascii_uppercase

    print(sol.leastInterval(list('AAABBB'), 2))
    print(sol.leastInterval(list('AAABBB'), 0))
    print(sol.leastInterval(['A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E'], 4))
    print(sol.leastInterval(['A', 'A', 'A', 'A', 'A', 'A', 'B', 'C', 'D', 'E', 'F', 'G'], 2))
    # print(sol.leastInterval(ascii_uppercase * (10000 // 26) + 'A' * 50, 100))
