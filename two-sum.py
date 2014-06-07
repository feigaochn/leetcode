# author: Fei Gao
#
# Two Sum
#
# Given an array of integers, find two numbers such that they add up to a specific target number.
# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
# You may assume that each input would have exactly one solution.
# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2


class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        nums = sorted(list(num))
        target = int(target)
        s = 0
        e = len(nums) - 1
        while s < e:
            su = nums[s] + nums[e]
            if su == target:
                si = num.index(nums[s])
                ei = num.index(nums[e], si+1 if nums[s] == nums[e] else 0)
                return min(si+1, ei+1), max(si+1, ei+1)
            elif su < target:
                s += 1
            elif su > target:
                e -= 1


def main():
    solver = Solution()
    tests = [([2, 7, 11, 15], 9), ([0, 4, 3, 0], 0)]
    for test in tests:
        result = solver.twoSum(*test)
        print(test)
        print(' ->')
        print(result)
        print('~'*10)
    pass


if __name__ == '__main__':
    main()
    pass
