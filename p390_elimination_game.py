class Solution:
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """

        def left(n):
            if n == 1:
                return 1
            return 2 * right(n // 2)

        def right(n):
            if n == 1:
                return 1
            return left(n // 2) * 2 - 1 + (n % 2)

        return left(n)


fn = Solution().lastRemaining

print(fn(999))
