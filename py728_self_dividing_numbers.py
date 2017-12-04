class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """

        def is_self_dividing(num: int) -> bool:
            return all(d > 0 and num % d == 0 for d in map(int, str(num)))

        self._cache = set([1, 2])

        res = []
        for num in range(left, right + 1):
            if num in self._cache:
                res.append(num)
            elif is_self_dividing(num):
                res.append(num)
                self._cache.add(num)
            else:
                continue

        return res


def main():
    sol = Solution().selfDividingNumbers
    print(sol(1, 22))


if __name__ == '__main__':
    main()
