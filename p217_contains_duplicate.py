# coding: utf-8

# author: Fei Gao
#
# Contains Duplicate

# Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice
# in the array, and it should return false if every element is distinct.
# Show Tags


class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))


def main():
    solver = Solution()
    tests = [
        ([0, 1],)
    ]
    for test in tests:
        print(test)
        print(' ->')
        result = solver.containsDuplicate(*test)
        print(result)
        print('~' * 10)
    pass


if __name__ == '__main__':
    main()
    pass
