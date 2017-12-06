# author: Fei Gao
#
# Anagrams
#
# Given an array of strings, return all groups of strings that are anagrams.
# Note: All inputs will be in lower-case.

import collections


class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = collections.defaultdict(list)
        for s in strs:
            dic[''.join(sorted(s))].append(s)
        return list(dic.values())


def main():
    solver = Solution()
    tests = [['aba', 'bab'], ['abc', 'cba'], ['aab', 'aba', 'bab', 'bba'],
        ["eat","tea","tan","ate","nat","bat"]]
    for test in tests:
        result = solver.groupAnagrams(test)
        print(test, ' ->\n', result)
    pass


if __name__ == '__main__':
    main()
    pass
