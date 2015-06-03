# author: Fei Gao
#
# Container With Most Water
#
# Given n non-negative integers a1, a2, ..., an, where each represents a
# point at coordinate (i, ai). n vertical lines are drawn such that the
# two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which
# together with x-axis forms a container, such that the container contains
# the most water.
# Note: You may not slant the container.


class Solution:
    # @return an integer
    def maxArea(self, height):
        if not height or len(height) < 2:
            return 0

        head_i = 0
        head_h = height[0]
        tail_i = len(height) - 1
        tail_h = height[-1]
        max_area = max(0, (tail_i - head_i) * min(tail_h, head_h))

        while head_i < tail_i:
            if head_h < tail_h:
                head_i += 1
            elif head_h > tail_h:
                tail_i -= 1
            else:
                head_i += 1
                tail_i -= 1
            if height[head_i] > head_h:
                head_h = height[head_i]
            if height[tail_i] > tail_h:
                tail_h = height[tail_i]
            max_area = max(max_area, (tail_i - head_i) * min(tail_h, head_h))

        return max_area


def main():
    solver = Solution()
    tests = [
        [1, 2, 1],
        [3, 4, 2, 2]
    ]
    for test in tests:
        print(test)
        print(' ->')
        result = solver.maxArea(test)
        print(result)
        print('~' * 10)
    pass


if __name__ == '__main__':
    main()
    pass
