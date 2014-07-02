#!/bin/env python3

# author: Fei Gao
#
# Valid Sudoku
#
# Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
# A partially filled sudoku which is valid.
# Note:
# A valid Sudoku board (partially filled) is not necessarily solvable.
# Only the filled cells need to be validated.


class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean

    def isValidSudoku(self, board):
        rows = [dict() for _ in range(9)]
        cols = [dict() for _ in range(9)]
        squares = [dict() for _ in range(9)]
        valid = True
        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == '.':
                    pass
                else:
                    val = int(val)
                    rows[row][val] = rows[row].get(val, 0) + 1
                    cols[col][val] = cols[col].get(val, 0) + 1
                    idx = (row // 3) * 3 + (col // 3)
                    squares[idx][val] = squares[idx].get(val, 0) + 1
        del val
        if not valid:
            return False
        for ind in range(9):
            if any([val > 1 for val in rows[ind].values()]):
                valid = False
            if any([val > 1 for val in cols[ind].values()]):
                valid = False
            if any([val > 1 for val in squares[ind].values()]):
                valid = False
        return valid


def main():
    solver = Solution()
    tests = [[list(range(1, 10))] + [['.']*9 for _ in range(8)],
             [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]]
    for test in tests:
        print(test)
        print(' ->')
        result = solver.isValidSudoku(test)
        print(result)
        print('~'*10)
    pass
if __name__ == '__main__':
    main()
    pass
