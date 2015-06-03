# author: Fei Gao
#
# Integer To Roman
#
# Given an integer, convert it to a roman numeral.
# Input is guaranteed to be within the range from 1 to 3999.


class Solution:
    # @return a string

    def intToRoman(self, n):
        roman_numeral_map = (
            ('M', 1000),
            ('CM', 900),
            ('D', 500),
            ('CD', 400),
            ('C', 100),
            ('XC', 90),
            ('L', 50),
            ('XL', 40),
            ('X', 10),
            ('IX', 9),
            ('V', 5),
            ('IV', 4),
            ('I', 1))

        result = ''
        for numeral, integer in roman_numeral_map:
            while n >= integer:
                result += numeral
                n -= integer
        return result


def main():
    solver = Solution()
    tests = []
    for test in tests:
        print(test)
        print(' ->')
        result = solver.intToRoman(test)
        print(result)
        print('~'*10)
    pass


if __name__ == '__main__':
    main()
    pass
