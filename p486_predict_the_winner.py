#!/usr/bin/env python
# coding: utf-8


"""
Given an array of scores that are non-negative integers. Player 1 picks one
of the numbers from either end of the array followed by the player 2 and then
player 1 and so on. Each time a player picks a number, that number will not
be available for the next player. This continues until all the scores have
been chosen. The player with the maximum score wins.

Given an array of scores, predict whether player 1 is the winner. You can
assume each player plays to maximize his score.
"""


class Solution:
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cache = {}

        def best(s, e):
            if (s, e) in cache:
                pass
            elif e - s <= 2:
                cache[(s, e)] = max(nums[s:e])
            else:
                cache[(s, e)] = sum(nums[s:e]) - min(best(s + 1, e), best(s, e - 1))
            return cache[(s, e)]

        return best(0, len(nums)) >= sum(nums) / 2


if __name__ == '__main__':
    sol = Solution().PredictTheWinner
    print(sol([1, 5, 2]))
    print(sol([1, 5, 233, 7]))
    print(sol([1, 5, 233, 7, 1]))
    print(sol(list(range(10)) + list(range(10, 0, -1))))
    print(sol([10, 17, 11, 16, 17, 9, 14, 17, 18, 13, 11, 4, 17, 18, 15, 3, 13, 10, 6, 10]), '?= true')
    print(sol([9337301, 0, 2, 2245036, 4, 1997658, 5, 2192224, 960000,
               1261120, 8824737, 1, 1161367, 9479977, 7, 2356738, 5, 4, 9]),
          '?= true')
    print(sol([877854, 7113184, 3270279, 2243110, 1902970, 9268285,
               8784788, 3837608, 6582224, 8751349, 6928223, 3108757,
               1120749, 1872910, 7762600, 4220578, 4692740, 3409910,
               6807125, 6808582]))
