# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: burst balloons
#
#     Given n balloons, indexed from 0 to n-1. Each balloon is painted with a
#     number on it represented by array nums.
# 
#     You are asked to burst all the balloons. If the you burst
#     balloon i you will get nums[left] * nums[i] * nums[right] coins. Here
# left
#     and right are adjacent indices of i. After the burst, the left and right
#     then becomes adjacent.
# 
#     Find the maximum coins you can collect by bursting the balloons wisely.
# 
# Note:
#     (1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore
# you can not burst them.
#     (2) 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
# 
# Example:
# 
#     Given [3, 1, 5, 8]
# 
#     Return 167
# 
#     nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
#    coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
# 
# Credits:Special thanks to @dietpepsi for adding this problem and creating
# all test cases.
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Divide and Conquer
# Dynamic Programming


class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: list[int]
        :rtype: int
        """
        nums.append(1)
        nums.insert(0, 1)
        le = len(nums)

        dp = [[0 for _ in range(le)] for _ in range(le)]

        for d in range(2, le):
            for s in range(le):
                e = s + d
                if e >= le:
                    break
                dp[s][e] = max(nums[s] * nums[k] * nums[e] + dp[s][k] + dp[k][e] for k in range(s + 1, e))
        return dp[0][le - 1]


def main():
    solver = Solution()
    tests = [
        (([3, 1, 5, 8],), 167),
        (([5],), 5),
        (([5,5],), 30),
        (([2]*500,), None)
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.maxCoins(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
