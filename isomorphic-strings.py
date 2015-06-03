# coding: utf-8

# author: Fei Gao
#
# Isomorphic Strings
#
# Given two strings s and t, determine if they are isomorphic.
# Two strings are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.
# For example,
# Given "egg", "add", return true.
# Given "foo", "bar", return false.
# Given "paper", "title", return true.
# Note:
# You may assume both s and t have the same length.
# Show Tags


class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        if not s:
            return True
        d1 = dict(zip(s, t))
        ss = ''.join(d1[c] for c in s)
        if ss != t:
            return False
        values = list(d1.values())
        if len(values) != len(set(values)):
            return False
        return True


def main():
    solver = Solution()
    tests = [
        ('egg', 'add'),
        ('foo', 'bar'),
        ('paper', 'title'),
    ]
    for test in tests:
        print(test)
        print(' ->')
        result = solver.isIsomorphic(*test)
        print(result)
        print('~'*10)
    pass


if __name__ == '__main__':
    main()
    pass
