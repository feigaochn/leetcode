class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        positions = dict()
        for i, c in enumerate(S):
            if c not in positions:
                positions[c] = []
            positions[c].append(i)

        result = []
        end = -1
        while True:
            st = end + 1
            if st >= len(S):
                break
            end = positions[S[st]][-1]
            while True:
                extend = max(positions[c][-1] for c in S[st:end + 1])
                if extend > end:
                    end = extend
                else:
                    break
            result.append(end - st + 1)
        return result


sol = Solution().partitionLabels
print(sol("ababcbacadefegdehijhklij"))
