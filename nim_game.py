# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: nim game
#
# You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove the stones.
# 
# Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game given the number of stones in the heap.
# 
# For example, if there are 4 stones in the heap, then you will never win the game: no matter 1, 2, or 3 stones you remove, the last stone will always be removed by your friend.
# 
# If there are 5 stones in the heap, could you figure out a way to remove the stones such that you will always be the winner? 
# 
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
# 
# Subscribe to see which companies asked this question
# 
# Show Similar Problems
# 
#  (M) Flip Game II

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 4 != 0


def main():
    solver = Solution()
    tests = [
        ((4,), False),
        ((5,), True)
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.canWinNim(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
