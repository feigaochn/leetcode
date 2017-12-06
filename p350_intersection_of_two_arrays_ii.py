# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: intersection of two arrays ii
#
# Given two arrays, write a function to compute their intersection.
# 
# Example:
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].
# 
# Note:
# 
# Each element in the result should appear as many times as it shows in both
# arrays.
# The result can be in any order.
# 
# Follow up:
# 
# What if the given array is already sorted? How would you optimize your
# algorithm?
# What if nums1's size is small compared to num2's size? Which algorithm is
# better?
# What if elements of nums2 are stored on disk, and the memory is limited such
# that you cannot load all elements into the memory at once?
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Binary Search
# Hash Table
# Two Pointers
# Sort
# 
# Show Similar Problems
# 
#  (E) Intersection of Two Arrays


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        results = []
        nums1.sort()
        nums2.sort()
        i1, i2 = 0, 0
        l1, l2 = len(nums1), len(nums2)
        while i1 < l1 and i2 < l2:
            if nums1[i1] == nums2[i2]:
                results.append(nums1[i1])
                i1 += 1
                i2 += 1
            elif nums1[i1] < nums2[i2]:
                i1 += 1
            else:
                i2 += 1

        return results


def main():
    solver = Solution()
    tests = [
        (([1, 2, 2, 1], [2, 2]), [2, 2]),
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.intersect(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
