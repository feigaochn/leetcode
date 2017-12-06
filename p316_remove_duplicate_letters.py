# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: remove duplicate letters
#
# Given a string which contains only lowercase letters, remove duplicate
# letters so that every letter appear once and only once. You must make sure
# your result is the smallest in lexicographical order among all possible
# results.
# 
# Example:
# 
# Given "bcabc"
# Return "abc"
# 
# Given "cbacdcbc"
# Return "acdb"
# 
# Credits:Special thanks to @dietpepsi for adding this problem and creating
# all test cases.
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Stack
# Greedy


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        def solve(s, prefix):
            """

            :type s: str
            :param prefix:
            :return:
            """
            unique = len(set(s))
            if len(s) == unique:
                return prefix + s
            else:
                p = len(s)
                ss = set()
                while len(ss) < unique:
                    p -= 1
                    ss.add(s[p])
                p += 1
                prefix += min(s[:p])
                remain = ''.join(c for c in s[1+s.find(prefix[-1]):] if c not in prefix)
                # print(prefix, remain, s, p, s[p])
                return solve(remain, prefix)
        return solve(s, '')


def main():
    solver = Solution()
    tests = [
        (('bcabc',), 'abc'),
        (('cbacdcbc',), 'acdb'),
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.removeDuplicateLetters(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
