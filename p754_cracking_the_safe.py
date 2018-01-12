#!/usr/bin/env python
# coding: utf-8


class Solution:
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if k == 1:
            return '0' * n
        # https://en.wikipedia.org/wiki/De_Bruijn_sequence
        alphabet = list(map(str, range(k)))

        a = [0] * (k * n * 2)
        sequence = []

        def db(t, p):
            if t > n:
                if n % p == 0:
                    sequence.extend(a[1:p + 1])
            else:
                a[t] = a[t - p]
                db(t + 1, p)
                for j in range(a[t - p] + 1, k):
                    a[t] = j
                    db(t + 1, t)

        db(1, 1)
        seq = ''.join(alphabet[i] for i in sequence)
        seq += seq[:n - 1]
        return seq


if __name__ == '__main__':
    sol = Solution().crackSafe
    print(sol(1, 1))
    print(sol(3, 1))
    print(sol(2, 2))
    print(sol(4, 10))
