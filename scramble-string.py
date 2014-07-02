# author: Fei Gao
#
# Scramble String
#
# Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.
# Below is one possible representation of s1 = "great":
#     great
#    /    \
#   gr    eat
#  / \    /  \
# g   r  e   at
#            / \
#           a   t
# To scramble the string, we may choose any non-leaf node and swap its two children.
# For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".
#     rgeat
#    /    \
#   rg    eat
#  / \    /  \
# r   g  e   at
#            / \
#           a   t
# We say that "rgeat" is a scrambled string of "great".
# Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".
#     rgtae
#    /    \
#   rg    tae
#  / \    /  \
# r   g  ta  e
#        / \
#       t   a
# We say that "rgtae" is a scrambled string of "great".
# Given two strings s1 and s2 of the same length, determine if s2 is a
# scrambled string of s1.


class Solution:
    # @return a boolean

    def isScramble(self, s1, s2):
        if len(s1) != len(s2):
            return False
        elif s1 == s2 or s1 == reversed(s2):
            return True
        elif sorted(list(s1)) != sorted(list(s2)):
            return False
        else:
            answer = False
            for len1 in range(1, len(s1)):
                if (self.isScramble(s1[:len1], s2[:len1]) and
                        self.isScramble(s1[len1:], s2[len1:])) or \
                        (self.isScramble(s1[:len1], s2[-len1:]) and
                         self.isScramble(s1[len1:], s2[:-len1])):
                    answer = True
                if answer:
                    break
            return answer


def main():
    solver = Solution()
    tests = [('great', 'rgtae'),
             ('abc', 'bca'),
             ("abcdefghijklmn", "efghijklmncadb"),
             ('a'*50+'b', 'a'*40+'b'+'a'*10)]
    for test in tests:
        print(test)
        print(' ->')
        result = solver.isScramble(*test)
        print(result)
        print('~'*10)
    pass


if __name__ == '__main__':
    main()
    pass
