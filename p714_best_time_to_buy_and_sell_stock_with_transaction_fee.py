class Solution:
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        best1 = -prices[0]
        best0 = 0
        for p in prices[1:]:
            best1n = max(best1, best0 - p)
            best0n = max(best0, best1 + p - fee)
            best1, best0 = best1n, best0n
        return max(best1, best0)


def main():
    fn = Solution().maxProfit
    print(fn([1, 3, 2, 8, 4, 9], 2))


if __name__ == '__main__':
    main()
