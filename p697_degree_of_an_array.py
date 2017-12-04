class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos = dict()
        for idx, value in enumerate(nums):
            if value in pos:
                pos[value].append(idx)
            else:
                pos[value] = [idx]
        degree, length = 0, len(nums)
        for value, positions in pos.items():
            # print(value, positions)
            if len(positions) > degree:
                degree = len(positions)
                length = positions[-1] - positions[0] + 1
            elif len(positions) == degree:
                length = min(length, positions[-1] - positions[0] + 1)
        return length


def main():
    sol = Solution().findShortestSubArray
    print(sol([1, 2, 2, 3, 1]), '-> 2')
    print(sol([1, 2, 2, 3, 1, 4, 2]), '-> 6')


if __name__ == '__main__':
    main()
