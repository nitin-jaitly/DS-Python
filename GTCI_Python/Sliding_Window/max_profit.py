

def max_profit(price, n):
    profit = 0

    for i in range(n):
        if price[i] > price[i-1]:
            print(profit)
            profit += price[i] - price[i-1]
    return profit


def buy_sell_stock(prices, n):
    buy = 0
    sell = 1
    profit = 0
    maximum_profit = 0

    for sell in range(1, n):
        if prices[buy] < prices[sell]:
            profit = prices[sell] - prices[buy]
            maximum_profit = max(maximum_profit, profit)
            print("profit = " + str(profit))
            print("max profit = " + str(maximum_profit))
        else:
            buy = sell
    return maximum_profit


def driver_buy_sell_stock():
    prices = [10, 4, 11, 1, 5]
    print("Max profit " + str(buy_sell_stock(prices, len(prices))))

# buy = 10, sell = 4
# buy = 4 , sell = 4
# buy = 4, sell = 11  profit = 7
# buy = 4, sell = 1
# buy = 1 , sell = 1
# buy = 1 , sell = 5 , profix = 4

def driver_max_profit():
    prices = [100, 180, 260, 310, 40, 535, 695]
    profit = max_profit(prices, len(prices))
    print("Prices = " + str(prices))
    print("Max Profit " + str(profit))

