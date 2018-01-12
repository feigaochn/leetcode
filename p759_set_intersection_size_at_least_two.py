class Solution:
    def intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda p: (p[1], p[0]))
        cover = [intervals[0][1] - 1]
        cover.append(cover[-1] + 1)
        for a, b in intervals[1:]:
            if a <= cover[-2] and cover[-1] <= b:
                pass
            elif cover[-1] < a:
                cover.append(b - 1)
                cover.append(b)
            elif cover[-2] < a <= cover[-1] <= b:
                if cover[-1] == b:
                    cover[-1] = b - 1
                cover.append(b)
        # print(cover)
        return len(cover)


sol = Solution().intersectionSizeTwo

print(sol([[1, 3], [1, 4], [2, 5], [3, 5]]))
print(sol([[1, 2], [2, 3], [2, 4], [4, 5]]))
print(sol([[1, 10]]))
print(
    sol([[2, 10], [3, 7], [3, 15], [4, 11], [6, 12], [6, 16], [7, 8], [7, 11],
         [7, 15], [11, 12]]))  # 5
