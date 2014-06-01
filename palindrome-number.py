# author: Fei Gao
#
# Palindrome Number
#
# Determine whether an integer is a palindrome. Do this without extra space.
# click to show spoilers.
# Some hints:
# Could negative integers be palindromes? (ie, -1)
# If you are thinking of converting the integer to string, note the restriction of using extra space.
# You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?
# There is a more generic way of solving this problem.


class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1] if x != 0 else True
        pass


def main():
    solver = Solution()
    pass


if __name__ == '__main__':
    main()
    pass
