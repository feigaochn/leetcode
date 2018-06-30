class Solution:
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        if len(start) != len(end):
            return False
        start = [(c, i) for i, c in enumerate(start) if c != 'X']
        end = [(c, i) for i, c in enumerate(end) if c != 'X']
        if len(start) != len(end):
            return False
        for (sc, si), (ec, ei) in zip(start, end):
            if sc != ec:
                return False
            elif sc == ec == 'L' and si < ei:
                return False
            elif sc == ec == 'R' and si > ei:
                return False
        return True


sol = Solution().canTransform

print(sol(start="RXXLRXRXL", end="XRLXXRRLX"))
print(sol(start="RXXLRXRXL", end="XRLXXRRLXX"))
print(sol("XXRXXLXXXX", "XXXXRXXLXX"))  # false
