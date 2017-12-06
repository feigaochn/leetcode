#!/usr/bin/env python3
# coding: utf-8

import sys


class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        from collections import defaultdict
        cpid = defaultdict(list)

        for p, pp in zip(pid, ppid):
            cpid[pp].append(p)

        killed = {kill}
        while True:
            updates = set()
            for p in killed:
                for c in cpid[p]:
                    if c not in killed:
                        updates.add(c)
            if not updates:
                break
            killed.update(updates)
        return list(killed)


def main(args):
    sol = Solution()

    print(sol.killProcess([1, 3, 10, 5], [3, 0, 5, 3], 3))
    return


if __name__ == '__main__':
    main(sys.argv[1:])
