#!/usr/bin/env python
# coding: utf-8


class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        stack = []
        time = [0 for _ in range(n)]
        last_ts = 0
        for log in logs:
            # print(log, stack, time)
            pid, state, ts = log.split(':')
            pid, ts = int(pid), int(ts)
            if state == 'start':
                if stack:
                    time[stack[-1]] += ts - last_ts
                stack.append(pid)
            elif state == 'end':
                ts += 1
                time[stack[-1]] += ts - last_ts
                stack.pop()
            last_ts = ts
        return time


if __name__ == '__main__':
    sol = Solution()
    print(sol.exclusiveTime(n=2,
                            logs=
                            ["0:start:0",
                             "1:start:2",
                             "1:end:5",
                             "0:end:6"]))
