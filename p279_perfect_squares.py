# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: perfect squares
#
# Given a positive integer n, find the least number of perfect square numbers
# (for example, 1, 4, 9, 16, ...) which sum to n.
# 
# For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13,
# return 2 because 13 = 4 + 9.
# 
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Dynamic Programming
# Breadth-first Search
# Math
# 
# Show Similar Problems
# 
#  (E) Count Primes
#  (M) Ugly Number II


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = {0: 0}
        frontier = [0]
        while True:
            top = frontier.pop(0)
            cur = ans[top]
            x = 0
            while True:
                x += 1
                val = top + x * x
                if val == n:
                    return cur + 1
                elif val > n:
                    break
                else:
                    if val not in ans:
                        ans[val] = cur + 1
                        frontier.append(val)


def main():
    solver = Solution()
    tests = [
        ((12,), 3),
        ((13,), 2)
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.numSquares(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
