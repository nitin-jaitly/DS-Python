
class Solution:
    def maxProfit(self,prices: list[int]) -> int:

        l, r = 0, 1 ## where l = buy and r = sell

        maxProfit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r

            r += 1

        return maxProfit

    def driver_max_profit(self):
        prices = [7, 1, 5, 3, 6, 4]
        print(self.maxProfit(prices))

        prices  = [7,6,4,3,1]
        print(self.maxProfit(prices))
