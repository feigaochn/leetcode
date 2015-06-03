#!/usr/bin/env python3
# -*- coding: utf8 -*-


class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        v1.extend([0] * max(0, len(v2) - len(v1)))
        v2.extend([0] * max(0, len(v1) - len(v2)))
        if v1 < v2:
            return -1
        elif v1 > v2:
            return 1
        else:
            return 0


def main():
    pass


if __name__ == '__main__':
    main()