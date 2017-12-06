#!/usr/bin/env python
# coding: utf-8

# p676

class MagicDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._words = dict()  # type: dict[int, list[str]]

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for word in dict:
            self._words[len(word)] = self._words.get(len(word), []) + [word, ]

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        for w in self._words.get(len(word), []):
            if MagicDictionary.__distance(w, word) == 1:
                return True
        else:
            return False

    @staticmethod
    def __distance(w1, w2):
        return sum(c1 != c2 for c1, c2 in zip(w1, w2))


if __name__ == '__main__':
    # Your MagicDictionary object will be instantiated and called as such:
    obj = MagicDictionary()
    obj.buildDict(["hello", "hallo", "leetcode"])
    print(obj._words)
    print(obj.search("hello"))
    print(obj.search("hhllo"))
    print(obj.search("hell"))
