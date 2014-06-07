# author: Fei Gao
#
# Length Of Last Word
#
# Given a string s consists of upper/lower-case alphabets and empty space
# characters ' ', return the length of last word in the string.
# If the last word does not exist, return 0.
# Note: A word is defined as a character sequence consists of non-space
# characters only.
# For example,
# Given s = "Hello World",
# return 5.


class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        words = s.strip().split()
        return 0 if len(words) == 0 else len(words[-1])


def main():
    solver = Solution()
    for test in ['hi wor  ', ' ']:
        print(test, solver.lengthOfLastWord(test))
    pass


if __name__ == '__main__':
    main()
    pass
