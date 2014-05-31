import itertools


class Solution:

    # @return a string

    def getPermutation(self, n, k):
        self.result = next(
            itertools.islice(
                itertools.permutations(
                    range(
                        1,
                        n+1)),
                k-1,
                None),
            None)
        return ''.join([str(i) for i in self.result])


for i in range(1, 6+1):
    result = Solution().getPermutation(3, i)
    print(i, result)

result = Solution().getPermutation(9, 273815)
print(result)
