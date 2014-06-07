# author: Fei Gao
#
# Regular Expression Matching
#
# Implement regular expression matching with support for '.' and '*'.
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).
# The function prototype should be:
# bool isMatch(const char *s, const char *p)
# Some examples:
# isMatch("aa","a") -> false
# isMatch("aa","aa") -> true
# isMatch("aaa","aa") -> false
# isMatch("aa", "a*") -> true
# isMatch("aa", ".*") -> true
# isMatch("ab", ".*") -> true
# isMatch("aab", "c*a*b") -> true


class Solution:
    # @return a boolean

    def isMatch(self, s, p):
        # hack the TLE case: ("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c") -> False
        p = str(p)
        alphas = set(list(p)) - {'*'}
        for k in alphas:
            pt = k + '*' + k + '*'
            while p.find(pt) != -1:
                p = p.replace(pt, k + '*')
        # print('p: ', p)

        def ismatch(s, p):
            if p[0] == '\0':
                return s[0] == '\0'
            if p[1] != '*':
                return ((p[0] == s[0]) or
                        (p[0] == '.' and s[0] != '\0')) \
                       and ismatch(s[1:], p[1:])

            while p[0] == s[0] or (p[0] == '.' and s[0] != '\0'):
                if ismatch(s, p[2:]):
                    return True
                s = s[1:]

            return ismatch(s, p[2:])

        return ismatch(s + '\0', p + '\0')


def main():
    solver = Solution()
    tests = [
        ("aa", "a"),
        ("aa", "aa"),
        ("aaa", "aa"),
        ("aa", "a*"),
        ("aa", ".*"),
        ("ab", ".*"),
        ("aab", "c*a*b"),
        ("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c")]
    for test in tests:
        print(test)
        print(' ->')
        result = solver.isMatch(*test)
        print(result)
        print('~' * 10)
    pass


if __name__ == '__main__':
    main()
    pass
