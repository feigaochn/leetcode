#!/bin/env python3

# author: Fei Gao
#
# Largest Number
#
# Given a list of non negative integers, arrange them such that they form the largest number.
# For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.
# Note: The result may be very large, so you need to return a string instead of an integer.
# Credits:Special thanks to @ts for adding this problem and creating all test cases.
# Show Tags


class Solution:
    # @param num, an integer[]
    # @return a string
    def largestNumber(self, num):
        def cmp_to_key(mycmp):
            'Convert a cmp= function into a key= function'

            class K(object):
                def __init__(self, obj, *args):
                    self.obj = obj

                def __lt__(self, other):
                    return mycmp(self.obj, other.obj) < 0

                def __gt__(self, other):
                    return mycmp(self.obj, other.obj) > 0

                def __eq__(self, other):
                    return mycmp(self.obj, other.obj) == 0

                def __le__(self, other):
                    return mycmp(self.obj, other.obj) <= 0

                def __ge__(self, other):
                    return mycmp(self.obj, other.obj) >= 0

                def __ne__(self, other):
                    return mycmp(self.obj, other.obj) != 0

            return K

        def cmp2(s1, s2):
            if s1 + s2 > s2 + s1:
                return -1
            elif s1 + s2 == s2 + s1:
                return 0
            else:
                return 1

        ss = map(str, num)
        ss = sorted(ss, key=cmp_to_key(cmp2))
        ss = ''.join(ss)
        ss = ss.lstrip('0')
        if not ss: ss = '0'
        return ss


def main():
    solver = Solution()
    tests = [[3, 30, 34, 5, 9], [0, 0]]
    for test in tests:
        print(test)
        print(' ->')
        result = solver.largestNumber(test)
        print(result)
        print('~' * 10)
    pass


if __name__ == '__main__':
    main()
    pass
