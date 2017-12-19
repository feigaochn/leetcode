class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        import bisect

        return letters[bisect.bisect_right(letters, target) % len(letters)]


fn = Solution().nextGreatestLetter

for data in [["cfj", "a"],
    ["cfj", "c"],
    ["cfj", "d"],
    ["cfj", "g"],
    ["cfj", "j"],
    ]:
    print(data, fn(*data))
