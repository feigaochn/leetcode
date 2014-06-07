# author: Fei Gao
#
# Count And Say
#
# The count-and-say sequence is the sequence of integers beginning as follows:
# 1, 11, 21, 1211, 111221, ...
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth sequence.
# Note: The sequence of integers will be represented as a string.


class Solution:
    # @return a string
    def countAndSay(self, n):
        def process(s):
            l = []
            start = 0
            for end in range(1, len(s)):
                if s[end] != s[end-1]:
                    l.append(s[start:end])
                    start = end
            l.append(s[start:])
            res = ''
            for ls in l:
                res += str(len(ls)) + ls[0]
            return res
        seq = ['', '1']
        for i in range(1, n):
            seq.append(process(seq[i]))
        return seq[n]


def main():
    solver = Solution()
    for n in range(10):
        print(n, ': ', solver.countAndSay(n))
    pass


if __name__ == '__main__':
    main()
    pass
