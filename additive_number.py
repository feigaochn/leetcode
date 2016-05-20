# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: additive number
#
# Additive number is a string whose digits can form additive sequence.
# A valid additive sequence should contain at least three numbers. Except for
# the first two numbers, each subsequent number in the sequence must be the
# sum of the preceding two.
# 
# For example:
# "112358" is an additive number because the digits can form an additive
# sequence: 1, 1, 2, 3, 5, 8.
# 1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
# "199100199" is also an additive number, the additive sequence is: 1, 99,
# 100, 199.
# 1 + 99 = 100, 99 + 100 = 199
# 
# Note: Numbers in the additive sequence cannot have leading zeros, so
# sequence 1, 2, 03 or 1, 02, 3 is invalid.
# 
# Given a string containing only digits '0'-'9', write a function to determine
# if it's an additive number.
# 
# Follow up:
# How would you handle overflow for very large input integers?
# 
# Credits:Special thanks to @jeantimex for adding this problem and creating
# all test cases.
# 
# Subscribe to see which companies asked this question


class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """

        def ok(lst, rest):
            # assert isinstance(lst, list) and isinstance(rest, str)
            if len(rest) == 0: return True
            s = lst[-1] + lst[-2]
            ss = str(s)
            if rest.find(ss) != 0:
                return False
            else:
                return ok(lst + [s], rest[len(ss):])

        for la in range(1, len(num) // 2 + 1):
            a = int(num[:la])
            if len(str(a)) != la: break
            for lb in range(1, len(num) // 2 + 1):
                if len(num) - (la + lb) < max(la, lb):
                    break
                b = int(num[la: la + lb])
                if len(str(b)) != lb: break
                if ok([a, b], num[la + lb:]):
                    return True
        return False


def main():
    solver = Solution()
    tests = [
        (('112358',), 'y'),
        (('199100199',), 'y'),
        (('1203',), 'n'),
        (('0235813',), 'n'),
        (('101',), 'y'),
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.isAdditiveNumber(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
