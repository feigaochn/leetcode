#!/usr/bin/env python
# coding: utf-8


class Solution:
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        N = len(nums)
        from itertools import accumulate
        sums = list(accumulate(nums))
        for i in range(len(nums) - 1, k - 1, -1):
            sums[i] -= sums[i - k]
        print(sums)
        best_k_any = [-1] * (k - 1)
        best_k_any.append(k - 1)
        for i in range(k, N):
            last = best_k_any[-1]
            if sums[i] > sums[last]:
                best_k_any.append(i)
            else:
                best_k_any.append(last)
        # print(best_k_any)
        best_2k = [(-1, -1)] * (2 * k - 1)
        best_2k.append((k - 1, 2 * k - 1))
        for i in range(2 * k, N):
            last = best_2k[-1]
            last_sum = sums[last[0]] + sums[last[1]]
            i1 = best_k_any[i - k]
            cur_sum = sums[i1] + sums[i]
            if cur_sum > last_sum:
                best_2k.append((i1, i))
            else:
                best_2k.append(last)
        # print(best_2k)
        best_3k = [(-1, -1, -1)] * (3 * k - 1)
        best_3k.append((k - 1, 2 * k - 1, 3 * k - 1))
        for i in range(3 * k, len(nums)):
            last = (l0, l1, l2) = best_3k[-1]
            last_sum = sums[l0] + sums[l1] + sums[l2]
            i0, i1 = best_2k[i - k]
            cur_sum = sums[i0] + sums[i1] + sums[i]
            if cur_sum > last_sum:
                best_3k.append((i0, i1, i))
            else:
                best_3k.append(last)
        # print(best_3k)
        return [x - k + 1 for x in best_3k[-1]]


if __name__ == '__main__':
    sol = Solution().maxSumOfThreeSubarrays
    print(sol([1, 2, 1, 2, 6, 7, 5, 1], 2))
