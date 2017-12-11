class Solution:
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        english = [
            'zero',  # z
            'one',  # o
            'two',  # w
            'three',  # r
            'four',  # u
            'five',  # f
            'six',  # x
            'seven',  # s
            'eight',
            'nine'
        ]
        from collections import Counter
        answer = [0 for _ in range(10)]
        raw = Counter(s)

        trick = [
            (6, 'x'),
            (2, 'w'),
            (0, 'z'),
            (4, 'u'),
            (1, 'o'),
            (5, 'f'),
            (7, 's'),
            (3, 'r'),
            (8, 't'),
            (9, 'i'),
        ]

        for digit, hint in trick:
            answer[digit] = raw[hint]
            for c in english[digit]:
                raw[c] -= answer[digit]

        return ''.join(str(d) * c for d, c in enumerate(answer))


fn = Solution().originalDigits
print(fn('owoztneoer'))
print(fn('fviefuro'))
