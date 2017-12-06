# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: reverse vowels of a string
#
# Write a function that takes a string as input and reverse only the vowels of
# a string.
# 
# Example 1:
# Given s = "hello", return "holle".
# 
# Example 2:
# Given s = "leetcode", return "leotcede".
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Two Pointers
# String
# 
# Show Similar Problems
# 
#  (E) Reverse String


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        sl = list(s)
        vs = 'aeiouAEIOU'
        l = len(s)
        head, tail = 0, l-1
        while True:
            while head < l and sl[head] not in vs:
                head += 1
            while tail >= 0 and sl[tail] not in vs:
                tail -= 1
            if head >= tail:
                break
            sl[head], sl[tail] = sl[tail], sl[head]
            head += 1
            tail -= 1
        return ''.join(sl)


def main():
    solver = Solution()
    tests = [
        (('param',), 'result'),
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.reverseVowels(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
