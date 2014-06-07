# author: Fei Gao
#
# 3sum
#
# Given an array S of n integers, are there elements a, b, c in S
# such that a + b + c = 0? Find all unique triplets in the array
# which gives the sum of zero.
#
# Note:
# Elements in a triplet (a,b,c) must be in non-descending order. (ie, a <= b <= c)
# The solution set must not contain duplicate triplets.
# For example, given array S = {-1 0 1 2 -1 -4},
# A solution set is:
#     (-1, 0, 1)
#     (-1, -1, 2)

import collections


class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        result = list()

        unique = collections.defaultdict(int)
        for v in num:
            unique[v] += 1

        num = list(unique.keys())
        num_set = set(num)
        num.sort()

        # (-a, -a, 2a) or (-2a, a, a) for a > 0
        for v in num_set - {0}:
            if unique[v] >= 2 and -2 * v in num_set:
                result.append([v, v, -2 * v] if v < 0 else [-2 * v, v, v])

        # (-a, 0, a)
        if 0 in num_set:
            # (0, 0, 0)
            if unique[0] >= 3:
                result.append([0, 0, 0])
            # (-a, 0, a), a > 0
            for a in num:
                if a >= 0:
                    break
                elif -a in num_set:
                    result.append([a, 0, -a])

        # (a, b, c) for a < b < c
        n = len(num)
        for ai in range(n):
            a = num[ai]
            if a >= 0:
                break
            for bi in range(ai + 1, n):
                b = num[bi]
                c = -(a + b)
                if b == 0:
                    continue
                if c <= b:
                    break
                if c in num_set:
                    result.append([a, b, c])
        return result

    def threeSum2(self, num):
        # TLE
        num.sort()

        n = len(num)

        sum2 = collections.defaultdict(list)
        for i in range(n):
            for j in range(i):
                sum2[num[i] + num[j]].append([j, i])

        three2index = lambda l: l[0] + n * (l[1] + n * l[2])
        id2num = lambda l: [num[l[0]], num[l[1]], num[l[2]]]

        three = set()
        result = list()
        for i in range(n):
            for pair in sum2[-num[i]]:
                if i > pair[-1]:
                    indices = pair + [i]
                    thr = id2num(indices)
                    if thr not in result:
                        result.append(thr)
        return result


def main():
    solver = Solution()
    tests = [
        [-1, 0, 1, 2, -1, -4],
        [-9, 14, -7, -8, 9, 1, -10, -8, 13, 12, 6, 9, 3, -3, -15, -15, 1, 8, -7, -4, -6, 8, 2, -10, 8, 11, -15, 3, 0,
         -11, -1, -1, 10, 0, 6, 5, -14, 3, 12, -15, -7, -5, 9, 11, -1, 1, 3, -15, -5, 11, -12, -4, -4, -2, -6, -10, -6,
         -6, 0, 2, -9, 14, -14, -14, -9, -1, -2, -7, -12, -13, -15, -4, -3, 1, 14, 3, -12, 3, 3, -10, -9, -1, -7, 3, 12,
         -6, 0, 13, 4, -15, 0, 2, 6, 1, 3, 13, 8, -13, 13, 11, 11, 13, 14, -6],
        [-7, -10, -1, 3, 0, -7, -9, -1, 10, 8, -6, 4, 14, -8, 9, -15, 0, -4, -5, 9, 11, 3, -5,
         -8, 2, -6, -14, 7, -14, 10, 5, -6, 7, 11, 4, -7, 11, 11, 7, 7, -4, -14, -12, -13, -14,
         4, -13, 1, -15, -2, -12, 11, -14, -2, 10, 3, -1, 11, -5, 1, -2, 7, 2, -10, -5, -8, -10,
         14, 10, 13, -2, -9, 6, -7, -7, 7, 12, -5, -14, 4, 0, -11, -8, 2, -6, -13, 12, 0, 5,
         -15, 8, -12, -1, -4, -15, 2, -5, -9, -7, 12, 11, 6, 10, -6, 14, -12, 9, 3, -10, 10, -8,
         -2, 6, -9, 7, 7, -7, 4, -8, 5, -4, 8, 0, 3, 11, 0, -10, -9],
        [0, 0]
    ]
    for test in tests:
        print(test)
        print(' ->')
        result1 = sorted(solver.threeSum(test[:]))
        print(result1)
        result2 = sorted(solver.threeSum2(test[:]))
        print(result2)
        print(sorted(solver.threeSum(test[:]))) == sorted(solver.threeSum2(test[:]))
        print('~' * 10)
    pass


if __name__ == '__main__':
    main()
    pass
