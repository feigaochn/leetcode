#!/usr/bin/env python3
# coding: utf-8

"""A simple python3 script template.
"""

import sys
from collections import Counter


class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        c = Counter(s)
        return ''.join(s * r for s, r in c.most_common())


def main(args):
    print(Solution().frequencySort("aabbaAAz"))


if __name__ == '__main__':
    main(sys.argv[1:])
