#!/bin/env python3

# author: Fei Gao
#
# Excel Sheet Column Title
#
# Given a positive integer, return its corresponding column title as appear in an Excel sheet.
# For example:
#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB 
# Credits:Special thanks to @ifanchu for adding this problem and creating all test cases.
# Show Tags


class Solution:
    # @param n, an integer
    # @return a string
    def convertToTitle(self, n):
        s = ''
        while n != 0:
            s = chr(ord('A') + (n-1)%26) + s
            n = (n-1) // 26
        return s


def main():
    solver = Solution()
    tests = [1, 2, 26, 1*26+1, 1*26+2, 1*26+26, 2*26 + 1]
    for test in tests:
        print(test)
        print(' ->')
        result = solver.convertToTitle(test)
        print(result)
        print('~'*10)
    pass
if __name__ == '__main__':
    main()
    pass
