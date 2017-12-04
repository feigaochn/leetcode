#!/usr/bin/env python
# coding: utf-8


"""
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.
"""


class Solution:
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        p = 0
        while p < len(asteroids) - 1:
            if p < 0:
                p += 1
            elif asteroids[p] > 0 and asteroids[p + 1] < 0:
                m1 = abs(asteroids[p])
                m2 = abs(asteroids[p + 1])
                if m1 > m2:
                    asteroids.pop(p + 1)
                elif m1 < m2:
                    p -= 1
                    asteroids.pop(p + 1)
                elif m1 == m2:
                    asteroids.pop(p + 1)
                    asteroids.pop(p)
                    p -= 1
            else:
                p += 1
        return asteroids


if __name__ == '__main__':
    sol = Solution().asteroidCollision
    print(sol([5, 10, -5]))
    print(sol([]))
    print(sol([1, -2, -2, 2]))
    print(sol(list(range(1, 10000)) + [-100000]))
    print(sol([1, 2, 3, -5]))
    print(sol([-1, 1]))
    print(sol([8, -8]))
    print(sol([10, 2, -5]))
    print(sol([-2, -1, 1, 2]))
