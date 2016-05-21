# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: integer to english words
#
# Convert a non-negative integer to its english words representation. Given
# input is guaranteed to be less than 231 - 1.
# 
# For example,
# 
# 123 -> "One Hundred Twenty Three"
# 12345 -> "Twelve Thousand Three Hundred Forty Five"
# 1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty
# Seven"
# 
# Did you see a pattern in dividing the number into chunk of words? For
# example, 123 and 123000.
# Group the number by thousands (3 digits). You can write a helper function
# that takes a number less than 1000 and convert just that chunk to words.
# There are many edge cases. What are some good test cases? Does your code
# work with input such as 0? Or 1000010? (middle chunk is zero and should not
# be printed out)
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Math
# String
# 
# Show Similar Problems
# 
#  (M) Integer to Roman


class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: return 'Zero'
        n2s = dict(
            [(1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five'), (6, 'Six'), (7, 'seven'),
             (8, 'eight'), (9, 'nine'), (10, 'ten'), (11, 'eleven'), (12, 'twelve'), (13, 'thirteen'), (14, 'fourteen'),
             (15, 'fifteen'), (16, 'sixteen'), (17, 'seventeen'), (18, 'eighteen'), (19, 'nineteen'),
             (20, 'twenty'), (30, 'thirty'), (40, 'forty'), (50, 'fifty'), (60, 'sixty'), (70, 'seventy'),
             (80, 'eighty'), (90, 'ninety')])

        if num in n2s: return n2s[num].capitalize()

        def three(n):
            results = []
            if n >= 100:
                results.extend([n2s[n // 100], 'hundred'])
            n %= 100
            if n in n2s:
                results.append(n2s[n])
            else:
                if n >= 20: results.extend([n2s[n - (n % 10)], n2s[n % 10]])
            return results

        r = []
        if num >= 10 ** 9:
            r.extend(three(num // (10 ** 9)))
            r.append('billion')
            num %= (10 ** 9)
        if num >= 10 ** 6:
            r.extend(three(num // (10 ** 6)))
            r.append('million')
            num %= (10 ** 6)
        if num >= 10 ** 3:
            r.extend(three(num // (10 ** 3)))
            r.append('thousand')
            num %= (10 ** 3)
        r.extend(three(num))
        return ' '.join(map(str.capitalize, r))


def main():
    solver = Solution()
    tests = [
        ((123,), "One Hundred Twenty Three"),
        ((12345,), "Twelve Thousand Three Hundred Forty Five"),
        ((1234567,), "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"),
        ((0,), 'Zero'),
        ((10000,), 'Ten Thousand'),
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.numberToWords(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
