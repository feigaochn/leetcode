# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: bulb switcher
#
# There are n bulbs that are initially off. You first turn on all the bulbs. Then, you turn off every second bulb. On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the nth round, you only toggle the last bulb.
# 
# Find how many bulbs are on after n rounds.
# 
# Example:
# 
# Given n = 3. 
# At first, the three bulbs are [off, off, off].
# After first round, the three bulbs are [on, on, on].
# After second round, the three bulbs are [on, off, on].
# After third round, the three bulbs are [on, off, off]. 
# So you should return 1, because there is only one bulb is on.
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Math
# Brainteaser

class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        return int(math.sqrt(n))


def main():
    solver = Solution()
    tests = [
        ((3,), 1),
    ]
    for params, expect in tests:
        print('-'*5 + 'TEST' + '-'*5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.bulbSwitch(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
