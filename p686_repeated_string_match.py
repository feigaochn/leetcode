#!/usr/bin/env python
# coding: utf-8


"""
Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

Note:
The length of A and B will be between 1 and 10000.
"""


class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        from math import ceil
        repeats = int(ceil(len(B) / len(A)))
        container = ""
        for _ in range(repeats):
            container += A
        if container.find(B) != -1:
            return repeats
        container += A
        if container.find(B) != -1:
            return repeats + 1
        return -1


if __name__ == '__main__':
    sol = Solution().repeatedStringMatch
    print(sol("abcd", "cdabcdab"))
    print(sol("abc", "cdabcdab"))
    print(sol("abc", "cdabcdab"))
