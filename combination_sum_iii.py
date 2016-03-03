# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: combination sum iii
#
# Find all possible combinations of k numbers that add up to a number n, given
# that only numbers from 1 to 9 can be used and each combination should be a
# unique set of numbers.
# Ensure that numbers within the set are sorted in ascending order.
# 
#  Example 1:
# Input:  k = 3,  n = 7
# Output:
# 
# [[1,2,4]]
# 
#  Example 2:
# Input:  k = 3,  n = 9
# Output:
# 
# [[1,2,6], [1,3,5], [2,3,4]]
# 
# Credits:Special thanks to @mithmatt for adding this problem and creating all
# test cases.
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Array
# Backtracking
# 
# Show Similar Problems
# 
#  (M) Combination Sum


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        # TODO
        solutions = []

        def sol(lo, k, n, ps):
            if k == 1:
                if lo <= n <= 9:
                    solutions.append(ps + [n])
                else:
                    return
            for x in range(lo, 10):
                sol(x + 1, k - 1, n - x, ps + [x])

        sol(1, k, n, [])
        return solutions


def main():
    solver = Solution()
    tests = [
        ((3, 7), 'result'),
        ((3, 9), None)
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.combinationSum3(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
