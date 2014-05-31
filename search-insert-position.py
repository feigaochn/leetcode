# author: Fei Gao
#
# Search insert position
#
# Given a sorted array and a target value, return the index if the target
# is found. If not, return the index where it would be if it were inserted
# in order.
# You may assume no duplicates in the array.
# Here are few examples.
# [1,3,5,6], 5 &#8594; 2
# [1,3,5,6], 2 &#8594; 1
# [1,3,5,6], 7 &#8594; 4
# [1,3,5,6], 0 &#8594; 0

import bisect


class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        return bisect.bisect_left(A, target)
        pass


def main():
    pass


if __name__ == '__main__':
    pass
