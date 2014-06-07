# author: Fei Gao
#
# Longest Substring Without Repeating Characters
#
# Given a string, find the length of the longest substring without repeating
# characters. For example, the longest substring without repeating letters for
# "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring
# is "b", with the length of 1.

import collections


class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        dp = [0]

        def f():
            return -1

        od = collections.defaultdict(f)
        for i, c in enumerate(s):
            dp.append(min(dp[-1]+1, i - od[c]))
            od[c] = i
        return max(dp[1:])


def main():
    solver = Solution()
    for test in [None, 'abcabcbb', 'bbb', '', 'wlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsjybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmco']:
        print(test, '\n', solver.lengthOfLongestSubstring(test))
    pass


if __name__ == '__main__':
    main()
    pass
