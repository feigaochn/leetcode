# author: Fei Gao
#
# Pascals Triangle II
#
# Given an index k, return the kth row of the Pascal's triangle.
# For example, given k = 3,
# Return [1,3,3,1].
# Note:
# Could you optimize your algorithm to use only O(k) extra space?


class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        if rowIndex < 0:
            return []
        half = [1]
        for i in range(1, 1+rowIndex):
            half.append(half[-1] * (rowIndex + 1 - i) / i)
        return half

def main():
    solver = Solution()
    tests = [0, 1, 2, 3, 4, 5]
    for test in tests:
        print(test)
        print(' ->')
        result = solver.getRow(test)
        print(result)
        print('~'*10)
    pass


if __name__ == '__main__':
    main()
    pass
