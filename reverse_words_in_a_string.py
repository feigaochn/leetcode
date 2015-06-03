# author: Fei Gao
# date: Sun Jun  1 13:08:22 2014
#
# Reverse Words In A String
#
# Given an input string, reverse the string word by word.
# For example,
# Given s = "the sky is blue",
# return "blue is sky the".
# click to show clarification.
# Clarification:
# What constitutes a word?
# A sequence of non-space characters constitutes a word.
# Could the input string contain leading or trailing spaces?
# Yes. However, your reversed string should not contain leading or trailing spaces.
# How about multiple spaces between two words?
# Reduce them to a single space in the reversed string.


class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        return ' '.join(filter(lambda x: len(x) > 0, s.split(' '))[::-1]) if s is not None else ''
        pass


def main():
    solver = Solution()

    s = ' blue - hi    word'
    print(s, solver.reverseWords(s))

    s = None
    print(s, solver.reverseWords(s))

    pass


if __name__ == '__main__':
    main()
    pass
