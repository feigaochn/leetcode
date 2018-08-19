"""
Given a list of words, we may encode it by writing a reference string S and a
list of indexes A.

For example, if the list of words is ["time", "me", "bell"], we can write it as
S = "time#bell#" and indexes = [0, 2, 5].

Then for each index, we will recover the word by reading from the reference
string from that index until we reach a "#" character.

What is the length of the shortest reference string S possible that encodes the
given words?

Example:

Input: words = ["time", "me", "bell"]
Output: 10
Explanation: S = "time#bell#" and indexes = [0, 2, 5].

Note:

    1 <= words.length <= 2000.
    1 <= words[i].length <= 7.
    Each word has only lowercase letters.
"""


class Solution:

    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words.sort(key=len, reverse=True)
        unseen = set(words)
        ref = set()
        for w in words:
            if w not in unseen:
                continue
            unseen.remove(w)
            ref.add(w)
            for i in range(len(w)):
                if w[i:] in unseen:
                    unseen.remove(w[i:])
        result = 0
        for w in ref:
            result += len(w) + 1
        return result


from random import choices, randint, seed
from string import ascii_lowercase

seed(42)

sol = Solution().minimumLengthEncoding
tests = [
    ((["time", "me", "bell"],), 10),
    (
        (["".join(choices(ascii_lowercase, k=randint(1, 7))) for _ in range(2000)],),
        None,
    ),
]
for inputs, expect in tests:
    print(sol(*inputs), " ?= ", expect)
