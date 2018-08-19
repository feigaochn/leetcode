"""
Special binary strings are binary strings with the following two properties:

The number of 0's is equal to the number of 1's.
Every prefix of the binary string has at least as many 1's as 0's.

Given a special string S, a move consists of choosing two consecutive,
non-empty, special substrings of S, and swapping them. (Two strings are
consecutive if the last character of the first string is exactly one index
before the first character of the second string.)

At the end of any number of moves, what is the lexicographically largest
resulting string possible?

Example 1:

Input: S = "11011000"
Output: "11100100"
Explanation:
The strings "10" [occuring at S[1]] and "1100" [at S[3]] are swapped.  This is
the lexicographically largest string possible after some number of swaps.

Note:
    S has length at most 50.
    S is guaranteed to be a special binary string as defined above.
"""


class Solution:

    def makeLargestSpecial(self, S):
        """
        :type S: str
        :rtype: str
        """
        from itertools import accumulate
        from functools import reduce
        from operator import add

        def sep(xs):
            result = []
            st = 0
            for i, s in enumerate(accumulate(xs)):
                if s == 0:
                    result.append(xs[st : (i + 1)])
                    st = i + 1
            return result

        def work(xs):
            xss = sep(xs)
            for x in xss:
                x[1:-1] = work(x[1:-1])
            xs = reduce(add, sorted(xss), list())
            return xs

        def from_str(s):
            return [-1 if x == "1" else 1 for x in s]

        def to_str(s):
            return "".join(["1" if x == -1 else "0" for x in s])

        return to_str(work(from_str(S)))


sol = Solution().makeLargestSpecial
tests = [(("11011000",), "11100100"), (("101100",), "110010")]
for inputs, expect in tests:
    print(sol(*inputs), " ?= ", expect)
