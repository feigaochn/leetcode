# author: Fei Gao
# date: Sun Jun  1 18:21:43 2014
#
# Best Time To Buy And Sell Stock III
#
# Say you have an array for which the ith element is the price of a given stock
# on day i.
# Design an algorithm to find the maximum profit. You may complete at most two
# transactions.
# Note:
# You may not engage in multiple transactions at the same time (ie, you
# must sell the stock before you buy again).


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

        # (best win from here to end, max price after here)
        best_from_end = [(0, prices[-1])]
        for cur_price in prices[-1::-1]:
            next_best, next_max = best_from_end[-1]
            cur_max = max(next_max, cur_price)
            cur_best = max(next_best, cur_max - cur_price)
            best_from_end.append((cur_best, cur_max))
        best_from_end.reverse()

        return max([a[0] + b[0]
                   for (a, b) in zip(best_from_start, best_from_end)])


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
