# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: word pattern
#
# Given a pattern and a string str, find if str follows the same pattern.
#  Here follow means a full match, such that there is a bijection between a
# letter in pattern and a non-empty word in str.
# 
# Examples:
# 
# pattern = "abba", str = "dog cat cat dog" should return true.
# pattern = "abba", str = "dog cat cat fish" should return false.
# pattern = "aaaa", str = "dog cat cat dog" should return false.
# pattern = "abba", str = "dog dog dog dog" should return false.
# 
# Notes:
# You may assume pattern contains only lowercase letters, and str contains
# lowercase letters separated by a single space.
# 
# Credits:Special thanks to @minglotus6 for adding this problem and creating
# all test cases.
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Hash Table
# 
# Show Similar Problems
# 
#  (E) Isomorphic Strings
#  (H) Word Pattern II


class Solution(object):
    def wordPattern(self, pattern, string):
        """
        :type pattern: str
        :type string: str
        :rtype: bool
        """
        words = string.split(' ')
        if len(pattern) != len(words) or len(set(pattern)) != len(set(words)):
            return False
        from collections import defaultdict
        match = defaultdict(set)
        for p, w in zip(pattern, words):
            match[p].add(w)
        return all(len(l) == 1 for l in match.values())


def main():
    solver = Solution()
    tests = [
        (('abba', 'd c c d'), True),
        (('abba', 'd c c f'), False),
        (('aaaa', 'd c c d'), False),
        (('abba', 'd d d d'), False),
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.wordPattern(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
