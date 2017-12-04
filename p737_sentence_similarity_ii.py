#!/usr/bin/env python
# coding: utf-8

"""
Given two sentences words1, words2 (each represented as an array of strings), and a list of similar word pairs pairs, determine if two sentences are similar.

For example, words1 = ["great", "acting", "skills"] and words2 = ["fine", "drama", "talent"] are similar, if the similar word pairs are pairs = [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]].

Note that the similarity relation is transitive. For example, if "great" and "good" are similar, and "fine" and "good" are similar, then "great" and "fine" are similar.

Similarity is also symmetric. For example, "great" and "fine" being similar is the same as "fine" and "great" being similar.

Also, a word is always similar with itself. For example, the sentences words1 = ["great"], words2 = ["great"], pairs = [] are similar, even though there are no specified similar word pairs.

Finally, sentences can only be similar if they have the same number of words. So a sentence like words1 = ["great"] can never be similar to words2 = ["doubleplus","good"].

Note:

The length of words1 and words2 will not exceed 1000.
The length of pairs will not exceed 2000.
The length of each pairs[i] will be 2.
The length of each words[i] and pairs[i][j] will be in the range [1, 20].
"""


class Solution(object):
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        all_words = list(set(words1) | set(words2) | set([w for p in pairs for w in p])) + [None]

        parent = dict(zip(all_words, all_words))

        def grand_parent(w):
            if parent[w] == w:
                return w
            else:
                gp = grand_parent(parent[w])
                parent[w] = gp
                return gp

        # print(parent)
        for w1, w2 in pairs:
            gpw1 = grand_parent(w1)
            gpw2 = grand_parent(w2)
            if gpw1 < gpw2:
                parent[gpw2] = gpw1
            else:
                parent[gpw1] = gpw2

        from itertools import zip_longest
        return all(grand_parent(w1) == grand_parent(w2)
                   for w1, w2 in zip_longest(words1, words2))


if __name__ == '__main__':
    sol = Solution().areSentencesSimilarTwo
    print(sol(
        words1=["great", "acting", "skills"],
        words2=["fine", "drama", "talent"],
        pairs=[["great", "good"], ["fine", "good"], ["acting", "drama"], ["skills", "talent"]]))
    print(sol(
        words1=["great", "acting", "skills", "talent"],
        words2=["fine", "drama", "talent"],
        pairs=[["great", "good"], ["fine", "good"], ["acting", "drama"], ["skills", "talent"]]))

    print(sol(["an", "extraordinary", "meal"],
              ["one", "good", "dinner"],
              [["great", "good"], ["extraordinary", "good"], ["well", "good"], ["wonderful", "good"],
               ["excellent", "good"], ["fine", "good"], ["nice", "good"], ["any", "one"], ["some", "one"],
               ["unique", "one"], ["the", "one"], ["an", "one"], ["single", "one"], ["a", "one"], ["truck", "car"],
               ["wagon", "car"], ["automobile", "car"], ["auto", "car"], ["vehicle", "car"], ["entertain", "have"],
               ["drink", "have"], ["eat", "have"], ["take", "have"], ["fruits", "meal"], ["brunch", "meal"],
               ["breakfast", "meal"], ["food", "meal"], ["dinner", "meal"], ["super", "meal"], ["lunch", "meal"],
               ["possess", "own"], ["keep", "own"], ["have", "own"], ["extremely", "very"], ["actually", "very"],
               ["really", "very"], ["super", "very"]]), '?= True')
