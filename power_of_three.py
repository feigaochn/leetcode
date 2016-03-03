# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: power of three
#
#     Given an integer, write a function to determine if it is a power of
# three.
# 
# Follow up:
#     Could you do it without using any loop / recursion?
# 
# Credits:Special thanks to @dietpepsi for adding this problem and creating
# all test cases.
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Math
# 
# Show Similar Problems
# 
#  (E) Power of Two


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n > 1:
            if n % 3 == 0:
                n //= 3
            else:
                break
        return n == 1


def main():
    solver = Solution()
    tests = [
        ((1,), True),
        ((2,), False),
        ((3,), True)
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.isPowerOfThree(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
