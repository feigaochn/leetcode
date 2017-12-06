# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: game of life
#
# According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
# 
# Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):
# 
# Any live cell with fewer than two live neighbors dies, as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population..
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# 
# Write a function to compute the next state (after one update) of the board given its current state.
# 
# Follow up: 
# 
# Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
# In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?
# 
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Array
# 
# Show Similar Problems
# 
#  (M) Set Matrix Zeroes


class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        import itertools
        if not board or not board[0]:
            return
        rows = len(board)
        cols = len(board[0])

        def neighbors(r, c):
            nr, nc = [r], [c]
            if r > 0: nr.append(r-1)
            if r < rows - 1: nr.append(r+1)
            if c > 0: nc.append(c-1)
            if c < cols - 1: nc.append(c+1)
            return list(itertools.product(nr, nc))[1:]

        def live(nb, se):
            if se % 100 == 1:
                if 2 <= nb % 100 <= 3:
                    return 1
                else:
                    return 0
            elif se % 100 == 0:
                if nb % 100 == 3:
                    return 1
                else:
                    return 0

        for r, c in itertools.product(range(rows), range(cols)):
            board[r][c] += 100 * live((sum(board[x][y] for x, y in neighbors(r, c))) % 100, board[r][c])

        for r, c in itertools.product(range(rows), range(cols)):
            board[r][c] //= 100


def main():
    solver = Solution()
    tests = [
        (([[1, 1, 1, 1, 1, 1],
           [0, 0, 1, 0, 0, 1]],), 'result'),
        (([[1, 1], [1, 0]],), None)
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        solver.gameOfLife(*params)
        print('Result: ' + str(params))
    pass


if __name__ == '__main__':
    main()
    pass
