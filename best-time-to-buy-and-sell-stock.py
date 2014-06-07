# author: Fei Gao
# date: Sun Jun  1 18:55:12 2014
#
# Best Time To Buy And Sell Stock
#
# Say you have an array for which the ith element is the price of a given stock
# on day i.
# If you were only permitted to complete at most one transaction (ie, buy one
# and sell one share of the stock), design an algorithm to find the maximum
# profit.


class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if prices is None or len(prices) == 0:
            return 0

        # (best win from start to here, min price before here)
        best_from_start = [(0, prices[0])]
        for cur_price in prices[1:]:
            pre_best, pre_min = best_from_start[-1]
            cur_min = min(pre_min, cur_price)
            cur_best = max(pre_best, cur_price - cur_min)
            best_from_start.append((cur_best, cur_min))

        return best_from_start[-1][0]


def main():
    solver = Solution()
    import random
    prices = [random.randrange(-5, 6) for _ in range(10)]
    print(prices, solver.maxProfit(prices))
    prices = list(range(10000))[::-1]
    print(solver.maxProfit(prices))
    pass


if __name__ == '__main__':
    main()
    pass
