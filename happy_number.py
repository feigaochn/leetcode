# coding: utf-8

# author: Fei Gao
#
# Happy Number
#
# Write an algorithm to determine if a number is "happy".
# A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
# Example:&nbsp;19 is a happy number
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
# Credits:Special thanks to @mithmatt and @ts for adding this problem and creating all test cases.
# Show Tags


class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        def tran(m):
            return sum(map(lambda x: int(x) ** 2, list(str(m))))

        nums = {n}

        while True:
            n = tran(n)
            if n == 1:
                return True
            elif n in nums:
                return False
            else:
                nums.add(n)


def main():
    solver = Solution()
    tests = [19, 20, 2]
    for test in tests:
        print(test)
        print(' ->')
        result = solver.isHappy(test)
        print(result)
        print('~' * 10)
    pass


if __name__ == '__main__':
    main()
    pass