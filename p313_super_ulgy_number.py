class Solution:
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        import heapq
        ugly = [(1, 0)]
        for _ in range(n - 1):
            top = heapq.heappop(ugly)
            while ugly and ugly[0][0] == top[0]:
                heapq.heappop(ugly)
            for i, p in enumerate(primes[top[1]:], top[1]):
                heapq.heappush(ugly, (p * top[0], i))
        return ugly[0][0]


fn = Solution().nthSuperUglyNumber
print(fn(12, [2, 7, 13, 19]))

print(
    fn(100000, [
        7, 19, 29, 37, 41, 47, 53, 59, 61, 79, 83, 89, 101, 103, 109, 127, 131,
        137, 139, 157, 167, 179, 181, 199, 211, 229, 233, 239, 241, 251
    ]))  # 1092889481
