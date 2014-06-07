# author: Fei Gao
# date: Wed Jun  4 22:46:25 2014
#
# Climbing Stairs
#
# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        if n < 2:
            return 1
        a, b = 1, 1
        for i in range(2, n+1):
            a, b = b, a+b
        return b


def main():
    solver = Solution()
    for n in range(1, 10):
        print(n, solver.climbStairs(n))
    pass


if __name__ == '__main__':
    main()
    pass
