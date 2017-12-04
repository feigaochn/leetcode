class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.insert(0, 0)
        # nums.append(0)
        from itertools import accumulate
        sums = list(accumulate(nums))
        # print(sums)
        for idx, psum in enumerate(sums[:-1]):
            if psum * 2 + nums[idx+1] == sums[-1]:
                return idx
        return -1


def main():
    sol = Solution().pivotIndex
    print(sol([1, 7, 3, 6, 5, 6]), '-> 3')
    print(sol([1, 2, 3]), '-> -1')
    print(sol([1, 1, 1]), '-> 1')
    print(sol([1, -1, 0]), '-> 2')
    print(sol([-1, -1, -1, 0, 1, 1]), '-> 0')


if __name__ == '__main__':
    main()
