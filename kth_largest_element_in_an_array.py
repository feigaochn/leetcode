# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: kth largest element in an array
#
# Find the kth largest element in an unsorted array. Note that it is the kth
# largest element in the sorted order, not the kth distinct element.
# 
# For example,
# Given [3,2,1,5,6,4] and k = 2, return 5.
# 
# Note:
# You may assume k is always valid, 1 ≤ k ≤ array's length.
# Credits:Special thanks to @mithmatt for adding this problem and creating all
# test cases.
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Divide and Conquer
# Heap


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # TODO
        return


def main():
    solver = Solution()
    tests = [
        (('param',), 'result'),
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.findKthLargest(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
