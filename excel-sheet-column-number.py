#!/bin/env python3

# author: Fei Gao
#
# Excel Sheet Column Number
#
# Related to question Excel Sheet Column Title
# Given a column title as appear in an Excel sheet, return its corresponding column number.
# For example:
# A -&gt; 1
#     B -&gt; 2
#     C -&gt; 3
#     ...
#     Z -&gt; 26
#     AA -&gt; 27
#     AB -&gt; 28 
# Credits:Special thanks to @ts for adding this problem and creating all test cases.
# Show Tags


class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        n = 0
        b = 1
        for c in s[::-1]:
            n += (ord(c) - ord('A') + 1) * b
            b = b * 26
        return n


def main():
    solver = Solution()
    tests = ['A', 'B', 'Z', 'AA', 'AB', 'AZ', 'BA', 'BB', 'BZ']
    for test in tests:
        print(test)
        print(' ->')
        result = solver.titleToNumber(test)
        print(result)
        print('~' * 10)
    pass


if __name__ == '__main__':
    main()
    pass
