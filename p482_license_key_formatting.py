class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.replace('-', '').upper()
        S = S.rjust(((len(S) - 1) // K + 1) * K)
        # print(S)
        return '-'.join(
            S[i * K:(i + 1) * K] for i in range(len(S) // K)).strip()


fn = Solution().licenseKeyFormatting

print(fn("5F3Z-2e-9-w", K=4))
print(fn("2-5g-3-J", K=2))
