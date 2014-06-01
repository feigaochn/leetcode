# author: Fei Gao
# date: Sun Jun  1 10:21:15 2014
#
# Letter Combinations Of A Phone Number
#
# Given a digit string, return all possible letter combinations that the number could represent.
# A mapping of digit to letters (just like on the telephone buttons) is given below.
# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# Note:
# Although the above answer is in lexicographical order, your answer could be in any order you want.

import itertools


class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        number_letters = {}
        for i in range(2, 7):
            number_letters[str(i)] = [chr(j + ord('a')) for j in range((i - 2) * 3, (i - 2) * 3 + 3)]
        number_letters[str(7)] = 'pqrs'
        number_letters[str(8)] = 'tuv'
        number_letters[str(9)] = list('wxyz')
        number_letters[str(0)] = ' '
        number_letters['*'] = '+'
        number_letters['#'] = ''
        number_letters['1'] = ''
        # print(number_letters.items())
        result = ['']
        for n in digits:
            result = [a + b for a, b in itertools.product(result, number_letters[n])]
        return result
        pass


def main():
    solver = Solution()
    for i in range(10):
        print(str(i), solver.letterCombinations(str(i)))

    print('', solver.letterCombinations(''))
    pass


if __name__ == '__main__':
    main()
    pass
