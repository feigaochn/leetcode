class WordFilter:
    def __init__(self, words):
        """
        :type words: List[str]
        """
        from collections import defaultdict
        self.prefix = defaultdict(list)
        self.suffix = defaultdict(list)
        for wi, word in enumerate(words):
            for i in range(len(word) + 1):
                self.prefix[word[0:i]].append(wi)
                self.suffix[word[i:len(word)]].append(wi)

    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        i, j = len(self.prefix[prefix]) - 1, len(self.suffix[suffix]) - 1
        while i >= 0 and j >= 0:
            if self.prefix[prefix][i] == self.suffix[suffix][j]:
                return self.prefix[prefix][i]
            elif self.prefix[prefix][i] < self.suffix[suffix][j]:
                j -= 1
            elif self.prefix[prefix][i] > self.suffix[suffix][j]:
                i -= 1
        else:
            return -1

# # Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(["apple"])
# print(obj.f("a", "e"))
# print(obj.f("b", "e"))


obj = WordFilter([
    "cabaabaaaa", "ccbcababac", "bacaabccba", "bcbbcbacaa", "abcaccbcaa",
    "accabaccaa", "cabcbbbcca", "ababccabcb", "caccbbcbab", "bccbacbcba"
])
for p, s in [
    ["bccbacbcba", "a"],
    ["ab", "abcaccbcaa"],
    ["a", "aa"],
    ["cabaaba", "abaaaa"],
    ["cacc", "accbbcbab"],
    ["ccbcab", "bac"],
    ["bac", "cba"],
    ["ac", "accabaccaa"],
    ["bcbb", "aa"],
    ["ccbca", "cbcababac"],
]:
    print(obj.f(p, s))
