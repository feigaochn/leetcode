# author: Fei Gao
#
# Longest Common Prefix
#
# Write a function to find the longest common prefix string amongst an array of strings.


class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if strs is None or len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        # assert isinstance(strs, list)
        strs.sort(key=len)
        if len(strs[0]) == 0:
            return ""
        n = 0
        for n in range(len(strs[0])):
            if len(set(s[n] for s in strs)) != 1:
                n -= 1
                break
        return strs[0][:n + 1]
        pass


def main():
    solver = Solution()
    ls = ['a' * 5, 'ab' * 2]
    print(solver.longestCommonPrefix(ls))
    pass


if __name__ == '__main__':
    main()
    pass
