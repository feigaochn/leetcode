# coding: utf-8

# author: Fei Gao
#
# Add And Search Word Data Structure Design

# Design a data structure that supports the following two operations:
# void addWord(word)
# bool search(word)
# search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.
# For example:
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
# Note:
# You may assume that all words are consist of lowercase letters a-z.
# click to show hint.
# You should be familiar with how a Trie works. If not, please work on this problem: Implement Trie (Prefix Tree) first.


class WordDictionary:
    def __init__(self):
        from collections import defaultdict

        self.words = defaultdict(set)

    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        self.words[len(word)].add(word)

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        import re

        for w in self.words[len(word)]:
            if re.findall(word, w):
                return True
        return False


def main():
    wordDictionary = WordDictionary()
    wordDictionary.addWord("word")
    print(wordDictionary.search("pattern"))


if __name__ == '__main__':
    main()
    pass
