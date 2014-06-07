# author: Fei Gao
#
# Valid Parentheses
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.


class Solution:
    # @return a boolean
    def isValid(self, s):
        # None or empty string
        if not s:
            return True
        # odd length
        if len(s) % 2 == 1:
            return False
        match = {'(': ')', '[': ']', '{': '}'}
        filo = list()
        for c in s:
            if c in '([{':
                filo.append(c)
            else:
                if not filo or match[filo[-1]] != c:
                    return False
                else:
                    filo.pop()
        return not filo


def main():
    solver = Solution()
    for test in [None, "", "()", "()[]{}", "(]", "([)]"]:
        print(test, solver.isValid(test))
    pass


if __name__ == '__main__':
    main()
    pass
