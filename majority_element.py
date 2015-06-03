#!/bin/env python3

# author: Fei Gao
#
# Majority Element
#
# Given an array of size n, find the majority element. The majority element is the element that appears more than &lfloor; n/2 &rfloor; times.
# You may assume that the array is non-empty and the majority element always exist in the array.
# Credits:Special thanks to @ts for adding this problem and creating all test cases.
# Show Tags


class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        from collections import Counter

        c = Counter(num)
        return c.most_common(1)[0][0]


def main():
    solver = Solution()
    tests = [[1], [1,2], [1,2,2]]
    for test in tests:
        print(test)
        print(' ->')
        result = solver.majorityElement(test)
        print(result)
        print('~' * 10)
    pass


if __name__ == '__main__':
    main()
    pass
