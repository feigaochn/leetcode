#!/usr/bin/env python
# coding: utf-8

# p657

class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x, y = 0, 0
        for m in moves:
            if m == 'U':
                y += 1
            elif m == 'D':
                y -= 1
            elif m == 'L':
                x -= 1
            elif m == 'R':
                x += 1
        return (x, y) == (0, 0)


if __name__ == '__main__':
    sol = Solution()
    print(sol.judgeCircle("UD"))
    print(sol.judgeCircle("LL"))
