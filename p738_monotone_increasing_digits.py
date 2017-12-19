class Solution:
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """

        def is_mono(num, ub=9):
            if num <= ub:
                return True
            elif num % 10 > ub:
                return False
            else:
                return is_mono(num // 10, num % 10)

        if is_mono(N):
            return N
        else:
            return self.monotoneIncreasingDigits(N // 10 - 1) * 10 + 9


fn = Solution().monotoneIncreasingDigits

for N in [10, 1234, 332, 321, 10**8]:
    print(N, '->', fn(N))
