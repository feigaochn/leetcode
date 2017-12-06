# author: Fei Gao
# date: Sun Jun  1 18:45:42 2014
#
# Best Time To Buy And Sell Stock II
#
# Say you have an array for which the ith element is the price of a given stock
# on day i.
# Design an algorithm to find the maximum profit. You may complete as many
# transactions as you like (ie, buy one and sell one share of the stock
# multiple times). However, you may not engage in multiple transactions at the
# same time (ie, you must sell the stock before you buy again).

# Note: if price drops today, sell out yesterday and buy in today!


class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if prices is None or len(prices) <= 1:
            return 0

        win = 0
        buy = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < prices[i-1]:
                # sell yesterday
                win += prices[i-1] - buy
                # buy today
                buy = prices[i]
        if prices[-1] > buy:
            win += prices[-1] - buy

        return win


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
