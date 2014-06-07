# author: Fei Gao
# date: Sun Jun  1 16:03:26 2014
#
# Search In Rotated Sorted Array Ii
#
# Follow up for "Search in Rotated Sorted Array":
# What if duplicates are allowed?
# Would this affect the run-time complexity? How and why?
# Write a function to determine if a given target is in the array.


class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
        isinstance(A, list)
        try:
            A.index(target)
            return True
        except:
            return False
        pass


def main():
    solver = Solution()
    lst = list(range(5))
    for i in range(5):
        rlst = lst[i:] + lst[:i]
        t = 6
        print(t, solver.search(rlst, t))
    pass


if __name__ == '__main__':
    main()
    pass
