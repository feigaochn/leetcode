#!/bin/env python3

# author: Fei Gao
#
# Number Of Islands
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
# Example 1:
# 11110110101100000000
# Answer: 1
# Example 2:
# 11000110000010000011
# Answer: 3
# Credits:Special thanks to @mithmatt for adding this problem and creating all test cases.
# Show Tags


class Solution:
    def numIslands(self, grid):
        """
        @param grid: list of list of char
        @rtpye: int
        """
        num = 0
        if not grid:
            return num
        rows = len(grid)
        for r in range(rows):
            grid[r] = list(grid[r])
        cols = len(grid[0])
        def work(r, c):
            # print(r,c)
            # r = int(input('r'))
            queue = [(r,c)]
            idx = 0
            grid[r][c] = -1
            while idx < len(queue):
                r, c = queue[idx]
                # print('working', idx, r, c, grid[r][c])
                idx += 1
                if r + 1 < rows and grid[r+1][c] == '1':
                    queue.append((r+1, c))
                    grid[r+1][c] = -1
                if r - 1 >= 0 and grid[r-1][c] == '1':
                    queue.append((r-1, c))
                    grid[r-1][c] = -1
                if c + 1 < cols and grid[r][c+1] == '1':
                    queue.append((r, c+1))
                    grid[r][c+1] = -1
                if c - 1 >= 0 and grid[r][c-1] == '1':
                    queue.append((r, c-1))
                    grid[r][c-1] = -1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    work(r, c)
                    num = num + 1
        return num

def main():
    solver = Solution()
    tests = [
        ['11110', '11010', '11000', '00000'],
        ['11000', '11000', '00100', '00011'],
        ["11111011111111101011","01111111111110111110","10111001101111111111","11110111111111111111","10011111111111111111","10111111011101110111","01111111111101101111","11111111111101111011","11111111110111111111","11111111111111111111","01111111011111111111","11111111111111111111","11111111111111111111","11111011111110111111","10111110111011110111","11111111111101111110","11111111111110111100","11111111111111111111","11111111111111111111","11111111111111111111"]
    ]
    for test in tests:
        print(test)
        print(' ->')
        result = solver.numIslands(test)
        print(result)
        print('~'*10)
        pass

if __name__ == '__main__':
    main()
    pass
