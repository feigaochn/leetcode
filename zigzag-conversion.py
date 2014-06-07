# author: Fei Gao
#
# Zigzag Conversion
#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
# string convert(string text, int nRows);
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".


class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows == 1:
            return s
        cycle = nRows * 2 - 2
        rows = ['' for _ in range(nRows)]
        for i, c in enumerate(s):
            m = i % cycle
            if m < nRows - 1:
                rows[m] += c
            else:
                rows[cycle - m] += c
        return ''.join(rows)


def main():
    solver = Solution()
    tests = [('PAYPALISHIRING', 3), ('', 10), ('abcabc', 1)]
    for test in tests:
        result = solver.convert(*test)
        print(test)
        print(' ->')
        print(result)
        print('~'*10)
    pass


if __name__ == '__main__':
    main()
    pass
