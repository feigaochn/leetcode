"""
We are given an array A of positive integers, and two positive integers L and R
(L <= R).

Return the number of (contiguous, non-empty) subarrays such that the value of
the maximum array element in that subarray is at least L and at most R.

Example :
Input:
A = [2, 1, 4, 3]
L = 2
R = 3
Output: 3
Explanation: There are three subarrays that meet the requirements: [2], [2, 1],
             [3].

Note:
    L, R  and A[i] will be an integer in the range [0, 10^9].
    The length of A will be in the range of [1, 50000].
"""


class Solution:

    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        from itertools import groupby, accumulate

        def cmp(x):
            if x < L:
                return -1
            elif L <= x <= R:
                return 1
            else:
                return 0

        gps = [k * len(list(l)) for k, l in groupby(A, cmp)]

        def splitAt(lst, v):
            result = [[]]
            for x in lst:
                if x == v:
                    result.append([])
                else:
                    result[-1].append(x)
            return [r for r in result if r]

        result = 0
        for gp in splitAt(gps, 0):
            for i, (n, ps) in enumerate(zip(gp, accumulate(map(abs, gp)))):
                if n > 0:
                    result += n * (n + 1) // 2
                result += abs(n * (ps - (abs(n))))

        return result


sol = Solution().numSubarrayBoundedMax
tests = [(([2, 1, 4, 3], 2, 3), 3), (([1, 1, 0, 1, 0, 0], 1, 1), 17)]
for inputs, expect in tests:
    print(sol(*inputs), " ?= ", expect)
