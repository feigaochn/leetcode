#!/bin/env python3

# author: Fei Gao
#
# Sqrtx
#
# Implement int sqrt(int x).
# Compute and return the square root of x.


class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        x = float(x)
        eps = 0.000000001
        old = 1.0
        new = 1.0
        while True:
            old, new = new, (new + x/new) / 2.0
            # print(old, new)
            if abs(new-old) < eps:
                break
        return int(new)


def main():
    solver = Solution()
    tests = [0, 1, 2, 3, 4, 5]
    for test in tests:
        print(test)
        print(' ->')
        result = solver.sqrt(test)
        print(result)
        print('~'*10)
    pass
if __name__ == '__main__':
    main()
    pass
