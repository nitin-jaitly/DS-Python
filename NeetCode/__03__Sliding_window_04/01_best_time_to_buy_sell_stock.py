

def maxProfit(prices: list[int]) -> int:

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
