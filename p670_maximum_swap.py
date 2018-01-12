#!/usr/bin/env python
# coding: utf-8


class Solution:
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num
        digits = [int(c) for c in str(num)]
        if all(a >= b for a, b in zip(digits, digits[1:])):
            return num
        digits = [(v, i) for i, v in enumerate(digits)]

        def find_big(items):
            big = max(items)
            if items[0][0] == big[0]:
                return find_big(items[1:])
            else:
                return big

        big = find_big(digits)

        small = None
        for (v, j) in digits:
            if v < big[0]:
                small = (v, j)
                break
        digits[small[1]] = big
        digits[big[1]] = small
        # print(big, small)
        return int(''.join(str(d) for d, _ in digits))


if __name__ == '__main__':
    sol = Solution().maximumSwap
    print(sol(2736))
    print(sol(9973))
    print(sol(99901))
    print(sol(98004365))
    print(sol(0))
