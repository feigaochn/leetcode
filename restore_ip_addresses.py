# author: Fei Gao
#
# Restore Ip Addresses
#
# Given a string containing only digits, restore it by returning all possible valid IP address combinations.
# For example:
# Given "25525511135",
# return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)

import itertools


class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        one = [str(i) for i in range(256)]
        result = []

        def rec(s, n, p):
            s = str(s)
            if n == 0:
                if s == '':
                    result.append('.'.join(p))
                return
            else:
                for st in one:
                    if s.startswith(st):
                        rec(s[len(st):], n-1, p+[st])
                return

        rec(s, 4, [])
        return result


def main():
    solver = Solution()
    tests = ["25525511135"]
    for test in tests:
        result = solver.restoreIpAddresses(test)
        print(test, ' ->\n', result)
    pass


if __name__ == '__main__':
    main()
    pass
