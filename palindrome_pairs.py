# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: palindrome pairs
#
#     Given a list of unique words. Find all pairs of distinct indices (i, j)
# in the given list, so that the concatenation of the two words, i.e. words[i]
# + words[j] is a palindrome.
# 
# Example 1:
#     Given words = ["bat", "tab", "cat"]
#     Return [[0, 1], [1, 0]]
#     The palindromes are ["battab", "tabbat"]
# 
# Example 2:
#     Given words = ["abcd", "dcba", "lls", "s", "sssll"]
#     Return [[0, 1], [1, 0], [3, 2], [2, 4]]
#     The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]
# 
# Credits:Special thanks to @dietpepsi for adding this problem and creating
# all test cases.
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Hash Table
# String
# Trie
# 
# Show Similar Problems
# 
#  (M) Longest Palindromic Substring
#  (H) Shortest Palindrome


class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        # TODO
        from collections import defaultdict
        p_lr = defaultdict(set)
        p_rl = defaultdict(set)
        for iw, w in enumerate(words):
            for i in range(1, len(w) + 1):
                p_lr[w[:i]].add(iw)
                p_rl[w[-i::-1]].add(iw)
        print(p_lr, p_rl)
        results = []
        for iw, w in enumerate(words):
            for j in p_rl[w]:
                if j == iw:
                    continue
                nw = w + words[j][::-1]
                if nw == nw[::-1]:
                    results.append([iw, j])
            for j in p_lr[w[::-1]]:
                if j == iw:
                    continue
                nw = words[j] + w[::-1]
                if nw == nw[::-1]:
                    results.append([j, iw])
        return results


def main():
    solver = Solution()
    tests = [
        ((["bat", "tab", "cat"],), [[0, 1], [1, 0]]),
        ((["abcd", "dcba", "lls", "s", "sssll"],), [[0, 1], [1, 0], [3, 2], [2, 4]]),
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.palindromePairs(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
