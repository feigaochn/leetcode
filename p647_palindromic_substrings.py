#!/usr/bin/env python
# coding: utf-8


class Solution(object):
    def countSubstrings(self, string):
        """
        :type string: str
        :rtype: int
        """
        result = 0
        nlen = len(string)
        subs = [(i, i) for i in range(nlen)]  # (start, end) inclusive!!
        subs += [(i, i + 1) for i in range(nlen - 1) if string[i] == string[i + 1]]
        while subs:
            # print(subs)
            result += len(subs)
            new_subs = []
            for s, e in subs:
                if 0 <= s - 1 < e + 1 < nlen and string[s - 1] == string[e + 1]:
                    new_subs.append((s - 1, e + 1))
            subs = new_subs[::]
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.countSubstrings("abc"))
    print(sol.countSubstrings("aaa"))
