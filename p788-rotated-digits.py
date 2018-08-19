"""
X is a good number if after rotating each digit individually by 180 degrees, we
get a valid number that is different from X.  Each digit must be rotated - we
cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. 0, 1, and 8
rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each
other, and the rest of the numbers do not rotate to any other number and become
invalid.

Now given a positive number N, how many numbers X from 1 to N are good?

Example:
Input: 10
Output: 4
Explanation:
There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after
rotating.

Note:
    N  will be in range [1, 10000].
"""


class Solution:

    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """

        def rotate(x):
            if x in "018":
                return x
            elif x == "2":
                return "5"
            elif x == "5":
                return "2"
            elif x == "6":
                return "9"
            elif x == "9":
                return "6"
            else:
                return "z"

        r = 0
        for n in range(1, N + 1):
            ns = str(n)
            ms = "".join(map(rotate, ns))
            if ms != ns and "z" not in ms:
                r += 1
        return r


sol = Solution().rotatedDigits
print(sol(10))
print(sol(10000))
