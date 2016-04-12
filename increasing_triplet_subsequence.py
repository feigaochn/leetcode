# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: increasing triplet subsequence
#
# Given an unsorted array return whether an increasing subsequence of length 3
# exists or not in the array.
# 
# Formally the function should:
# Return true if there exists i, j, k
# such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1
# else return false.
# 
# Your algorithm should run in O(n) time complexity and O(1) space complexity.
# 
# Examples:
# Given [1, 2, 3, 4, 5],
# return true.
# 
# Given [5, 4, 3, 2, 1],
# return false.
# 
# Credits:Special thanks to @DjangoUnchained for adding this problem and
# creating all test cases.
# 
# Subscribe to see which companies asked this question
# 
# Show Similar Problems
# 
#  (M) Longest Increasing Subsequence


class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # TODO
        if len(nums) < 3:
            return False
        dp = [nums[0]]
        for n in nums[1:]:
            if len(dp) == 2:
                if dp[-1] < n:
                    return True
                elif dp[0] < n < dp[1]:
                    dp[1] = n
                elif n < dp[0]:
                    dp.append(n)  # len 3: [1 2 0]
            elif len(dp) == 1:
                if dp[-1] < n:
                    dp.append(n)
                elif n < dp[-1]:
                    dp[0] = n
            elif len(dp) == 3:
                if dp[1] < n:
                    return True
                elif dp[2] < n <= dp[1]:
                    dp = [dp[2], n]
                elif n < dp[2]:
                    dp[2] = n
        return False


def main():
    solver = Solution()
    tests = [
        (([1,2,3,4,5],), True),
        (([3,2,1],), False),
        (([1,2,0,2,3],), True)
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.increasingTriplet(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
