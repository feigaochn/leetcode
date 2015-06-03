# coding: utf-8

# author: Fei Gao
#
# Contains Duplicate Ii

# Given an array of integers and an integer k, find out whether there there are two distinct indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k.
# Show Tags


class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        if len(nums) <= k:
            return len(set(nums)) != len(nums)

        unique = set(nums[:k + 1])
        if len(unique) <= k:
            return True

        for i in range(len(nums) - k - 1):
            unique.remove(nums[i])
            unique.add(nums[i + k + 1])
            if len(unique) <= k:
                return True

        return False


def main():
    solver = Solution()
    tests = [
        ([0, 1, 0], 2),
        ([0, 1, 0], 1),
    ]
    for test in tests:
        print(test)
        print(' ->')
        result = solver.containsNearbyDuplicate(*test)
        print(result)
        print('~' * 10)
    pass


if __name__ == '__main__':
    main()
    pass
