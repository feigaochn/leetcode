class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words = sorted(words, key=lambda w: (-len(w), w))
        ws = set(words)
        for w in words:
            if all(w[:i + 1] in ws for i in range(len(w))):
                return w
        return ""


def main():
    sol = Solution().longestWord
    print(sol(["w", "wo", "wor", "worl", "world"]), '-> "world"')
    print(
        sol(["a", "banana", "app", "appl", "ap", "apply", "apple"]),
        '-> "apple"')
    print(sol(["ab"]))


if __name__ == '__main__':
    main()
