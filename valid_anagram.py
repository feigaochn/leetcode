# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: valid anagram
#
# Given two strings s and t, write a function to determine if t is an anagram of s.
# For example,
# s = "anagram", t = "nagaram", return true.
# s = "rat", t = "car", return false.
# 
# Note:
# You may assume the string contains only lowercase alphabets.
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Hash Table
# Sort
# 
# Show Similar Problems
# 
#  (M) Group Anagrams
#  (E) Palindrome Permutation


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(list(s)) == sorted(list(t))


def main():
    solver = Solution()
    tests = [
        (('abc', 'cba'), True),
        (('abc', 'def'), False)
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.isAnagram(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
