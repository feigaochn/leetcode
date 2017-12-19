class Solution:
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        cache = [[-1 for _ in (s)] for _ in (s)]

        def find2(lb, rb):
            if cache[lb][rb] != -1:
                return cache[lb][rb]
            elif rb == lb:
                cache[lb][rb] = 1
                return 1
            elif lb > rb:
                cache[lb][rb] = 0
                return 0
            elif s[lb] == s[rb]:
                result = 2 + find2(lb + 1, rb - 1)
                cache[lb][rb] = result
                return result
            else:
                result = max(find2(lb + 1, rb), find2(lb, rb - 1))
                cache[lb][rb] = result
                return result

        return find2(0, len(s) - 1)


fn = Solution().longestPalindromeSubseq
from random import choice
print(fn("bbbab"))
print(fn("cbbd"))
print(fn(''.join(choice("ab") for _ in range(1000))))

print(
    fn("fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffgggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg"
       ))
