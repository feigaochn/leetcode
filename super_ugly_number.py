# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: super ugly number
#
#     Write a program to find the nth super ugly number.
# 
#     Super ugly numbers are positive numbers whose all prime factors are in
# the given prime list
#     primes of size k. For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28,
# 32]
#  is the sequence of the first 12 super ugly numbers given primes
#     = [2, 7, 13, 19] of size 4.
# 
# Note:
#     (1) 1 is a super ugly number for any given primes.
#     (2) The given numbers in primes are in ascending order.
#     (3) 0 k ≤ 100, 0 n ≤ 106, 0 primes[i]
# 
# Credits:Special thanks to @dietpepsi for adding this problem and creating
# all test cases.
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Math
# Heap
# 
# Show Similar Problems
# 
#  (M) Ugly Number II


class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        import heapq
        heap = [1]
        heapq.heapify(heap)
        last = 0
        idx = 1
        while idx < n:
            while True:
                top = heapq.heappop(heap)
                if top != last:
                    last = top
                    break

            for p in primes:
                v = p * top
                heapq.heappush(heap, v)
            idx += 1
            heap[n - idx + 3:] = []
        # print(queue)
        # TODO: TLE
        return heap[0]


def main():
    solver = Solution()
    tests = [
        ((12, [2, 7, 13, 19]), 32),
        ((750,
          [2, 3, 7, 17, 19, 29, 31, 37, 41, 47, 53, 59, 61, 67, 71, 79, 83, 101, 109, 131, 139, 151, 163, 173, 179, 197,
           199, 229, 233, 263]), None),
        ((100000,
          [7, 19, 29, 37, 41, 47, 53, 59, 61, 79, 83, 89, 101, 103, 109, 127, 131, 137, 139, 157, 167, 179, 181, 199,
           211, 229, 233, 239, 241, 251]), None)
    ]
    import time
    t1 = time.clock()
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.nthSuperUglyNumber(*params)
        print('Result: ' + str(result))

    print('Time: ', time.clock() - t1)
    pass


if __name__ == '__main__':
    main()
    pass
