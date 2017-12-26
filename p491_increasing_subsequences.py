class Solution:
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from itertools import groupby
        subseqs = [[]]
        for v in nums:
            end = len(subseqs)
            for seq_i in range(end):
                seq = subseqs[seq_i]
                if not seq:
                    subseqs.append([v])
                elif seq[-1] <= v:
                    subseqs.append(seq + [v])
        return [gp[0] for gp in groupby(
                    sorted([seq for seq in subseqs if len(seq) >= 2]))]


fn = Solution().findSubsequences

print(fn([4, 6, 7, 7]))
