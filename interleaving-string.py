# author: Fei Gao
#
# Interleaving String
#
# Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.
# For example,
# Given:
# s1 = "aabcc",
# s2 = "dbbca",
# When s3 = "aadbbcbcac", return true.
# When s3 = "aadbbbaccc", return false.

import collections


class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        if not s1 or not s2:
            return s3 == s1 + s2
        if len(s1) + len(s2) != len(s3):
            return False
        l1 = len(s1) + 1
        l2 = len(s2) + 1
        dp = [[False for _ in range(l2)] for _ in range(l1)]
        for i in range(l1):
            dp[i][0] = (s1[:i] == s3[:i])
        for j in range(l2):
            dp[0][j] = (s2[:j] == s3[:j])
        for i in range(1, l1):
            for j in range(1, l2):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or \
                    (dp[i][j-1] and s2[j-1] == s3[i+j-1])
        return dp[l1-1][l2-1]


def main():
    solver = Solution()
    tests = [['aabcc', 'dbbca', 'aadbbcbcac'],
             ['aabcc', 'dbbca', 'aadbbbaccc'],
             ["abbbbbbcabbacaacccababaabcccabcacbcaabbbacccaaaaaababbbacbb",
              "ccaacabbacaccacababbbbabbcacccacccccaabaababacbbacabbbbabc",
              "cacbabbacbbbabcbaacbbaccacaacaacccabababbbababcccbabcabbac" + \
              "cabcccacccaabbcbcaccccaaaaabaaaaababbbbacbbabacbbacabbbbabc"]]
    for test in tests:
        print(test)
        print(' ->')
        result = solver.isInterleave(*test)
        print(result)
        print('~'*10)


if __name__ == '__main__':
    main()
    pass
