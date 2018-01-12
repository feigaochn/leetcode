#!/usr/bin/env python
# coding: utf-8


class Solution:
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        vcs = [[nums[0], 1]]
        for n in nums[1:]:
            if n == vcs[-1][0]:
                vcs[-1][1] += 1
            else:
                vcs.append([n, 1])

        cur = [vcs[0][0], vcs[0][1], 0, 0, 0]
        for v, c in vcs[1:]:
            if v > cur[0] + 1:
                if cur[1] > 0 or cur[2] > 0:
                    return False
                else:
                    cur = [v, c, 0, 0, 0]
            elif v == cur[0] + 1:
                if c < cur[1] + cur[2]:
                    return False
                cur = [v,
                       max(0, c - (sum(cur[1:]))),
                       cur[1],
                       cur[2] + min(cur[3], c - (cur[1] + cur[2]))]
        return cur[1] == 0 and cur[2] == 0


if __name__ == '__main__':
    sol = Solution().isPossible
    print(sol([1, 2, 3, 3, 4, 5]))
    print(sol([1, 2, 3, 4, 4, 5]))
    print(sol([1, 2, 3, 3, 4, 4, 5, 5]))
