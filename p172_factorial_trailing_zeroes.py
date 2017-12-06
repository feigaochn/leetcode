#!/usr/bin/env python3
# -*- coding: utf8 -*-

class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        f = 5
        cnt = 0
        while f <= n:
            cnt += (n // f)
            f *= 5
        return cnt


def main():
    pass


if __name__ == '__main__':
    main()