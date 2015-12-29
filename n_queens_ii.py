# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: n queens ii
#
# Follow up for N-Queens problem.
# Now, instead outputting board configurations, return the total
# number of distinct solutions.
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Backtracking
# 
# Show Similar Problems
# 
#  (H) N-Queens


class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.solutions = []
        self.n = n
        self.recursiveSolve([], [], [])
        return len(self.solutions)

    def recursiveSolve(self, partial, diag, anti_diag):
        idx = len(partial)
        if idx == self.n:
            self.solutions.append(partial[:])
            return
        for val in range(self.n):
            if val not in partial \
                    and val - idx not in diag \
                    and val + idx not in anti_diag:
                partial.append(val)
                diag.append(val - idx)
                anti_diag.append(val + idx)
                self.recursiveSolve(partial, diag, anti_diag)
                partial.pop()
                diag.pop()
                anti_diag.pop()


def main():
    solver = Solution()
    tests = [
        ((8,), 92),
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.totalNQueens(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
