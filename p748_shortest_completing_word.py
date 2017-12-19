class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        from collections import Counter
        import re
        plate = Counter(re.findall(r'[a-z]', licensePlate.lower()))
        best = None
        for word in words:
            wc = Counter(re.findall(r'[a-z]', word.lower()))
            for k in plate:
                if plate[k] > wc.get(k, 0):
                    break
            else:
                if best is None or len(best) > len(word):
                    best = word
        return best


fn = Solution().shortestCompletingWord

print(fn(licensePlate="1s3 PSt", words=["step", "steps", "stripe", "stepple"]))
print(fn(licensePlate="1s3 456", words=["looks", "pest", "stew", "show"]))
