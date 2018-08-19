# We are to write the letters of a given string S, from left to right into
# lines. Each line has maximum width 100 units, and if writing a letter would
# cause the width of the line to exceed 100 units, it is written on the next
# line. We are given an array widths, an array where widths[0] is the width of
# 'a', widths[1] is the width of 'b', ..., and widths[25] is the width of 'z'.

# Now answer two questions: how many lines have at least one character from S,
# and what is the width used by the last such line? Return your answer as an
# integer list of length 2.


class Solution:

    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        if not S:
            return [0, 0]
        lines = [0]
        for c in S:
            w = widths[ord(c) - ord("a")]
            if lines[-1] + w > 100:
                lines.append(w)
            else:
                lines[-1] += w
        return [len(lines), lines[-1]]


sol = Solution().numberOfLines
print(
    sol(
        widths=[
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
        ],
        S="abcdefghijklmnopqrstuvwxyz",
    )
)  # [3, 60]
print(
    sol(
        widths=[
            4,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
        ],
        S="bbbcccdddaaa",
    )
)  # [2, 4]
