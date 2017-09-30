#! /usr/bin/env python3


class Solution:
    def flipLights(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        from functools import reduce
        from operator import xor

        lights = 2**n - 1
        flip_all = lights
        flip_odd = reduce(xor, [2**k for k in range(0, n, 2)], 0)
        flip_even = reduce(xor, [2**k for k in range(1, n, 2)], 0)
        flip_3k = reduce(xor, [2**k for k in range(0, n, 3)], 0)
        flips = [flip_all, flip_odd, flip_even, flip_3k]
        # print(*map(bin, [flip_all, flip_odd, flip_even, flip_3k]))
        # m %= 4
        old = set([lights])
        while m:
            new = set(xor(light, flip) for flip in flips for light in old)
            old = new
            m -= 1
        # print(*map(bin, old))
        return len(old)


sol = Solution()

print(sol.flipLights(1, 1))
print(sol.flipLights(2, 1))
print(sol.flipLights(3, 1))
print(sol.flipLights(1000, 999))
