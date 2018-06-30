class Solution:
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        pos2ppl = dict()
        ppl2pos = dict()
        for s, p in enumerate(row):
            pos2ppl[s] = p
            ppl2pos[p] = s
        swaps = 0
        for i in range(0, len(row), 2):
            # i -> cur_p
            # i + 1 -> neighbor_p
            # next_pos -> next_p
            cur_p = pos2ppl[i]
            neighbor_p = pos2ppl[i + 1]
            next_p = cur_p + 1 if cur_p % 2 == 0 else cur_p - 1
            if next_p == neighbor_p:
                continue

            swaps += 1
            next_pos = ppl2pos[next_p]
            pos2ppl[i + 1], pos2ppl[next_pos] = next_p, neighbor_p
            ppl2pos[neighbor_p], ppl2pos[next_p] = next_pos, i + 1
        return swaps


sol = Solution().minSwapsCouples
print(sol([0, 2, 1, 3]))
print(sol([3, 2, 0, 1]))
print(sol([0, 2, 4, 6, 7, 1, 3, 5]))
print(sol([0, 1, 4, 6, 7, 2, 3, 5]))

print(sol([0, 1, 4, 5, 7, 2, 3, 6]))
print(sol([0, 1, 7, 6, 4, 2, 3, 5]))

print(sol([0, 1, 7, 6, 4, 5, 3, 2]))
