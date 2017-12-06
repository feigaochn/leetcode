# author: Fei Gao
#
# Decode Ways
#
# A message containing letters from A-Z is being encoded to numbers using the following mapping:
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given an encoded message containing digits, determine the total number of ways to decode it.
# For example,
# Given encoded message "12",
# it could be decoded as "AB" (1 2) or "L" (12).
# The number of ways decoding "12" is 2.


class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        if s is None or s == '':
            return 0
        seen = {'': 1, '0': 0}

        def dp(s):
            if s in seen:
                return seen[s]
            if s[:1] == '0':
                return 0
            result = dp(s[1:])
            if len(s) > 1 and 10 <= int(s[:2]) <= 26:
                result += dp(s[2:])
            seen[s] = result
            return result

        return dp(s)
        pass


def main():
    solver = Solution()

    # for i in range(100):
    #     num = str(i)
    #     print(num, ": ", solver.numDecodings(num))

    num = '12' * 10
    print(num, ": ", solver.numDecodings(num))

    pass


if __name__ == '__main__':
    main()
    pass
