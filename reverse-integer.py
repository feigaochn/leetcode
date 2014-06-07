# author: Fei Gao
#
# Reverse Integer
#
# Reverse digits of an integer.
# Example1: x =  123, return  321
# Example2: x = -123, return -321
#
# click to show spoilers.
# Have you thought about this?
# Here are some good questions to ask before coding. Bonus points
# for you if you have already thought through this!
# If the integer's last digit is 0, what should the output be? ie,
# cases such as 10, 100.
# Did you notice that the reversed integer might overflow? Assume
# the input is a 32-bit integer, then the reverse of 1000000003
# overflows. How should you handle such cases?
# Throw an exception? Good, but what if throwing an exception is
# not an option? You would then have to re-design the function
# (ie, add an extra parameter).


class Solution:
    # @return an integer
    def reverse(self, x):
        return int((('-' if x < 0 else '') + str(abs(x))[::-1]))


def main():
    solver = Solution()
    tests = [123, -123, 0, -1]
    for test in tests:
        print(test)
        print(' ->')
        result = solver.reverse(test)
        print(result)
        print('~' * 10)
    pass


if __name__ == '__main__':
    main()
    pass
