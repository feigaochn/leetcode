class Solution:

    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        from string import ascii_lowercase

        morse = dict(
            zip(
                ascii_lowercase,
                [
                    ".-",
                    "-...",
                    "-.-.",
                    "-..",
                    ".",
                    "..-.",
                    "--.",
                    "....",
                    "..",
                    ".---",
                    "-.-",
                    ".-..",
                    "--",
                    "-.",
                    "---",
                    ".--.",
                    "--.-",
                    ".-.",
                    "...",
                    "-",
                    "..-",
                    "...-",
                    ".--",
                    "-..-",
                    "-.--",
                    "--..",
                ],
            )
        )
        trans = set(["".join(morse[c] for c in w) for w in words])
        return len(trans)


sol = Solution().uniqueMorseRepresentations
print(sol(["gin", "zen", "gig", "msg"]))
