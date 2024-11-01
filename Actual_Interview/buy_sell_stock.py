"""
Best Time to Buy and Sell Stock
You are given an array price where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""

class Solution:
    def buy_sell_stock(self, prices):
        left , right = 0, 0

        max_profit = 0
        for i in range(len(prices)):
            for j in range(len(prices)):
                if j > i and prices[j] > prices[i]:
                    profit = prices[j] - prices[i]
                    max_profit = max(max_profit  , profit)
        return max_profit

def main():
    prices = [7,1,5,3,6,4]
    sol = Solution()
    print(sol.buy_sell_stock(prices))

    assert 5 == sol.buy_sell_stock(prices)
    prices = [7, 6, 4, 3, 1]

    print(sol.buy_sell_stock(prices))
    assert 0 == sol.buy_sell_stock(prices)

if __name__ == "__main__":
    main()