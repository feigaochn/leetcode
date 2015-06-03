class Solution:
    # @param str, a string
    # @return an integer
    def myAtoi(self, s):
        import re
        try:
            f = re.findall(r'^[+-]?\d+', s.strip())
            if not f:
                return 0
            f = int(f[0])
            if f > 2147483647: return 2147483647
            elif f < -2147483648: return -2147483648
            else: return f
        except:
            return 0