#!/usr/bin/env python3
# coding: utf-8

import sys


class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return []
        nr, nc = len(matrix), len(matrix[0])
        ret = []
        for s in range(nr + nc - 1):
            if s % 2 == 1:
                for i in range(max(0, s - nc + 1), min(nr, s + 1)):
                    try:
                        ret.append(matrix[i][s - i])
                    except IndexError:
                        pass
            else:
                for i in range(min(nr - 1, s), max(0, s - nc + 1) - 1, -1):
                    try:
                        ret.append(matrix[i][s - i])
                    except IndexError:
                        pass
        return ret


def main(args):
    mat = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    mat = [[i,] for i in  range(100)]
    print(Solution().findDiagonalOrder(mat))
    return


if __name__ == '__main__':
    main(sys.argv[1:])
