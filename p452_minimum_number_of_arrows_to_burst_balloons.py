class Solution:
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        arrows = 0
        heads = sorted(points)
        tails = sorted(points, key=lambda p: (p[1], p[0]))
        # print(heads)
        # print(tails)
        last_shot = None
        while heads:
            s, e = heads.pop()
            if last_shot is not None and e >= last_shot:
                continue
            shoot = False
            while tails:
                if tails[-1][1] >= s:
                    tails.pop()
                    shoot = True
                else:
                    break
            if shoot:
                arrows += 1
                last_shot = s
        return arrows


fn = Solution().findMinArrowShots

print(fn([[10, 16], [2, 8], [1, 6], [7, 12]]))
