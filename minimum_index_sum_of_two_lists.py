#!/usr/bin/env python
# coding: utf-8


class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        d1 = dict(zip(list1, range(len(list1))))
        d2 = dict(zip(list2, range(len(list2))))

        best_idx = len(list1) + len(list2)
        best = []
        for key in set(d1) & set(d2):
            idx = d1[key] + d2[key]
            if idx < best_idx:
                best_idx = idx
                best = [key]
            elif idx == best_idx:
                best.append(key)
        return best


if __name__ == '__main__':
    sol = Solution()
    print(sol.findRestaurant(
        ["Shogun", "Tapioca Express", "Burger King", "KFC"],
        ["KFC", "Shogun", "Burger King"]))
