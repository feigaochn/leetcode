# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: first bad version
#
# You are a product manager and currently leading a team to develop a new
# product. Unfortunately, the latest version of your product fails the quality
# check. Since each version is developed based on the previous version, all
# the versions after a bad version are also bad.
# 
# Suppose you have n versions [1, 2, ..., n] and you want to find out the
# first bad one, which causes all the following ones to be bad.
# 
# You are given an API bool isBadVersion(version) which will return whether
# version is bad. Implement a function to find the first bad version. You
# should minimize the number of calls to the API.
# 
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Binary Search
# 
# Show Similar Problems
# 
#  (M) Search for a Range
#  (M) Search Insert Position


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool

versions = []


def build_versions(a, b):
    global versions
    versions = [False] * (a + 1) + [True] * b


def isBadVersion(version):
    return versions[version]


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo, hi = 0, n
        while lo < hi - 1:
            mi = (lo + hi + 1) // 2
            if isBadVersion(mi):
                hi = mi
            else:
                lo = mi
        return hi


def main():
    for a, b in [(0, 1), (2, 2)]:
        build_versions(a, b)
        print(a, b, Solution().firstBadVersion(a + b))


if __name__ == '__main__':
    main()
    pass
