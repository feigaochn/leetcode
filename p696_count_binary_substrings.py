"""
Give a string s, count the number of non-empty (contiguous) substrings that
have the same number of 0's and 1's, and all the 0's and all the 1's in these
substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they
occur.
"""


class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        from itertools import groupby
        alters = [len(list(gp[1])) for gp in groupby(s)]
        return sum(min(l, r) for l, r in zip(alters, alters[1:]))


def main():
    sol = Solution().countBinarySubstrings
    print(sol("00110011"), '?= 6')
    print(sol("10101"), '?= 4')


if __name__ == '__main__':
    main()
