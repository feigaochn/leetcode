# author: Fei Gao
#
# Anagrams
#
# Given an array of strings, return all groups of strings that are anagrams.
# Note: All inputs will be in lower-case.

import collections
import itertools


class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        dic = collections.defaultdict(list)
        for s in strs:
            dic[''.join(sorted(s))].append(s)
        return list(itertools.chain(*[s for s in dic.values() if len(s) > 1]))


def main():
    solver = Solution()
    tests = [['aba', 'bab'], ['abc', 'cba'], ['aab', 'aba', 'bab', 'bba']]
    for test in tests:
        result = solver.anagrams(test)
        print(test, ' ->\n', result)
    pass


if __name__ == '__main__':
    main()
    pass
