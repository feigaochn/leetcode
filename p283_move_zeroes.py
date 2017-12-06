# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: move zeroes
#
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# 
# For example, given nums  = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
# 
# Note:
# 
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
# 
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Array
# Two Pointers
# 
# Show Similar Problems
# 
#  (E) Remove Element

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        iz = 0
        while iz < len(nums):
            if nums[iz] != 0:
                iz += 1
                continue
            elif nums[iz] == 0:
                inz = iz
                while inz < len(nums):
                    if nums[inz] != 0:
                        break
                    inz += 1
                if inz >= len(nums):
                    break
                else:
                    nums[iz] = nums[inz]
                    nums[inz] = 0


def main():
    solver = Solution()
    tests = [
        (([0, 1, 0, 3, 12],), [1, 3, 12, 0, 0]),
    ]
    for params, expect in tests:
        print('-'*5 + 'TEST' + '-'*5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        solver.moveZeroes(*params)
        print('Result: ' + str(params))
    pass


if __name__ == '__main__':
    main()
    pass
