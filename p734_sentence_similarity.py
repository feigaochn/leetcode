class Solution:
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        from itertools import zip_longest
        return all(w1 == w2 or [w1, w2] in pairs or [w2, w1] in pairs
                   for w1, w2 in zip_longest(words1, words2))


def test_p734():
    sol = Solution().areSentencesSimilar
    assert sol(["a"], ["a"], []) == True
    assert sol(["a"], ["b"], [["b", "a"]]) == True
    assert sol(["a"], ["a", "b"], []) == False
    assert sol(["a", "b"], ["a", "c"], []) == False


test_p734()
