# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: h index ii
#
# Follow up for H-Index: What if the citations array is sorted in ascending
# order? Could you optimize your algorithm?
# 
# Expected runtime complexity is in O(log n) and the input is sorted.
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Binary Search
# 
# Show Similar Problems
# 
#  (M) H-Index


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # TODO
        return


def main():
    solver = Solution()
    tests = [
        (('param',), 'result'),
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.hIndex(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
