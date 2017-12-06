# Surrounded Regions
# Total Accepted: 7716 Total Submissions: 56446 My Submissions
#
# Given a 2D board containing 'X' and 'O', capture all regions surrounded by
# 'X'. A region is captured by flipping all 'O's into 'X's in that surrounded
# region.
#
# For example,
# X X X X
# X O O X
# X X O X
# X O X X
#
# After running your function, the board should be:
# X X X X
# X X X X
# X X X X
# X O X X


class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.

    def solve(self, board):
        if len(board) is 0:
            return
        q = []
        # first row
        for j in range(len(board[0])):
            if board[0][j] is 'O':
                q.append((0, j))
                board[0][j] = 'o'
        # last row
        for j in range(len(board[-1])):
            if board[len(board)-1][j] is 'O':
                q.append((len(board)-1, j))
                board[len(board)-1][j] = 'o'
        for i in range(len(board)):
            n = len(board[i])
            if n > 0:
                # first column
                if board[i][0] is 'O':
                    board[i][0] = 'o'
                    q.append((i, 0))
                # last column
                if board[i][n-1] is 'O':
                    board[i][n-1] = 'o'
                    q.append((i, n-1))
        while len(q) > 0:
            i, j = q.pop(0)
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= i+di < len(board) and 0 <= j+dj < len(board[i+di]) \
                        and board[i+di][j+dj] is 'O':
                    board[i+di][j+dj] = 'o'
                    q.append((i+di, j+dj))
        for row in board:
            for j in range(len(row)):
                if row[j] is 'o':
                    row[j] = 'O'
                elif row[j] is 'O':
                    row[j] = 'X'


if __name__ == '__main__':
    board = [['X', 'X', 'X', 'X'],
             ['X', 'O', 'O', 'X'],
             ['X', 'X', 'O', 'X'],
             ['X', 'O', 'X', 'X']]
    Solution().solve(board)
    print(board)
    board = []
    Solution().solve(board)
    print(board)
