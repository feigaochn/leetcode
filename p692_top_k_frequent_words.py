class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        from collections import Counter
        c = Counter(words)
        return [w[0] for w in sorted(c.items(), key=lambda p: (-p[1], p[0]))[:k]]


fn = Solution().topKFrequent

print(fn(["i", "love", "leetcode", "i", "love", "coding"], k=2))
print(
    fn(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"],
       k=4))
