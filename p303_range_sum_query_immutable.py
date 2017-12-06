# coding: utf-8

# author: Fei Gao
#
# Range Sum Query Immutable

# Given an integer array nums, find the sum of the elements between indices i and j (i &le; j), inclusive.
# Example:
# Given nums = [-2, 0, 3, -5, 2, -1]
# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
# Note:
# You may assume that the array does not change.
# There are many calls to sumRange function.
# Subscribe to see which companies asked this question


class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self._sums = [0]
        for num in nums:
            self._sums.append(num + self._sums[-1])
        

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self._sums[j+1] - self._sums[i]
        


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)
        return True


def main():
    solver = NumArray([-2, 0, 3, -5, 2, -1])
    tests = [
        (0, 2),
        (2, 5),
        (0, 5)
    ]
    for test in tests:
        print(test)
        print(' ->')
        result = solver.sumRange(*test)
        print(result)
        print('~'*10)
    pass


if __name__ == '__main__':
    main()
    pass
