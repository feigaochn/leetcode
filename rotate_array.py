class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, num, k):
        k = k % len(num)
        n = num[-k:] + num[:-k]
        for i in range(len(num)):
            num[i] = n[i]