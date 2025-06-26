
"""
L = [ 7,1,5,3,6,4]


"""
class Solution:
    def maxProfit(self,prices: list[int]) -> int:
        n = len(prices)
        print("prices = ", prices)

        hold = [-1 * prices[i] for i in range(n)]
        print("hold  = ", hold)

        sell = [hold[i] + prices[i + 1] for i in range(n - 1)]
        print("sell = ", sell )

        maxProfit = 0
        for j in range(len(sell)):
            if sell[j] > 0:
                maxProfit += sell[j]

        return maxProfit

    def maxProfit2(self, prices: list[int]) -> int:
        l, r = 0, 1
        max_profit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                l = r
            r += 1
        print(max_profit)
        return max_profit


    def driver_max_profit(self):
        prices = [7, 1, 5, 3, 6, 4]
        # assert 7 == self.maxProfit(prices)
        assert 5 == self.maxProfit2(prices)
        #
        prices  = [7,6,4,3,1]
        # assert 0 == self.maxProfit(prices)
        assert 0 == self.maxProfit2(prices)
        #
        prices = [1,2,3,4,5]
        # assert 4 == self.maxProfit(prices)
        assert 4 == self.maxProfit2(prices)

        prices = [10,1,5,6,7,1]
        assert 6 == self.maxProfit2(prices)
        #assert 6 == self.maxProfit(prices)

def main():
    sol = Solution()
    sol.driver_max_profit()

if __name__ == "__main__":
    main()