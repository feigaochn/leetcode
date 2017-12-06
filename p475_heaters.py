# !/usr/bin/env python
# coding: utf-8


class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: list[int]
        :type heaters: list[int]
        :rtype: int
        """
        if not houses:
            return 0
        houses.sort()
        heaters.sort()
        heaters.insert(0, (houses[-1] + heaters[-1]) * -3)
        heaters.append((houses[-1] + heaters[-1]) * 3)
        p = 0
        h = 0
        best = 0
        while h < len(houses):
            while houses[h] >= heaters[p + 1]:
                p += 1
            assert heaters[p] <= houses[h] < heaters[p + 1]
            radius = min(abs(houses[h] - heaters[p]), abs(houses[h] - heaters[p + 1]))
            best = max(best, radius)
            h += 1

        return best


if __name__ == '__main__':
    sol = Solution()
    print(sol.findRadius([1, 2, 3], [2]))
    print(sol.findRadius([1, 2, 3, 4], [1, 4]))
    print(sol.findRadius([1, 2, 3, 4], [1]))
    print(sol.findRadius(list(range(25000)), [1]))
    print(sol.findRadius([1, 19], [9, 10, 11]))
